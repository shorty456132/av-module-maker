# NV Series Endpoint as a Decoder

> Source: https://help.qsys.com/Content/Application_Integration/NV_Series_Endpoint_Application/NV_Series_Endpoint_Decoder.htm

# NV Series Endpoint as a Decoder

The NV-32-H and the NV-21-HU Video Endpoints can be configured as Decoders in Q-SYS Software. Decoding is the process of decoding or un-compressing encoded video in real-time. A video decoder converts an encoded video stream to HDMI for display on a screen.

[Configuring NV Series Endpoint as Decoder](javascript:void(0))

1. In Q-SYS Designer Software, you can place your NV Series device into the design like any other Q-SYS Component, located in the Video category under Audio-Video I/O.
   * **v9.8.2 and later**: Add an NV-21-HU to the design.
   * **v8.1 and later**: Add an NV-32-H to the design.

2. Under Properties, configure the parameters as needed. In the examples portrayed in this topic, the only configuration necessary in most cases is selecting Encoder or Decoder.
3. You can set up multiple NV Series Endpoints devices in the design as needed to accommodate additional sources, displays, and locations.

[NV-32-H Peripheral Mode vs Core Mode](javascript:void(0))

The NV-32-H (Core Capable) is shipped with Peripheral Mode active by default. The following sections describe the operation and applications surrounding the use of the product when operated in Peripheral Mode. Refer to [Switching Modes](../../Hardware/Video/NV-32-H_Core_Capable.htm#SwitchingModes) for further applications information about how to configure and utilize the NV-32-H (Core Capable) in Core Mode.

**Note:** Only the NV-32-H (Core Capable) is available for both Peripheral Mode and Core Mode. The NV-21-HU is considered a Peripheral only.

[NV-32-H as a Decoder](javascript:void(0))

As a decoder, the NV-32-H can receive a single 4K60 AV stream from the network and deliver it to HDMI Out 1. The HDMI output will automatically scale to the resolution of the connected display.

When set as a single-output decoder, the NV-32-H can select from AV streams as well as locally connected HDMI sources.

With both outputs HDMI 1 and HDMI 2 enabled, the NV-32-H can select any two content sources from among network AV streams and the local HDMI inputs. It will scale the output content to match the resolution of the displays.

[NV-21-HU as a Decoder](javascript:void(0))

The NV-21-HU as a Decoder can support both HDMI Mode and USB-C Mode.

[HDMI Mode](javascript:void(0))

The HDMI output can show network content, or local content coming from the HDMI input. The USB-C connector bridges the Q-SYS camera and audio feeds and charges the connected device.

[USB-C Mode](javascript:void(0))

The HDMI output can show network content, or local content coming from the HDMI input. The USB-C connector bridges the Q-SYS camera and audio feeds and charges the connected device.
