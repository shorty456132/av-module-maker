# Loop Player

> Source: https://help.qsys.com/Content/Schematic_Library/loop_player.htm

# Loop Player

Use the Loop Player component to queue groups of audio files for playback and optionally synchronize playback to a time source. Loop Player is controlled via a Lua script (using a scripting component, such as [Scriptable Controls](scriptable_controls.htm) or [Text Controller](device_controller_script.htm)), or externally via [Q-SYS Remote Control Protocol (QRC)](../External_Control_APIs/QRC/QRC_Overview.htm), which uses JSON-RPC.

[Configuration Overview](javascript:void(0))

### Set properties

In your schematic, select the component to configure its properties, including the number of playback outputs, and whether playback is synchronized to a selected time source. See [Properties](#Properti).

### Configure a control script

Loop Player can only be controlled with a Lua script or externally via Q-SYS QRC using JSON-RPC. See [Schematic Examples](#Examples) for Lua examples and visit [Loop Player Control Methods](../External_Control_APIs/QRC/QRC_Commands.htm#Loop) for additional JASON-RPC scripting examples.

### Connect inputs and outputs

See [Inputs and Outputs](#Inputs) for further detail.

### Run your design and configure controls

1. Press F5 to save your design to the Core and run it.
2. Using your configured script and controls, start playback.
3. Double-click the Loop Player component to open its control panel.
4. Output status, elapsed time, and remaining time are shown. You can also adjust the output gain. See [Controls](#Controls).

[Inputs and Outputs](javascript:void(0))

### Input Pins

There are no input pins except when the Time Source property is set to 'LTC'. In this mode, connect the pin, represented by a () circle, to an upstream external Linear Timecode (LTC) source, such as the [SMPTE LTC Generator](linear_timecode_encoder.htm) component.

### Output Pins

#### Audio Output 1-*n*

Connect the right side pins, represented by a () circle, to a downstream audio components. Set the number of outputs using the Output Count property. Outputs correspond to the respective player tracks.

[Schematic Examples](javascript:void(0))

[Loop Player with Time Synchronization](javascript:void(0))

In this example, we are using a [SMPTE LTC Reader](linear_timecode_decoder.htm) to synchronize the Loop Player's `Start`, `Stop`, and `Cancel` according to a specific time.

[LoopPlayer.Start](javascript:void(0))

### Syntax

LoopPlayer.Start

### Arguments

*Files*: The name of the audio file in which you wish to play.

*Log*: If set to `true`, messages and errors will be sent to the Q-SYS Core processor's system log file.

*Name*: The name of the Loop Player as designated in Properties.

*Outputs*: The Loop Player output numbers for which to start audio playback.

*Current Time + or -*: With time synchronization, you have the option to add or subtract from the `currentTime`.

* `-1`: Starts immediately
* `-2`: Starts at the end of the current audio track playing in the Loop Player
* `0`: (default) Starts playing once it is queued up
* `+1`: Starts 1 second after the command

### Example

```lua
Controls.go.EventHandler = function()  
  local currentTime = Controls.time.Value  
  print(string.format("time is %f", currentTime ))  
  
  LoopPlayer.Start {  
    Files = { { Name = "/Audio/loop-1.wav", Output = 1 }},  
    Log = true,  
    Name = "loop",  
    StartTime = currentTime + 1  
  }  
    
end
```

[LoopPlayer.Stop](javascript:void(0))

### Syntax

LoopPlayer.Stop

### Arguments

*Files*: The name of the audio file in which you wish to stop.

*Log*: If set to `true`, messages and errors will be sent to the Q-SYS Core processor's system log file.

*Name*: The name of the Loop Player as designated in Properties.

*Outputs*: The Loop Player output numbers for which to stop playback.

*Current Time + or -*: With time synchronization, you have the option to add or subtract from the `currentTime`.

* `-1`: Stops immediately
* `-2`: Stops at the end of the current audio track playing in the Loop Player
* `0`: (default) Stops playing once it is queued up
* `+1`: Stops 1 second after the command

### Example

```lua
Controls.go.EventHandler = function()  
  local currentTime = Controls.time.Value  
  print(string.format("time is %f", currentTime ))  
    
  LoopPlayer.Stop {  
    Files = { { Name = "/Audio/loop-1.wav", Output = 1 }},  
    Log = true,  
    Name = "loop",  
    Outputs = { 1, 2, 3  }  
  }  
end 
```

[LoopPlayer.Cancel](javascript:void(0))

### Syntax

LoopPlayer.Cancel

### Arguments

*Files*: The name of the audio file in which you wish to cancel.

*Log*: If set to `true`, messages and errors will be sent to the Q-SYS Core processor's system log file.

*Name*: The name of the Loop Player as designated in Properties.

*Outputs*: The Loop Player output numbers for which to stop playback.

*Current Time + or -*: With time synchronization, you have the option to add or subtract from the `currentTime`.

* `-1`: Cancels immediately
* `-2`: Cancels at the end of the current audio track playing in the Loop Player
* `0`: (default) Cancels playing once it is queued up
* `+1`: Cancels 1 second after the command

### Example

```lua
Controls.go.EventHandler = function()  
  local currentTime = Controls.time.Value  
  print(string.format("time is %f", currentTime ))  
  
  LoopPlayer.Cancel {  
    Files = { { Name = "/Audio/loop-1.wav", Output = 1 }},  
    Log = true,  
    Name = "loop",  
    Outputs = { 1, 2, 3  }  
  }  
  
end
```

[Loop Player without Time Synchronization](javascript:void(0))

In this example, we are not using time synchronization, so the components are only the Loop Player and the Text Controller.

[LoopPlayer.Start](javascript:void(0))

### Syntax

LoopPlayer.Start

### Arguments

*Files*: The name of the audio file in which you wish to play.

*Log*: If set to `true`, messages and errors will be sent to the Q-SYS Core processor's system log file.

*Name*: The name of the Loop Player as designated in Properties.

*Outputs*: The Loop Player output numbers for which to start audio playback.

### Example

```lua
Controls.go.EventHandler = function()  
  LoopPlayer.Start {  
    Files = { { Name = "/Audio/loop-1.wav", Output = 1 }},  
    Log = true,  
    Name = "loop",  
  }  
    
end
```

[LoopPlayer.Stop](javascript:void(0))

### Syntax

LoopPlayer.Stop

### Arguments

*Files*: The name of the audio file in which you wish to stop.

*Log*: If set to `true`, messages and errors will be sent to the Q-SYS Core processor's system log file.

*Name*: The name of the Loop Player as designated in Properties.

*Outputs*: The Loop Player output numbers for which to stop playback.

### Example

```lua
Controls.go.EventHandler = function()  
  LoopPlayer.Stop {  
    Files = { { Name = "/Audio/loop-1.wav", Output = 1 }},  
    Log = true,  
    Name = "loop",  
    Outputs = { 1 }  
  }  
end 
```

[LoopPlayer.Cancel](javascript:void(0))

### Syntax

LoopPlayer.Cancel

### Arguments

*Files*: The name of the audio file in which you wish to cancel.

*Log*: If set to `true`, messages and errors will be sent to the Q-SYS Core processor's system log file.

*Name*: The name of the Loop Player as designated in Properties.

*Outputs*: The Loop Player output numbers for which to stop playback.

### Example

```lua
Controls.go.EventHandler = function()  
  
  LoopPlayer.Cancel {  
    Files = { { Name = "/Audio/loop-1.wav", Output = 1 }},  
    Log = true,  
    Name = "loop",  
    Outputs = { 1 }  
  }  
  
end
```

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Loop Player Properties

#### Time Source

Select whether the Loop Player synchronizes to a time source. Additional Properties will appear depending upon the Time Source selected.

[GPS](javascript:void(0))

Requires a locally-connected GPS receiver, and the Core must be its own PTP Grandmaster. The time is in Universal Coordinated Time (UTC) and is bound to the GMT time source. Your offset depends on your relative time zone from GMT. The time specified for Start commands can be in floating point increments of 1ms â for example, adding .456 to the integer of the second results in playback beginning 456ms into the program.

#### Output Count

Specify the number of outputs.

#### Buffer Adjustment

Specify how far into the future Loop Player pre-buffers audio for playback. Lowering this value results in less audio buffering, which may enable you to schedule playback with a sooner start time.

**Note:** Reducing this value may cause audio playback artifacts on heavily-loaded systems.

[LTC](javascript:void(0))

When enabled, a single audio input (left side) pin is exposed for the reception of SMPTE Linear Timecode (LTC) encoded audio from an external LTC source, such as the [SMPTE LTC Generator](linear_timecode_encoder.htm) component. The Time value sent in the Start command specifies the hours, minutes, seconds, and frames as floating point seconds. The decimal portion rounds to the nearest frame and varies depending on the Frame Rate (fps) property.

#### Frame Rate (fps)

For LTC mode only, this sets the frames per second of incoming SMPTE LTC encoded audio.

#### Output Count

Specify the number of outputs.

#### Buffer Adjustment

Specify how far into the future Loop Player pre-buffers audio for playback. Lowering this value results in less audio buffering, which may enable you to schedule playback with a sooner start time.

**Note:** Reducing this value may cause audio playback artifacts on heavily-loaded systems.

[GPS External](javascript:void(0))

Similar to GPS mode, but the Core is a PTP slave to another Grandmaster for audio clock synchronization. UTC time from the Grandmaster Core is forwarded to the slave Core via the [Control Link](project_link.htm) component, which is configured as a server on the Grandmaster Core and client on the slave core. Configure the Control Link client for the "Time knob" type, as this uses the proper range of 0 to 86399 by default. The time specified for Start commands can be in floating point increments of 1ms â for example, adding .456 to the integer of the second results in playback beginning 456ms into the program.

**Note:** GPS External mode requires the PTP Force On property to be enabled in Design Properties if your design does not already use PTP clock synchronization. For more information, see [Design Properties](design_properties.htm).

#### Output Count

Specify the number of outputs.

#### Buffer Adjustment

Specify how far into the future Loop Player pre-buffers audio for playback. Lowering this value results in less audio buffering, which may enable you to schedule playback with a sooner start time.

**Note:** Reducing this value may cause audio playback artifacts on heavily-loaded systems.

[PTP](javascript:void(0))

In this mode, the Core is a slave to a PTP Grandmaster time source (for example, a Evertz master time clock or Meinberg Grandmaster). The PTP packets contain the time of day in atomic time format, omitting leap seconds.

#### Output Count

Specify the number of outputs.

#### Buffer Adjustment

Specify how far into the future Loop Player pre-buffers audio for playback. Lowering this value results in less audio buffering, which may enable you to schedule playback with a sooner start time.

**Note:** Reducing this value may cause audio playback artifacts on heavily-loaded systems.

#### User UTC Offset

For PTP mode only, specify whether to enable the UTC offset based on your time zone. Your offset will depend on your relative time zone from GMT.

[None](javascript:void(0))

No time source is used. The Loop Player functions as a real-time multi-track player. In this mode, the Start command starts playing audio for each track as soon as possible â there is no guarantee of absolute sample sync among tracks started with the same command. If sample-accurate track playback is required, use one of the other modes.

**Note:** The Cancel command has no purpose in this mode, as nothing in the queue can be canceled. Playback can only be started or stopped.

#### Output Count

Specify the number of outputs.

#### Buffer Adjustment

Specify how far into the future Loop Player pre-buffers audio for playback. Lowering this value results in less audio buffering, which may enable you to schedule playback with a sooner start time.

**Note:** Reducing this value may cause audio playback artifacts on heavily-loaded systems.

[Controls](javascript:void(0))

The available controls depend on the Time Source set in Properties.

#### UTC

Indicates the UTC time value.

#### Offset

Indicates the UTC offset value.

#### LTC

Indicates the LTC time value.

#### Output *n* File

Indicates the audio file playing on the output.

#### Output *n* Elapsed

Indicates the elapsed time since the audio file started playback.

#### Output *n* Remaining

Indicates the remaining time for playback of the audio file.

#### Output *n* Next

Indicates the next audio file in the queue for this output.

#### Output *n* Gain

Adjusts the gain of the output.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Output *n* Elapsed | â | HH:MM:SS | â | Input / Output |
| Output *n* Gain | -100 to 20 | -100dB to 20dB | 0 to 1.00 | Input / Output |
| Output *n* Next | (text) | | | Output |
| Output *n* Remaining | â | HH:MM:SS | â | Input / Output |
| Output *n* Status | (text) | | | Output |
| UTC | â | HH:MM:SS | â | Input / Output |
| UTC Offset | (text) | | | Input / Output |
| LTC | â | HH:MM:SS | â | Output |

[Troubleshooting](javascript:void(0))

### File Not Playing at Correct Spot

If the GPS recommended minimum (RMC) received by the serial port too close to the pulse per second (PPS) coming in, the Loop Player may not start playing at the correct spot of the file. Lowering the baud rate, which effectively delays the reception of the RMC message will resolve the issue.

**Tip:** Check your GPS system's default baud rate and set it to 19.2k.

### Multi-Channel files not playing through Loop Player

Only mono (single channel) audio files are supported through the Loop Player. If multichannel files are used, only the first channel will play.
