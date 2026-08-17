# Room Controls

> Source: https://help.qsys.com/Content/RoomSuite/RoomControls.htm

# Room Controls

The Room Controls section provides a focused set of options that affect how the room behaves during normal use. Within Room Controls, settings are organized into three main areas:

* Touch Panel - Controls how the standard user control interface (UCI) appears on the in room touch panel.
* Occupancy - Defines how the room responds to people entering, using, or leaving the space.
* LED - Controls how in room LED indicators behave during normal use.

## Touch Panel

#### Edit Button

Switches the page into an editable state.

### Theming

Allows you to update the accent colors of the standard touch panel UCI to better match your organization's branding. The page is divided into two main areas:

* A Preview of the touch panel on the left.
* A set of Theming Controls on the right.

Your changes to the theming controls update the preview so you can see how the UCI will look before you save.

#### Simple

Selecting Simple gives you basic control of the following:

#### Mode: Light / Dark

Sets the general background style.

#### Primary (color)

Sets the main brand color for the touch panel. Pick or enter a color value.

#### Text (color)

Sets the color used for text and affects how labels and other text appear against the chosen background.

#### Background (color)

Sets the background color of the touch panel theme. Pick or enter a color value. This works together with the Mode and Text color to define overall readability and contrast.

#### Fonts

Sets the font used for text on the touch panel.

#### Advanced

Selecting Advanced allows you to fine-tune more parts ofhte touch panel appearance than in Simple.

#### Color

Exposes extra color controlsâPrimary, Icon, Heading, Success, Warning, Disabled, Text, Background, Navigation Background, Active Background, and Active Border.

#### Fonts

Sets the font used for text on the touch panel, same as in Simple.

### Images

Allows you to choose your own image to appear on the roomâs standard touch panel interface.

#### Background Image

upload your background, which displays in in locations reserved for branding in RoomSuite Modular System. Delete and upload as necessary.

#### Brand Logo Image

Upload your logo, which displays in locations reserved for branding in RoomSuite Modular System. Delete and upload as necessary.

### Icons

Allows you to choose which icon is used to represent a video source on the touch panel. The actual video sources are set up on the Devices page.

#### Room PC Icon / Laptop Icon

Use the drop-down lists to choose which icon represents the Room PC and Laptop video sources on the touch panel.

### Pages

Allows you to edit the text that appears on the touch panelâs built-in pages.

#### Home Page

Allows you to enter the text shown on the touch panel home page and includes the Room Name and Welcome Message.

#### Help Page

Allows you to control whether the Help page is available on the touch panel and what it displays.

* Show Help Page: Toggle On or Off to show or hide the Help page on the touch panel.
* Help Message: Enter a short message that appears on the Help page.
* Support Phone Number: Enter the phone number users should use for support.
* Support URL: Enter a website address for additional help. A QR code that links to the URL will also be generated.

### Backlight

Allows you to adjust how the touch panel behaves over time.

#### Backlight level

A slider that sets the touch panelâs backlight level; move slider left or right to decrease or increase the brightness.

#### Dim Timeout (Minutes, 0 to disable)

Enter the number of minutes the panel should wait before dimming the backlight. If you set this value to 0, the dim timeout is disabled.

#### On, Dim, Off Buttons

* On turns the touch panel backlight fully on.
* Dim sets the touch panel to its dimmed state, which is lower in brightness, but not fully off.
* Off turns the touch panel backlight completely off.

## Occupancy

Occupancy lets you use a physical room occupancy sensor with your RoomSuite Modular System so the room can respond automatically when people enter or leave. By monitoring motion or presence through the sensor, RoomSuite Modular System can turn on displays when someone walks in and powers them off after the room has been empty for a while. This automation helps save energy, extend equipment life, and make the room ready without manual intervention.

Youâll find Occupancy under:

Room Controls > Occupancy in the left navigation.

When selected, the main content area is titled Occupancy and is divided into two sections:

1. Sensor â how the sensor is connected and enabled.
2. Display Behavior â how RoomSuite responds to activity and inactivity.

To change any of the Occupancy settings, select the Edit button in the top-right corner of the main content pane. This opens the settings for editing, allowing you to adjust the sensor to enable the toggle, select the activity status, and display behavior controls.

#### Sensor

The Sensor section describes how the occupancy sensor is connected to the system.

**Connection Example**

âConnect a +24VDC (50mA max) analog occupancy sensor to the 3-pin "GPIO In" on the RMP-100.â

Sensor type

Use a ceiling or wall mounted occupancy / motion sensor designed for low-voltage systems, that can operate from +24 VDC, up to 50 mA. These sensors typically use passive infrared (PIR) or ultrasonic technology to detect movement.

