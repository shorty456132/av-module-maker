# Software Dante RX

> Source: https://help.qsys.com/Content/Schematic_Library/soft_dante_input.htm

# Software Dante RX

The Software Dante TX and RX components transmit and receive Dante audio streams to and from Dante-enabled devices on the network. The capabilities of software-based Dante are similar to the CDN64 Dante Audio Bridge Card, except that the sample rate is fixed at 48 kHz.

**Note:** See the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic for the details and requirements for Software Dante licensing.

[Requirements](javascript:void(0))

* The Software Dante components are licensed elements that require a Q-SYS Feature License when included in a design deployed to a supported Q-SYS Core processor. See the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic in the Q-SYS Core Manager help.
* Your deployment must meet the network requirements for Dante, including clocking, QoS, and redundancy. See [Other Networked Audio](../Networking/Other_Networked_Audio.htm).
* When using Software Dante, the Q-SYS Core name must be 31 characters or less. This is due to an Audinate limitation that applies to any Dante device hostname.
* Software Dante component names are limited to 28 characters or less. Combined with leading channel number (two digits plus a space), Dante default channel names are therefore limited to 31 characters.

[Channel and Stream Usage](javascript:void(0))

* Each Software Dante TX and RX component consumes Q-SYS Core processor Network Audio Channels and Streams. Use the File > Check Design feature to see how many network channels and streams your design uses.

* Consumption is determined by the Channel Count property and whether one or both LAN interfaces are enabled for use by Software Dante in the [Design Properties](design_properties.htm): LAN A or LAN B = Non-redundant, while Both (LAN A and LAN B) = Redundant.
* Each Software Dante component consumes at least one flow, regardless of the channel count.
* Each Software Dante component appears in Audinate's Dante Controller software as a Channel Group.

### Software Dante Resources: Core Maximums

|  | Maximum Channels | Maximum Flows | Included Channels | Licensable Tiers |
| --- | --- | --- | --- | --- |
| Core 110f | 32x32 | 16x16 | 8x8[1](#8x8) | 8x8[1](#8x8), 16x16, 32x32 |
| Core Nano, Core 8 Flex | 32x32 | 16x16 | 8x8 | 16x16, 32x32 |
| NV-32-H (Core Capable) in Core Mode | 32x32 | 16x16 | N/A | 8x8, 16x16, 32x32 |
| Core 24f | 64x64 | 32x32 | 8x8 | 16x16, 32x32, 64x64 |
| Server Core X10 | 128x128 | 64x64 | 8x8 | 16x16, 32x32, 64x64, 128x128 |
| Server Core X20r | 256x256 | 128x128 | 8x8 | 16x16, 32x32, 64x64, 128x128, 256x256 |
| Core 510i | 128x128 | 64x64 | 8x8[2](#8x82) | 8x8[2](#8x82), 16x16, 32x32, 64x64, 128x128 |
| Core 610 | 256x256 | 128x128 | 8x8 | 16x16, 32x32, 64x64, 128x128, 256x256 |
| Core 5200 | 512x512 | 192x192 | 8x8[2](#8x82) | 8x8[2](#8x82), 16x16, 32x32, 64x64, 128x128, 256x256, 512x512 |
| Core 6000 CXR | 256x256 | 192x192 | 8x8 | 16x16, 32x32, 64x64, 128x128, 256x256 |

###### 1. 8x8 channels are included with the Core 110f after March 30, 2020.

###### 2. 8x8 channels are included with the Core 510i and Core 5200 after January 1, 2021.

### Software Dante Resources: Component Maximums

These tables show the flow consumption, network channel consumption, and network stream consumption â per selected channel count â for each Software Dante component in your design. You can drag in multiple Software Dante components into your design up to the maximum channel count supported by your Core model and licensed tier.

[Core 110f](javascript:void(0))

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 128 | 4 of 64 (Non-redundant)  4 of 64 (Redundant) |
| 16 | 8 | 16 of 128 | 8 of 64 (Non-redundant)  8 of 64 (Redundant) |
| 32 | 16 | 32 of 128 | 16 of 64 (Non-redundant)  16 of 64 (Redundant) |

[Core Nano, Core 8 Flex](javascript:void(0))

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 64 | 4 of 32 (Non-redundant)  4 of 32 (Redundant) |
| 16 | 8 | 16 of 64 | 8 of 32 (Non-redundant)  8 of 32 (Redundant) |
| 32 | 16 | 32 of 64 | 16 of 32 (Non-redundant)  16 of 32 (Redundant) |

[NV-32-H (Core Capable) in Core Mode](javascript:void(0))

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 32 | 4 of 16 (Non-redundant)  4 of 16 (Redundant) |
| 16 | 8 | 16 of 32 | 8 of 16 (Non-redundant)  8 of 16 (Redundant) |
| 32 | 16 | 32 of 32 | 16 of 16 (Non-redundant)  16 of 16 (Redundant) |

[Core 24f](javascript:void(0))

**Note:** Drag in multiple Software Dante TX or RX components in your design to achieve the desired capacity up to the maximum supported by the Core. See [Software Dante Resources: Core Maximums](#Software).

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 160 | 4 of 160 (Non-redundant)  4 of 160 (Redundant) |
| 16 | 8 | 16 of 160 | 8 of 160 (Non-redundant)  8 of 160 (Redundant) |
| 32 | 16 | 32 of 160 | 16 of 160 (Non-redundant)  16 of 160 (Redundant) |
| 64 | 32 | 64 of 160 | 32 of 160 (Non-redundant)  32 of 160 (Redundant) |

[Server Core X10](javascript:void(0))

**Note:** Drag in multiple Software Dante TX or RX components in your design to achieve the desired capacity up to the maximum supported by the Core. See [Software Dante Resources: Core Maximums](#Software).

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 128 | 4 of 128 (Non-redundant)  4 of 128 (Redundant) |
| 16 | 8 | 16 of 128 | 8 of 128 (Non-redundant)  8 of 128 (Redundant) |
| 32 | 16 | 32 of 128 | 16 of 128 (Non-redundant)  16 of 128 (Redundant) |
| 64 | 32 | 64 of 128 | 32 of 128 (Non-redundant)  32 of 128 (Redundant) |

[Server Core X20r](javascript:void(0))

**Note:** Drag in multiple Software Dante TX or RX components in your design to achieve the desired capacity up to the maximum supported by the Core. See [Software Dante Resources: Core Maximums](#Software).

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 256 | 4 of 256 (Non-redundant)  4 of 256 (Redundant) |
| 16 | 8 | 16 of 256 | 8 of 256 (Non-redundant)  8 of 256 (Redundant) |
| 32 | 16 | 32 of 256 | 16 of 256 (Non-redundant)  16 of 256 (Redundant) |
| 64 | 32 | 64 of 256 | 32 of 256 (Non-redundant)  32 of 256 (Redundant) |

[Core 510i](javascript:void(0))

**Note:** Drag in multiple Software Dante TX or RX components in your design to achieve the desired capacity up to the maximum supported by the Core. See [Software Dante Resources: Core Maximums](#Software).

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 256 | 4 of 256 (Non-redundant)  4 of 256 (Redundant) |
| 16 | 8 | 16 of 256 | 8 of 256 (Non-redundant)  8 of 256 (Redundant) |
| 32 | 16 | 32 of 256 | 16 of 256 (Non-redundant)  16 of 256 (Redundant) |
| 64 | 32 | 64 of 256 | 32 of 256 (Non-redundant)  32 of 256 (Redundant) |

[Core 610](javascript:void(0))

**Note:** Drag in multiple Software Dante TX or RX components in your design to achieve the desired capacity up to the maximum supported by the Core. See [Software Dante Resources: Core Maximums](#Software).

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 256 | 4 of 256 (Non-redundant)  4 of 256 (Redundant) |
| 16 | 8 | 16 of 256 | 8 of 256 (Non-redundant)  8 of 256 (Redundant) |
| 32 | 16 | 32 of 256 | 16 of 256 (Non-redundant)  16 of 256 (Redundant) |
| 64 | 32 | 64 of 256 | 32 of 256 (Non-redundant)  32 of 256 (Redundant) |

[Core 5200](javascript:void(0))

**Note:** Drag in multiple Software Dante TX or RX components in your design to achieve the desired capacity up to the maximum supported by the Core. See [Software Dante Resources: Core Maximums](#Software).

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 512 | 4 of 256 (Non-redundant)  4 of 256 (Redundant) |
| 16 | 8 | 16 of 512 | 8 of 256 (Non-redundant)  8 of 256 (Redundant) |
| 32 | 16 | 32 of 512 | 16 of 256 (Non-redundant)  16 of 256 (Redundant) |
| 64 | 32 | 64 of 512 | 32 of 256 (Non-redundant)  32 of 256 (Redundant) |

[Core 6000 CXR](javascript:void(0))

**Note:** Drag in multiple Software Dante TX or RX components in your design to achieve the desired capacity up to the maximum supported by the Core. See [Software Dante Resources: Core Maximums](#Software).

| Channel Count Property | Dante Flows Consumed | Network Channels Consumed | Network Streams Consumed |
| --- | --- | --- | --- |
| 8 | 4 | 8 of 512 | 4 of 256 (Non-redundant)  4 of 256 (Redundant) |
| 16 | 8 | 16 of 512 | 8 of 256 (Non-redundant)  8 of 256 (Redundant) |
| 32 | 16 | 32 of 512 | 16 of 256 (Non-redundant)  16 of 256 (Redundant) |
| 64 | 32 | 64 of 512 | 32 of 256 (Non-redundant)  32 of 256 (Redundant) |

[Configuration Overview](javascript:void(0))

1. Read the Requirements section before proceeding.
2. From the Inventory > Streaming I/O menu, add Software Dante RX to your inventory list.
3. Configure the component [Properties](#Properti).
4. Drag the Status/Control component into your schematic.
5. Connect output audio pins from the Software Dante RX component to one or more audio components in your design.
6. In File > Design Properties, configure the Receive Latency and Interface for Software Dante. See the [Design Properties](design_properties.htm) topic for information.
7. Press F5 to save and run your design to the Core.
8. Double-click the Software Dante RX component to open its control panel.
9. For each output Channel:
   * Select a Device. This is another Dante device on the network that is transmitting audio.
   * Select a Channel on that device. You can select channels by number (and associated name, if available), or select 'All' to populate all output channels with the selected Dante device channels.

   See [Controls](#Controls) for more information.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins.

### Output Pins

#### Channel 1 - n

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Software Dante RX is set to 8 audio output channels. You can choose between 8, 16, or 32.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Channel Count

The number of input channels: 8 (default), 16, or 32. The number of usable channels is determined by the Software Dante feature license â refer to the [Licensing](../Core_Manager/Core_Management/Licensing.htm) topic in the Q-SYS Core Manager help.

#### External Config/Control

Determines whether Dante configuration is allowed by an external program, such as Dante Controller:

* When set to Yes, you configure Dante with an external program. In this mode, some controls within the Software Dante RX component in Q-SYS Designer become read-only.
* When set to No (default), you configure Dante with the Software Dante RX component in Q-SYS Designer. In this mode, any changes you make in an external program are ignored.

**Tip:** You can set this property individually for Software Dante TX and RX.

[Controls](javascript:void(0))

### Dante

#### Peak Input Level (dBFS)

Measures the received audio peak input level, from -120 dB to 0 dB. The measurement is taken directly from the Dante input signal before the Digital controls.

### Digital

#### Invert

Inverts the polarity of the audio signal.

#### Mute

Mutes the digital audio signal.

#### Gain

Controls the gain of the digital audio signal, from -100 dB to 20.0 dB (default is 0).

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

### Subscriptions

A Q-SYS input channel can subscribe to a specific channel on a specific Dante device. The transmitting device is given a name and each channel on that device can have a name. Each channel has the following controls.

#### Device

Select a Device for a Q-SYS input channel from a list of Dante output devices advertising on the network. The Device name is a unique name on the Dante network.

The Device drop-down menu can display:

* Device Name only â The Channel control then displays all the channels available on the device. For Q-SYS Core processor devices, this includes channels from all Software Dante components, which are interpreted as Channel Groups in Dante Controller.
* Device Name : Channel Group â The Channel control then displays only the channels from the selected Channel Group. For Q-SYS Core processor devices, this would be the channels only from the selected Software Dante component name.

**Note:** To learn about Audinate's support of Channel Groups, see the [Dante Controller User Guide](https://dev.audinate.com/GA/dante-controller/userguide/webhelp/content/channel_groups.htm) on the Audinate website.

#### Channel

Select a Channel from a list of channel names on the selected Device or Device : Channel Group. Each channel has a unique name on the device.

Each Dante Channel has a name that is set by the transmitting device that cannot be changed by the Receiver. The Q-SYS Software Dante TX component, for example, by default uses channel names "01", "02", etc. followed by the Software Dante TX component name. Refer to the [Software Dante TX](soft_dante_output.htm) component topic for more information about channel naming.

#### Subscription Status

The LED and status bar indicate the current status of the channel subscription. Normally, this should indicate 'OK'. A 'Fault' status indicates a problem with the channel subscription. If the message following the 'Fault' status is in all caps, it is a message returned directly from the Dante code.

These are some common Dante subscription status messages:

* Initializing - UNRESOLVED: Dante is looking for the device to whose channel it is subscribed.
* Compromised - Unresolved: Timed out looking for the device.
* Fault - NO\_TX: The Dante transmitting device to which Q-SYS is trying to subscribe has run out of Transmit Flows.
* Fault - NO\_RX: This Dante receiver has run out of available Receive Flows.

### Config

#### Device Name

This is a read-only value, set to the name of the Q-SYS Core processor.

#### Interface

Indicates what network interface on the Q-SYS Core is being used to receive Dante audio. Configure the interface in File > [Design Properties](design_properties.htm).

#### Rx Flows

Displays the number of flows currently used out of the maximum. The maximum number of flows is determined by the Channel Count property. Refer to the 'Channel and Stream Usage' section.

#### Subscriptions > Clear All

Click to clear all Devices and Channels for all output channels.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel *n* | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  inverted | 0  1 | Input / Output |
| Level | -120 to 0 | -120dB to 0dB | - | Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
| Subscription Channel | (text) | | | Input / Output |
| Subscription Device | (text) | | | Input / Output |
| Subscription Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Clear All | (trigger) | | | Input / Output |
| Dante Interface | - | LAN A  LAN B  Both | - | Output |
| Dante Name | (text) | | | Output |
| Input Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Rx Flows | - | *nn*/*nn* | - | Output |
