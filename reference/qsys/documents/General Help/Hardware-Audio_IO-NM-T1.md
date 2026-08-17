# NM-T1

> Source: https://help.qsys.com/Content/Hardware/Audio_IO/NM-T1.htm

# NM-T1

The Q-SYS NM Series NM-T1 is a tabletop network PoE microphone native to Q-SYS and ideal for the collaboration space. The microphone features advanced beamforming technology that ensures optimal clarity and separation for all surrounding talkers. It also offers onboard call controls, programmable user button and touchless muting capability, which lets users mute or unmute with the wave of a hand. As a native Q-SYS product, the NM-T1 integrates seamlessly into your Q-SYS system without the need for complex programming.

**Note:** This topic provides an overview of the NM-T1. For specifications and installation documentation, see the [NM-T1 product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/nm-t1/) on the Q-SYS website.

[Features](javascript:void(0))

* Native beamforming microphone solution for Q-SYS
* Four software-configurable zones provide up to 360Â° coverage
* Touchless mute via proximity motion sensor
* Programmable RGB light ring for customizable color, pattern, and speed
* Onboard call controls, including a programmable user button customizable in Q-SYS Designer Software
* Power-over-Ethernet enables single cable installation
* Q-SYS Call Sync compatible, letting you sync status across devices without complicated programming
* Simple drag-and-drop integration and comprehensive management via Q-SYS Designer Software and Q-SYS Reflect

[NM-T1 Quantity and AEC Channel Limits](javascript:void(0))

NM Series NM-T1 microphones and third-party microphone AEC processing share similar processing resources. When using both in the same Q-SYS design, the maximum number of NM-T1 and third-party AEC microphone channel / capabilities works on a sliding scale. Limits are based on the Bandwidth property (Wideband or Fullband), as configured in the [Mic In (NM-T1)](../../Schematic_Library/microphone_beamformer_with_aec.htm) component. Refer to the calculator on the [NM-T1 product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/nm-t1/) at qsys.com to assist with NM-T1 capacity planning.

**Note:** These numbers represent guidelines to support collaboration applications and their typical audio processing requirements. In some cases, additional NM-T1 mics and third-party AEC processing may be possible. Refer to the Q-SYS Designer Software compiler results (File > Check Design) for validation of your design.

[Wideband Mode Limits](javascript:void(0))

