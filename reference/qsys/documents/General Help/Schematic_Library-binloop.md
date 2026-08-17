# Bin Loop

> Source: https://help.qsys.com/Content/Schematic_Library/binloop.htm

# Bin Loop

Use the Bin Loop component to seamlessly loop one or more audio files for playback to one or more synchronized outputs. You can specify loop counts for individual files. To accommodate a need to play a file for an indeterminate amount of time, such as during a show intermission or similar, you can loop a file indefinitely until manually "breaking" to the next file.

[Requirements](javascript:void(0))

* Refer to the Q-SYS Core Manager > [Files](../Core_Manager/Core_Management/Audio_Files.htm) topic to learn how to upload audio files to the Q-SYS Core processor for use with Bin Loop.
* To reduce CPU usage, any queued WAV files should be 24-bit with a 48k sample rate.
* Bin Loop supports multichannel playback, but all tracks must be muxed into a single audio file.
* It is not possible to use Bin Loop in emulation mode (F6).

[Configuration Overview](javascript:void(0))

1. Add a Bin Loop component to your design.
2. In the Properties pane, set the number of synchronized outputs for playback and wire the outputs to downstream audio components.
3. Press F5 to save your design to the Core and run it.
4. Double-click Bin Loop to open its control panel:
   * In the File Name text box, type the complete path and extension of an audio file stored on the Q-SYS Core processor. For example: `Audio/01 My Happy File.mp3`
   * In the Play Count box, specify how many times the file should play before moving to the next file in the sequence, from -1 to 1000. (A play count of -1 means that you want the file to play indefinitely. This is used in conjunction with the Break control â see [Controls](#Controls).)
   * Press Submit to add the file to the list. Add more files as desired.
   * Click Start to begin playback of the sequence. When a file completes playback, it is removed from the list. You can add files to the list during playback.

**Note:** If you stop running the design on the Q-SYS Core processor, the queued list is cleared.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

#### Output *n*

The number of Output pins depends on the Output Count property. Connect each pin to a downstream audio component. All outputs are synchronized during playback.

[Schematic Examples](javascript:void(0))

[Example 1: Showtime!](javascript:void(0))

In this example, Bin Loop is configured with eight outputs, each wired to an input of an I/O-8 Flex Out component. All outputs send the same synchronized show audio. The show consists of:

* A pre-show, whose length of time is unknown. Therefore, the audio file's Play Count is set to -1, which loops the audio until the show operator presses Break to move to the next file.
* Parts 1 and 2, whose audio is configured to play twice.
* A closing portion, whose audio is configured to play once.

[Example 2: Show Builder Script](javascript:void(0))

In this example, the design uses a Text Controller component configured to be a Show Builder. It provides a convenient method to create playlists from audio files saved to the Q-SYS Core.

The Text Controller ("Show Builder v1.0") consists of:

#### Text Boxes

* **Bin Loop Player Name**: The custom name used to create Named Component control connections between the player and control script.
* **File Name *n***: The name of the file to add to the Bin Loop queue.

#### Input Control Pins, Buttons, and Knobs

* **Play Count *n***: The number of times to play the audio file before progressing to the next file in the queue.
* **Submit *n***: Add the file and play count to the queue.
* **Submit All**: Add all files and play counts to the Bin Loop queue.

#### Lua Script

```lua
--Initialize the Named Controls connection to the Bin Loop Player component----------------------------------------------------------------------------
function GetBinLoopPlayerName()
  Player = Component.New(Controls["Bin Loop Player Name"].String)
end

GetBinLoopPlayerName()

Controls["Bin Loop Player Name"].EventHandler = function()
  GetBinLoopPlayerName()
end

--Add individual files and play counts to the Bin Loop Player playlist----------------------------------------------------------------------------------
for k,_ in ipairs (Controls["Submit"]) do
  Controls["Submit"][k].EventHandler = function()
    if  Player["file.name"] and Controls["Bin Loop Player Name"].String ~= "" and Controls["File Name"][k].String ~= "" then
      Player["file.name"].String = Controls["File Name"][k].String
      Player["play.count"].String = Controls["Play Count"][k].Value
      Player["submit"]:Trigger()
    else
      print ("Bin Loop Player Name or File Name field not configured correctly")
    end
  end
end

--Add all of the files and play counts to the Bin Loop Player playlist-----------------------------------------------------------------------------------
Controls["Submit All"].EventHandler = function()
  for k,v in ipairs (Controls["Submit"]) do
    if Player["file.name"] and Controls["Bin Loop Player Name"].String ~= "" and Controls["File Name"][k].String ~= "" and Player["file.name"].String then
      Player["file.name"].String = Controls["File Name"][k].String
      Player["play.count"].String = Controls["Play Count"][k].Value
      Player["submit"]:Trigger()
    else
      print ("Bin Loop Player Name or File Name field not configured correctly for item "..k)
    end
  end
end
```

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Bin Loop Properties

#### Output Count

Specify the number of output pins, from 0 to 128. All outputs are synchronized during playback.

[Controls](javascript:void(0))

#### File Name

Specify the complete path and extension of an audio file to add to the queue.

#### Play Count

The number of times to play the audio file, from -1 to 1000. Specify -1 for indefinite playback, which occurs until the Break control button is pressed.

#### Submit

Click to add the file and its play count to the queue.

#### Queue

This list of upcoming audio files and play counts for playback.

#### Start

Begin processing the queue.

#### Stop

Stop playback of the current file.

**Note:** If you press Start after stopping playback, the queue resumes with the next file in the list, not with the next count of the current file.

#### Break

Click to finish playback of the current file and move to the next file in the queue, effectively setting the play count to 1. If a queued file's Play Count is set to -1, the file plays continuously until you press Break. This is useful for show vamping.

#### Clear

Click to clear the queue.

#### Current File

This is the file currently being played.

#### Current Time

The elapsed time of playback for the current file.

#### Current Play Count

This counts down to 0 as playback iterations occur for the current audio file.

#### Is Playing

LED glows green if playback is actively occurring.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Break | (trigger) | | | Input / Output |
| Clear | (trigger) | | | Input / Output |
| Current File | (text) | | | Output |
| Current Play Count | 0 to 1000 | 0 to 1000 | - | Output |
| Current Time | - | *hh*:*mm*:*ss* | - | Input / Output |
| File Name | (text) | | | Input / Output |
| Is Playing | 0  1 | false  true | 0  1 | Output |
| Play Count | -1 to 1000 | -1 to 1000 | - | Input / Output |
| Queue | (text) | | | Input / Output |
| Start Trigger | (trigger) | | | Input / Output |
| Stop Trigger | (trigger) | | | Input / Output |
| Submit Task | (trigger) | | | Input / Output |

[Troubleshooting](javascript:void(0))

### Audio file playback does not start

If a file does not play, check to make sure you have specified the exact path, including the directory and filename extension, of the audio file. For example, if the file "xyz.mp3" is stored in the Core's "Audio/Show" directory, this is what you'd type in the File Name text box:

`Audio/Show/zyz.mp3`
