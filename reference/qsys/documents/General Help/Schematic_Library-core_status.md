# Status (Core)

> Source: https://help.qsys.com/Content/Schematic_Library/core_status.htm

# Status (Core)

The Core is the centralized digital signal processor (DSP) for the Q-SYS system.

**Note:** The Status component control panel for vCore Virtualized Processors only indicates the Status LED and Status box.

[Core Specifications](javascript:void(0))

**Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information.

Network Audio Streams vs. Channels

Each Q SYS Core has separate limits for Network Audio Channels and Network Audio Streams. A single stream may carry one or more audio channels. In many cases, you will reach the stream limit before you hit the channel limit.

For most Core models, the maximum number of Network Audio Streams (Tx and Rx) is half of the maximum Network Audio Channels. Notable exceptions:

* Core 510i and Core 510c: support 256 x 256 streams and 256 x 256 channesl.
* Core 610: supports 256 x 256 streams and up to 384 x 384 channels (with capacity scaling license); applying a capacity scaling license does not increase the stream limit.

The Check Design window in Q-SYS Designer always shows the authoritative maximum for both Network Audio Channels and Network Audio Streams for the selected Core model.

| Core Model | Local I/O Channels | Network Audio Channels[5](#The) | Network Audio Streams | Software Dante Audio Channels[4](#Software) | AEC Processors[5](#The) | Multitrack Audio Players | Local I/O Card Capacity | VoIP Instances |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm) | HDMI (8-ch per port) Stereo 3.5 mm (1 x 1) | 64 x 64 | 32 x 32 | Up to 32 x 32 (none included) | 8 | 16 | N/A | 1 |
| [Core Nano](../Hardware/Processing/Core_Nano.htm) | 8x8 USB audio | 64 x 64 (128 x 128 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | 32 x 32 (64 x 64 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | Up to 32 x 32 (8 x 8 included) | 8 | 16 (upgradable to 32) | N/A | 2 |
| [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm) | 8 flex, 8x8 USB audio | 64 x 64 (128 x 128 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | 32 x 32 (64 x 64 w/ [Licensing](../Core_Manager/Core_Management/Licensing.htm)) | Up to 32 x 32 (8 x 8 included) | 8 | 16 (upgradable to 32) | N/A | 2 |
| [Core 110f](../Hardware/Processing/Core_110f.htm) | 24 (8 analog in, 8 analog out, 8 analog flex in/out), 16x16 USB audio | 128 x 128[1](#top) | 64 x 64 | Up to 32 x 32 (8 x 8 included[3](#For)) | 16 | 16 (upgradable to 32) | N/A | 4 |
| [Core 24f](../Hardware/Processing/Core_24f.htm) | 24 (8 analog in, 8 analog out, 8 analog flex in/out) | 160 x 160 | 80 x 80 | Up to 64 x 64 (8 x 8 included) | 24 | 4 | N/A | 8 |
| [Server Core X10](../Hardware/Processing/Server_Core_X10.htm) | N/A | 256 x 256 | 128 x 128 | Up to 128 x 128 (8 x 8 included) | 64 | 128 | N/A | 32 |
| [Server Core X20r](../Hardware/Processing/Server_Core_X20r.htm) | N/A | 384 x 384 | 192 x 192 | Up to 256 x 256 (8 x 8 included) | 128 | 256 | N/A | 64 |
| [Core 510i](../Hardware/Processing/Core_510i.htm) | Up to 32 analog, 128x128 (AES/CobraNet/Dante/AVB cards) | 256 x 256 | 256 x 256 | Up to 128 x 128 (8 x 8 included[2](#Starting)) | 64 | 16 (upgradable to 128) | 8 | 64 |
| [Core 610](../Hardware/Processing/Core_610.htm) | N/A | 256 x 256 (384 x 384 with Licensing) | 256 x 256 (streams stay fixed) | Up to 256 x 256 (8 x 8 included) | 64 | 16 (upgradable to 128) | N/A | 64 |
| [Core 5200](../Hardware/Processing/Core_5200.htm) | N/A | 512x512 | 256 x 256 | Up to 512 x 512 (8 x 8 included[2](#Starting)) | 160 | 16 (upgradable to 128) | N/A | 64 |
| [Core 6000 CXR](../Hardware/Processing/Core_6000_CXR.htm) | N/A | 256 x 256, upgradeable to 512 x 512 | 128 x 128 (upgradeable to 256 x 256) | Up to 512 x 512 (8 x 8 included) | 80, upgradeable to 160 | 16 (upgradable to 128) | N/A | 64 |
| Discontinued |  | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Core 110c](../Hardware/Processing/Core_110c.htm) | 24 (8 analog in, 8 analog out, 8 analog flex in/out), 16 x 16 USB audio | 128 x 128[1](#top) |  | N/A | 4 | 16 (upgradable to 32) | N/A | 1 |
| [Core 510c](../Hardware/Processing/Core_510c.htm) | Up to 32 analog, 128 x 128 (AES/CobraNet/Dante/AVB cards) | 256 x 256 |  | N/A | 64 | 16 (upgradable to 128) | 8 | 4 |
| [Core 6000 CXR](../Hardware/Processing/Core_6000_CXR.htm) | N/A | 256 x 256, upgradeable to 512 x 512 |  | Up to 512 x 512 (8 x 8 included) | 80, upgradeable to 160 | 16 (upgradable to 128) | N/A | 64 |

###### 1. When using the Core 110f on-board USB Device Port for video bridging, the Q-LAN / AES67 maximum audio channel count is 80 x 64 (Q-SYS version 9.7 and later) or 64 x 64 (Q-SYS version 9.6 and earlier).

###### 2. For units shipped after January 1, 2021. See [Licensing](../Core_Manager/Core_Management/Licensing.htm).

###### 3. For units shipped after March 31, 2020. See [Licensing](../Core_Manager/Core_Management/Licensing.htm).

###### 4. Software Dante channels count towards Network Audio Channels.

###### 5. The maximum number of third-party microphone AEC Processors and input Network Audio Channels is affected by the quantity of Q-SYS NM-T1 microphones in the design. See [NM-T1 Quantity and AEC Channel Limits](../Hardware/Audio_IO/NM-T1.htm#NM-T1).

[Properties](javascript:void(0))

[Core Properties](javascript:void(0))

**Note:** For NV-32-H (Core Capable) properties related to HDMI, see the [HDMI I/O (NV-32-H)](streamer_hdmi_switcher.htm) topic.

#### Name

The Name may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. Names cannot begin or end with a hyphen. No other symbols, punctuation characters, or blank spaces are permitted. Core names are limited to 63 characters.

**Note:** This name must match the Hostname for the Core as defined in [Core Manager](../Core_Manager/CoreManager_Overview.htm). If you use Telnet or third-party external control, you must enter the Name exactly as it is entered here.

#### Location

User-defined name that groups the component with other components in the same physical location â for example, "Rack 1" â or in the same organizational scheme.

#### Model

Select your Q-SYS Core processor model. See [Core Specifications](#Core) for a list of selectable Core models.

#### Is Redundant

If you have redundant Cores in the installation, select Yes, otherwise, leave it as No.

**Note:** The NV-32-H (Core Capable) does not support Core Redundancy.

#### Backup Name

This property displays when you set Is Redundant to Yes. Same requirements as the primary Core Name.

#### Redundant Power

*Applicable only for the Core X20r.* Indicates whether the device is equipped with dual power supplies to ensure continuous operation in case one power source fails. Setting this property to "Yes" signifies that the device has redundant power supplies installed. Selecting "No" means the device operates with a single power supply.

#### GPIO

(Core 110 Series models only)

This property determines whether to expose GPIO In and GPIO Out components in the Inventory tree.

* Disabled: GPIO components are not shown in the Inventory tree. Use this setting for Core 110v2, which does not include GPIO inputs and outputs.
* Enabled: (default) GPIO components are shown in the Inventory tree. Use this setting for Core 110f v1 or Core 110c, as these models include GPIO inputs and outputs.
* Optional: GPIO components are shown in the Inventory tree. However, reporting of Missing, Compromised, or Fault statuses related to the actual hardware presence of GPIO will not occur.

#### External USB Audio

When enabled, you can connect an external audio device to the USB input and route audio to and from that device. See [External USB Audio Device In](alsa_receiver_sound_card.htm) and [External USB Audio Device Out](alsa_transmitter_sound_card.htm).

#### Network Receive Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Receive Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks.

Because the specified additional latency is added both to transfers from IO Frames to the Core and from the Core to IO Frames, the additional system latency is twice the amount of additional receive buffer selected. Total system latency based on this setting is calculated and displayed immediately below the Network Receive Buffer property.

[USB Bridging](javascript:void(0))

### USB Bridging â Common Properties

These properties appear based on the USB bridging capabilities of the Q-SYS device. Refer to the [USB Video Bridge](usb_uvc.htm) and [USB Audio Bridge](USB_Audio_Bridge.htm) topics to see what Q-SYS Core processors and peripherals support USB bridging.

#### USB Bridge Name

User-defined name given to the USB Bridge, from 1 to 24 characters. The Name may contain ASCII letters 'a' through 'z' (case-insensitive), the digits '0' through '9', and the hyphen. Names cannot begin or end with a hyphen. No other symbols, punctuation characters, or blank spaces are permitted.

#### Zoom Compatibility

If you are using the [HID Conferencing](usb_telephony.htm) component to control a remote computer running Zoom or Google Meet, set this property to 'Enabled.' Otherwise, when controlling another conferencing app such as Skype for Business, set to 'Disabled' (default). When this property is enabled, the USB Bridge Name property is disabled.

**Tip:** Enabling Zoom Compatibility may improve the user experience with macOS conferencing solutions.

#### USB Video Bridge

Enable the USB Video Bridge to bridge Q-SYS Mediacast streams to USB, enabling you to view Mediacast video on a connected computer. This exposes the USB Video Bridge component in the I/O-USB Bridge Inventory tree. To see what Properties are available when the USB Video Bridge is enabled, see [USB Video Bridge](usb_uvc.htm).

#### USB Audio Bridge

Provides the capability of passing audio via USB. When this is set to anything except 'Disabled', you can drag the Speakerphone and/or Sound Card components from the device's Inventory tree into your design. To see what Properties are available when the USB Audio Bridge is enabled, see [USB Audio Bridge](USB_Audio_Bridge.htm).

* Disabled: (Default)
* Speakerphone (1 x 1): Provides a speakerphone with an input and output component, each having 1 audio connection.
* Sound Card (2 x 2): Provides a sound card with an input and output component, each having two (stereo) audio connections.
* Speakerphone and Sound Card: Provides one speakerphone and one sound card with the same capabilities as described above.
* Advanced â If supported, allows up to any combination of four speakerphone / sound cards.

#### Speakerphone Mode

This selection is available only when Speakerphone or Speakerphone and Sound Card is selected in the USB Audio Bridge property. Indicates if the Q-SYS design has Echo Canceling (EC) or Non-Echo Canceling (NEC). This information is provided to the PC or Mac operating system so it can determine whether or not to use its own echo canceling.

[Telephony (Core 110f, Core 110c, QIO-TEL2, and POTS card only)](javascript:void(0))

#### Telephone Country

Select the country in which the telephone service resides.

#### Telephone Tone Output

When 'Yes' is selected, the Ring, Entry, Exit, and DTMF tones are fed to a separate output channel (Tone Output) on the POTS In component. These tones can now be routed independent of the voice audio.

#### Enable Call Sync

Use the Call Sync component to simplify the integration of Q-SYS collaboration devices and calling systems. It synchronizes mute state, call controls, and LED light behavior across multiple calling components, including USB HID Conferencing, Softphone, and POTS Controller. See the [Call Sync](call_sync.htm) topic

[Miscellaneous](javascript:void(0))

#### I/O Slot

Identifies the type of I/O card installed in the physical Core. The number of I/O Slots varies depending on the Core Model. After you make your selection, the I/O card displays under the Core in the Inventory list. The choices are:

* [Line Out](io_output_card.htm)
* [Mic/Line In](io_input_card.htm)
* [DataPort Out](io_card_dataport.htm)
* [AES3 In / Out](io_aes_card.htm)
* [CobraNet](io_cobranet_input_card.htm)
* [Dante](io_dante_input_card.htm)
* [AES3 16-channel In](io_aes_16_input_card.htm)

#### SRC Disabled (AES3)

When an AES3 In / Out or AES3 16-channel In card is selected for the I/O Slot Property, you have the ability to disable or enable the AES3 Sample Rate Conversion.

#### Network Receive Buffer

Adds extra buffer time to the default maximum of 1 ms.

Additional Network Receive Buffer time is useful in (rare) cases where the network latency through the network exceeds the default maximum. Additional network latency my be introduced by sub-optimal QoS functionality, some layer-3 routing implementations, long distances or large networks.

Because the specified additional latency is added both to transfers from IO Frames to the Core and from the Core to IO Frames, the additional system latency is twice the amount of additional receive buffer selected. Total system latency based on this setting is calculated and displayed immediately below the Network Receive Buffer property.

[Clocking](javascript:void(0))

**Note:** The PTP settings for the Core are now available in the Design Properties dialog. (Menu > File > [Design Properties](design_properties.htm).)

#### Sample Rate

Selects the sample rate. Typically, 48kHz is used as the Sample Rate. In scenarios where Q-SYS is externally synchronized to a (video) house sync signal you would use 48kHz Pull Down as the Sample Rate.

#### Clock Source

The AES3-1 and AES3-2 options display when you have an AES3 In / Out card selected for the Core I/O slot. When you have an AES3 16-channel In card selected, only the AES3-1 option is available. Use these options to sync to an external AES3 signal. The AES3 selections require either regular AES3 or AES3 black. The clock should be connected to the [AES3 card](../Hardware/IO_Expanders/CAES4.htm) either connector **Channel 1/2 In**, or **Channel 3/4 In**.

The GPIO selections require an external TTL level word clock or a GPS connection: pin 3 is signal, pin 8 is ground. When you select GPIO A-1 or GPIO B-1 as the clock source, the respective GPIO 1 Property changes to "Input used as clock source". The clock source should be connected to pin 3 of the respective GPIO connector - either GPIO A or GPIO B.

**Note:** Typically, Internal is used as the clock source. Only if there is a need to synchronize the Q-SYS system to an external clock would you use GPIO or AES3. You would use GPIO if the external clock signal is a word clock or GPS. You would use AES3 if the external clock signal is an AES3 signal. Often an AES3 signal without audio is used to reduce the clock jitter. This signal is called AES3 black.

#### Clock Type

When the Clock Source is set to a GPIO pin, the Clock Type field is available.

#### Baud Rate

* For 1PPS clocks, the default baud rate is 4800.
* For 5PPS clocks, the default baud rate is 19200.

#### Verbose

Adds CPU Statistics Audio and Network to the Core Status component, along with a Reset button to reset the statistics to zero. You must have the Core Status component in the schematic area, and selected.

[Graphic Properties](javascript:void(0))

#### Label

Use the Label property to change the name of the component in the schematic. The Label property defaults to the component name. To learn more about renaming schematic elements, see [Organizing Your Design](../Q-SYS_Designer/Using_the_Schematic/Labeling_and_Organizing_Schematic_Elements.htm).

#### Position

The coordinates reference a specific place in the schematic - for example,"100,100" (horizontal, vertical). 0,0 is the upper left corner of the schematic.

#### Fill

Sets the fill color of the component in the schematic.

[Script Access](javascript:void(0)) 

#### Code Name

Displays the currently assign name for control access. You can use the auto-assigned name or customize it. Q-SYS will automatically check all Code Names in the design to ensure name is unique.

#### Script Access

Defines whether the component will be accessible by script and/or externally, or not at all. Choices include All, External, None (default), and Script.

* **None** (default) - Not accessible by any script, plugin, or by [Q-SYS Remote Control Protocol (QRC)](../External_Control_APIs/QRC/QRC_Overview.htm).
* **Script** - Can be accessed by scripts, such as Text Controller, Block Controllers, and plugins only.
* **External** - Can only be accessed by 3rd party controls systems using component commands from the [Q-SYS Remote Control Protocol (QRC)](../External_Control_APIs/QRC/QRC_Overview.htm).
* **All** - No restrictions, can be accessed by 3rd party control systems via [Q-SYS Remote Control Protocol (QRC)](../External_Control_APIs/QRC/QRC_Overview.htm), or script objects or plugin objects.

**Tip:** Use [Script Programmer Mode](script_programmer_mode.htm) to quickly view the Script Access setting directly on the component in the design schematic without the need to disconnect from the Q-SYS Core processor.

[Controls](javascript:void(0))

[Status (NV-32-H Core Capable)](javascript:void(0))

### Core Status

#### ID

Click to flash the green ID LED on the front of the NV-32-H unit. The indicator flashes indefinitely until you press the ID button again.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### CPU Temperature

The current temperature, in Celsius, of the NV-32-H central processing unit.

#### VPU Temperature

The current temperature, in Celsius, of the NV-32-H video processing unit.

#### I/O Temperature

The current temperature, in Celsius, of the NV-32-H HDMI I/O hardware.

#### Fan 1, 2

Indicates the current RPMs of the two fans within the NV-32-H.

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

### Power

#### PoE < 90w

This LED glows if the NV-32-H is connected to a switch port that does not support the required PoE++ (802.3bt [Type 4 A Type 4 power supply provides 90 watts of power, which the NV-32-H requires.](javascript:void(0))) power standard. This is accompanied by an "Insufficient power" fault in the NV-32-H Status section.

**Note:** This LED can also glow if the switch port to which the NV-32-H is connected does not properly negotiate the 802.3bt Type 4 standard, despite being capable of providing proper power. If you believe this is the case, enable the Operate with any PoE Power Sourcing Equipment option in Core Manager. For more information, see the Core Manager > [Network > Basic](../Core_Manager/Core_Management/Network_Settings.htm) topic.

#### PoE = 90w, 802.3bt

This LED glows if the NV-32-H is receiving power from a switch port that supports the required PoE++ (802.3bt Type 4) standard.

#### Aux Power

This LED glows if the NV-32-H is receiving power via 48V DC.

### USB Reset

#### USB Reset

This reinitializes the USB driver without the need for a full design redeploy, restoring connections and USB functionality after a few seconds.

[Status (All Other Cores)](javascript:void(0))

Some controls require a specific setting in the Properties to make them available. To see all settings, ensure the following is set in the Properties panel:

* **Is Redundant** set to **Yes**
* **Verbose** set to **Yes**
* **Clock Source** set to something **other than Internal**

### Core Status

#### ID

When the ID/Identify button, in the Q-SYS Designer Status component, or the Configurator's Network Configuration for the hardware, or on the physical hardware is pressed, the ID buttons in the Configurator and Status component flash, and the LCD on the physical Hardware flashes to indicate the association between the three.

The indicators will flash for 5 minutes unless you stop them by pressing any one of the buttons.

#### Status LED

This LED changes color to indicate the current status of the Core. See Status for the meanings of the various colors.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### External Clock

The Clock Source in the Core's Properties must NOT be set to Internal. The External Clock illuminates if the Core receives a valid external word clock or AES3 signal. (Not available on Core 5200)

#### External Lock

The Clock Source in the Core's Properties must NOT be set to Internal. The External Lock illuminates if the Core is able to successfully synchronize to the external clock signal. (Not available on Core 5200).

#### Clock Master

LED indicating if the Core is the Master Clock for the Q-SYS system or not. The Core can be the Master Clock even if the clock is synchronized to an external clock.

#### Grandmaster

Displays either the Q-SYS Core processor name or the PTP Clock GUID. Note that:

* There can only be one Grandmaster for a Q-SYS design (for all LAN interfaces of the device). It is possible for Q-SYS to resolve to a PTP Grandmaster present on LAN B, if enabled and present.
* If available, the Core Name is displayed instead of the raw PTP clock GUID. (The Core Name is not available in some clocking topologies â for example, when a higher priority boundary clock between systems is present or with some Software Dante configurations, as when the Core syncs indirectly to another device via Software Danteâs boundary clock.)
* A PTP Clock GUID can look similar to a MAC address, but is not the same and may not be related to a deviceâs actual MAC address.
* If the PTP Clock GUID is derived from a MAC address (whether a Q-SYS Core processor or third-party device), it can be any MAC address on that device (any LAN interface, including those without a network connection).

#### Processor Temp.

The current temperature, in Celsius, of the Core processor.

#### Chassis Temp.

The current temperature, in Celsius, of the Core chassis.

#### Memory Usage

The percentage of memory used.

#### External Frequency

The Clock Source in the Core's Properties must NOT be set to Internal. The frequency of the clock sync connected to GPIO. This is usually 48000 (+- a few samples). If you are using GPS sync it will be either 5 (for 5pps) or 1 (for 1pps) (Not available on Core 5200).

#### Processor Fan

The current speed of the processor fan in RPM. The speed varies based on the temperature. Not all Cores have this field.

#### Clock Offset

Indicates how much of an offset exists, in microseconds, between this Core and the Master Clock. If this Core is the Master Clock, the offset is zero.

#### Parent Port

The device and interface name that this device is syncing to when it's not the clock master. Usually it is the same as the Grandmaster name.

#### Chassis Fan

The current speed of the chassis fan in RPM. The speed varies based on the temperature.

#### Memory Usage

*Verbose Property must be Yes.* Displays the percentage of memory used.

#### Control Compute Usage [BETA]

The percentage of non-DSP, control-only CPU usage.

**Note:** This is a BETA control. Though functional, it is not feature complete and must not be relied upon in production environments.

#### Network Compute Usage [BETA]

The percentage of network usage for DSP.

**Note:** This is a BETA control. Though functional, it is not feature complete and must not be relied upon in production environments.

#### Process Compute Usage [BETA]

The percentage of CPU usage for DSP, both Category 1 and Category 2 processing.

**Note:** This is a BETA control. Though functional, it is not feature complete and must not be relied upon in production environments.

#### Lua Compute Usage [BETA]

The percentage of CPU usage for script processing.

**Note:** This is a BETA control. Though functional, it is not feature complete and must not be relied upon in production environments.

#### Audio File Sync

Text field indicating whether or not the audio files on the inactive Core, of a redundant pair, are in sync with the active Core.

#### Details

This section is available only when the **Verbose Property** is set to **Yes**.

Text indicating the Details of any errors occurring with the Core. The information in this field is updated regularly and is cumulative. None of the items listed below display unless there is a value associated with it. If there are values associated with these, call [Support](../Support.htm).

|  |  |
| --- | --- |
| fpga\_fifo\_error | sequence\_error |
| recv\_fifo\_error | xmit\_task\_early |
| xmit\_fifo\_error | xmit\_task\_late |
| recv\_dma\_error | xmit\_task\_error |
| xmit\_dma\_error | xmit\_overrun |
| sync\_error | clock\_sync\_loss |

#### Compute Usage Averaging Time

You can set the desired usage averaging time between 2.00s and 60.0s.

### Primary / Backup

This section is available only when the **Is Redundant** Property is set to **Yes**.

#### Active

Identifies which Core is currently **Active**

#### Standby

Lights if the Core is in **Standby** mode. When the Core is booting, this LED is lit.

#### Go Active

Click this button to force the inactive Core to become **Active**. [1](#redundant_core_switch)

###### 1. In a redundant Core, redundant network system when the LAN-A connection to one Core is removed, and the LAN-B connection to the other Core is removed, you cannot switch between Cores using the Go-Active button.

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

### DSP Statistics

This section is available only when the **Verbose Property** is set to **Yes**.

#### DSP Core *n* Audio (audio processing time â microseconds)

Contains the following information when the count is not zero:

* current
* minimum
* average
* spread
* maximum
* lat\_current
* lat\_minimum
* lat\_average
* lat\_spread
* lat\_maximum
* periods
* overruns
* timeouts

#### DSP Core *n* Block (block processing time â microseconds)

Contains the following information when the count is not zero:

* current
* minimum
* average
* spread
* maximum
* lat\_current
* lat\_minimum
* lat\_average
* lat\_spread
* lat\_maximum
* periods
* overruns
* timeouts

#### DSP Core *n* Parameter (parameter processing time â microseconds)

Contains the following information when the count is not zero:

* current
* minimum
* average
* spread
* maximum
* lat\_current
* lat\_minimum
* lat\_average
* lat\_spread
* lat\_maximum
* periods
* overruns
* timeouts

#### Reset

Resets the statistics in the Audio, Block, and Parameter fields.

While the Reset button resets all entries in these fields, the average, periods, and overruns are the most noticeable.

#### CPU Statistics Notes:

* **average**
  - the result of the number displayed in the **average** field, divided by 300, then multiplied by 100 should be slightly less than the **DSP Usage** shown in File -> Check Design....
* **maximum**
  - a value of > 333 causes **overruns** to increment, which means a dropout in the audio. An isolated dropout sounds like a click and is usually inaudible with program material but can be heard when listening to pure tones. There may occasionally be overruns when the design starts or when the primary and backup of a redundant pair of cores are swapped because of clock mastership change. This is OK because audio streams are not running at these points.

### USB Reset

#### USB Reset

*(Only available on the Core 110f, Core Nano, NV-32-H Core and Peripheral Mode, NV-21-HU, Core 8 Flex, and TSC-G3 Touch Panels)* This reinitializes the USB driver without the need for a full design redeploy, restoring connections and USB functionality after a few seconds.

[USB Audio](javascript:void(0))

The following information is available only when the USB Audio Bridge, in the Properties, is set to anything except Disabled, and one or more of the USB Audio components are in the schematic.

#### Connection

Green LED indicating that the USB out component is connected to a computer.

#### USB Speed

Speed of the USB Connection. For example: High (2.0).

#### Active

Green LED indicating that signal is streaming.

#### Reset

Resets the Sample count for the associated audio device.

[USB Video](javascript:void(0))

The following information is available only when the USB Audio Bridge, in the Properties, is set to anything except Disabled, and one or more of the USB Audio components are in the schematic.

### Input

#### Input LED

Indicates whether or not there is active input to the Q-SYS video input device.

#### Input Connection

The network name of the Q-SYS video input device.

#### Bitrate (Kb/s)

The current input video bitrate, in kilobits per second.

#### Frames per Sec

Number of frames per second being sent by the video device.

#### Frame Count

Total number of frames sent.

#### Packet Count

Total number of packets since the last reset.

#### Packets Lost

Number of packets lost since the last reset.

#### Packet Loss%

The percentage of packets lost based on Packets Lost and Packet Count.

#### Test Button

Test the network setup for the Q-SYS video streaming implementation without having a PC or any USB connection. This tests QoS and IGMP on multicast.

### USB

#### USB Active LED

Video Bridge USB Active: Indicates if the USB is active or not.

#### USB Bridge Name

The network name of the Q-SYS video bridging device.

#### Video Format

Displays the format of the video present on the USB â for example, "1920x1080p30".

#### Encoding

Displays the type of encoding used for the USB video stream - for example, "MJPEG".

#### USB Speed

Displays the detected USB speed capability of the connection â for example, "High Speed (2.0)".

#### Bitrate (Mb/s)

USB bitrate, in megabits per second.

#### Frames per Sec

USB frames per second

#### SRC-

The number of samples removed in order to match the USB clock with the Q-SYS PTP clock

#### SRC+

The number of samples added in order to match the USB clock with the Q-SYS PTP clock

### Reset

#### Reset Button

Clears the readings, and restarts monitoring.

[Control Pins](javascript:void(0))

**Note:** The Control Pins that are available depend on the Properties selected.

[NV-32-H (Core Capable)](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Aux Power Active | 0  1 | false  true | 0  1 | Output |
| Core Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| CPU Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Fan 1, 2 RPM | *n* | *n* | - | Output |
| I/O Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Network Clock Grandmaster Name | (text) | | | Output |
| Network Clock Master | 0  1 | false  true | 0  1 | Output |
| Network Clock Offset from Master | - | *n*us | - | Output |
| Network Clock Parent Port Name | (text) | | | Output |
| PoE < 90w | 0  1 | false  true | 0  1 | Output |
| PoE = 90w | 0  1 | false  true | 0  1 | Output |
| VPU Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |

[All Other Cores](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Primary / Backup (must be redundant) | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| Go Active | 0  1 | false  true | 0  1 | Input / Output |
| Standby | 0  1 | false  true | 0  1 | Output |
| Chassis Fan | | | | |
| RPM | 4-digit number | text | N/ A | Output |
| Compute Usage [BETA] (Verbose property must be set to Yes) | | | | |
| Compute Usage Averaging Time | 2.00-60.0 | 2.00-60.0 | 0.0-1.00 | Input / Output |
| Control Compute Usage | 0 to 100 | 0-100% | 0.0 to 1.00 | Output |
| Lua Compute Usage | 0 to 100 | 0-100% | 0.0 to 1.00 | Output |
| Network Compute Usage | 0 to 100 | 0-100% | 0.0 to 1.00 | Output |
| Process Compute Usage | 0 to 100 | 0-100% | 0.0 to 1.00 | Output |
| Network |  | | | |
| Clocking |  | | | |
| Clock Master | 0  1 | false  true | 0  1 | Output |
| Clock Grandmaster Name | Text box indicating the network name of the Network Clock Grandmaster | | | Output |
| Clock Offset From Master | â | 0 ms to *n* ms | â | Output |
| Clock Parent Port Name | Text box indicating the network name of the Parent port, usually the same as the Network Clock Grandmaster with the LAN appended. | | | Output |
| PTPv1 Dante | Text | | | Output |
| LAN A / B | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| IP Address | Text | | | Output |
| Mode | Text | | | Output |
| PTP State | Text | | | Output |
| Speed | Text | | | Output |
| Statistics (must be Verbose) | | | | |
| Audio *n* | Text box with statistics on the audio processing for each DSP core | | | Output |
| Block *n* | Text box with statistics on the block processing for each DSP core | | | Output |
| Parameter *n* | Text box with statistics on the parameter processing for each DSP core | | | Output |
| Reset | trigger | | | Input / Output |
| USB Sound Card *n* In/Out | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| Video Bridge | | | | |
| IP Stream 1 | | | | |
| Bitrate | *n*.*n* | *n*.*n* | - | Output |
| FPS | *n* | *n* | - | Output |
| Frame Count | *n* | *n* | - | Output |
| Packet Count | *n* | *n* | - | Output |
| Packet Loss Percentage | *n*.*n* | *n*.*n* | - | Output |
| Packet Lost | *n* | *n* |  | Output |
| Test Stream 1 | 0  1 | false  true | 0  1 | Input / Output |
| USB | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| Bitrate | 0.0000 and up | 0 and up | 0.00 to 1.00 | Output |
| Bridge Name | (text) | | | Output |
| Encoding | (text) | | | Output |
| FPS | 0 to 30 | 0 to 30 | 0.00 to 1.00 | Output |
| SRC- | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| SRC+ | 0 and up | 0 and up | 0.00 to 1.00 | Output |
| USB Speed | (text) | | | Output |
| Video Format | (text) | | | Output |
| Input Active | 0  1 | false  true | 0  1 | Output |
| Input Connection | (text) | | | Output |
| Reset | (trigger) | | | Input / Output |
| Audio File Sync | Text box with information regarding syncing audio files between redundant Cores | | | Output |
| Chassis Temperature | Text box displaying the internal temperature of the Core in Centigrade. | | | Output |
| Core Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
| External Clock  (clock must not be internal) | 0  1 | false  true | 0  1 | Output |
| External Clock Frequency  (clock must not be internal) | Text box displaying the external clocks frequency in Hz. | | | |
| External Lock  (clock must not be internal) | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Power Supply *n* Status | 0  1 | false  true | 0  1 | Output |
| Memory Used | 0 to 100 | Text  0 to 100% | 0.0 to 1.00 | Output |
| Processor Temperature | Text box displaying the temperature of the Core's processor in Centigrade. | | | Output |
| System Info (Details) | Text field displaying system information. | | | Output |
| USB Reset | off  on | 0  1 | off  on | Input |

[Troubleshooting](javascript:void(0))

### "Fault - Audio Enabled Peripherals LAN B disabled in Network Services"

If your design contains an AES67 Receiver or Atmos Receiver (cinema only) component that was originally added to your design prior to version 7.0.1, you may see the aforementioned fault message in the Core Status component after saving your design to the Core. To resolve, replace these components in your design with new versions.
