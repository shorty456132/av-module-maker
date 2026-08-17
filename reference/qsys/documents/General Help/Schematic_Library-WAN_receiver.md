# WAN Receiver

> Source: https://help.qsys.com/Content/Schematic_Library/WAN_receiver.htm

# WAN Receiver

The WAN stream components allow you to stream MP3-compressed, 48 kHz sample rate audio between Cores, or between a Core and other devices, over a Wide Area Network (WAN). There are two WAN Stream components: the [WAN Transmitter](WAN_transmitter.htm), and the WAN Receiver.

The WAN Receiver is disabled on the inactive Core of a redundant pair. If the inactive Core becomes active, the WAN Receiver is enabled on that Core.

The WAN Receiver can receive audio from a WAN Transmitter on another Core, or from compatible media players such as VLC, or compatible hardware such as the Barix Instreamer.

[Core Maximums](javascript:void(0))

The maximum number of Media Stream Receivers plus WAN Receivers you can have in a design for each Core is shown in the table below.

**Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information.

| Core Model | Max Number of Receiver Components/Streams | Max Number of Receive Channels |
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

This component does not have any input pins.

### Output Pins

#### Channel 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the WAN Receiver component is set to **Stereo**, which allows for a left and right output. You can choose **Mono**, which gives only one output. Or you can select **Multi-Channel**, which lets you choose between 3 and 16 outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Channels

#### Type

Sets the type of Channels in the WAN Receiver.

Must match the Transmitter.

#### Count

For Multi-Channel, sets the number of channels available for use on the Receiver.

Must match the Transmitter.

If you have multiple WAN Receivers in your design, the maximum number of received channels is 32.

### Streams

#### Count

Sets the number of unicast audio streams for the Receiver, which should match the Transmitter.

If you have multiple WAN Receivers in your design, the maximum number of received streams is 16.

### Stream (1 - 8)

#### Interface

Select the network interface on which the Stream (1 - 8) is to be received.

**Note:** To avoid inconsistent streaming performance and network issues, both the WAN Transmitter and WAN Receiver should be assigned to the same network Interface.

#### Even IP Port

Sets the port number for streaming.

[Controls](javascript:void(0))

#### Peak Level (dBFS)

Meter displaying the Peak Input Level.

#### Invert

Button to invert the input audio signal.

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

[Using the WAN Receiver](javascript:void(0))

1. Drag the Receiver component into the Schematic of the design on the Receiving Core.
2. Select the Properties for the Receiver.
3. Ensure the Properties for this Receiver match the associated Transmitter on the other Core.
4. Make the appropriate connections between the Receiver channels and the component, in the design, where you want the audio to begin the local processing.
5. Both Cores must be running their respective designs.
6. Start Transmission.

[External Streaming](javascript:void(0))

The Q-SYS WAN Receiver is capable of receiving 48 kHz streaming audio from the VLC media player and a BARIX Instreamer.

[VLC media player](javascript:void(0))

To stream 48 kHz audio from a VLC media player on a Windows PC to the Q-SYS WAN Receiver:

1. You must have a Q-SYS Designer design running with a Receiver properly configured.
2. Download and install the latest open source [VLC media player](http://www.videolan.org/vlc/download-windows.html) on a Windows PC.
3. **MP3 File:** At a Windows Command Prompt window, enter the following to start streaming 48 kHz MP3 audio to the WAN Receiver:

   "\Program Files\VideoLAN\VLC\vlc.exe" "file.mp3" :sout=#rtp{dst=core\_ip\_address,port-audio=udp\_port\_number}

   `file.mp3` = path and file name of the file you want to play,

   `core_ip_address` = address of the Core you are streaming to,

   `udp_port_number` = the Even Port Number of the WAN Receiver.
4. **WAV File:** At a Windows Command Prompt window, enter the following to start streaming a .wav file at 64 kbit/sec to the WAN Receiver:

   "\Program Files\VideoLAN\VLC\vlc.exe" "file.wav" :sout=#transcode{acodec=mpga,ab=64,channels=2,samplerate=48000}:rtp{dst=core\_ip\_address,port-audio=udp\_port\_number} -vv

   `file.wav` = path and file name of the file you want to play,

   `core_ip_address` = address of the Core you are streaming to,

   `udp_port_number` = the Even Port Number of the WAN Receiver,

   `ab=64` = the compression bit rate. The 64 can be replaced with: 32, 48,64, 96, 128, 160, 224, 320 (kbit / second).
5. The VLC Media Player is opened with the requested file. You can use the controls on the VLC Media Player as required. The audio is streamed to the destination WAN Receiver.

[Barix Instreamer](javascript:void(0))

To stream 48 kHz (MP3) audio from a [Barix Instreamer](http://www.barix.com/Instreamer/301/) to the Q-SYS WAN Receiver:

1. You must have a Q-SYS Designer design running with a WAN Receiver properly configured.
2. You must have a Barix Instreamer connected to your WAN per the manufacturer's instructions.
3. On the Barix Instreamer Device Configuration web page ([http://xxx.xx.xxx.xxx This is the IP address of the Barix Instreamer as assigned per the manufacturer's instructions.](javascript:void(0))/uiconfig.html ) enter the following information:
   1. Network: Leave at the default of zeros, or enter static information for the Barix Instreamer.
   2. Audio:
      1. Channel Mode: Stereo or Mono to match the WAN Receiver setting.
      2. Encoding+Frequency: MPEG1 / 48 kHz (MP3)
   3. Streaming:
      1. Stream to: Conn. type: RTP, IP address of the Core, Port as on the WAN Receiver, or  
         Conn. type: RTP, Port as on the WAN Receiver
   4. All other settings can be left at the default.
4. Start streaming audio.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* Gain | -100 to 20 | *n* dB | 0  1 | Input / Output |
| Channel *n* Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Channel *n* Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Channel *n* Peak Input Level | -120 to 43 | -120 dB to 43 dB | 0  1 | Output |
| Receiver Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |
