# paredit

This is an implementation of [paredit](http://www.emacswiki.org/emacs/ParEdit)
for [sublime text](http://www.sublimetext.com/).

## Installation

### With package control (recommended)

Use [Sublime Package Control](http://wbond.net/sublime_packages/package_control),
the package is called `paredit`.

### Manually

1. Clone the repository or download the [zipfile](https://github.com/odyssomay/paredit/archive/master.zip).
2. The resulting folder - either from cloning or unzipping - should be moved to
`Installed Packages` inside your [data directory](http://docs.sublimetext.info/en/latest/basic_concepts.html#the-data-directory).

## Usage

See [the cheatsheet](http://pub.gajendra.net/src/paredit-refcard.pdf).

## Configuration

Paredit configuration can be found in the menu `Preferences->Package Settings->Paredit`. It has the following menu items:

<table>
	<tr><td>Enabled</td>
		<td>If unchecked paredit is completely disabled. The checkbox does not reflect if the current file uses paredit or not.</td>
	</tr>
	<tr><td>Settings - Default</td>
		<td>The default settings. Should not be edited.</td>
	</tr>
	<tr><td>Settings - User</td>
		<td>Add your own custom settings here. See below for more info.</td>
	</tr>
	<tr><td>Key Bindings – Default</td>
		<td>The default bindings for all platforms. Should not be edited.</td>
	</tr>
	<tr><td>Key Bindings – OSX Extension</td>
		<td>Only on OSX. Adds extra bindings for osx involving the *meta* key.</td></tr>
	<tr><td>Key Bindings – User</td>
		<td>Add your own custom bindings here.</td>
	</tr>
</table>

The settings are:

<table>
	<tr><td>enabled</td>
		<td>Completely enable or disable paredit.
			Default: **true**</td></tr>
	<tr><td>strict_mode</td><td></td></tr>
	<tr><td>syntax</td>
		<td>A list of syntax names which will activate paredit.

			Each item in the list is a regex that will be used to find a match anywhere in the syntax name.

			Find the syntax name of the current file by pressing ``ctrl+``` (to open the console), paste `view.settings().get("syntax")` into the text field at the bottom and press enter.

			Default: **["Clojure", "Lisp"]**</td></tr>
	<tr><td>file_name</td>
		<td>Works exactly like the *syntax* option but activates on file name.

			Default: **[]**</td></tr>
</table>

See the default settings (that you open through the menu) for an example on how the file should look.

## Implementation Status

Below is a list of all currently **not** implemented paredit commands
from the cheatsheet.

* paredit-backslash
* paredit-recentre-on-sexp
* paredit-reindent-defun
* paredit-backward-up
* paredit-backward-down
* paredit-forward-up
* paredit-forward-down

## Testing

Press *ctrl+shift+p* to open the command palette. Type *test*
and run *Paredit: Run Tests*.
