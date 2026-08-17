# Debug Output

> Source: https://help.qsys.com/Content/Schematic_Library/debug_output.htm

# Debug Output

The Debug Output window displays print output from the script, as well as any error messages from the Lua engine describing errors in the script.

[Deleting, Copying, and Scrolling Output](javascript:void(0))

* Click  to delete all current output in the window.
* Click  to copy the current output to your computer's clipboard. You can then paste it into a text program.
* If your script generates a high rate of output, click  to stop the output from scrolling. Click  to resume scrolling.

[Viewing Output](javascript:void(0))

You can view output in normal and hex format.

* Select Normal (default) to view all output as normal text.
* Select Normal + Hex to view output as normal text and translate any unprintable characters to hex. (Only unprintable characters are translated to hex.)
* Select Hex to translate all output to hex format. (Every character is shown as hex.)

[Saving Output](javascript:void(0))

* Select AutoSave to specify a text file name and location on your computer to continuously save the debug output when new data is written.
* Click  to select a new file name and location for the saved output.

**Note:** AutoSave is deactivated if you close the tab containing the script Debug Output window.

[Troubleshooting](javascript:void(0))

If you reference an input or output that has nothing connected to it, you'll see this error message or similar:

[string "cin\_speaker = Controls.Inputs[1]..."]:43: attempt to index global 'cin\_ramptime' (a nil value)