| Processor | Max NM-T1 Mics | Max Third-Party Mic AEC Channels (200ms) @ Max NM-T1[1](#For) |
| --- | --- | --- |
| NV-32-H (Core Capable) | 3 | 0 |
| Core Nano, Core 8 Flex  + Collaboration Bundle Scaling License[2](#For2) | 3  6 | 0  4 |
| Core 24f | 10 | 8 |
| Core 110f  + active on-board USB Video Bridging[3](#Applicab) | 4  4 | 8  8 |
| Core 510i | 14 | 64 |
| Server Core X10 | 16 | 40 |
| Server Core X20r | 24 | 128 |
| Core 610 | 14 | 64 |
| Core 5200 | 28 | 96 |
| Core 6000 CXR  + Core 6000 CXR Scaling License[2](#For2) | 14  28 | 64  96 |

###### 1. For standard AEC channel maximums per Core at all tail lengths, see the [Acoustic Echo Canceler](../../Schematic_Library/acoustic_echo_canceler_simd.htm) topic.

###### 2. For more information, see the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic.

###### 3. Applicable when using the Core 110f on-board USB Device Port for video bridging.

[Fullband Mode Limits](javascript:void(0))

| Processor | Max NM-T1 Mics | Max Third-Party Mic AEC Channels (200ms) @ Max NM-T1[4](#For3) |
| --- | --- | --- |
| NV-32-H (Core Capable) | 2 | 0 |
| Core Nano, Core 8 Flex  + Collaboration Bundle Scaling License[5](#For4) | 2  3 | 0  8 |
| Core 24f | 6 | 0 |
| Core 110f  + active on-board USB Video Bridging[6](#Applicab2) | 2  2 | 8  8 |
| Core 510i | 14 | 40 |
| Server Core X10 | 16 | 16 |
| Server Core X20r | 24 | 96 |
| Core 610 | 14 | 40 |
| Core 5200 | 28 | 48 |
| Core 6000 CXR  + Core 6000 CXR Scaling License[5](#For4) | 14  28 | 40  48 |

###### 4. For standard AEC channel maximums per Core at all tail lengths, see the [Acoustic Echo Canceler](../../Schematic_Library/acoustic_echo_canceler_simd.htm) topic.

###### 5. For more information, see the [Licensing](../../Core_Manager/Core_Management/Licensing.htm) topic.

###### 6. Applicable when using the Core 110f on-board USB Device Port for video bridging.

[Design Components](javascript:void(0))

These Inventory components are available for the NM-T1:

* [Status (NL Series, NM Series, QIO Series)](../../Schematic_Library/lcqln_status.htm)
* [Mic In (NM-T1)](../../Schematic_Library/microphone_beamformer_with_aec.htm)
* [Control (NL-SB42, NM-T1)](../../Schematic_Library/lcqln_tym_control_panel.htm)

[Connections and Callouts](javascript:void(0))

### Top

1. Mute Buttons: Four touch-sensitive buttons control the mute status for all beams. When a Mute button is pressed, all active mic beams are muted.
2. Call Button: Touch sensitive-call button.
3. User Button: Touch -sensitive programmable user button.
4. LED Light Ring: Indicates mute and call status with programmable color, brightness, and pattern.
5. Proximity Sensor: Allows the user to trigger a Q-SYS Control event by placing a hand 4 to 6 inches above the mic.

### Bottom

1. Q-LAN/PoE Port: For Q-LAN connection. The NM-T1 is a PoE Enabled Device (PoE Type 1 Class 2). Use a suitable PoE network switch or supply connected to this port.
2. ID Button: Press to identify this unit in Q-SYS Designer Software or Q-SYS Configurator.
3. Reset Button: Use the Reset button to restore default network settings and recover factory default settings. Before attempting a reset, refer to the [Device Reset](#Device) section for details.

[Specifications and Dimensions](javascript:void(0))

Product specifications and dimension drawings for the NM-T1 can be found on the [NM-T1 product page](https://www.qsys.com/products-solutions/q-sys/audio-io-peripherals/nm-t1/) on the Q-SYS website.

[Device Reset](javascript:void(0))

You can perform either a short reset or long reset:

* Use a Short Reset to restore connectivity to a device in the event that unintended network settings were specified in Q-SYS Peripheral Manager or the device is otherwise unreachable. A short reset will restore device IP settings back to Auto mode (DHCP) and delete all Static Routes. The configured hostname is retained.
* Use a Long Reset to restore the device to factory condition. This is useful for deeper troubleshooting, or when preparing the device for decommissioning or transfer.

  **CAUTION:** A Long Reset clears all network settings (including hostname), disables 802.1x, deletes user-installed device certificates, deletes all logs, and clears the device password.

### Performing a Short Reset

1. Press and hold the Reset Button until the Status LED (NL, NM Series) or Power LED (QIO Series) begins flashing blue slowly â approximately 10 seconds.
2. Release the button before 20 seconds elapse.
3. The device performs its prescribed Short Reset and reboots.

**Note:** To cancel the Short Reset, release the button before 10 seconds has elapsed.

### Performing a Long Reset

1. Press and hold the Reset Button until the Status LED (NL, NM Series) or Power LED (QIO Series) begins flashing blue rapidly â approximately 20 seconds.
2. Release the button when the LED begins flashing rapidly.
3. Within 30 seconds, press the Reset Button again to confirm the reset.
4. The device performs its prescribed Long Reset and reboots.

**Note:** To cancel the Long Reset, do not press the Reset Button again during the 30 second confirmation period.
