# Control Link

> Source: https://help.qsys.com/Content/Schematic_Library/project_link.htm

# Control Link

The Control Link component allows you to link controls from different designs running on Cores on the same Q-LAN or other specified network. Control linking works on a server / client basis. You can have one server, and many clients. The server and client(s) are identified by the Direction, and linked based on the Link Name given them in the components properties. You place a server Control Link in one design, and the client Control Link in the other, both configured with the same controls. The easiest way to do this is to configure one component then copy and paste into the other, making sure you change the Direction property to the correct direction. Once the two are linked, their controls are linked and follow which ever one changes. If a control has a different value in the client than the value in the server, the control in the server takes precedence.

When you initially place a Control Link in the schematic, and open the Control Panel, there are no controls. You must add the controls from the list provided in the component's properties.

**Note:** Emulation mode does not support Control Link.

[Control Link Characteristics](javascript:void(0))

### Control Link Component Characteristics

* The Control Link component has only Control input and output, no audio inputs or outputs.
* You can create a Control Link component with the type and number of controls you want.
* Controls of the same type are in Groups. You cannot have duplicate Groups in the same Component.
* You can have up to 10 different types, or Groups, of controls.
* Each Group can have up to 256 controls (of the same type).
* Each Group can have a different number of controls.
* You can give a label to the Control Link component by selecting the component in the Schematic and simply start typing and press enter or click off of the component when you're finished. You cannot "edit" the label once it has been entered, but you can replace the label in the same way it was entered initially.

### Control Characteristics

* Trigger controls are only sent from a client to the server.
* Meter controls and LEDs are only sent from the server to the client.
* Text displays are sent only from the server to the client.
* Text controls are not available.
* All other controls are peers, meaning you can adjust the control in either design and it will change in the other.
* If a control value differs when the client connects to the server, the server's value will propagate to the client.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Control Link Properties

#### Link Name

The name given to the server and client Control Link components. This name is used by the server to advertise, and the client to discover over the Q-LAN network.

#### Direction

Identifies the Control Link component as a Server or Client.

#### Specify Server IP Address

When direction is set to Client, setting to Yes allows the user to define the server IP to receive from.

#### Server IP Address

Used to enter the specified server IP. This allows the client server relationship to communicate across other LAN connections (having differing IP scopes). Q-SYS Designer allows up to four (4) IP Addresses and cycles through them if it fails. This is best used with a remote Core or Redundant pair of Cores and it will cycle through them until it finds one that connects.

#### Redundant Network

Set this control to Yes if your Cores are on a redundant network, to No if they are not. When operating redundantly, it actively seeks out both LAN A and LAN B connections, when not, only LAN A is considered. However, the control link connection is only functional for LAN A to LAN A connections or LAN B to LAN B connections.

#### Type

Selects the type of control for the Group. See [Controls](#Controls) for allowable values.

Initially, there is only one Group visible. When you select a Type for the first Group, a second Group is displayed, and so on until you have 10 Groups.

When you select a Type, Control Pins for each control of that Type, display below the Component in the Schematic, and below the Properties in the Control Pins Section.

#### Count

Selects the number of controls for the Group, from 1 to 256. Each Group can have a different Count.

#### Default range message

Some of the Control Types have variable ranges. See [Controls](#Controls) for allowable values. This message gives the default range for the specific Control. If there is no range, as with a Toggle Button, there is no message.

#### Customize range

Specifies if you want to customize the Control's range or not.

#### Minimum

If you set the Customize Range to Yes, enter the minimum of the desired range.

#### Maximum

If you set the Customize Range to Yes, enter the maximum of the desired range.

[Controls](javascript:void(0))

| Type | Default / Range | Custom | |
| --- | --- | --- | --- |
| Minimum | Maximum |
| Distance knob  (meters) | 0 to 100 | 0 | 999 |
| Frequency knob  (Hz) | 20 to 20000 | 0.1 | 20000 |
| Generic float knob | 0 to 1 | -1,000,000,000 | 1,000,000,000 |
| Generic integer knob | 0 to 1 | -2,147,483,648 | 2,147,483,647 |
| LED | Off / On | â | â |
| Level fader w/taper  (dBFS) | -100 to 20 | â | â |
| Level knob  (dBFS) | -100 to 20 | -100 | 100 |
| Meter  (dB) | -100 to 20 | â | â |
| Momentary button  (Click, hold, release) | Off / On | â | â |
| Mute button  (Toggle) | Off / On | â | â |
| Pan Knob | -1 to 1 | â | â |
| Percent knob (%) | 0 to 100 | 0 | 100 |
| Position knob | 0 to 1 | â | â |
| Status Display | â | â | â |
| Text display | â | â | â |
| Time knob (seconds) | 0 to 1 | 0 | 999 |
| Toggle button | Off / On |  |  |
| <Remove > (Can only be used on the last in list) | â | â | â |

[Control Pins](javascript:void(0))

**Note:** The values in the following table are taken at the default setting of the Control.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Frequency knob  (Hz) | 0 to 25 and Infinity | 10 Hz to 20.0 kHz | 0.00 to 1.00 | Input / Output |
| Generic float knob | 0 to 1 | 0 to 1.00 | 0.00 to 1.00 | Input / Output |
| Generic integer knob | 0  1 | 0 or 1 | 0  1 | Input / Output |
| LED | 0  1 | false  true | 0  1 | Input / Output |
| Level fader  (dBFS) | -100 to 20 | -100dB to 20.0dB | 0.00 to 1.00 | Input / Output |
| Level knob  (dBFS) | -100 to 20 | -100dB to 20.0dB | 0.00 to 1.00 | Input / Output |
| Meter  (dB) | -100 to 20 | -100dB to 20.0dB | 0.000 (-60 dB)  1.000 | Input / Output |
| Momentary button | 0  1 | false  true | 0  1 | Input / Output |
| Mute button | 0  1 | unmute  mute | 0  1 | Input / Output |
| Pan knob | -1 to 1 | -1.00 to 1.00 | 0.00 to 1.00 | Input / Output |
| Percent knob | 0 to 1 |  | 0 to 1 | Input / Output |
| Position knob | 0 to 1 | â | 0 to 1 | Input / Output |
| Text display | [1](#text_display) | text | [1](#text_display) | Input / Output |
| Time knob  (seconds) | 0.000 to 1.00 | 0 ms to 1 s | 0.000 to 1.00 | Input / Output |
| Toggle button | 0  1 | false  true | 0  1 | Input / Output |
| Trigger button |  |  |  | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. If there is a value/position type input to a Text Display there will be a value, string, and position output as well. If there is a text input, there is no value or position output, only text. | | | | |

[See More Like This](javascript:void(0))

[Core-to-Core Paging](core_to_core_paging.htm): Paging Communication.

[Q-LAN Receiver](input_box.htm) / [Q-LAN Transmitter](output_box.htm): Unicast Audio Streams.

[System Link](system_link.htm): AV Streams & Multicast Audio Streams.
