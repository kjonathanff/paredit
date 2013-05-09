
import sublime, sublime_plugin
try:
	from paredit import shared
except:
	import shared

def char_type(c):
	if c == "\"": return "string"
	elif c == "(" or c == "[" or c == "{": return "lbracket"
	elif c == ")" or c == "]" or c == "}": return "rbracket"

def remove_empty_expression(view, edit, point, fail_direction):
	(lb, rb) = shared.get_expression(view, point)
	if lb and rb:
		expr_region = sublime.Region(lb, rb)
		expression = view.substr(expr_region)
		if shared.is_expression_empty(expression):
			return shared.erase_region(view, edit, expr_region)
		else:
			return sublime.Region(point + fail_direction, point + fail_direction)
	else:
		return point

def paredit_delete(view, edit, is_forward):
	def f(region):
		if not region.begin() == region.end():
			return shared.erase_region(view, edit, region)

		point = region.begin()

		if is_forward:
			direction = 1
			next_char = view.substr(point)
			skip_char_type = "lbracket"
		else:
			direction = -1
			next_char = view.substr(point - 1)
			skip_char_type = "rbracket"

		next_char_type = char_type(next_char)

		if next_char_type == "string":
			if shared.is_inside_string(view, point):
				return remove_empty_expression(view, edit, point, direction)
			else:
				return region.begin() + direction
		elif next_char_type == skip_char_type: return region.begin() + direction
		elif next_char_type:
			return remove_empty_expression(view, edit, point, direction)
		else:
			if is_forward:
				view.erase(edit, sublime.Region(point, point + direction))
				return region
			else:
				view.erase(edit, sublime.Region(point - 1, point))
				return point - 1

	shared.edit_selections(view, f)

def paredit_forward_delete(view, edit):
	paredit_delete(view, edit, True)

def paredit_backward_delete(view, edit):
	paredit_delete(view, edit, False)

def paredit_kill_abstract(view, edit, expression):
	def f(region):
		point = region.begin()
		if region.end() == point:
			(lb, rb) = shared.get_expression(view, point)
			if lb and rb:
				if expression:
					view.erase(edit, sublime.Region(lb + 1, rb - 1))
					return lb + 1
				else:
					view.erase(edit, sublime.Region(point, rb - 1))
					return point
			else:
				return point
		else:
			return region

	shared.edit_selections(view, f)

def paredit_kill(view, edit):
	paredit_kill_abstract(view, edit, False)

def paredit_kill_expression(view, edit):
	paredit_kill_abstract(view, edit, True)

####
#### Commands
class Paredit_forward_deleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		paredit_forward_delete(self.view, edit)

class Paredit_backward_deleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		paredit_backward_delete(self.view, edit)

class Paredit_killCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		paredit_kill(self.view, edit)

class Paredit_kill_expressionCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		paredit_kill_expression(self.view, edit)
