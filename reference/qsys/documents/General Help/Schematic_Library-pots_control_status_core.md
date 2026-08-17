# POTS Controller

> Source: https://help.qsys.com/Content/Schematic_Library/pots_control_status_core.htm

# POTS Controller

The POTS Controller component controls the features of the Q-SYS interface with a Plain Old Telephone Service (POTS).

If you are connecting to an analog phone system, you can connect from the wall RJ-11 jack directly to Q-SYS hardware supporting a POTS connection:

* The [Core 110f](../Hardware/Processing/Core_110f.htm) and [Core 110c](../Hardware/Processing/Core_110c.htm) provide a single RJ-11 telephone connection.
* The [CTEL4 â Analog Telephony Card](../Hardware/IO_Expanders/CTEL4.htm) provides four RJ-11 telephone connections.
* The [QIO-TEL2](../Hardware/IO_Expanders/QIO-TEL2.htm) provides two RJ-11 telephone connections.

If you are connecting to a digital system, you can use an FXO Gateway that has an analog POTS connection and a network connection.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

[Dialer Tab](javascript:void(0))

### Dialing

#### Dial String

The number of the phone or device you are calling. This number is a numeric text string entered by either the Keypad, keyboard, or using the Dial String Control Pin.

#### Backspace Key

The Backspace key deletes the last character typed, and can continue deleting one character at a time.

#### X (Clear Key)

The clear key (X) clears the entire Outgoing dial digits field.

#### Progress

Displays the CID number, the CID name (if available), and the call status of the incoming call. (You can display these separately using the corresponding Control pins.)

For an outgoing call this field shows the current state of the call, for example, Dialing, Line Fault - Disconnected, waiting for dial tone, and so on.

#### DND (do not disturb)

Activating the DnD feature causes Q-SYS to ignore any incoming calls. If connected to an IP-PBX, that system handles the response given to the incoming caller. For example, busy signal, message, and so on.

#### Disconnect (hang up)

Press this button to disconnect the call.

#### Connect (Dial / Answer)

Enter the Outgoing dial string then press this button to initiate the call. If there is an incoming call, press this button to answer the call.

#### Off Hook LED

This LED indicates that your call is active. It lights when the call is connected, and goes off when you press the Hang Up key or the line is disconnected.

#### Ringing LED

LED indicates that there is an incoming call.

#### Call Control Call Connect Time

Digital readout of the time the call has been connected.

#### Hook Flash

Click the button for a quick off-hook/on-hook/off-hook cycle. The result of the hook flash is determined by the phone company.

If your phone company office is configured for 3-way calling, push this button to initiate a 3-way call.

#### Auto Answer

Enables and disables the Auto Answer feature. The button illuminates when the feature is active.

#### After # Rings

This parameter sets the number of rings before the Auto Answer feature answers the call.

**Note:** This control acts like a knob - click and drag to change, or key in the number of rings.

### Keypad

#### Keypad

This is a standard 12-key numeric keypad used to key in the Outgoing dial digits, or send DTMF while off hook. For example, you can enter additional numbers to navigate an answering system.

### Recent Calls

#### Recent Calls

List of recent calls, up to 100 maximum. The list includes the dialed digits, incoming / outgoing icon, caller ID if available, and number of calls to / from the same number.

* Blue = Outgoing
* Green = Incoming
* Red = Call failed

#### Clear

Clears the list of Recent Calls

### Status

#### Status LED

Multi-color LED giving the status of the Softphone.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

[Control Tab](javascript:void(0)) 

### Control

#### Loop Drop Auto Hangup

If the call is disconnected for reasons outside of Q-SYS, then the call is automatically disconnected. If Auto Hangup is not enabled, the line stays open.

#### Call Progress Auto Hangup

If an outgoing call is not answered, for example a busy signal, the call is automatically disconnected. If Auto Hangup is not enabled, the line stays open.

#### Hook Flash Time (ms)

Determines the length of time the system is off hook when the hook flash is initiated.

#### Dial Tone Gain (dB)

