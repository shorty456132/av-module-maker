# Astronomical Clock

> Source: https://help.qsys.com/Content/Schematic_Library/sun.htm

# Astronomical Clock

Use the Astronomical Clock component to determine your location's latitude and longitude, and then trigger events based on that location's sunrise, sunset, or solar noon.

**Note:** The component uses <https://sunrise-sunset.org/api> to obtain astronomical data for your location. An internet connection is required.

[Configuration Overview](javascript:void(0))

1. Drag the Astronomical Clock component into your schematic.
2. Connect the Solar Noon Trigger, Sunrise Trigger, and/or Sunset Trigger control pins (exposed by default) to the input control pins of other components. Use these pins to trigger events in your design.

   **Tip:** You can also expose the 'Is Day' control pin, which provides a boolean value of whether the current time is after sunrise and before sunset. This may be simpler than using conditional logic with sunrise and sunset times.
3. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)
4. Click **Get** to obtain the coordinates for your location based on IP address.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Example](javascript:void(0))

In this example, the Astronomical Clock component is configured to trigger Audio Player playback based on the sunrise and sunset times for a set location. When sunrise occurs, playback begins. When sunset occurs, playback stops.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Astronomical Clock Properties

This component has no configurable properties.

[Controls](javascript:void(0))

**Note:** The component refreshes its state every minute, so it can take up to 59 seconds to reflect a change.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Latitude and Longitude

Indicates the latitude and longitude, in Degrees Minutes Seconds (DMS) format, obtained using the Get button. Or, you can manually enter values in decimal format. (Manually-entered decimal values are converted to DMS format.)

#### Sunrise

Text indicator of the sunrise time, as determined by the location coordinates.

#### Sunset

Text indicator of the sunset time, as determined by the location coordinates.

#### Solar Noon

Text indicator of the solar noon time, as determined by the location coordinates.

#### Day Length

Text indicator of the hours, minutes, and seconds in the daytime period, as determined by the location coordinates.

#### Daytime

Boolean indicator of whether the current time is between the sunrise and sunset times.

#### Get

Click to obtain the latitude and longitude of your system's location, based on IP address.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Solar Noon Trigger | (trigger) | | | Output |
| Sunrise Trigger | (trigger) | | | Output |
| Sunset Trigger | (trigger) | | | Output |
| Day Length | â | *hh*:*mm*:*ss* | â | Input / Output |
| Get | (trigger) | | | Input / Output |
| Is Day | 0  1 | false  true | â | Output |
| Latitude | â | **Input**: [-]*nnn*.*nnnnn*  **Output**: *nnn*Â° *nn*' *nn*.*nn*" N|S | â | Input / Output |
| Longitude | â | **Input**: [-]*nnn*.*nnnnn*  **Output**: *nnn*Â° *nn*' *nn*.*nn*" W|E | â | Input / Output |
| Solar Noon | â | *hh*:*mm*:*ss* AM|PM | â | Input / Output |
| Sunrise Time | â | *hh*:*mm*:*ss* AM|PM | â | Input / Output |
| Sunset Time | â | *hh*:*mm*:*ss* AM|PM | â | Input / Output |
