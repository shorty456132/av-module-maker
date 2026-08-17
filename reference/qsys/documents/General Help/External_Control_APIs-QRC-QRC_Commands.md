# QRC Commands

> Source: https://help.qsys.com/Content/External_Control_APIs/QRC/QRC_Commands.htm

# QRC Commands

QRC is a Unicode-based TCP/IP control protocol. The client connects to the Q-SYS Core (or emulator) on port 1710 and sends JSON RPC 2.0 null-terminated commands.

**Note:** For the JSON-RPC 2.0 Specification, visit [jsonrpc.org](http://www.jsonrpc.org/specification).

**Tip:** In all QRC commands, `id` acts as an identifier and allows for the sender to match the response with the command. The `id` will be copied and returned to the sender in the response. The `id` field must be a number and you can use whatever value you want.

[Formatting Requirements](javascript:void(0))

Every QRC command must meet both of the following requirements:

1. It must be a command from the supported commands listed below.
2. Each command must be terminated in a null.

For the first requirement, you can find the full list of supported QRC commands below.

For the second, a zero character following the escape character should be used for the null, as shown [here](https://support.qsys.com/application-notes/how-to-|-formatting-a-qrc-command/version/1?kb_language=en_US).

[Connection Methods](javascript:void(0))

Use these methods to log on to the Q-SYS Core processor via the QRC protocol and maintain the socket connection.

**Note:** User credentials must first be created in [Users (Administrator)](../../Administrator/Users.htm)

[Logon](javascript:void(0))

Logs on to the system.

### Parameters

`User`, `Password`

### Example

```lua
{  
  "jsonrpc":"2.0",  
  "method":"Logon",  
  "params":{  
    "User":"username",  
    "Password":"1234"  
  }  
}
```

### Response

```lua
{
  "jsonrpc": "2.0",
  "id" : <id_send_with_command>,								
  "error" : <error if command failed>,								
  "response" : <response if command succeeded>, 								
}								
```

[NoOp](javascript:void(0))

This is a simple, "do nothing" method for making sure that the socket remains open.

### Parameters

None.

### Example

```lua
{  
  "jsonrpc":"2.0",  
  "method":"NoOp",  
  "params":{  
  }  
}
```

[Status Methods](javascript:void(0))

Use these methods to obtain the status of the Q-SYS Core.

[EngineStatus](javascript:void(0))

This method is automatically deployed to return the status of the Q-SYS Core whenever a client connects to the QRC port or the status changes.

**Note:** When the connection is open and there is a status change on any device in the inventory, an unsolicited EngineStatus message will be sent.

### Parameters

`State` : One of the following strings â "Idle", "Active", "Standby".

`DesignName` : Name of the currently running design.

`DesignCode` : GUID of the currently running design.

`IsRedundant` : True if the design is configured to be a redundant design.

`IsEmulator` : True if the design is currently running in the emulator.

### Example

```lua
{  
  "jsonrpc":"2.0",   
  "method":"EngineStatus",   
  "params":{  
    "State":"Active",   
    "DesignName":"MyDesign",   
    "DesignCode":"qALFilm6IcCo",   
    "IsRedundant":false,   
    "IsEmulator":true  
  }  
}
```

[StatusGet](javascript:void(0))

Manually request the current status. Returns the EngineStatus of the Q-SYS Core.

### Parameters

NA

### Response Results

`Platform` : The Q-SYS Core model.

`State` : One of the following strings â "Idle", "Active", "Standby".

`DesignName` : Name of the currently running design.

`DesignCode` : GUID of the currently running design.

`IsRedundant` : True if the design is configured to be a redundant design.

`IsEmulator` : True if the design is currently running in the emulator.

### Example

```lua
{  
  "jsonrpc": "2.0",   
  "method": "StatusGet",   
  "id": 1234,  
  "params": 0  
}
```

### Response

```lua
{
  "jsonrpc":"2.0", 
  "id":1234
  "result":{ 
    "Platform":"Core 510i", 
    "State":"Active",
    "DesignName":"SAFâMainPA", 
    "DesignCode":"qALFilm6IcAz", 
    "IsRedundant":false, 
    "IsEmulator":true, 
    "Status":{
      "Code":0 
      "String":"OK"
    }
  }
}
```

[Control Methods](javascript:void(0))

Use these methods to get and set Named Control values.

[Control.Get](javascript:void(0))

Specify an array of Named Control strings, receive an array of control values.

### Parameters

Array of Named Control strings, e.g.:

["*Named\_Control\_Name*", "*Named\_Control\_Name*"]

### Response

`Name` : Name of the control, relative to the component.

`Value` : The value of the control. This can be a number, string, or boolean.

`String` : String representation of the control.

### Example 1: Single Named Control

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "Control.Get",  
  "params": ["MainGain"]  
}
```

#### Response

```lua
{
  "jsonrpc": "2.0",
  "id": 1234,
  "result": [
    {
      "Name": "MainGain", 
      "Value": â12
    }
  ]
}
```

### Example 2: Multiple Named Controls

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method":  "Control.Get",   
  "params": ["MainGain", "MainMute"]  
}
```

#### Response

```lua
{
  "jsonrpc": "2.0",
  "id": 1234,
  "result": [
    {
      "Name": "MainGain", 
      "Value": â12 
      "String" : "â12.0dB"
    },
    {
      "Name": "MainMute", 
      "Value": false, 
      "String" : "Unmuted"
    }
  ]
}
```

[Control.Set](javascript:void(0))

Set a control's value. Specify a single control name, value, and optional ramp time.

### Parameters

`Name` : Name of the control, relative to the component.

`Value` : The value of the control. This can be a number, string, or boolean.

`Ramp` : (Optional) The ramp time used to set the control.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "Control.Set",   
  "params": {  
    "Name": "MainGain",   
    "Value": â12  
  }  
}
```

[Component Control Methods](javascript:void(0))

Use these methods to get and set controls within Named Components, or obtain a list of all Named Components in a design.

[Component.Get](javascript:void(0))

Returns the values of one or more specified controls within a specified Named Component.

### Parameters

`Name` : The name of the named component.

`Controls` : An array of control values.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "Component.Get",   
  "params": {  
    "Name": "My APM",  
    "Controls": [  
      { "Name": "ent.xfade.gain" }  
    ]  
  }  
}
```

#### Response

```lua
{
  "jsonrpc": "2.0", 
  "result": {
    "Name": "My APM",
    "Controls": [
    {
      "Name": "ent.xfade.gain", 
      "Value": â100.0,
      "String": "â100.0dB" 
      "Position": 0
    }
    ]
  }
}					
```

[Component.GetControls](javascript:void(0))

Returns a table of all controls and their values in a specified Named Component.

### Parameters

`Name` : The name of the named component.

### Example

```lua
{  
    "jsonrpc": "2.0",  
    "id": 1234,  
    "method": "Component.GetControls",  
    "params": {  
        "Name": "MyGain"  
    }  
}
```

#### Response

```lua
{
 "jsonrpc": "2.0",
 "result": {
   "Name": "MyGain",
   "Controls": [
     {
       "Name": "bypass",
       "Type": "Boolean",
       "Value": false,
       "String": "no",
       "Position": 0.0,
       "Direction": "Read/Write"
	 },
	 {
	   "Name": "gain",
	   "Type": "Float",
	   "Value": 0.0,
	   "ValueMin": -100.0,
	   "ValueMax": 20.0,
	   "StringMin": "-100dB",
	   "StringMax": "20.0dB",
	   "String": "0dB",
	   "Position": 0.83333331,
	   "Direction": "Read/Write"
	 },
	 {
	   "Name": "invert",
	   "Type": "Boolean",
	   "Value": false,
	   "String": "normal",
	   "Position": 0.0,
	   "Direction": "Read/Write"
	 },
	 {
	   "Name": "mute",
	   "Type": "Boolean",
	   "Value": false,
	   "String": "unmuted",
	   "Position": 0.0,
	   "Direction": "Read/Write"
	 }
   ]
 },
 "id": 1234
}
```

[Component.Set](javascript:void(0))

Set one or more controls for a single named component. Returns a list of unknown controls after processing.

### Parameters

`Name` : The name of the named component.

`Controls` : An array of control values.

`ResponseValues` : (optional). Can be set to either `true` or `false`. When set to `true`, the response will return the new Values of the controls.

