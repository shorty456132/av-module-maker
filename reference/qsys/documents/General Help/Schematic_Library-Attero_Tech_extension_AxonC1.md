# Attero Tech Axon C1

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_AxonC1.htm

# Attero Tech Axon C1

Use this extension to connect to and control the Axon C1 Single-Gang networked audio controller (Attero Tech by QSC).

**Note:** See the [Axon C1 product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/attero-tech-network-wall-controllers/axon-c1/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 1.2.0 and above. For best results, use the latest Attero Tech device firmware.

[Integration Requirements](javascript:void(0))

### Syncronization

The Axon C1 is initially configured using the Attero Tech unIFY Control Panel to create the basic menu structure required for the end user application. After you have connected to the C1 with the Q-SYS extension, you must click Sync to pull the menu structure into the extension. If you later change the configuration in unIFY, the extension will show an orange Compromised status, which indicates that the C1 and extension are out-of-sync. You must then click Sync again.

### Events

Configure each C1 with a set of events. You can structure events into menus that can be up to four layers deep. Each configured event can be of one of three types:

* Source select event: Use this type to select specific inputs on a Router component in the Q-SYS design. The extension supports up to eight source select events.
* Preset (Snapshot) event: Use this type to select a specific Snapshot that places some or all of the system into a specific state. The extension supports up to eight Snapshot events.
* General event: Use this type to drive output control pins that are wired to other control elements in the Q-SYS design. The extension supports up to 16 general events.

### Named Components

Certain extension functions require the association of other design components. For these components to become available within the extension's menus, you must give them a custom name. Components you may wish to include and rename include:

* [Gain](gain.htm): Allows the C1 to control volume and mute. You can assign multiple C1 extensions to manipulate the same gain control, which enables more than four C1 units to control the same volume / mute in the system.
* [Router](router_with_output.htm): Allows C1 events to control source selection. If the router component has multiple outputs, the desired specific output must also be selected.
* [True Peak/RMS Meter](meter2.htm): Allows the C1âs LED bar to indicate audio level. If metering isnât necessary, this association can be left unassigned and metering will not be active.
* [Snapshot Controller](snapshot_controller.htm): Allows C1 events to control a snapshot, either the global snapshot bank or a user-defined bank. If the extension is configured to set different snapshots, each selectable snapshot must be part of the same snapshot bank.
* [Room Combiner](room_combiner.htm): In Room Combiner mode (set in Properties), allows the C1 to control volume and mute.

**Tip:** When you select a new Router or Snapshot Controller component during configuration, the extension checks to see if the updated configuration is valid. For example, if you originally select a Router with six inputs and you then change it to a Router with three inputs, the event associations for inputs 4-6 will be marked in red since those inputs no longer exist.

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. In the IP field, specify the IP address of the device and press Enter.

   The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.
3. Click Sync to pull the current menu structure from the device and populate the event controls based on the response.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

Select the number of control pins for the extension, from 0 to 16 (default is 0).

#### Plugin Mode

Choose the type of controls for the extension:

* 'Normal' (default) uses a gain for volume, mute, and a router for source selection.
* 'Room Combiner' uses a Room Combiner component instead.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

#### Sync

Click to pull the current menu structure from the device and populate the event controls based on the response.

#### Identify

Causes the power LED on the front of the device to start blinking so it can easily be identified. The identify function remains active until manually turned off. Click the button to toggle between states.

#### Status

Normally, this shows Initializing (blue) for a few moments after starting your design, followed by OK (green).

* If you see a Fault or Missing (red) status, check your connection parameters, ensure that the C1 is powered on and connected to the network, and that the C1 is configured for "Q-SYS" mode â refer to the C1 User Manual for more information.
* If you see a Compromised (orange) status, click the Sync button to pull in the latest menu structure from the C1.

#### Details

Provides information on the connected device such as MAC address, IP address, and MCU version.

### Zone Control

**Note:** Fields highlighted in red indicate an invalid control configuration.

#### Name

Use this control to override the zone name shown on the volume screen of the C1 that is defined as part of the menu structure. When added to a snapshot along with other extension fields such as Gain, it allows the C1 to do multi-zone control by allowing the name shown to reflect the current zone selected.

#### Gain Ctl

Only visible in Normal mode. Associates the Gain component to which the C1âs volume and mute controls are applied. If visible and left unassigned, the volume and mute functions of the C1 do not operate. The control is marked in red if the component name cannot be found.

#### Room Combiner

Only visible in Room Combiner mode. Associates the Room Combiner component to which the C1âs volume and mute controls are applied. Room Combiner components must be given a custom name (Named Component) or they will not appear on the list. If this field is visible and left unassigned, the volume and mute functions of the C1 do not operate. The control is marked in red if the component name cannot be found.

**Note:** When you run or emulate a design, the C1 extension checks the Gain Ctl / Room Combiner field to see if the selected control is of the correct type for the mode to which the extension is set (See Plugin Mode property). If the control does not match the mode, the field is automatically erased.

#### Room #

Only visible in Room Combiner mode. This is the specific room number of the associated Room Combiner component to which the the C1âs volume and mute controls are applied. If this field is visible and left unassigned, the volume and mute functions of the C1 do not operate.

#### Max/Min

The maximum and minimum values of the associated gain control. Used for scaling on the C1.

#### Current

The current level of the associated gain control rounded to the nearest integer. This value is also shown on the C1.

#### Mute

Button shows the state of the mute of the associated mute control.

#### Meter Ctl

Meter control for indicating the audio level on the C1. Meter components must be given a custom name (Named Component) or they will not appear on the list. If the C1 is not required to indicate a level, this control can remain unassigned. The control is marked in red if the component name cannot be found.

#### Meter #

Specific channel of the associated meter control used for indicating audio level on the C1. If the C1 is not required to indicate a level, this control can remain unassigned. If the choice becomes invalid for any reason, it becomes highlighted in red.

#### Meter

Indicates the level read from the associated meter. This is the metering level sent to the C1.

### Source Select

**Note:** Fields highlighted in red indicate an invalid control configuration.

Source selection controls are only enabled if one or more âsource selectâ type events are defined for the connected C1. The source select feature requires use of a Router component within the Q-SYS design.

#### Router Ctl

Only visible in Normal mode. Selects the Router control to be used for source select. Router components must be given a custom name (Named Component) or they will not appear on the list. The control is marked in red if the component name cannot be found.

#### Router Output #

Only visible in Normal mode. Sets the specific output on the associated Router component to be used for source select. If the choice becomes invalid for any reason, it becomes highlighted in red.

#### Event

The name of the event as shown on the C1âs menu.

#### Input #

In Normal mode, this is the specific input of the Router that corresponds to the selected source. In Room Combiner mode, this is the specific BGM input of the associated Room Combiner that corresponds to the selected source. If the choice becomes invalid for any reason, it becomes highlighted in red.

### Snapshot Control

**Note:** Fields highlighted in red indicate an invalid control configuration.

Extension controls for snapshots are only enabled if one or more âSnapshotâ type events are defined for the connected C1. Each snapshot event from a C1 can be assigned to activate a specific snapshot. If a C1 has multiple snapshot events, they must all be defined in a single snapshot bank. (Up to 24 different snapshots can be defined per bank.) For each event, you select what specific snapshot to load when that event occurs.

#### Event

Name of the event as shown on the C1âs menu.

#### Snapshot Ctl

Lists the available Snapshot components that this event can control. Snapshot components must be given a custom name (Named Component) or they will not appear on the list. The control is marked in red if component name cannot be found.

#### #

The specific snapshot that will be loaded from the selected Snapshot Controller component. If the choice becomes invalid for any reason, it becomes highlighted in red.

### Menu Button Function

The menu button can be used as a zone select or even source select. This is only possible if the C1 does not have any menus defined and is set to âVolume onlyâ control. In this mode, each time the menu button is pressed, it calls up the associated snapshot, which reconfigures the C1 extension's associated components. The specific loaded snapshot is defined by the fields for the menu button function.

#### Menu Button Snapshot Ctl

The snapshot bank that contains the zone/source select configuration that the C1 uses.

#### Menu Button Snapshot #

Identifies what specific snapshot to load next when the menu button is pressed. For example, the zone 1 snapshot should point to zone 2, zone 2 to zone 3, and so on, with the last zone pointing back to zone 1.

### General Event Assignment

**Note:** Fields highlighted in red indicate an invalid control configuration.

Use general events to manipulate the levels on the extension's control pins. If the Control Pins property is 0, configuration of these events is disabled. Each event can manipulate a control pin in a given way. Multiple events can be tied to the same control pin â for example, one event could turn it on, and a different event could turn it off.

#### Event

Name of the event as shown on the C1âs menu.

#### Type

Select the action to send to the control pin: âNoneâ, âTurn Onâ, âTurn offâ, âToggleâ and âPulseâ.

#### Pin #

Name of the event as shown on the C1âs menu.

#### Indicator LEDs

The indictors across the top show the current state of each of the control pins. The indicators on the right show the state of the specific control pin assigned to that particular event.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Control *n* | 0  1 | false  true | 0  1 | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Meter | (text) | | | Output |
| Mute | 0  1 | false  true | 0  1 | Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
