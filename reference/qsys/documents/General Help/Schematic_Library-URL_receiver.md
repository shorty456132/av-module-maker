# Media Stream Receiver

> Source: https://help.qsys.com/Content/Schematic_Library/URL_receiver.htm

# Media Stream Receiver

The Media Stream Receiver provides a method to receive compressed audio streamed over the network.

[Supported Sources and Codecs](javascript:void(0))

### Sources

**Note:** For streams that include both audio and video (e.g. StadiumVision), the audio is de-multiplexed and decoded, and the video is discarded.

* Unicast or Multicast Streams over raw UDP or RTP, including:
  + MPEG Transport Streams
  + Q-SYS Media Stream Transmitter
  + Barix Instreamer
* SDP (Session Description Protocol)
* Cisco StadiumVision
* SHOUTcast
* SVSi 7.1
* WyreStorm â audio stream ingest from NetworkHD 100 and 200 Series transmitters
* Atlona â audio stream ingest from OmniStream 111 and 112 transmitters, including the following stream types:
  + 2-channel and 6-channel PCM (8-channel PCM is not supported)
  + DTS HD
  + DTS 5.1
  + AC-3

  **Note:** Media Stream Receiver cannot receive streams from Atlona devices running firmware version 1.2.x or later due to stream format changes in later firmware versions. QSC recommends that you switch to AES67 streaming. Alternatively, do not update Atlona devices to firmware version 1.2.x to maintain compatibility with Media Stream Receiver.

### Languages

The Media Stream Receiver also supports languages embedded in the stream. This feature is currently available for IPTV (Internet Protocol Television) MPEG TS streams.

### Codecs

* MP3 (MPEG-2 Audio Layer III)
* AC-3 (ATSC A/52)
* G.711
* LPCM
* FLAC (Free Lossless Audio Codec)
* Vorbis

**Note:** The Media Stream Receiver does not support AAC audio due to licensing restrictions.

[Core Maximums](javascript:void(0))

The maximum number of Media Stream Receivers plus WAN Stream Receivers you can have in a design for each Core is shown in the table below.

**Note:** Q-SYS Scaling Licenses expand the capabilities of some Q-SYS Core processor models. Refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for more information.

| Core Model | Max Number of Receiver Channels | Max Number of Receiver Components/Streams | Max Number of Muxed A/V Receiver Channels | Max Number of Muxed A/V Receivers |
| --- | --- | --- | --- | --- |
| NV-32-H (Core Capable) | 12 | 6 | 12 | 6 |
| Core Nano | 12 | 6 | 12 | 6 |
| Core Nano / Core 8 Flex (Commercial AV Bundle) | 24 | 12 | 24 | 12 |
| Core 8 Flex | 12 | 6 | 12 | 6 |
| Core 110f | 24 | 12 | 24 | 12 |
| Core 24f | 36 | 36 | 36 | 36 |
| Server Core X10 | 64 | 64 | 64 | 64 |
| Core 510i | 64 | 32 | 96 | 16 |
| Core 610 | 64 | 32 | 96 | 32 |
| Server Core X20r | 96 | 96 | 96 | 96 |
| Core 610 (Scaling License) | 96 | 48 | 96 | 48 |
| Core 5200 | 256 | 128 | 192 | 32 |

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Channel 1 - 2

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Media Stream Receiver allows for two incoming channels.

### Output Pins

This component does not have any output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Media Stream Receiver Properties

#### Multiplexed A/V