### Example 1: Set a single control

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "Component.Set",   
  "params": {  
    "Name": "My APM",  
    "Controls": [  
      {  
        "Name": "ent.xfade.gain",   
        "Value": â100.0,  
        "Ramp": 2.0  
      }  
    ]  
  }  
}
```

### Example 2: Set multiple controls

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "Component.Set",   
  "params": {  
    "Name": "My APM",  
    "Controls": [  
      {  
        "Name": "ent.xfade.gain",   
        "Value": â100.0,  
        "Ramp": 2.0  
      },  
      {  
        "Name": "bgm.xfade.gain",   
        "Value": 0.0,  
        "Ramp": 1.0  
      }  
    ]  
  }  
}
```

### Example 3: Setting `ResponseValues` to `True`

```lua
=> {  
  "jsonrpc": "2.0",  
  "method": "Component.Set",  
  "params": {  
    "Name": "Gain",  
    "ResponseValues": true,  
    "Controls": [  
      {  
        "Name": "gain",  
        "Value": -10,  
        "Ramp": 0  
      }  
    ]  
  },  
  "id": 101  
}  
  
<= {  
  "jsonrpc": "2.0",  
  "result": [  
    {  
      "Component": "Gain",  
      "Name": "gain",  
      "String": "-10.0dB",  
      "Value": -10,  
      "Position": 0.75  
    }  
  ],  
  "id": 101  
}
```

[Component.GetComponents](javascript:void(0))

Get a list of all named components in a design, along with their type and properties.

### Parameters

NA

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "method": "Component.GetComponents",   
  "params": "test",  
  "id": 1234  
}
```

#### Response

```lua
{
 "jsonrpc": "2.0", 
 "result": [
   {
    "ID": "MyGain",
    "Name": "MyGain", 
    "Type": "gain", 
    "Properties": [
      {
       "Name": "max_gain",
       "Value": 20,
       "PrettyName": "Max Gain (dB)"
      },
      {
       "Name": "min_gain",
       "Value": "-100",
       "Pretty Name": Min Gain (dB)"
      },
      {
       "Name": "enable_stepper",
       "Value": "False",
       "PrettyName": "Enable Ramp Controls"
      },
      {
       "Name": "num_steps",
       "Value": "8",
       "PrettyName": "Number of Steps"
      },
      {
       "Name": "multi_channel_count",
       "Value": "8",
       "PrettyName": "Count"
      }
    ],
    "Controls": null,
    "ControlSource": 2
   }
  ],
  "id": 1234
}
```

The table contains the following fields:

#### Name

The Code Name of the Named Component.

#### ID

This also contains the Code Name of the Named Components returned by `Component.GetComponents()`, `Name` and `ID` are in this context, identical. Both fields do not imply different behavior.

#### Type

A string that identifies the component's class / type. Instances of the same component class share the same `Type` value. The exact format of this string may vary depending on where the component comes fromâbuilt-in, plugin, extension.

#### ControlSource

This field is primarily used for internal diagnostics and not needed in scripts.

#### Controls

Not usable by Lua scripts.

#### Properties

Table of properties of the named component that are set in Designer at design time. Values can be read, but not changed by a script.

[Change Group Methods](javascript:void(0))

Use these methods to create, manipulate, and poll change groups.

**Note:** There is a maximum limit of four change groups, but there is no restriction on the number of controls within a change group

[ChangeGroup.AddControl](javascript:void(0))

Create a change group and/or add controls to a change group via Named Controls.

### Parameters

`Id` : Change group ID.

`Controls` : Array of control names.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.AddControl",   
  "params": {  
    "Id": "my change group",   
    "Controls" : [  
      "some control", "another control"  
    ]  
  }  
}
```

[ChangeGroup.AddComponentControl](javascript:void(0))

Create a change group and/or add controls to a change group via a Named Component.

### Parameters

`Id` : Change group ID.

`Component` : Named Component name and array of controls.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.AddComponentControl",   
  "params": {  
    "Id": "my change group",   
    "Component" : {  
      "Name": "My Component",   
      "Controls": [  
        { "Name": "gain" },  
        { "Name": "mute" }  
      ]  
    }  
  }  
}
```

[ChangeGroup.Remove](javascript:void(0))

Remove controls from a change group via Named Controls. Returns a list of unknown controls after processing.

### Parameters

`Id` : Change group ID.

`Controls` : Array of control names.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.Remove",   
  "params": {  
    "Id": "my change group"   
    "Controls" : [  
      "some control"  
    ]  
  }  
}
```

