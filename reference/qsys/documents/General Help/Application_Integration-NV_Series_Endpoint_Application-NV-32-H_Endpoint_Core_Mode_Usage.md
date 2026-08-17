# NV-32-H Core Mode Usage and Applications

> Source: https://help.qsys.com/Content/Application_Integration/NV_Series_Endpoint_Application/NV-32-H_Endpoint_Core_Mode_Usage.htm

# NV-32-H Core Mode Usage and Applications

The NV-32-H (Core Capable) is a multipurpose, software-configurable video endpoint native to the Q-SYS Platform, offering two distinct operating modes to choose between, based on the needs of the application. â**Core Mode**â transforms the device into a fully integrated Q-SYS processor with local HDMI switching capabilities. â**Peripheral Mode**â allows multi-stream video encoding or decoding for network-based HDMI video distribution.

**Note:** The following information is only applicable to the NV-32-H as the NV-21-HU is a peripheral only.

[Switching Modes](javascript:void(0))

The NV-32-H (Core Capable) is configurable in Core Mode or Peripheral Mode. By default, the NV-32-H (Core Capable) ships from the factory in Peripheral Mode. It's easy to switch modes. For more information, visit the NV-32-H [Switching Modes](../../Hardware/Video/NV-32-H_Core_Capable.htm#SwitchingModes) topic.

[Small Meeting Room](javascript:void(0))

[Small Meeting Room Schematic Example](javascript:void(0))

In this example, the following audio and video sources and sinks are available.

#### HDMI Input Sources

* Wired BYOD Screen Share
* Room PC â Display Output 1
* Room PC â Display Output 2

#### HDMI Output Sinks

* Display 1
* Display 2

#### Audio Sources

* Network Microphone (Dante or AES67)
* USB Audio from Room PC (from Far End)

#### Audio Sinks

* Network PoE Loudspeaker (Dante or AES67)
* USB Audio to Room PC (to Far End)

#### Control

* TSC for in room user interface

The following sample design illustrates the necessary Q-SYS Designer schematic elements to implement a possible small meeting room use case.

[Video Routing and Configuration](javascript:void(0))

This design enables the use of the NV-32-H in Core Mode as a 3x2 video switcher. The video output count is enabled in a similar manner as the NV-32-H operated in peripheral mode.

To configure the video input, navigate to the NV-32-H (Core Capable) properties to set the HDMI Output mode to HDMI 1 + HDMI 2. When enabling both outputs, the maximum video resolution for each output will be 1080p60. If 4k60 resolution is desired, only a single HDMI output may be used to achieve this resolution.

[USB AV Routing and configuration](javascript:void(0))

In order to enable USB AV bridging, the Core properties for USB Video Bridge and USB Audio Bridge must also be enabled.

Once a USB video bridge is enabled, any Q-SYS IP camera may be routed directly to the USB Video Bridge.

In addition, once USB audio bridging is enabled, the processed microphone audio can be connected to the USB audio bridge that is interfaced to the Room PC in order to deliver this audio to far end meeting participants for web conferencing applications.

[Network Audio Routing, Audio Processing and Configuration](javascript:void(0))

In this design, we are targeting the use of network audio peripherals. These could be either Dante or AES67 enabled endpoints. Add the respective network audio blocks to the design from the Inventory and the Streaming I/O component list.

Input and output audio processing can be applied by the NV-32-H while operated in Core Mode to simplify the design and limit additional processing hardware that would otherwise be required for the application.

**Note:** The NV-32-H (Core Capable) does not include software Dante and requires the purchase of a license to support this functionality.

[Small Classroom](javascript:void(0))

[Small Classroom Schematic Example](javascript:void(0))

In this example, the following audio and video sources and sinks are available. The application diagram shows a podium and equipment rack. Depending on the distances between the sources and sinks, it may be advisable to locate the NV-32-H (Core Capable) at the podium location. As distances exceed HDMI video extension limits, it is advisable to install CAT-x or fiber video extender solutions.

#### HDMI Input Sources

* Wireless Presentation Device
* Room PC â Single Video Output
* Document Camera

#### HDMI Output Sinks

* Projector
* Monitor (Located on Podium)

#### Audio Sources

* Network Microphone (Dante or AES67)
* USB Audio from Room PC (from Far End)

#### Audio Sinks

* Line Out to QSC SPA series amplifier
* USB Audio to Room PC (to Far End)

#### Control

* TSC for in room user interface
* Occupancy Sensor Logic Input
* Projector Screen Lift Control
* IP Lighting Control

The following sample design illustrates the necessary Q-SYS Designer schematic elements to implement a possible small classroom use case.

[USB AV Routing and configuration](javascript:void(0))

In order to enable USB AV bridging, the Core properties for USB Video Bridge and USB Audio Bridge must also be enabled.

Once a USB video bridge is enabled, any Q-SYS IP camera may be routed directly to the USB Video Bridge. In this application, multiple Q-SYS IP cameras are supported for both audience and presenter camera views which may be switched by the system operator using a customized UCI running on the TSC hardware.

In addition, once USB audio bridging is enabled, the processed microphone audio can be connected to the USB audio bridge that is interfaced to the Room PC in order to deliver this audio to far end meeting participants for web conferencing applications.

Additionally, any USB audio source content from web conferencing applications or presentation media from the Room PC can be used for local playback within the conference room by connecting USB Audio bridge input of the NV-32-H (Core Capable) and routing it to the main mixer comp.

[Network Audio Routing, Audio Processing and Configuration](javascript:void(0))

In this design, we are targeting a mix of both analog and digital audio I/O.

For microphone input, a podium mounted Dante or AES67 enabled microphone as well as a Dante or AES67 wireless microphone receiver can be added by adding a Software Dante RX component from the System I/O inventory.

For local audio reinforcement, the Line Out component of the NV-32-H can be used to route analog audio to an SPA series amplifier connected to the analog output of the NV-32-H.

Input and output audio processing can be applied by the NV-32-H while operated in Core Mode to simplify the design and limit additional processing hardware that would otherwise be required for the application.

**Note:** The NV-32-H (Core Capable) does not include software Dante and requires the purchase of a license to support this functionality.

[Control](javascript:void(0))

In this design, the NV-32-H GPIO inputs can be connected to contact closure output occupancy sensors to facilitate room automation (i.e., wake up projector, raise/lower projector screen and automate room lighting).

Additionally, the GPIO output can be interfaced to a motorized projector screen lift to raise and lower the screen by manual input from the system operator utilizing the TSC with a customized UCI or via room automation based on sensor hardware interfaced to the NV-32-H GPIO inputs.

Customization of the control logic is left to the system designer and could be applied in the Room Automation block shown in the schematic example
