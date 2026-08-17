# Channel Group  Component

> Source: https://help.qsys.com/Content/Schematic_Library/channel_group.htm

# Channel Group [BETA]

The Channel Group component allows you to define a group of DSP components and have it automatically replicated a number of times. Each replication is called a *Channel*. You can select one or more Channels, and change the controls within a component or components and those changes are made only within the selected Channels. For example, if you place a Gain component in a Channel Group that has four Channels, you effectively have four gain components that you can control individually, all four as a group or multiple groups. You cannot place a Channel Group within another Channel group.

**Note:** This is a BETA component. Though it is functional, it is not feature complete and is subject to change.

[Using the Channel Group](javascript:void(0))

The Channel Group is designed to be able to create multiple identical groups of DSP components where the controls in the in the components can be changed separately per Channel, or simultaneously in all or some of the Channels. The Channel Group takes the place of manually making and connecting duplicate groups of DSP Components.

### Rules

* You can have all the Channels in a Channel Group, with different control settings in each Channel, acting on a single input source, with multiple outputs. For example, you have multiple rooms with the same audio feed, but each room has different EQ requirements.
* You can have all the Channels in a Channel Group, with the same or different control settings in each Channel, acting on multiple input sources.
* If you place components in a Channel Group, then delete the Channel Group, you also delete any components that are in the Channel Group.
* You cannot use items from the Inventory in a Channel Group.
* You can use Signal Name receivers inside a Channel Group; they will receive signals from outside the Channel Group. You cannot use Signal Name transmitters inside a Channel Group.
* When more than one Channel is selected, any controls that are set differently in the selected Channels are highlighted in orange.
* If you change one of the highlighted controls, that control in all selected Channels, snaps to the same value and the highlighting is removed.
* When using the [Probe](probe.htm "View the Probe topic.") inside a Channel Group, if more than one Channel is selected, the probe is "attached" to the lowest number selected Channel.
* When you make a change to an Input to the Channel Group, it affects all associated Channels.

**Note:** Components and controls within Channel Groups are not supported in Snapshots.

### Procedure

1. Place the desired component(s) in the Channel Group and make the appropriate connections inside of and to/from the Channel Group. You now have *n* duplicates of your components and connections based on the number of Channels set in the Properties. The Inputs and Outputs per Channel are set in the Properties.
2. If necessary, move the Input and Output pins that are inside the Channel Group to help with organization.
3. Select one or more Channels.
   * Exclusive - You can select only one Channel at a time; the Channel buttons act like radio buttons. Any adjustments made to controls are made for that Channel only.
   * Select All - Selects all Channels; the Channel buttons act like independent toggle buttons. Any adjustments made to controls are made for only the selected Channels.
   * Select None - Clears or de-selects all Channels; the Channel buttons act like independent toggle buttons. When there are no Channels selected, you can not make any adjustments to the Component's controls.
   * Prev and Next - Moves the Channel selection to the left or to the right, and stops at Channel 1, or the highest number Channel. Any adjustments made to controls are made for the selected Channel only.
4. As you select the desired Channels, make adjustments to the Components' controls as necessary.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Channel Count**, **Audio Input** / **Output Count**, and **Control Input** / **Output Count** Properties.

### Input Pins

#### Channel 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Channel Group [BETA] component has 4 audio input pins.

### Output Pins

#### Channels 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the Channel Group [BETA] component has 8 audio output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Channel Group [BETA] Properties

#### Name

User-defined name to identify the Channel Group component.

#### Channel count

Sets the number of Channels available. You can choose between 2 and 256.

#### Audio Input Count

Sets the number of Audio Input connections per Channel.

Maximum is 512 divided by Channel count - rounded down

#### Audio Output Count

Sets the number of Audio Output connections per Channel.

Maximum is 512 divided by Channel count - rounded down.

#### Control Input Count

Sets the number of Control Input connections per Channel.

Maximum is 512 divided by Channel count - rounded down

#### Control Output Count

Sets the number of Control Output connections per Channel.

Maximum is 512 divided by Channel count - rounded down

[Controls](javascript:void(0))

The Gain and Bandwidth controls below are set differently (orange highlighting) in at least one of the Channels when the All button is selected.

**Tip:** The following Controls can be copied and used in a User Control Interface.

#### 1 - n

Buttons to identify and select the Channels one at a time. You can select multiple Channels.

#### Prev

Moves focus to previous Channel

#### Next

Moves focus to next Channel

#### Exclusive

Allows only one Channel to be selected at a time

#### Select All

Selects all Channels

#### Select None

Clears any selected Channels

[Control Pins](javascript:void(0))

The Channel Group has no Control Pins.