[ChangeGroup.Poll](javascript:void(0))

Poll a change group.

### Parameters

`Id` : Change group ID.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.Poll",   
  "params": {  
    "Id": "my change group"  
  }  
}
```

#### Response

```lua
{
  "jsonrpc": "2.0",
  "id": 1234,
  "result": {
    "Id": "my change group", 
    "Changes": [
      { // Named control return value 
      "Name": "some control", 
      "Value": â12
      "String": "â12dB"
      },
      { // Named component return value 
      "Component": "My Component", 
      "Name": "gain",
      "Value": â12 
      "String": "â12dB"
      }
    ]
  }
}
```

[ChangeGroup.Destroy](javascript:void(0))

Destroy a change group.

### Parameters

`Id` : Change group ID.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.Destroy",   
  "params": {  
    "Id": "my change group"  
  }  
}
```

[ChangeGroup.Invalidate](javascript:void(0))

Invalidates a change group, which causes all controls to be resent.

### Parameters

`Id` : Change group ID.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.Invalidate",   
  "params": {  
    "Id": "my change group"  
  }  
}
```

[ChangeGroup.Clear](javascript:void(0))

Clears a change group, which removes all controls.

### Parameters

`Id` : Change group ID.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.Clear",   
  "params": {  
    "Id": "my change group"  
  }  
}
```

[ChangeGroup.AutoPoll](javascript:void(0))

Set up automatic polling.

### Parameters

`Id` : Change group ID.

`Rate` : The polling interval, in seconds.

### Example

Configure automatic polling to receive a response every 5 seconds:

```lua
{  
  "jsonrpc": "2.0",  
  "id": 1234,  
  "method": "ChangeGroup.AutoPoll",   
  "params": {  
    "Id": "my change group",   
    "Rate": 5  
  }  
}
```

#### Response

```lua
{
  "jsonrpc": "2.0",
  "id": 1234,
  "result": {
    "Id": "my change group", 
    "Changes": [
      { // Named control return value 
        "Name": "some control", 
        "Value": â12
        "String": "â12dB"
      },
      { // Named component return value 
        "Component": "My Component", 
        "Name": "gain",
        "Value": â12 
        "String": "â12dB"
      }
    ]
  }
}
```

[Mixer Control Methods](javascript:void(0))

Use the mixer control API methods to set mixer input and output parameters.

### String Syntax

The mixer control API uses a string specification to determine to which inputs and outputs to apply changes. The syntax supports space- or comma-separated numbers, ranges of numbers, all numbers (\*), and negation of a selection with the ! operator. For example:

|  |  |
| --- | --- |
| \* | everything |
| 1 2 3 | channels 1, 2, 3 |
| 1-6 | channels 1 through 6 |
| 1-6 9 | channels 1 through 6 and 9 |
| 1-3 5-9 | channels 1 through 3 and 5 through 9 |
| 1-8 !3 | channels 1 through 8 except 3 |
| \* !3-5 | everything but 3 through 5 |

### Methods

[Mixer.SetCrossPointGain](javascript:void(0))

Set the crosspoint gain value for specified mixer inputs and outputs over an optional ramp time.

### Parameters

