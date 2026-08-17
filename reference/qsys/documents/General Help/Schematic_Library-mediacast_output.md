# Mediacast Output (NV-32-H)

> Source: https://help.qsys.com/Content/Schematic_Library/mediacast_output.htm

# Mediacast Output (NV-32-H)

The NV-32-H Mediacast Output component converts video from the HDMI 1 output into a Mediacast preview stream that can be displayed within any UCI. UCI Designers can drag the Media Display from the Mediacast Output component directly into their UCIs to create low-latency, 30fps video on their TSC-G3 devices. Since it uses the actual HDMI Output 1 as its source, users can trust it will match the HDMI output. If HDMI Output 1 is disconnected or invalid, the preview stream will be black or show an error screen. The Mediacast Output component is available on NV-32-H Decoders as well as Encoders whose HDMI Output Mode is set to âHDMI 1â.

[AV Connection Requirements](javascript:void(0))

The HDMI 1 output must be connected to an HDMI sink device (like a display) for video to be passed to the Mediacast Output Preview stream. Without this, the video will be black.

**Note:** Each NV Series HDMI output supplies up to 120mA on the +5v signal line.

[Properties](javascript:void(0)) 

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### IP Streams

#### Preview Stream (LED)

The Streaming LED is on when the Mediacast Preview is actively streaming onto the network.

#### Enable

Determines if the multicast IP stream is available for use. When it is not enabled, the RTSP server will deny the media request and Media Display components in UCIs will show the 1fps preview slideshow instead.

#### RTSP URL

When the Preview Stream is enabled, this control displays the URL for the Mediacast RTSP Preview stream.

#### RTP Address

When the Preview Stream is enabled, this control displays the multicast RTP address assigned to the Mediacast Output preview stream. This address comes from Core Managerâs Multicast Address range for Cameras.

#### Stream Mode > fps

When Streaming Mode is set to 'Auto', the frames per second (fps) value is automatically adjusted for the Preview Stream. When a manual resolution is selected, you can choose an fps value from 1 to 30.

#### Max Format

This read-only control shows the maximum video format for the Mediacast stream.

#### Video Format

This read-only control shows the current, actively streaming format of the Mediacast stream.

#### Max Bitrate (Mbps)

The average Mediacast Preview Stream bitrate will not exceed the value specified here, from 0.5 to 2.0 Mbps.

**Note:**  Instantaneous bitrate can exceed this value up to the limitations of the network.

### Preview

The Media Display Preview window can be dragged into a UCI to display the Preview Stream.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| IP Stream | | | | |
| Preview Stream | | | | |
| Enable | 0  1 | no  yes | 0.00  1.00 | Input / Output |
| Max Bitrate | .500 to 3.00 | .500 to 2.00 | 0.000 to 1.00 | Input / Output |
| Max Format | (text) | | | Output |
| RTP Address | (text) | | | Output |
| RTSP URL | (text) | | | Output |
| Streaming | 0  1 | false  true | 0  1 | Output |
| Streaming Mode Format | N/A | Auto  h.264 640x360  h.264 480x270  h.264 320x180 | N/A | Input / Output |
| Streaming Mode Frame Rate | 1 to 30 | 1 to 30 | 0.000 to 1.00 | Input / Output |
| Video Format | (text) | | | Output |