Electrical connection

The sensor connects directly to the RMP-100 and in this example, to the 3-pin GPIO IN connector. This direct wiring eliminates the need for additional interface modules or converters, making installation simpler.

**Note:** Always refer to the sensor manufacturerâs installation and wiring guidelines to ensure proper operation and compliance with their specifications.

Power

The RMP-100 provides +24 VDC (50 mA max) to power the sensor. This built-in power source means you do not need a separate power supply.

By wiring the sensor directly to the RMP-100 and using its integrated power, you create a seamless link between physical room activity and RoomSuite Modular Systemâs automation logic. This connection is what allows the system to respond intelligently, turning displays on when the room becomes active and off when itâs idle, without manual intervention.

#### Enable / Disable the Occupancy Sensor

A toggle labeled Enable controls whether the system responds to the occupancy sensor.

Enable = Off

* The sensor input is ignored.
* Activity Status stays at Not Detected, and display behavior does not respond to the sensor.

Enable = On

* The RMP-100 monitors the occupancy sensor on the GPIO input.
* Activity Status shows when motion / occupancy is detected.

You can leave the sensor installed but disabled until you are ready to use occupancy based automation.

#### Activity Status

* Not Detected â No occupancy is currently detected.
* When the sensor is triggered, this changes to show that activity is detected, and the room is occupied.

This status is a simple way to confirm that the sensor is working and that the RoomSuite Modular System is receiving occupancy information.

#### Display Behavior

The Display Behavior settings determine how the roomâs displays respond automatically based on occupancy status. Once the occupancy sensor is enabled and detects activity, these controls define what happens when people enter or leave the room. This automation ensures the room is ready when needed and conserves energy when idle.

This section contains three controls:

1. Activity Detected
2. Inactivity Detected
3. Inactivity Delay (Minutes)

#### Activity Detected

This setting specifies what happens when the room transitions from idle to active. For example, when someone enters the room and the sensor detects motion, the system can automatically send a Power On command to the connected display(s).

* The room visually âwakes upâ as people arrive, creating a ready-to-use environment.
* Eliminates the need for manual display activation, saving time at the start of meetings.
* Typical Value: Power On.

#### Inactivity Detected

This setting defines what happens after the room has been empty for a certain period. When no motion is detected for the configured delay, RoomSuite Modular System sends a Power Off command to the displays.

* Reduces energy consumption by turning off unused equipment.
* Extends display life by minimizing unnecessary runtime.
* Provides a clear visual cue that the room is no longer in use.
* Typical value: Power Off.

#### Inactivity Delay (Minutes)

The Inactivity Delay setting controls how long the room must remain unoccupied before RoomSuite Modular System applies the Inactivity Detected action. You can enter this value in minutes. The default value is 10 minutes.

For example, if the delay is set to 10 minutes, the sensor must detect no activity for 10 continuous minutes before RoomSuite Modular System treats the room as inactive and sends a Power Off command to the displays. This prevents the system from shutting down too quickly if someone is still in the room.

#### Call LED

The Call LED page in RoomSuite Modular System lets you control the color and behavior of call status LEDs across supported Q SYS microphones, soundbars, and touch panels in the room.

These LEDs can change color, brightness, or on/off state to show whatâs happening in the room. The following LED behaviors are available:

* In Use Color â Shows that the roomâs audio system or microphone is actively in use. The LED displays the selected color and pattern to indicate that the device is currently engaged. Red might mean the room is busy.
* Mute Color â Indicates that the microphone or audio source is muted. The LED shifts to the chosen color and pattern so users can see at-a-glance that audio transmission is disabled. Red might mean the microphone is muted.
* Ringing Color â Indicates incoming call activity on supported devices. The LED can flash or change color to alert users that the room is receiving a call. Depending on configuration, it can follow the mute color, use a custom color, or flash at a defined speed to make the alert more noticeable. Yellow might mean an incoming call.
* Idle Color â Displays when the device is powered and connected but not actively in use. This color and pattern help users identify that the system is ready and waiting for interaction. Blue might indicate the system is starting up, connected to a call, or in a special mode.

#### Edit Button

Switches the page into an editable state.

#### LED Brightness

Adjusts the overall brightness level of the call LEDs.

#### Unmute

The Unmute section defines how the LED behaves when the system is in an unmuted state.

* Color â Sets the color used for the unmute state.
* Pattern â Sets the pattern used for the unmute state.

#### Mute

The Mute section defines how the LED behaves when the system is in a muted state.

* Color â Sets the color used for the mute state.
* Pattern â Sets the pattern used for the mute state.
