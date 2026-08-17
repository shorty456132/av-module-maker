# Design Properties

> Source: https://help.qsys.com/Content/Schematic_Library/design_properties.htm

# Design Properties

To access Design Properties, select File > Design Properties while in Design Mode.

#### PTPv2 Domain

This is the domain that Q-SYS will use whenever the design requires clock synchronization, such as when routing audio to and from Q-LAN RX and TX components (Core-to-Core streaming), AES67 Receiver and Transmitter components, or Q-SYS peripherals. You can also use this property to enable or disable synchronizing with other PTPv2-aware devices on the network. The value must be identical in each design requiring synchronization between Q-SYS Cores.

* Default (0): This is the default, predefined clock domain number (zero).
* Alt 1 (1), Alt 2 (2), Alt 3 (3): These are the predefined, alternate clock domain numbers.
* User (4 - 127): Select this option to specify your own PTPv2 User Domain, from 4 to 127.

#### PTP Priority 1, 2

In a system featuring multiple Q-SYS Cores or PTPv2-aware devices, these values help determine which device will be the PTPv2 Grandmaster (best master clock). For each priority, select a value from 0 to 255, where 254 is the default for Priority 1 and 100 is the default for Priority 2. Smaller values indicate higher priority.

If multiple designs share the same value for Priority 1, then Priority 2 is used as a backup. If the Priority 2 values are equal, then Q-SYS uses MAC address-based selection as a tiebreaker.

#### PTP Backup Priority 2

Used to provide finer control over whether the Primary or Backup Core will win the PTPv2 Grandmaster election in a Core redundant system, regardless which has the lower MAC address.

When *IsRedundant* Property is enabled for the Core, the PTP Backup Priority 2 property is shown, otherwise, it is hidden.

#### PTP Force On

This property determines whether PTP is enabled for a selected LAN interface (LAN A, LAN B, or Both) when it would not otherwise be required by the design. Some use cases, such as configuring a Loop Player component for GPS External as the time source, require this option to be enabled. By default, this property is Off.

**Tip:** PTP is automatically enabled if your design contains Core-to-Core streams or wired audio peripherals.

#### MTU Value

The maximum transfer unit (MTU) value determines the largest unit of data Q-SYS can transact on the Ethernet network before fragmenting packets. The default is 1500.

**Note:** Only adjust this property if your network is incompatible with the default value of 1500. If you are unsure, consult your network administrator.

#### QoS Preset

Select the DSCP Quality of Service (QoS) markings to apply to various Q-SYS data types. DSCP markings are used by the network switch to prioritize these data types with other data on the network. Switches will need to be configured to take these settings into account. For more information, see [Quality of Service (QoS)](../Networking/QoS.htm).

* Q-LAN: (Default) DSCP preset for Q-LAN traffic optimization. Q-LAN uses DSCP 46 for PTP, 34 for audio, and 26 for video.
* Audinate: DSCP preset for Audinate (Dante) traffic optimization. Dante uses DSCP 56 for PTP, 46 for audio, and 26 for video.
* Manual: Select your own DSCP values. When you choose this preset, you have the ability to customize and optimize traffic according to your specific requirements. This option allows you to manually specify the DSCP values you want to assign to these data types.

#### PTPv2 DSCP Value

In Manual mode, select a PTPv2 DSCP value from 0 to 63. PTPv2 must be the highest priority on your network to ensure that all Q-SYS devices are synchronized correctly. Poor clock sync over the network results in audio and video dropouts.

#### Audio DSCP Value

In Manual mode, select an Audio DSCP value from 0 to 63. Audio streams (both Q-LAN and AES67) must be the second highest priority on your network. Excessive delay of audio packets over the network results in audio dropouts.

#### Video DSCP Value

In Manual mode, select a Video DSCP value from 0 to 63. Video streams must be the third highest priority on your network to avoid video dropouts when using Q‑SYS AV-to-USB Bridging or when streaming between Q-SYS NV-32-H Network Video Endpoints.

### Software Dante

#### Receive Latency

To compensate for network latency variation, set the amount of latency to apply when receiving audio with the Software Dante RX component: 1ms, 2ms (default) or 5ms. Use this value to account for worst-case network transmission so that all devices play out common signals at the same time.

2ms means that no additional latency is applied as long as all other Dante devices are also set to 2ms latency (or less) and the network topology allows it. Note that when the Dante transmitter and receiver have different latency settings, the highest of the two is used.

**Note:** Refer to the [Dante Audio](../Networking/Dante_Audio.htm) topic for Dante network requirements, including clocking requirements for Software Dante.

#### Interface

Select the Q-SYS Core network interface to use to transmit and receive audio to and from the Software Dante RX and TX components: LAN A (default), LAN B, or Both.

**Note:** 'Both' is required for Dante redundant networking, and is the equivalent to Primary (LAN A) and Secondary (LAN B) on other Dante hardware capable of network redundancy.
