# Status/Control (Touch Screen)

> Source: https://help.qsys.com/Content/Schematic_Library/touch_screen_status.htm

# Status/Control (Touch Screen)

The touch screen Status / Control component provides the connection between the physical touch screen and the Q-SYS Designer User Control Interface (UCI). In order to make the connection, you must specify the hardware's hostname, network redundancy status, and assign a UCI. Once the physical hardware is identified, the touch screen component provides the hardware status.

For information on supported touch screens, see [Q-SYS Products](../Hardware/Hardware_Overview.htm).

**Note:** Make sure you use the proper Q-SYS Designer component for the hardware connected to your Core. The TSC components are not interchangeable.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Touch Screen Controller Properties

#### External USB Audio

(TSC -70-G3 and TSC-101-G3 only). When enabled, you can connect an external audio device to the USB input and route audio to and from that device. See [External USB Audio Device In and Out](alsa_receiver_sound_card.htm).

#### Is Paging Station

Indicates whether the touch screen is functioning as a paging station.

#### Orientation

(TSC Series Gen 2 and Gen 3 only (including the PS-TSCG3 Touchscreen Page Station)). Select the orientation to match the touchscreen physical installation. To prevent the need of reinstalling the unit, you can select one of the "flipped" orientations.

**Note:** When installing a touchscreen in portrait orientation, the Orientation property in the touchscreen Status/Control component and the [User Control Interface (UCI) Design Overview](user_control_interface.htm#Web_Control_Interface_Properties) must both be set to 'Portrait'.

#### UCI Assignment

The choices are Static, only the specified UCI is used, and Dynamic you can select the UCI when the UCI is running.

#### UCI

This field can be edited only when the UCI Assignment is set to Dynamic. With the UCI Assignment set to Static, the name of the assigned UCI displays in this field, but cannot be changed.

Use the pull-down list to select the UCI assigned to this TSC component.

#### External USB Keys

(TSC -70-G3 and TSC-101-G3 only). Refers to the capability of connecting external USB devices (such as Storm AudioNav ADA device, or a keyboard) to the TSC -70-G3 or TSC-101-G3. You can choose between 0 and 64 External USB Keys.

[Controls](javascript:void(0))

[Status](javascript:void(0))

#### ID

When the ID / Identify button, in the Q-SYS Designer Status component, or the Configurator's Network Configuration for the hardware, or on the physical hardware is pressed, the **ID** buttons in the Configurator and Status component flash, and the LCD on the physical Hardware flashes to indicate the association between the three.

The indicators will flash for 5 minutes unless you stop them by pressing any one of the buttons.

#### Status LED

This LED changes color to indicate the current status of the Touchscreen. See Touchscreen Status for the meanings of the various colors.

#### Touchscreen Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Temperature

The current temperature, in Celsius, of the Touch Screen's hardware.

#### Memory Usage

The percentage of memory used.

### Network

#### Clock Master

LED indicating if the Core is the Master Clock for the Q-SYS system or not. The Core can be the Master Clock even if the clock is synchronized to an external clock.

#### Grandmaster

Displays either the Q-SYS Core processor name or the PTP Clock GUID. Note that:

* There can only be one Grandmaster for a Q-SYS design (for all LAN interfaces of the device). It is possible for Q-SYS to resolve to a PTP Grandmaster present on LAN B, if enabled and present.
* If available, the Core Name is displayed instead of the raw PTP clock GUID. (The Core Name is not available in some clocking topologies â for example, when a higher priority boundary clock between systems is present or with some Software Dante configurations, as when the Core syncs indirectly to another device via Software Danteâs boundary clock.)
* A PTP Clock GUID can look similar to a MAC address, but is not the same and may not be related to a deviceâs actual MAC address.
* If the PTP Clock GUID is derived from a MAC address (whether a Q-SYS Core processor or third-party device), it can be any MAC address on that device (any LAN interface, including those without a network connection).

#### PTPv1 (Dante)

Used specifically for Dante audio networking integration within the Q-SYS ecosystem

#### Clock Offset

Indicates how much of an offset exists, in microseconds, between the device and the network Grandmaster.

#### Parent Port

The clock Parent Port is the device and interface name to which the device is syncing. Typically, this is the Grandmaster.

#### LAN A and/or B

#### Link

When the LED is lit, it means the interface is "UP," signifying that the network connection is active and functioning properly. Conversely, when the LED is not illuminated, it indicates that the interface is "DOWN," suggesting that there may be issues with the network connection.

#### IP Address

Displays the IP Address the Core is connected to.

#### Mode

Determines how device operates within the network environment.

*Auto*: The network interface automatically negotiates it settings with the network infrastructure.

*Static*: The network interface's settings are manually configured by the user, including the IP address, subnet mask, gateway, and other parameters.

*Off*: Disables the network interface, preventing it from sending or receiving network traffic.

#### Speed

Refers to the data transfer rate supported by a network interface or connection. Speed indicates the transfer rate of megabits per second (Mbps).

#### PTPv2 State

Refers to the operational state or role of a network device or interface.

*Passive*: A device in the passive state is not actively transmitting or receiving data.

*Slave*: A device in the slave state is subordinate to another device, known as the master.

*Master*: A device in the master state holds authority or control over one or more slave devices in a network.

*Uncalibrated*: The uncalibrated state indicates a transition state between modes.

### USB Reset

#### USB Reset

This reinitializes the USB driver without the need for a full design redeploy, restoring connections and USB functionality after a few seconds.

[UCI/Screen](javascript:void(0))

### UCI Control

#### Log Off

If a user is required to log on to the TSC, this button can log them off. Refer to the Q-SYS Core Manager [User Control Interfaces](../Core_Manager/System_Management/User_Control_Interfaces.htm) topic.

#### UCI

Displays the name of the UCI currently running on the TSC. You can change the currently running UCI if the **UCI Assignment** is set to Dynamic.

#### Page

Displays the name of the currently selected page in the UCI. You can click this field and change the viewed page.

### Screen Control

#### Backlight

Controls the brightness of the screen back-lighting.

#### Dim Timeout (minutes)

Sets the time from when the screen was last touched until the screen is dimmed.

#### Off Timeout (minutes)

Sets the time from when the screen was last touched until the unit is turned off.

If log on is required for the UCI, when this time expires, the user must log on to the UCI again.

#### Disable Popup Numpad

When this control is activated, the keypad that displays when you touch a numeric-type control (Gain knob, Fader, Time, and so on) is disabled. The keypad does not display when a numeric-type control is touched.

#### On

Momentary button to turn the TSC display on.

#### Dim

Momentary button to turn the TSC display on.

#### Off

Momentary button to turn the TSC display off.

#### Touch Activity

LED indicates if the touchscreen is actively being touched.

[External USB](javascript:void(0))

These controls are found on the External USB tab for the TSC-70-G3 and TSC-101-G3 only when the control panel is opened.

#### Key *n*

Customizable to perform a specific trigger with any external USB device that has keys. For each entry, you can select a key from the drop-down to assign the trigger, e.g., KEY\_UP or KEY\_ENTER.

#### LED

When the corresponding key is pressed, the associated LED will light up.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Mode | | | | |
| Dim | Trigger | | | Output |
| Off | Trigger | | | Output |
| On | Trigger | | | Output |
| Network | | | | |
| Clocking | | | | |
| Grandmaster Name | (text) | | | Output |
| Offset From Master | - | *n*us | - | Output |
| Parent Port Name | (text) | | | Output |
| LAN A | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| IP Address | (text) | | | Output |
| Mode | (text) | | | Output |
| PTP State | (text) | | | Output |
| Speed | (text) | | | Output |
| Screen | | | | |
| Backlight | 0 â 100 | 0 â 100% | 0.00 to 1.00 | Input / Output |
| Dim | Trigger | | | Input / Output |
| Dim Timeout  (minutes) | 0 â 9999 | 0 â 9999 | 0 to 1.00 | Input / Output |
| Disable Popup Numpad | 0  1 | no  yes | 0  1 | Input / Output |
| Off | Trigger | | | Input / Output |
| Off Timeout | 0 â 9999 | 0 â 9999 | 0 to 1.00 | Input / Output |
| On | Trigger | | | Input / Output |
| Touch Activity | 0  1 | false  true | 0  1 | Output |
| UCI | | | | |
| Current Page | Text edit | | | Input / Output |
| Current UCI | Text display | | | Output |
| Log Off | Trigger | | | Input / Output |
| Logged In | 0  1 | false  true | 0  1 | Output |
| USB | | | | |
| Key *n* Code | Text display | | | Input / Output |
| Key *n* Pressed | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Memory Usage | Text display | | | Output |
| Reboot | Trigger Input | | | Input |
| Temperature | Text display | | | Output |
| Touchscreen Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
| USB Reset | 0  1 | off  on | 0  1 | Input / Output |
