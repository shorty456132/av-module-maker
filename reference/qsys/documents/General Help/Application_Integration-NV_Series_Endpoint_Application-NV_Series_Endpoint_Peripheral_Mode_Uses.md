# NV Series Endpoint Usage and Applications

> Source: https://help.qsys.com/Content/Application_Integration/NV_Series_Endpoint_Application/NV_Series_Endpoint_Peripheral_Mode_Uses.htm

# NV Series Endpoint Usage and Applications

The NV Series Video Endpoints transmit video across the network with no more than two frames of latency end-to-end. This help topic describes operation and usage of the NV Series Video Endpoints in a Q-SYS ecosystem.

Switching among multiple sources on the same Encoder or Decoder, sources on different Encoders, or between encoded sources and locally connected ones are seamless.

[Audio Modes](javascript:void(0))

[HDMI Link](javascript:void(0))

Audio and video stream across the network together from an Encoder to a Decoder. Audio passes along with video on the HDMI output to play through the loudspeakers on the connected display. The audio destination could also be an HDMI-enabled soundbar or AV receiver.

The number of audio channels sent by the source deviceâas defined in its Extended Display Identification Data (EDID)âis set in its property **Audio Channels**.

#### NV-32-H

#### NV-21-HU

#### NV-1-H-WE

As the NV-1-H-WE is only an Encoder, you will have to pair it with another NV Series Decoder. In our case, we're using an NV-32-H.

[Decoder to Core](javascript:void(0))

This mode is used for routing audio from the NV Series to your Q-SYS system. It inherently contains all the logic for audio-follows-video; the audio pins will play content from the active selected video source. This mode makes the most efficient use of networked audio channels while still harnessing the power of the Q-SYS platform for routing, processing and control.

Define the number of audio channels the Decoder can send to the Q-SYS Core under its component properties in Q-SYS Designer Software.

**Note:** The NV-1-H-WE can only be used as an Encoder.

#### NV-32-H

#### NV-21-HU

[Source to Core](javascript:void(0))

This mode takes audio directly from the sources themselves and offers a system designer the greatest flexibility for routing or individual source processing. It uses the most networked audio channels, though.

#### NV-32-H

#### NV-21-HU

#### NV-1-H-WE

[Core to HDMI Display](javascript:void(0))

To combine the convenience of an installed HDMI display with built-in loudspeakers (or some other HDMI audio device, for that matter) with the power and flexibility of the Q-SYS Ecosystem, simply route the audioâand not necessarily just program audioâdirectly to the HDMI output of the NV Series.

To do so, go to the **Audio Source** property of the Generic HDMI Display component and select **Audio Input Pins**. Then you can wire audio from a Decoder or source component or any other Q-SYS audio pins directly to the Generic HDMI Display.

#### NV-32-H

#### NV-21-HU

#### NV-1-H-WE

As the NV-1-H-WE is only an Encoder, another NV Series Decoder must be used. In this example, it's an NV-21-HU.

[Single-Room Operational Modes](javascript:void(0))

[4K60 Mode - Video and Audio](javascript:void(0))

This example portrays a traditional conference / meeting space designed for audio-visual presentation.

#### NV-32-H

#### NV-21-HU

#### NV-1-H-WE

As the NV-1-H-WE is an Encoder only, it will need to be paired with another NV Series Decoder. In this example, it's an NV-21-HU.

At left are devices (laptop computers) plugged into a single NV Series video endpoint configured as an Encoder. At the right are two devices (a media player and a laptop computer) plugged into another NV Series configured as a Decoder and on the same network. The HDMI output of the Decoder connects to a display.

This configuration makes a 5 Ã 1 switching environment within the room: the display can show program content from any of the three laptops, from the media player, or from the desktop computer, depending on the control commands sent to the Encoder and Decoder by the Q-SYS system. Audio will also route from the selected source (i.e., audio-follow-video), and it can be broken out at the Decoder for processing and routing by the Q-SYS Core Processor.

[4K60 Mode - Video and Audio with AV Bridging](javascript:void(0))

This example also portrays a traditional meeting room design, but with a larger number of Q-SYS products and peripherals. This system not only has audio-visual presentation capability, but video / audio conferencing capability as well.

**Note:** The NV-1-H-WE does not support its own USB Soundcard.

#### NV-32-H

#### NV-21-HU

As in the previous example there are devices (laptop computers) plugged into the NV Series Encoder and a media player and desktop computer plugged into the Decoder, which is connected to the HDMI display. The display can show program content from any of the four sources. In addition, an NC Series camera can deliver its video feed via the Q-SYS network to both the Encoder and the Decoder. From the Encoder and Decoder, computers can receive the camera feed through USB connections.

To enable audio and video bridging on the NV Series, go into its device properties in the Q-SYS design.

[4K60 Mode - With Multiple Devices](javascript:void(0))

This next example shows two or more 4K60 displays or other devices in a meeting room.

#### NV-32-H

#### NV-21-HU

This scenario requires multicast. Therefore, you would set the NV Series Encoderâs AV IP Streaming property to either Multicast or Compiler Choice (the default setting).

#### NV-1-H-WE

[Dual Screens with Dynamic Switching](javascript:void(0))

Both Decoders in this scenario can send content up to 4K60 to their respective connected displays, whether it comes from network AV streams or locally connected sources. The Encoder, though, can stream only one source at 4K60; if multiple sources are selected simultaneously on the same Encoder, each source will see it as a Hot Plug Detect (HPD) event and dynamically lower the resolution in its EDID to a maximum of 1080p60.

**Note:** The NV-1-H-WE only supports one HDMI Input.

#### NV-32-H

#### NV-21-HU

To prevent HPD events that change video performance, the Encoder can be configured so that all its sources are limited to 1080p60. This is done through the **Encoder Mode** setting in the Encoder HDMI I/O or AV I/O component.

[Single-Room Multiple Encoders and Single Decoder](javascript:void(0))

Below, a display on a single Decoder can select from several Encoders, each fed from a laptop or other HDMI source offering up to 4K60 AV. Because each Encoder refrains from putting streaming data on the network until the Decoder sends it a request, streaming from source all the way to the display can be a full 4K60 all the time.

This arrangement could be used in such situations as: a large room that uses many HDMI inputs in various locations; a room with a number of HDMI sources at a table; or a room where the HDMI sources are in a rack location away from the Decoder and display.

#### NV-32-H

#### NV-21-HU

Similarly, with the NV-21-HU, a display on a single Decoder can select from several Encoders, even if the Encoder/Decoder are different products.

#### NV-1-H-WE

As the NV-1-H-WE only supports one HDMI Output per Encoder, a display can route through a separate Decoder to the HDMI Display.

[Single-Room 1080p60 Dual Screens](javascript:void(0))

If you opt for a lower video resolution such as 1080p60 or lower, the Q-SYS AV endpoint hardware pieces can handle more simultaneous streams. In this scenario, the NV-21-HU Encoder handles two 1080p60 streams simultaneously. The NV-32-H Decoder can decode two of the sources from the Encoder or display two local sources and send them to two displays. Thus, the system is a 6 Ã 2 matrix.

[Multi-Room Operational Modes](javascript:void(0))

You can easily scale up AV capabilities for a larger system by adding multiple Q-SYS NV Series video endpoints and associating them with the same Q-SYS Core Processor in the same design.

[Overflow Applications](javascript:void(0))

Start with a simple design. Add one or more rooms as needed. This overflow system features 4K60 connectivity.

For example, a facility may have a main meeting area while several other monitors in other rooms or elsewhere in the building can show the same AV feed. The feed must originate from an Encoder. In the Q-SYS design, select Multicast or Compiler Choice as the deviceâs IP Streaming property.

Q-LAN timing protocols will ensure that all the HDMI video outputs are synchronized with each other and all audio paths are synchronized with the video, preventing any lip-sync issues. Below is a representation of the Q-SYS design.

[Facility-Wide Distribution](javascript:void(0))

In this example there are three conference rooms with an equipment closet shared among them. Each room has local presentation capabilities. The rack of gear in the equipment closet can also provide feeds when any of the rooms are not in use.

The equipment rack in the closet has a courtesy monitor so that a technician could verify signals, select appropriate alternate program material, or navigate through guides or menus.

If the Q-SYS Core Processor is licensed to run scripts, the system could be scripted so that if nothing is plugged into a roomâs Encoder, the Decoder would send digital signage, cable TV, or other material to the display instead. It could also be scripted to switch all the Decoders to display a certain source if an emergency arises.