Controls the audio level of the dial tone when the phone is off hook.

#### DTMF Transmit Level (dBm)

The level of the DTMF high frequencies.

* Read only.
* This level is -8 dB to +4 dB relative to the level of the low-group frequency.
* This value changes depending on the Telephone Country selected.

#### DTMF Transmit Level Twist

The level of the DTMF low frequencies.

* Read only.
* This value changes depending on the Telephone Country selected.

#### DTMF Tone Duration

The duration of the DTMF tone being sent.

Read only.

#### DTMF Pause Duration

The pause duration between transmissions of DTMF tones.

Read only.

### Ring Tone

#### Enable

Enables the ring tone for incoming calls.

This also configures the ring-back tone on outgoing calls. If the far end of the outgoing call provides a ring tone, that tone overrides this configuration.

#### Gain (dB)

Sets the level of the incoming call ring tone and, for outgoing calls, this sets the level of the ring-back tone.

#### Filename

Specifies the file to play for the incoming call's ring tone, and outgoing call's ring-back tone.

### Entry Tone

#### Enable

Enables the entry tone for incoming calls.

The entry tone indicates that the incoming call has been Auto-answered.

#### Gain (dB)

Sets the level of the incoming call entry tone.

#### Filename

Specifies the file to play for the incoming call's entry tone.

### Exit Tone

#### Enable

Enables the exit tone for incoming calls.

The exit tone indicates that the incoming call has been disconnected (hung up).

#### Gain (dB)

Sets the level of the incoming call exit tone.

#### Filename

Specifies the file to play for the incoming call's exit tone.

### Keypad Tone

#### Enable

Enables the playback of the DTMF digits sent from your Core as keypad tones.

#### Tone Gain

Sets the level of the keypad tones.

#### Filename

Specifies the file to play keypad tones.

[Status Tab](javascript:void(0))

#### Line Voltage

The voltage on the transmit / receive line. If the line is unplugged, the voltage is 0.00 - an open circuit.

#### Line Current

The current present on the transmit / receive line. If the line is unplugged, the current is 0.00 an open circuit.

#### Line Fault (reason)

Text field displaying the reason for the line-fault indication. For example: Line Fault - Line disconnected.

#### Line Fault

Red LED indicating there is a line fault.

#### Line Ready

Green LED indicating the line is ready to be used.

#### Line in Use

Amber LED indicating the line is in use.

#### Line Intrusion

Red LED indicating that another telephone, on the same line, is off hook.

#### Dial In Progress

Yellow LED indicating a number is being dialed.

#### Dial Tone

Blue LED indicating that a dial tone is present.

#### Busy Tone

Blue LED indicating that the party called is on the phone. A busy signal is present.

#### Ring(back) Tone

Blue LED indicating that dialed party's phone is ringing. The ring-back tone is typically supplied by the telephone service carrier.

#### Disconnect Tone

Blue LED indicating the call has been disconnected.

#### Call Waiting

Amber LED indicating that an incoming call is waiting to be answered.

#### DTMF Rx

Last five DTMF characters received.

#### Event Logging

