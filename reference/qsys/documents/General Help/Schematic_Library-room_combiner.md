# Room Combiner

> Source: https://help.qsys.com/Content/Schematic_Library/room_combiner.htm

# Room Combiner

The Room Combiner allows you to take multiple separate sound systems and combine them into one larger sound system. A typical use is when you have multiple rooms (conference, ball, overflow) that can be combined physically or virtually as in the case of an overflow room.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Channel** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Room Combiner component is set to a **Mono** channel, which provides 8 inputs and 8 outputs. Additionally, you can set the Properties to allow for **Stereo**, which gives you Left and Right channel inputs and outputs per Room and Wall Count.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Room Combiner component is set to a **Mono** channel, which provides 8 inputs and 8 outputs. Additionally, you can set the Properties to allow for **Stereo**, which gives you Left and Right channel inputs and outputs per Room and Wall Count.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Room Combiner Properties

#### Rooms

The total number of rooms you can configure, from 2 to 256. There will be one Rooms setting for each room.

#### Walls

The number of walls, from 1 to 256. In most cases, this number should be equal to the number of physical walls that can be removed. For example, if there are three rooms in a row there are two removable walls separating them. Select 2 Walls in the Properties, and Configure them as 1 2, and 2 3. To combine rooms 1 and 2, Open the Wall configured 1 2, to combine 2 and 3, Open 2 3. To combine all three rooms, Open both Walls 1 2 and 2 3. Another example, if there are ten rooms in two rows of five, there would be a total of 13 removable walls. If you select 13 Walls in the Properties, you can combine any adjacent rooms. You may want to add one or two un-configured Walls for unusual cases when they occur.

#### Channels

Sets the type of Channel for each Room, Mono or Stereo.

**Note:** Stereo provides left and right channels for each Room; both channels are controlled by a single set of controls. For example, the Input Gain on Stereo Channels controls both left and right Channels equally.

#### BGM Inputs

The number of inputs for background music (BGM), from 0 to 32.

[Controls](javascript:void(0))

You can hover your mouse cursor over any control to see the name and current setting of that control.

When two or more Rooms are combined, the combined signals are present at all of the Outputs of the combined Rooms. For example, if you have Rooms 1 and 2 combined, the combined signals are present at the Output of Room 1 and the Output of Room 2. The two Outputs are identical.

[Input](javascript:void(0))

This is the input from the room into Q-SYS.

#### Input Mute

The Input Mute button mutes the Input signal from the associated Room only. The Input signal of the muted Room is removed from the Output signal to any Rooms with which the muted room may be combined. You can use this mute when rooms are combined and you will not need one or more of the room's inputs.

If the Link Input Mute button is engaged, the Input Mute buttons of any rooms combined with one another, are linked, and act as one.

#### Input Gain

The Input Gain knob adjusts the Input signal level from the associated Room only, from -100 to 20 dB (default is 0). The Input signal level is adjusted in the Output of any Rooms with which it may be combined.

If the Link Input Gain button is engaged, the Gain controls of any rooms combined with one another, are linked, and act as one.

#### Link Input Mute

Links the Input Mute buttons of any rooms combined with one another. If no rooms are combined, this has no effect.

If rooms are combined, and the Link Input Mute button is not engaged, then later engaged, if the individual room Mute buttons are in different states, they will all be placed in the mute state.

#### Link Input Gain

Links the Input Gain controls of any rooms combined with one another. If no rooms are combined, this control has no effect.

If rooms are combined, and the Link Input Gain button is not engaged, then later engaged, if the individual room Gain controls are at different settings, they all move to the lowest setting.

[BGM](javascript:void(0))

#### Mute

The Mute button mutes the background music (BGM) signal to the associated Room only. The BGM signal of the muted Room is removed from the Output signal of any Rooms with which it may be combined.

If the Link BGM Mute button is engaged, the BGM Mute buttons of any rooms combined with one another, are linked, and act as one.

#### Select

Selects and/or displays which BGM Input goes to which room, from 1 through *n*. You can select the BGM Input by hovering your mouse cursor over the Select text box and entering the BGM Input number (1 through *n*) then press Enter, or simply move your mouse cursor away from the text box.

#### Select Matrix

Select the BGM Input for a room by clicking the Select button (1 through *n*) for that room. The BGM Input number displays in the Select text box.

