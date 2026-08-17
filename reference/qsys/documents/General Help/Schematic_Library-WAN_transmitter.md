# WAN Transmitter

> Source: https://help.qsys.com/Content/Schematic_Library/WAN_transmitter.htm

# WAN Transmitter

The WAN stream components allow you to stream MP3-compressed, 48 kHz sample rate audio between Cores, or between a Core and other devices, over a Wide Area Network (WAN). There are two WAN components: the WAN Transmitter, and the [WAN Receiver](WAN_receiver.htm).

The WAN Transmitter can transmit audio to a WAN Receiver on another Core, or to compatible media players such as VLC, or compatible hardware such as the Barix Exstreamer.

[Core Maximums](javascript:void(0))

The following table shows the maximum sum of WAN Transmitters and Media Stream Transmitters per Core.

**Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information.

| Core Model | Max Number of Transmitter Components/Streams | Max Number of Transmit Channels |
| --- | --- | --- |
| NV-32-H (Core Capable) | 6 | 12 |
| Core Nano | 6 | 12 |
| Core 8 Flex | 6 | 12 |
| Core 110f | 12 | 24 |
| Core 510i | 32 | 64 |
| Core 5200 | 128 | 256 |

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type**Property.

### Input Pins

#### Channel 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the WAN Transmitter component is set to **Stereo**, which allows for a left and right output. You can choose **Mono**, which gives only one output. Or you can select **Multi-Channel**, which lets you choose between 3 and 16 outputs.

### Output Pins

This component does not have any output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Channels

#### Type

Sets the type of Channels in the WAN Transmitter.

Must match the Receiver.

#### Count

For Multi-Channel, sets the number of channels available for use on the Transmitter.

Must match the Receiver.

If you have multiple WAN Transmitters in your design, the maximum number of transmitted channels is 32

### Compression

#### Channel Bit Rate

Sets the bit rate for the Transmitter. Higher bit rate delivers higher quality audio and requires more network bandwidth.

When Multi-Channel is selected, the Multi-Channel Stream Bit Rate is the Channel Count times the Bit Rate.

### Streams

#### Count

Sets the number of audio streams for the Transmitter.

If you have multiple WAN Transmitters in your design, the maximum number of transmitted streams is 16.

### Stream (1 - 8)

#### Interface

Select the network interface on which the Stream (1 - 8) is to be transmitted.

The Interface selection allows you to associate streams with particular networks. For example, in a redundant network, redundant Core system, streams 1 and 2 to the primary Core would be associated with LAN A and LAN B respectively. It also allows use of the AUX A or AUX B interfaces, if desired.

**Note:** To avoid inconsistent streaming performance and network issues, both the WAN Transmitter and WAN Receiver should be assigned to the same network Interface.

#### Destination IP Address

The IP address of the destination receiver, which must be a valid unicast address.

#### Even IP Port

Sets the port number for streaming.

[Controls](javascript:void(0))

#### Peak Level (dBFS)

Meter displaying the Peak Output Level of the Transmitter.

#### Clip

Red LED indicating if the audio signal is being clipped.

#### Clip Hold

Button to hold the Clip LED on until released.

#### Invert

Button to invert the output audio signal.

#### Mute

Button to mute the input audio signal.

#### Gain (dB)

Controls the input gain.

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

[Using the WAN Transmitter](javascript:void(0))

1. Drag the Transmitter component into the Schematic of the design on the Transmitting Core.
2. Select the Properties for the Transmitter.
3. Connect the audio source to the inputs of the Transmitter.
4. Ensure the Receiver's Properties on the other Core are configured to match this Transmitter's configuration.
5. Both Cores must be running their respective designs.
6. Start Transmission.

[External Streaming](javascript:void(0))

The Q-SYS WAN Transmitter is capable of streaming audio to the VLC media player and Barix.

#### VLC media player

To stream audio to a VLC media player:

1. You must have a Q-SYS Designer design running with a Transmitter configured and connected to an audio source.
2. Download and install the latest open source [VLC media player](http://www.videolan.org/vlc/download-windows.html).
3. Launch the VLC media player.
4. On the VLC main menu select Media > Open Network.
5. Select RTP from the Protocol drop-down list.
6. Enter your design's WAN Transmitter's (UDP) Even Port Number in the Port text box.
7. Click Play.
8. You can start transmitting from Q-SYS and receiving with the VLC media player.

[Barix](javascript:void(0)) 

To stream audio to a [Barix Exstreamer](http://www.barix.com/Overview/771/):

1. You must have a Q-SYS Designer design running with a Transmitter configured and connected to an audio source.
2. You must have a Barix Exstreamer connected to your WAN per the manufacturer's instructions.
3. On the Barix Exstreamer Device Configuration web page ([http://xxx.xx.xxx.xxx This is the IP address of the Barix Exstreamer as assigned per the manufacturer's instructions.](javascript:void(0))) enter the following information:
   1. Stream Settings: URL: rtp://0.0.0.0: *<transmitter UDP port number>*  
      If you enter all zeros, as in the example, the Exstreamer receives anything coming to the specified port. This is the IP Address of the Exstreamer.
4. All other settings can be left at the defaults.
5. Start streaming audio.

[Control Pins](javascript:void(0))

The Control Pins are available for each channel, with the exception of the Status Control Pin which is for the whole component.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clip | 0  1 | false  true | 0  1 | Output |
| Clip Hold | 0  1 | false  true | 0  1 | Input / Output |
| Gain | -100 to 20 | -100 dB to 20 dB | 0  1 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Peak Output Level | -120 to 43 | -120 dB to 43 dB | 0  1 | Output |
| Transmitter Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