If a Media Stream Receiver will be receiving streams with Audio and Video multiplexed together (e.g. HDTV via MPEG-TS), Multiplexed A/V should be set to "Yes" (the default). See [Core Maximums](#Core) for the maximum number of multiplexed (muxed) A/V receivers allowed in a design.

If the received streams are audio only, Multiplexed A/V may be set to "No".

**Note:** If Multiplexed A/V is set to No, and the streams have Multiplexed A/V, you will encounter audio dropouts if you attempt to receive too many streams at one time.

**Note:** If you have a large number of possible input streams, but a fairly small number of outputs/listeners, don't use one Component per input stream attached to a big router. It is better to have only one Component per output/listener and dynamically change the input streams using a script.

#### Mode

Select the type of output Channels.

The Media Stream Receiver automatically performs the appropriate up-mixing or down-mixing if the number of output channels differs from the channels available in the input stream.

#### Channel Count

Available when Mode is set to "Multichannel". The maximum total number of received channels for all Receivers in your design is based on the Core model. Refer to [Core Maximums](#Core).

[Controls](javascript:void(0))

### Input / Channel

#### Peak Level (dBFS)

Meter displaying the Peak audio level.

#### Invert

Inverts the audio signal.

#### Mute

Mutes the audio signal.

#### Gain (dB)

Controls the gain.

### Status

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Stream

#### Enable

Starts and stops the streaming.

#### URL

Enter the location of the stream source. This can be a source on the internet, server, etc.

[Stream Source Examples](javascript:void(0))

Enter the location of the stream source based on examples provided below.

[Unicast RTP streams](javascript:void(0))

* rtp://:<port number> (port number specified by the stream source)

* Example: rtp://:4848

[SHOUTcast](javascript:void(0))

* http://streams1.kpfa.org:8000/kpfa\_24

[StadiumVision](javascript:void(0))

* udp://224.8.21.1:2000

[SDP](javascript:void(0))

* http/live555://<IP address>/pcm.sdp

[SVSi](javascript:void(0))

* svsi://<stream number>

* Example: svsi://2

[WyreStorm streams](javascript:void(0))

* wyre://<mac\_address\_of\_encoder>

* Example: wyre://xx:xx:xx:xx:xx:xx

* (lower-case letters only; colons required)

[Altona streams](javascript:void(0))

* atlona://<multicast\_address\_from\_encoder>:<port>

#### Buffer

Size of the internal network buffer. Longer buffer times improve network dropout resiliency at the expense of increased delay. You can use this control to adjust audio/video sync in mixed systems.

#### Interface

The network interface used to receive stream. Unicast sources can generally use "Auto" and the system will select an appropriate interface based on the available routing. All interfaces have Multicast reception enabled, so it may be necessary to specify on which interface multicast streams are present.

Interfaces can be LAN A, LAN B, AUX A, AUX B, and can be local or via the internet.

#### Preferred Language

Select the preferred language from the drop-down list. If that language is available in the stream, the Current Language will show the language you selected in the Preferred Language field.

The default selection of "- -stream default- -" means whatever language is available is the one used.

#### Preferred ISO 639 Language Code 1

This parameter is available only on the Control Pins of the component.

Three-character code reflecting the selection made in the Preferred Language field.

#### Current Language 1

Drop-down list of the languages currently available. The default choice is "- - preferred language - -", which means, use what you selected in Preferred Language.

This control lets you choose what you're currently listening to and also reflects what's actually playing. For example, if Preferred Language is set to "- -stream default- -" and Current Language is set to "- -preferred language- -", once the track starts this control will change to reflect the language you're actually listening to. You can then use the control to temporarily switch to another track/language. This control is not "sticky" - if the track changes it reverts back to "- -preferred language- -". Track changes can occur if you change the source control, but can also happen if the remote source changes what is being transmitted.

#### Current ISO 639 Language Code 1

This parameter is available only on the Control Pins of the component.

Three-character code reflecting the selection made in the Current Language field.

1 Dependent on what the stream advertises, and is only applicable (currently) to IPTV MPEG TS streams.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* Gain | -100 to 20 | *n* dB | 0  1 | Input / Output |
| Channel *n* Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Channel *n* Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Channel *n* Peak Input Level | -120 to 43 | -120 dB to 43 dB | 0  1 | Output |
| Current ISO 639 Language | (text) | | | Input / Output |
| Current Language | (text) | | | Input / Output |
| Current Track Name | (text) | | | Output |
| Enable | 0  1 | enabled  disabled | 0  1 | Input / Output |
| Interface | Text Input - valid Interface or "Auto" | | | Input / Output |
| Preferred ISO 639 Language Code | (text) | | | Input / Output |
| Preferred Language | (text) | | | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Initializing (blue) | 0  0.250  0.500  0.750  1.00 | Output |
| Stream Buffer  (seconds) | 0 to 2.0 | 0ms to 2.00sec | 0.00 to 1.00 | Input / Output |
| URL | (text input - valid URL) | | | Input / Output |
