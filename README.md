# Paste Repeater

## About
  This is a Sublime Text 3 plugin that will let you paste your system's clipboard into a file multiple times. So instead of hitting <kbd>Ctrl</kbd>+<kbd>v</kbd> two dozen times, you can use this plugin to tell Sublime Text to paste your clipboard as many times as you'd like in a single command.

## Usage
Tools -> Command Palette (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd> or <kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>P</kbd>) and type `repeater`.

-- or --

  <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>v</kbd> (or <kbd>Super</kbd>+<kbd>Cmd</kbd>+<kbd>Shift</kbd>+<kbd>v</kbd> if you're on a Mac).

## What Happens
The Sublime Text input panel will ask you how many times you'd like to paste your clipboard into the editor:

![input panel](input_panel.png)

Your system's clipboard will be pasted into the editor at the cursor's current location the number of times you request. All values are rounded down to the lowest whole number.