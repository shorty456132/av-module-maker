# Amplifier Redundancy

> Source: https://help.qsys.com/Content/Redundancy/Redundancy_Amplifier.htm

# Amplifier Redundancy

The DataPort Amplifier Backup Panel (DAB-801) provides N+1 redundancy for the DataPort amplifiers and can be used in Life-Safety applications. The DAB-801 can support redundant network and I/O Frames, and four 2-channel or two 4-channel amplifiers per panel. Two panels can be stacked, doubling the amplifier count.

**Note:** Within broad limits, Q-SYS can detect signal failure due to wiring faults; however, if a loudspeaker or its wiring is bad, there is no benefit to switching to a backup amplifier. Q-SYS flags such faults for service, and methods such as "interleaving" two zones within a given space can ensure that complete failure of sound is unlikely.

[DataPort Amplifier Backup Panel (DAB-801)](javascript:void(0))

**Note:** The DAB-801 is designed to work with up to four 2-channel amplifiers or two 4-channel amplifiers. The DAB-801 does not support 8-channel amplifiers.

The purpose of the DataPort Amplifier Backup Panel is to provide the redundancy and other functionality required by most Life-Safety/Evacuation systems. In order to meet those requirements, the DAB-801, when used in a Q-SYS system, must be used with QSC DataPort amplifiers and Q-SYS I/O Frames with DataPort cards installed. All of the amplifiers connected to a DAB-801, or a set of stacked DAB-801s, must be the same model/channel count.

The DAB-801 is intended to mount on rear rack rails, or behind an amplifier rack.

For information regarding installation of the DAB-801, refer to the [DataPort Amplifier Backup Panel](../Hardware/Accessories/017_DataPort_Amplifier_Backup_Panel.htm) topic, and to the user guide supplied with the hardware.

### Description

#### DataPorts

DataPorts are used to pass audio, and other information between the DataPort amplifiers and the Q-SYS system.

Each DAB-801 has four DataPort connectors giving a total of 8 audio channels for the primary amplifiers. Two DAB-801s can be stacked together giving eight DataPorts, or 16 channels. A Q-SYS I/O Frame has the capability of housing four DataPort cards giving a total of 8 DataPort connectors or 16 audio channels, which connect to two stacked DAB-801s.

#### Loudspeakers

The loudspeakers are connected directly to the DAB-801. A single DAB-801 has up to 8 channels of audio, so it supports 8 loudspeaker connections. In a stacked configuration, there are 16 loudspeaker connections available.

#### DataPort Amplifiers

All primary and backup amplifiers must be the same model and channel count.

The primary amplifier(s) and backup amplifier connect directly to the DAB-801. When an amplifier failure occurs, DataPort and loudspeakers are switched from the failed primary amplifier to the backup amplifier. You can connect 4 primary and one backup two-channel amplifiers, or 2 primary and 1 backup four-channel amplifiers to a single DAB-801. The count is doubled for the primary amplifiers only on dual DAB-801s.

#### GPIO (General Purpose Input Output)

The GPIO connection between the I/O Frame(s) and the DAB-801 provides control for the DAB-801 relays. Typically, when GPIO is used in a Q-SYS design, you must configure the GPIO for its intended use. With the DAB-801, the GPIO component on the I/O Frame to which it is connected, is automatically configured. If you attempt to configure the GPIO component for a DAB-801, the design will not compile.

#### Dual-Priority Inputs with Relay Override

Each DAB-801 has two analog audio inputs, Alarm, and Page. The Alarm input overrides all other signals, and is used for major emergencies. The Page input overrides all signals except the Alarm input, and can be used for other announcements. These inputs can be assigned to any combination of amplifier channels.

**Note:** If you have stacked DAB-801's you can use only the Alarm and Page inputs on the first DAB-801.

#### DAB-801 Power Supply

The DAB-801 uses an always-on power supply to operate the relays. It is very lightly loaded in normal use, but if this should fail, all relays relax to the "normal" mode, which passes signals from the Primary I/O Frame to the Primary amplifiers. There is no active audio circuitry in the DAB-801 that might fail; relays are used to re-route input and speaker signals.

The Alarm and Page inputs receive additional backup power from the amplifier DataPorts, so these "last chance" functions are still usable as long as at least one active amplifier is on line.

[N+1 Amplifier Redundancy](javascript:void(0))

