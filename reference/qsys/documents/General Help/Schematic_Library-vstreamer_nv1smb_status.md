# Status (NV-21-HU)

> Source: https://help.qsys.com/Content/Schematic_Library/vstreamer_nv1smb_status.htm

# Status (NV-21-HU)

The NV-21-HU Status component provides detailed information about the NV-21-HU, including hardware health, network AV source details and statistics, Q-SYS Core audio streaming details (if applicable), and USB audio and video bridging details (if enabled).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Network Video Endpoint Properties

#### External USB Audio

When enabled, you can connect an external audio device to the USB input and route audio to and from that device. See [External USB Audio Device In](alsa_receiver_sound_card.htm) and [External USB Audio Device Out](alsa_transmitter_sound_card.htm).

### HDMI / Shift AV

#### Device Type

Can set the NV-21-HU as a **Decoder** or **Encoder**.

[Decoder](javascript:void(0))

#### AV Input Count

For Decoders only, this property determines the number of exposed AV input pins, from 0 to 480. The default is '3'.

#### HDMI Output Mode

This property determines the functionality of the NV-21-HU HDMI outputs.

HDMI 1: Video and audio output is enabled for the HDMI 1 output connector.

#### HDMI 1 Audio Pins

If enabled in the component Properties (HDMI Output Mode is set to "HDMI 1 + HDMI 2"), select the number of audio pins to expose â from 0 to 8 â for routing to other Q-SYS audio components, such as a network amplifier. This audio corresponds to the HDMI Output 1 or 2 source you select in the HDMI I/O control panel.

**Tip:** These pins automatically send audio for whatever HDMI video source is selected for display. No additional programming is required to align audio and video signals.

[Encoder](javascript:void(0))

#### AV IP Streaming

For Encoders only, this property determines the network streaming method for Q-LAN AV streams:

* Compiler Choice: (Default) Select this option to allow Q-SYS Designer Software to determine whether unicast (one-to-one) or multicast (one-to-many) is best for your configuration. This is the recommended option.
* Unicast: Select this option when your design contains one-to-one AV routing, meaning that each AV output pin in your design is connected to a single AV input pin.
* Multicast: Select this option when your design contains one-to-many AV routing, meaning that an AV output pin is connected to multiple AV input pins.

#### HDMI Output Mode

This property determines the functionality of the NV-21-HU HDMI outputs.

* None: (Default) Video and audio output is **disabled** for the HDMI output connector.
* HDMI 1: Video and audio output is **enabled** for the HDMI 1 output connector.

[Controls](javascript:void(0))

Your configuration of the NV-21-HU determines which status tabs are shown:

* [Status](#Status)
* [Network AV Sources](#Network)
* [Core Stream Details](#Core)

## Status

### NV-21-HU Status

#### ID

Click to flash the green ID LED on the front of the NV-21-HU unit. The indicator flashes indefinitely until you press the ID button again.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Clock Offset

Indicates how much of an offset exists, in microseconds, between the NV-21-HU and the network Grandmaster.

#### Grandmaster

Indicates the current clock master of the network.

#### Processor Temperature

The current temperature, in Celsius, of the NV-21-HU central processing unit.

#### Chassis Temperature

The current temperature, in Celsius, of the NV-21-HU HDMI I/O hardware.

#### Parent Port

The clock Parent Port is the device and interface name to which the NV-21-HU is syncing. Typically, this is the Grandmaster.

#### Fan

Indicates the current RPMs of the fan within the NV-21-HU.

### Power

#### PoE = < 45W

This LED glows if the NV-21-HU is connected to a switch port that does not support the required PoE++ (802.3bt [Type 3 Class 5 A Type 3 power supply provides 40 watts of power, which the NV-21-HU requires.](javascript:void(0))) power standard. This is accompanied by an "Insufficient power" fault in the NV-21-HU Status section.

**Note:** This LED can also glow if the switch port to which the NV-21-HU is connected does not properly negotiate the 802.3bt Type 3 standard, despite being capable of providing proper power. If you believe this is the case, enable the Operate with any PoE Power Sourcing Equipment option in Peripheral Manager. For more information, see the Peripheral Manager > [Network Settings](../Peripheral_Manager/Network_Settings.htm) topic.

#### PoE = 40W, Class 5

This LED glows if the NV-21-HU is receiving power from a switch port that supports the required PoE++ (802.3bt Type 3 Class 5) standard.

#### Aux Power

This LED glows if the NV-21-HU is receiving power via 12V DC.

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

### USB Reset

#### USB Reset

This reinitializes the USB driver without the need for a full design redeploy, restoring connections and USB functionality after a few seconds.

### Power Delivery to Host

#### USB-C PD Active LED

The LED is on when power is ready to be delivered to the connected USB-C device.

* When a USB-C Host decides to use the USB-C PD power, the voltage and current it decides to use is seen in the *Requested Power* indicator text box.
* When the USB-C Host activates the PD power, the PD Active LED will go on.

**Note:** Some USB-C Host devices will select a power level, activate it, yet do not enable charging, meaning the PD Active LED is on and yet the Host isnât accepting the power.

#### USB-C PD Fault LED

The LED is on when an error delivering power to the USB-C Host has occurred.

* On when the USB-C Host has drawn too much current and stays on until the PD State machine enters the PD Idle State

**Note:** The only way to clear the fault is to unplug the cable or to disable the PD enable button.

#### USB-C PD Enable Button

The default is Off in new Designs. If set to Enable, device charging via USB-C is active. Whenever the button changes state, the existing USB-C connection is reset and the PD state machine enters the PD Idle State.

* When turned on: Enables 65w power delivery and advertisement.
* When turned off: Disables all power delivery and advertisement.

#### USB-C Requested Power Indicator

This control indicates the current voltage provided by the USB-Host.

**Note:** This control does not show the actual voltage and current being delivered to the USB-C Host, rather it displays the voltage and current requested by the host, the actual amounts are often different

* When the PD Active LED is off, the PD Power Indicator text box is blank, when on, the text indicates the power that the USB-C Host device has requested

## Network AV Sources

The information shown depends on whether the NV-21-HU is configured as an Encoder or Decoder.

[Encoder](javascript:void(0))

This tab reports the audio and video details and statistics for any HDMI Input on the NV-21-HU connected to a [Generic AV Source](vst_hdmi_source.htm).

#### Audio

The Details section displays cumulative information for HDMI audio being received from the source. This information resets during a design restart on the Q-SYS Core or whenever you click Reset Details.

#### Video

This section displays cumulative count information for HDMI video being received from the source and transmitted to a destination display. Information refreshes every second. Click Reset Statistics to clear the information.

* Tx Count: The number of video network packets actually placed on the network. This is the Payload Count less Drop Count.
* Drop Count: The number of video network packets that could not be placed on the network.
* Payload Count: The number of video network packets intended to be placed on the network.
* Bitrate: The rolling, averaged video bitrate for the last 1 second of transmission.
* Peak Bitrate: The highest recorded video bitrate for a single frame of video, rounded to the nearest Mbps, since the statistics were reset.

  **Note:** It is possible for the Peak Bitrate value to exceed the Bitrate (Mbps) control in the [AV I/O (NV-21-HU)](av_io.htm) component, as the Bitrate (Mbps) setting is a maximum average network video bitrate, not an absolute maximum.
* DSCP: The current QoS DSCP value being used for video packet transmission, as configured in the [Design Properties](design_properties.htm).
Network Test: Click this button to initiate a test of the network's ability to losslessly carry video data from an NV-21-HU Encoder to an NV-21-HU Decoder (or, in the case of a multicast configuration, multiple Decoders). You can initiate the test from the NV-21-HU Status component of either the Encoder or Decoder.

+ When you click the button, the Encoder generates a green, pixelated test pattern that should be visible on the display connected to the Decoder. This test pattern causes the NV-21-HU Encoder to create an IP video stream that reaches and sustains the Bitrate (Mbps) setting of the [AV I/O (NV-21-HU)](av_io.htm) component.
+ While the test runs, observe the Decoder's video statistics within the Network AV Sources > Video section. Lost packets, errors, and drops should be at or near 0.
+ If you do not see a test pattern, or you see a test pattern but the Decoder's video statistics indicate lost packets, errors, or drops, the network may not be configured properly or is otherwise unable to transport the desired video bitrate. Refer to the Q-SYS Networking > [Clocking, Audio, Video, & Control](../Networking/Clocking_Audio_Video_Control.htm) topic to learn about the requirements for Q-SYS Video.
+ Click the Network Test button again to end the test, which resumes the AV signal for the HDMI Input.

**Note:** Do not initiate a Network Test while the system is in use. Running a Network Test disrupts the AV signals being transmitted between Encoder and Decoder, as well as local HDMI output from an Encoder. Any hotplug event (such as an HDMI device waking from sleep, or connecting or disconnecting its HDMI cable) will end the test. For long term testing, you should unplug all HDMI sources.

[Decoder](javascript:void(0))

This tab reports the audio and video details and statistics for any HDMI Output on the NV-21-HU connected to a [Generic HDMI Display](vst_hdmi_display.htm).

#### Audio

The Details section displays cumulative information for HDMI audio being sent to a display. This information resets during a design restart on the Q-SYS Core or whenever you click Reset Details.

#### Video

This section displays cumulative count information for HDMI video being received from a source and transmitted to a display. Information refreshes every second. Click Reset Statistics to clear the information.

* Source Name: The currently-selected AV source being sent to the HDMI output.
* Bitrate: The rolling, averaged video bitrate for the last 1 second of transmission.
* Peak Bitrate: The highest recorded video bitrate for a single frame of video, rounded to the nearest Mbps, since the statistics were reset.
* BMcast IP Src: Bad Multicast IP Source. Displays the source IP addresses that are incorrectly broadcasting on this source's multicast address. (Only one device on the network should be using this multicasting IP address.)
* Packets Lost: Displays how many network packets were lost (due to errors, dropped packets, overruns, etc.) between the currently selected source and this device.
* Packet Loss %: The percentage of network packets lost from the Packet Count.
* Packet Count: The running total of network packets received by the device.
* Sequence Errs: The number of network packets that were received out of order.
* HW Drop Count: The number of network packets successfully retrieved from the network but could not be processed by the NV-21-HU hardware.
Network Test: Click this button to initiate a test of the network's ability to losslessly carry video data from an NV-21-HU Encoder to an NV-21-HU Decoder (or, in the case of a multicast configuration, multiple Decoders). You can initiate the test from the NV-21-HU Status component of either the Encoder or Decoder.

+ When you click the button, the Encoder generates a green, pixelated test pattern that should be visible on the display connected to the Decoder. This test pattern causes the NV-21-HU Encoder to create an IP video stream that reaches and sustains the Bitrate (Mbps) setting of the [AV I/O (NV-21-HU)](av_io.htm) component.
+ While the test runs, observe the Decoder's video statistics within the Network AV Sources > Video section. Lost packets, errors, and drops should be at or near 0.
+ If you do not see a test pattern, or you see a test pattern but the Decoder's video statistics indicate lost packets, errors, or drops, the network may not be configured properly or is otherwise unable to transport the desired video bitrate. Refer to the Q-SYS Networking > [Clocking, Audio, Video, & Control](../Networking/Clocking_Audio_Video_Control.htm) topic to learn about the requirements for Q-SYS Video.
+ Click the Network Test button again to end the test, which resumes the AV signal for the HDMI Input.

**Note:** Do not initiate a Network Test while the system is in use. Running a Network Test disrupts the AV signals being transmitted between Encoder and Decoder, as well as local HDMI output from an Encoder. Any hotplug event (such as an HDMI device waking from sleep, or connecting or disconnecting its HDMI cable) will end the test. For long term testing, you should unplug all HDMI sources.

## Core Stream Details

This tab appears only when your design requires NV-21-HU audio to be processed by the Q-SYS Core. This information resets during a design restart on the Q-SYS Core or whenever you click Reset Details.

#### Input Details (Audio to Core)

If audio is being passed to the Q-SYS Core from the NV-21-HU, details for that audio appear here, such as when any of these component output audio pins are wired in the design:

* [AV I/O (NV-21-HU)](av_io.htm) â AV Audio pins
* [Generic AV Source](vst_hdmi_source.htm) â Breakaway Channel pins
* [USB Audio Bridge â Speakerphone / Sound Card In](usb_receiver.htm)

#### Output Details (Audio from Core)

If audio is being passed from the Q-SYS Core to the NV-21-HU, details for that audio appear here, such as when any of these component input audio pins are wired in the design:

* [Generic HDMI Display](vst_hdmi_display.htm) â Breakaway Channel pins
* [USB Audio Bridge â Speakerphone / Sound Card Out](usb_transmitter.htm)

[Control Pins](javascript:void(0))

The control pins shown depend on whether the NV-21-HU is configured as an Encoder or Decoder, as well as the additional components present in the Schematic.

[Encoder](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Core Networked Audio | | | | |
| Input Stream Details | (text) | | | Output |
| Output Stream Details | (text) | | | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Network | | | | |
| Clocking | | | | |
| Grandmaster Name | (text) | | | Output |
| Offset From Master | - | *n*us | - | Output |
| Parent Port Name | (text) | | | Output |
| LAN A | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| IP Address | (text) | | | Output |
| Mode | (text) | | | Output |
| PTP State | (text) | | | Output |
| Speed | (text) | | | Output |
| Networked Audio | | | | |
| AV Input *n* | | | | |
| Details | (text) | | | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Networked Video | | | | |
| AV Input *n* | | | | |
| Bitrate | *n* | *n* | - | Output |
| Drop Count | *n* | *n* | - | Output |
| DSCP | *n* | *n* | - | Output |
| Network Test | 0  1 | false  true | 0  1 | Input / Output |
| Payload Count | *n* | *n* | - | Output |
| Peak Bitrate | *n* | *n* | - | Output |
| Tx Count | *n* | *n* | - | Output |
| USB Speakerphone / Sound Card In | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| USB Speakerphone / Sound Card Out | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| USB-C PD | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| Enable | 0  1 | false  true | 0  1 | Input / Output |
| Fault | 0  1 | false  true | 0  1 | Output |
| Requested Power | (text) | | | Output |
| Aux Power Active | 0  1 | false  true | 0  1 | Output |
| Aux Power Voltage | (text) | | | Output |
| Chassis Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Fan 1 RPM | *n* | *n* | - | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Networked Video Reset Statistics | 0  1 | false  true | 0  1 | Input / Output |
| NV-21-HU Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| PoE < 45w | 0  1 | false  true | 0  1 | Output |
| PoE = 45w | 0  1 | false  true | 0  1 | Output |
| Processor Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| USB Connected | 0  1 | false  true | 0  1 | Output |
| USB Reset | 0  1 | off  on | 0  1 | Input / Output |

[Decoder](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Core Networked Audio | | | | |
| Input Stream Details | (text) | | | Output |
| Output Stream Details | (text) | | | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Network | | | | |
| Clocking | | | | |
| Grandmaster Name | (text) | | | Output |
| Offset From Master | - | *n*us | - | Output |
| Parent Port Name | (text) | | | Output |
| LAN A | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| IP Address | (text) | | | Output |
| Mode | (text) | | | Output |
| PTP State | (text) | | | Output |
| Speed | (text) | | | Output |
| Networked Audio | | | | |
| HDMI Output 1 | | | | |
| Details | (text) | | | Output |
| Reset Details | 0  1 | false  true | 0  1 | Input / Output |
| Networked Video | | | | |
| HDMI Output 1 | | | | |
| Bitrate | *n* | *n* | - | Output |
| BMcast IP Src | (text) | | | Output |
| HW Drop Count | *n* | *n* | - | Output |
| Network Test | 0  1 | false  true | 0  1 | Input / Output |
| Packet Count | *n* | *n* | - | Output |
| Packet Loss % | *n* | *n.n* | - | Output |
| Packets Lost | *n* | *n* | - | Output |
| Peak Bitrate | *n* | *n* | - | Output |
| Sequence Errors | *n* | *n* | - | Output |
| Source | (text) | | | Output |
| USB Speakerphone / Sound Card In | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| USB Speakerphone / Sound Card Out | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| USB-C PD | | | | |
| Active | 0  1 | false  true | 0  1 | Output |
| Enable | 0  1 | false  true | 0  1 | Input / Output |
| Fault | 0  1 | false  true | 0  1 | Output |
| Requested Power | (text) | | | Output |
| Aux Power Active | 0  1 | false  true | 0  1 | Output |
| Aux Power Voltage | (text) | | | Output |
| Chassis Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| Fan 1 RPM | *n* | *n* | - | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Networked Video Reset Statistics | 0  1 | false  true | 0  1 | Input / Output |
| NV-21-HU Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| PoE < 45w | 0  1 | false  true | 0  1 | Output |
| PoE = 45w | 0  1 | false  true | 0  1 | Output |
| Processor Temperature | *n*.*n* | *n*.*n*Â°C | - | Output |
| USB Connected | 0  1 | false  true | 0  1 | Output |
| USB Reset | 0  1 | off  on | 0  1 | Input / Output |