Enables or disables Event Logging.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Call Control | | | | |
| Auto Answer | 0  1 | off  on | 0  1 | Input / Output |
| Auto Answer Rings | 0 to 99 | 0 to 99 | 0.00 to .99 | Input / Output |
| Connect | Trigger | | | Input / Output |
| Dial String | Text | | | Input / Output |
| Disconnect | Trigger | | | Input / Output |
| Do Not Disturb | 0  1 | off  on | 0  1 | Input / Output |
| Hook Flash | Trigger | | | Input / Output |
| Call History | | | | |
| Clear Call History | Trigger | | | Input / Output |
| Recent Calls | Text List | | | Input / Output |
| Call Status | | | | |
| Caller ID Date/Time  Incoming only. Date (01/01) and Time (24 hr) | Text | | | Output |
| Caller ID Name  Incoming only. | Text | | | Output |
| Caller ID Number  Incoming only. | numeric value of the calling number | Text | N / A | Output |
| Connect Time | Text | | | Output |
| Details | Text | | | Output |
| Off Hook | 0  1 | false  true | 0  1 | Output |
| Progress | Text | | | Output |
| Ring (trigger} | Trigger | | | Output |
| Ringing (state}  Incoming calls only. Cycles between true / false. | 0  1 | false  true | 0  1 | Output |
| State  Used to determine the current state of a call. | inactive  incoming  outgoing  active | | | Output |
| Configuration | | | | |
| Call Progress Auto Hangup | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Dial Tone Gain  (dB) | -100 to 0 | -100dB to 0dB | 0.00 to 1.00 | Input / Output |
| Entry Tone Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Entry Tone Filename | Text | | | Input / Output |
| Entry Tone Gain | -100 to 0 | -100dB to 0dB | 0.00 to 1.00 | Input / Output |
| Exit Tone Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Exit Tone Filename | Text | | | Input / Output |
| Exit Tone Gain | -100 to 0 | -100dB to 0dB | 0.00 to 1.00 | Input / Output |
| Hook Flash Time | 0.050  to  0.500 | 50.0ms  to  500ms | 0.00  to  1.00 | Input / Output |
| Keypad Tone Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Keypad Tone Filename | Text | | | Input / Output |
| Keypad Tone Gain | -100 to 0 | -100dB to 0dB | 0.00 to 1.00 | Input / Output |
| Loop Drop Auto Hangup | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Ringing Tone Enable | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Ringing Tone Filename | Text | | | Input / Output |
| Ringing Tone Gain | -100 to 0 | -100dB to 0dB | 0.00 to 1.00 | Input / Output |
| DTMF | | | | |
| Rx | Text | | | Output |
| Rx # | When a DTMF character is received, the output of the control pin is a text display of "yes" for the DTMF character received. Otherwise the output is "no". | | | Output |
| Rx \* | Output |
| Rx 0 | Output |
| Rx 1 | Output |
| Rx 2 | Output |
| Rx 3 | Output |
| Rx 4 | Output |
| Rx 5 | Output |
| Rx 6 | Output |
| Rx 7 | Output |
| Rx 8 | Output |
| Rx 9 | Output |
| Rx A | Output |
| Rx B | Output |
| Rx C | Output |
| Rx D | Output |
| Rx Any | Displays "yes" when any DTMF character is received. | | | Output |
| Tx | Text | | | Input / Output |
| Line Status | | | | |
| Busy Tone | 0  1 | no  yes | 0  1 | Output |
| Call Waiting | 0  1 | no  yes | 0  1 | Output |
| Current | *n* | *n*A | 0.00 to 1.00 | Output |
| Dial In Progress | 0  1 | no  yes | 0  1 | Output |
| Dial Tone | 0  1 | no  yes | 0  1 | Output |
| Disconnect Tone | 0  1 | no  yes | 0  1 | Output |
| Fault | 0  1 | no  yes | 0  1 | Output |
| Fault Message | Text | | | Output |
| In Use | 0  1 | no  yes | 0  1 | Output |
| Intrusion | 0  1 | no  yes | 0  1 | Output |
| Ready | 0  1 | no  yes | 0  1 | Output |
| Ring(back) Tone | 0  1 | no  yes | 0  1 | Output |
| Voltage | *n* | *n*V | 0.00 to 1.00 | Output |
| PinPad | | | | |
| # | Trigger-input to Dial String | | | Input / Output |
| \* | Input / Output |
| 0 | Input / Output |
| 1 | Input / Output |
| 2 | Input / Output |
| 3 | Input / Output |
| 4 | Input / Output |
| 5 | Input / Output |
| 6 | Input / Output |
| 7 | Input / Output |
| 8 | Input / Output |
| 9 | Input / Output |
| Backspace | Input / Output |
| Clear | Input / Output |
| Event Logging | 1  0 | enabled  disabled | 1  0 | Input / Output |
| Simulate incoming call | 0  1 | false  true | 0  1 | Input / Output |
| Status | Text describing the current status of the Q-SYS POTS system. | | | Output |