The DAB-801 provides N+1 amplifier redundancy for QSC 2 and 4-channel DataPort amplifiers, and supports I/O Frame redundancy. Two DAB-801s can be stacked to provide double the primary amplifier redundancy.

* A single DAB-801 supports four 2-channel primary amplifiers with one 2-channel backup amplifier, or two 4-channel primary amplifiers with one 4-channel backup amplifier.
* A pair of DAB-801s support eight 2-channel primary amplifiers with one 2-channel backup amplifier, or four 4-channel primary amplifiers with one 4-channel backup amplifier.

**Note:** The DAB-801 does not support 8-channel amplifiers.

**Note:** Amplifier models/channel count cannot be mixed on a DAB-801, or two stacked DAB-801s.

**Note:** In the example above, the single-line connections from the I/O Frames to the DAB-801s represent two DataPort cards with two connectors each. One DataPort connector supports two channels. The GPIO connections are not shown in this example.

When an amplifier fails, Q-SYS detects the failure and sends a signal to the I/O Frame which directs the DAB-801 to switch from the failed amplifier to the backup amplifier, switching DataPort communicatioN / Audio, GPIO, and loudspeaker connections. The detected failure can be the whole amplifier, or a single channel in the amplifier. After the backup amplifier is substituted, no further action can occur until the failed primary amplifier has been replaced.

Typically, a single backup amplifier is used with two stacked DAB-801s, however, you can have one backup amplifier per DAB-801.

All primary amplifiers are continuously monitored by Q-SYS along with the power-on status of the backup amplifier. Periodic full tests of the backup system can be programmed to ensure signal integrity and meet regulatory requirements.

[I/O Frame Redundancy](javascript:void(0))

The Q-SYS Core, I/O Frame, and network can be redundant. The DAB-801 has the capability of connecting two I/O Frames to support these redundancies. The Q-SYS Core is responsible for monitoring the health of these components, and failing-over to a backup when necessary. Refer to the [Q-SYS Redundancy](Redundancy.htm) topic for more information.

The Primary and Backup I/O Frames are identified in Q-SYS Designer as to which is primary, and which is the backup. Both I/O Frames are connected to the DAB-801 with DataPort and GPIO (control) cables. A "heartbeat" signal that depends on orderly processing must be received by the Q-SYS Core for an I/O Frame to remain in control of the DAB-801. When the heartbeat from the primary I/O Frame stops, all input DataPort and GPIO cables are switched simultaneously to the backup I/O Frame.

[Complete Q-SYS Failure or "Last-Chance" Paging Inputs](javascript:void(0))

The DAB-801 provides a low-tech means of making emergency announcements; the Alarm and Page inputs.

#### Alarm (Top Priority)

When Q-SYS detects an input on this circuit, all other inputs are disconnected. This is typically for fire marshal use. The input is Line Level.

#### Page (Second Priority)

When Q-SYS detects an input on this circuit, all other inputs are disconnected by the DAB-801 relays except the Alarm input which overrides the Page Input. The input is Line Level.

#### General

The facility design must incorporate appropriate paging stations and routing switches that access the appropriate amplifier racks. Within a rack, the DAB-801 determines which amplifiers receive the paging signals.

The Alarm and Page use the primary amplifier, or the backup amplifier if it is switched in. When an Alarm or Page is initiated, all Q-SYS audio inputs are disconnected. Q-SYS detects the page, and takes no action to correct the disconnected input situation. Since only the Q-SYS audio inputs are disconnected the various telemetry functions such as output voltage, temperature, clipping and so on, are still active during Alarm/Page mode. The telemetry information can be of value during system commissioning and drills.

Q-SYS gives you the option to mute the audio outputs of the DataPort cards, in addition to the relay disconnection in the DAB-801, when an Alarm or Page is detected. Refer to the [DAB-801 DataPort Amplifier Backup](../Schematic_Library/amplifier_redundancy_panel.htm) topic for more information.

#### Alarm/Page Input Setup Requirements

* Audio Input - 3 V peak analog balanced signal (Line Level)
* Switching - use either a 300 ma contact closure or +12 V, 5 ma trigger signal
* Alarm and Page inputs are routed to any combination of amplifiers using a multi-pole DIP switch on the DAB-801. In some cases such as subwoofer or tweeter channels, certain amplifiers may not be needed for paging and therefore need not be selected.