`Name` : Name of the mixer.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Outputs` : String specification of mixer outputs. See [String Syntax](#Input).

`Value` : The gain value to set.

`Ramp` : Ramp time to use for setting the gain value.

### Example

Set all crosspoints on a mixer to -100dB over 5 seconds.

```lua
{  
  "jsonrpc": "2.0",  
  "method": "Mixer.SetCrossPointGain",   
  "id": 1234,  
  "params": {  
    "Name": "Parade",  
    "Inputs": "*",  
    "Outputs": "*",  
    "Value": â100.0,  
    "Ramp": 5.0  
  }  
}
```

[Mixer.SetCrossPointDelay](javascript:void(0))

Set the crosspoint delay value for specified mixer inputs and outputs over an optional ramp time.

### Parameters

`Name` : Name of the mixer.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Outputs` : String specification of mixer outputs. See [String Syntax](#Input).

`Value` : The delay value to set.

`Ramp` : Ramp time to use for setting the delay value.

[Mixer.SetCrossPointMute](javascript:void(0))

Enable or disable crosspoint muting for specified mixer inputs and outputs.

### Parameters

`Name` : Name of the mixer.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Outputs` : String specification of mixer outputs. See [String Syntax](#Input).

`Value` : The boolean mute value to set.

[Mixer.SetCrossPointSolo](javascript:void(0))

Enable or disable crosspoint solo for specified mixer inputs and outputs.

### Parameters

`Name` : Name of the mixer.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Outputs` : String specification of mixer outputs. See [String Syntax](#Input).

`Value` : The boolean solo value to set.

[Mixer.SetInputGain](javascript:void(0))

Set the gain value for specified mixer inputs over an optional ramp time.

### Parameters

`Name` : Name of the mixer.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Value` : The input gain value to set.

`Ramp` : Ramp time to use for setting the input gain value.

[Mixer.SetInputMute](javascript:void(0))

Enable or disable muting for specified mixer inputs.

### Parameters

`Name` : Name of the mixer.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Value` : The boolean input mute value to set.

### Example

Mute inputs 4-6:

```lua
{  
  "jsonrpc": "2.0",  
  "method": "Mixer.SetInputMute",   
  "params": {  
    "Name": "Parade",   
    "Inputs": "4â6",   
    "Value": true,  
    "Ramp": 0.0  
  },  
  "id": 1234  
}
```

[Mixer.SetInputSolo](javascript:void(0))

Enable or disable solo for specified mixer inputs.

### Parameters

`Name` : Name of the mixer.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Value` : The boolean input solo value to set.

[Mixer.SetOutputGain](javascript:void(0))

Set the gain value for specified mixer outputs over an optional ramp time.

### Parameters

`Name` : Name of the mixer.

`Outputs` : String specification of mixer outputs. See [String Syntax](#Input).

`Value` : The output gain value to set.

`Ramp` : Ramp time to use for setting the output gain value.

[Mixer.SetOutputMute](javascript:void(0))

Enable or disable muting for specified mixer outputs.

### Parameters

`Name` : Name of the mixer.

`Outputs` : String specification of mixer outputs. See [String Syntax](#Input).

`Value` : The boolean output mute value to set.

[Mixer.SetCueMute](javascript:void(0))

Enable or disable muting for specified mixer cues.

### Parameters

`Name` : Name of the mixer.

`Cues` : String specification of mixer cues.

`Value` : The boolean cue mute value to set.

[Mixer.SetCueGain](javascript:void(0))

Set the gain value for specified mixer cues over an optional ramp time.

### Parameters

`Name` : Name of the mixer.

`Cues` : String specification of mixer cues.

`Value` : The cue gain value to set.

`Ramp` : Ramp time to use for setting the cue gain value.

[Mixer.SetInputCueEnable](javascript:void(0))

Enable or disable cues for specified mixer inputs.

### Parameters

`Name` : Name of the mixer.

`Cues` : String specification of mixer cues.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Value` : The boolean cue enable value to set.

[Mixer.SetInputCueAfl](javascript:void(0))

Enable or disable cue AFL (After Fader Level) for specified mixer inputs.

### Parameters

`Name` : Name of the mixer.

`Cues` : String specification of mixer cues.

`Inputs` : String specification of mixer inputs. See [String Syntax](#Input).

`Value` : The boolean cue AFL value to set.

[Loop Player Control Methods](javascript:void(0))

Use the Loop Player control API methods to queue up file playback into a named Loop Player.

**Note:** In all Loop Player commands, there is a `Log` option that allows you to set it to `true` or `false`. This option enables Event Log logging for the command.

[LoopPlayer.Start](javascript:void(0))

Start audio playback.

### Parameters

`Name` : The name of the Loop Player.

`StartTime` : The time of day, in seconds, to start the job.

`Files` : Array of file specifications, including:

`Name` : Name of the file to play.

`Mode` : mono | stereo

`Output` : The Loop Player output number for playback.

`Loop` : If true, file playback loops.

`RefID`: If provided, a notification will be sent when a job has failed in some way. The error will be visible in the [Event Log](../../Core_Manager/Event_Log.htm) to make sense of what job failed. Additionally, the error will also be shown in the [Q-SYS Remote Control Protocol (QRC)](QRC_Overview.htm).

`Seek` : The optional time, in seconds, to seek into each file before playback.

### LoopPlayer.Start Example

```lua
{  
  "jsonrpc": "2.0",  
  "method": "LoopPlayer.Start",   
  "params": {  
    "Files": [  
      {  
        "Name": "Audio/mainloop.wav",   
        "Mode": "mono",  
        "Output": 1  
      }  
    ],  
    "Name": "test",   
    "StartTime": 62600,   
    "Loop": false,   
    "Log": true  
  },  
  "id": 1234  
}
```

### LoopPlayer.Error Example

```lua
{  
  "jsonrpc": "2.0",  
  "method": "LoopPlayer.Error",   
  "params": {   
    "Error": "JobInPast",   
    "RefId": <Insert_id_from_LoopPlayer>,   
  }  
}
```

[LoopPlayer.Stop](javascript:void(0))

Stop audio playback for specified outputs.

### Parameters

`Name` : The name of the Loop Player.

`Outputs` : The Loop Player output numbers for which to stop playback.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "method": "LoopPlayer.Stop",   
  "params": {  
    "Name": "test",  
    "Outputs": [ 1, 3, 4 ],   
    "Log": true  
  },  
  "id": 1234  
}
```

[LoopPlayer.Cancel](javascript:void(0))

Cancel audio playback for specified outputs.

### Parameters

`Name` : The name of the Loop Player.

`Outputs` : The Loop Player output numbers for which to stop playback.

### Example

```lua
{  
  "jsonrpc": "2.0",  
  "method": "LoopPlayer.Cancel",   
  "params": {  
    "Name": "test",  
    "Outputs": [ 1, 3, 4 ],   
    "Log": true  
  },  
  "id": 1234  
}
```

[Snapshot Methods](javascript:void(0))

Use these methods to load and save snapshots.

[Snapshot.Load](javascript:void(0))

Load control settings from a specified snapshot bank and number with an optional ramp time.

### Parameters

`Name` : String. The name of the snapshot bank from which to load the snapshot. This is the name given to the bank when it was created in Q-SYS Designer Software.

`Bank` : Integer. Identifies a snapshot within a snapshot bank. The range is 1 to the number of snapshots in the bank, inclusive.

`Ramp` : Double. Optional argument, in seconds, for specifying the ramp time when loading the snapshot.

### Example

From a snapshot bank called "MySpecialBank", load control settings from snapshot # 7 with a ramp time of 8.5 seconds...

```lua
{  
  "jsonrpc": "2.0",  
  "method": "Snapshot.Load",   
  "params": {  
    "Name": "MySpecialBank",  
    "Bank": 7,   
    "Ramp": 8.5  
  },  
  "id": 1234  
}
```

[Snapshot.Save](javascript:void(0))

Save control settings to a specified snapshot bank and number.

### Parameters

`Name` : String. The name of the snapshot bank to which to save the snapshot. This is the name given to the bank when it was created in Q-SYS Designer Software.

`Bank` :  Integer. Identifies a snapshot within a snapshot bank. The range is 1 to the number of snapshots in the bank, inclusive.

### Example

Save control settings to a snapshot bank called "MyVerySpecialBank" to snapshot # 4.

```lua
{  
  "jsonrpc": "2.0",  
  "method": "Snapshot.Save",   
  "params": {  
    "Name": "MyVerySpecialBank",  
    "Bank": 4,   
  },  
  "id": 1234  
}
```

[Error Code Reference](javascript:void(0))

These codes can be returned as the code value in a JSON-RPC error object.

| Code | Details |
| --- | --- |
| -32700 | Parse error. Invalid JSON was received by the server. |
| -32600 | Invalid request. The JSON sent is not a valid Request object. |
| -32601 | Method not found. |
| -32602 | Invalid params. |
| -32603 | Server error. |
| -32604 | Core is on Standby. This code is returned when a QRC command is received while the Core is not the active Core in a redundant Core configuration. |
| 2 | Invalid Page Request ID |
| 3 | Bad Page Request - could not create the requested Page Request |
| 4 | Missing file |
| 5 | Change Groups exhausted |
| 6 | Unknown change croup |
| 7 | Unknown component name |
| 8 | Unknown control |
| 9 | Illegal mixer channel index |
| 10 | Logon required |