#### Gain

The BGM Gain knob adjusts the Output signal level to the associated Room only, from -100 to 20 dB (default is 0).

If the Link BGM Gain button is engaged, the BGM Gain controls of any rooms combined with one another, are linked, and act as one.

#### Link BGM Mute

Links the BGM Mute buttons of any rooms combined with one another. If no rooms are combined, this has no effect.

If rooms are combined, and the Link BGM Mute button is not engaged, then later engaged, if the individual room Mute buttons are in different states, they will all be placed in the mute state.

#### Link BGM Select

Links the BGM Select buttons of any rooms combined with one another. If no rooms are combined, this has no effect.

If rooms are combined, and the Link BGM Select button is not engaged, then later engaged, if the individual room Select buttons are at different settings, they all move to the lowest number BGM Input setting.

#### Link BGM Gain

Links the BGM Gain controls of any rooms combined with one another. If no rooms are combined, this has no effect.

If rooms are combined, and the Link BGM Gain button is not engaged, then later engaged, if the individual room Gain controls are at different settings, they all move to the lowest setting.

[Output](javascript:void(0))

The Output controls for a Room affect the signals at the Output for only that Room.

#### Mute

Mutes the signal at the Output of the associated Room, including all Rooms with which it is combined.

#### Gain

Adjusts the signal level at the Output of the associated Room, including the signals of all Rooms with which it is combined, from -100 to 10 dB (default is 0).

#### Link Output Mute

Links the Output Mute buttons of any rooms combined with one another. If no rooms are combined, this has no effect.

If rooms are combined, and the Link Output Mute button is not engaged, then later engaged, if the individual room Mute buttons are in different states, they will all be placed in the mute state.

#### Link Output Gain

Links the Output Gain controls of any rooms combined with one another. If no rooms are combined, this has no effect.

If rooms are combined, and the Link Output Gain button is not engaged, then later engaged, if the individual room Gain controls are at different settings, they all move to the lowest setting.

[BGM Input](javascript:void(0))

The number of background music input controls depends on how many BGM controls are selected in the Room Combiner Properties.

#### Mute

Mutes the BGM Input into the Room Combiner.

#### Gain

Controls the gain of the BGM Input into the Room Combiner, from -100 to 20 dB.

[Wall](javascript:void(0))

A Wall can be physical, as in the case of a large room in a hotel that can be divided into multiple smaller rooms or have the walls removed to create one large room, or it can be virtual as in the case of an overflow room that may or may not have common walls with the main room.

#### Open

When engaged (white), the Wall is opened and the Room numbers listed in the Rooms control are combined. The default position for this button is "closed" or gray.

#### Rooms

In the text box, enter the Room numbers you want combined when a Wall is opened. You can specify Room numbers using a variety of separators:

* Separate individual Room numbers with `<space>`, `+`, or `,`
* Use `-` or `>` to define a range
* Use `*` for "all"
* Use `!` or `~` for "not"

[Example](javascript:void(0))

| Rooms Value | Equals |
| --- | --- |
| `1-4` | 1,2,3,4 |
| `* ! 8` | Everything but 8 |
| `1-5 ~ 2` | 1,3,4,5 |
| `1-4 6>8` | 1,2,3,4,6,7,8 |

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| BGM Input *n* Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.000 | Input / Output |
| BGM Input *n* Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Link BGM Gain | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Link BGM Mute | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Link BGM Select | 0  1 | false  true | 0  1 | Input / Output |
| Room *n* Input Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.000 | Input / Output |
| Room *n* Input Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Room *n*BGM Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.000 | Input / Output |
| Room *n*BGM Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Room *n*BGM Select | 1 to 32 | 1 to 32 | 0.000 to 1.000 | Input / Output |
| Room *n* Output Gain | -100 to 10 | -100 dB to 10 dB | 0.000 to 1.000 | Input / Output |
| Room *n* Output Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Wall *n* Configure | N / A [1](#Chance) | User Defined | 0  1 [1](#Chance) | Input / Output |
| Wall *n* Open | 0  1 | false  true | 0  1 | Input / Output |

###### 1. The Value output of the Wall Configure Control Pin will equal the number of the first wall you entered, the Position will be 1. If nothing or zero is entered the Control Pin Value and Position equal 0.

###### 2. The position will be in increments of (1 divided by the (number of Select buttons - 1)).
