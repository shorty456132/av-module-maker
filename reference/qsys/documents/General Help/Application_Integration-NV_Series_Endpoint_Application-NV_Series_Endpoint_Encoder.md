# NV Series Endpoint as an Encoder

> Source: https://help.qsys.com/Content/Application_Integration/NV_Series_Endpoint_Application/NV_Series_Endpoint_Encoder.htm

# NV Series Endpoint as an Encoder

The NV-32-H and the NV-21-HU Video Endpoints can be configured as Encoders in Q-SYS Software. Encoders are used to compress and reduce the size of video content so that it can take up less storage space and be easier to transfer from one part of a design to another.

[Configuring NV Series Endpoint as an Encoder](javascript:void(0))

1. In Q-SYS Designer Software, you can place your NV Series device into the design like any other Q-SYS Component, located in the Video category under Audio-Video I/O.
   * **v9.13.0 and later**: Add an NV-1-H-WE to the design.
   * **v9.8.2 and later**: Add an NV-21-HU to the design.
   * **v8.1 and later**: Add an NV-32-H to the design.

2. Under Properties, configure the parameters as needed. In the examples portrayed in this topic, the only configuration necessary in most cases is selecting Encoder or Decoder.

**Note:** The NV-1-H-WE can only be configured as an Encoder.

3. You can set up multiple NV Series Endpoints devices in the design as needed to accommodate additional sources, displays, and locations.

[NV-32-H Peripheral Mode vs Core Mode](javascript:void(0))

The NV-32-H (Core Capable) is shipped with Peripheral Mode active by default. The following sections describe the operation and applications surrounding the use of the product when operated in Peripheral Mode. Refer to [Switching Modes](../../Hardware/Video/NV-32-H_Core_Capable.htm#SwitchingModes) for further applications information about how to configure and utilize the NV-32-H (Core Capable) in Core Mode.

**Note:** Only the NV-32-H (Core Capable) is available for both Peripheral Mode and Core Mode.

[NV-32-H as an Encoder](javascript:void(0))

As an encoder, the NV-32-H can route video from any of three local HDMI sources to anywhere on the local network, at resolutions as high as 4K60 4:4:4. In this setup, HDMI Out 1 feeds a courtesy monitor, and it can scale the video as needed.

The NV-32-H is able to stream all three local HDMI sources simultaneously at a maximum resolution of 1080p60 4:4:4 while providing a single courtesy monitor output as well.

[NV-21-HU as an Encoder](javascript:void(0))

The NV-21-HU as an Encoder can support both HDMI Mode and USB-C Mode.

[HDMI Mode](javascript:void(0))

The HDMI input receives video content up to 4K60 4:4:4. The USB-C connector bridges the Q-SYS camera and audio feeds and charges the connected device. The HDMI output can be connected to a monitor for preview. It will show video from the HDMI input.

[USB-C Mode](javascript:void(0))

The USB-C connector receives alt-mode DisplayPort video (up to 4K60 4:4:4), AND bridges the Q-SYS camera and audio feeds and charges the connected device. The HDMI output can be connected to a monitor for preview. It will show video from the USB-C input.

[NV-1-H-WE as an Encoder](javascript:void(0))

As an Encoder, the NV-1-H-WE is a single-channel HDMI wallplate that receives video content up to 4K60 4:4:4. The device can transmit this video over the network, making it available for other Q-SYS endpoints. Additionally, the HDMI input can be connected to a monitor for preview, displaying the video from the HDMI input.
