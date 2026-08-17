# Devices

> Source: https://help.qsys.com/Content/RoomSuite/Devices.htm

# Devices

The Devices page shows you everything that is physically connected to your RoomSuite Modular System and how each device is being used in the room. Think of it as the âfront panelâ of your system. You can see your processor, expander, cameras, mics, speakers, HDMI and USB paths, and quickly confirm that everything is online and configured for your meeting workflow.

Use this page whenever you:

* Set up a new room and want to confirm device pairing.

* Add or move peripherals (cameras, mics, speakers, displays, touch panels).

* Need to quickly understand âwhatâs connected whereâ before troubleshooting.

## Getting Started on the Devices Page

### Before You Begin

When starting up for the first time, the Devices menu will display a âGet Startedâ indicator. Select this to begin the initial setup process. The discovery and pairing process is the first major step in setting up a RoomSuite Modular System. During this phase, the system identifies all connected peripherals, assigns them to the room, and prepares them for use. You will be asked to confirm the device list, update device names if needed, and complete pairing.

The discovery and pairing process is the first major step in setting up a RoomSuite Modular System. During this phase, the system identifies all connected peripherals, assigns them to the room, and prepares them for use. You will be asked to confirm the device list, update device names if needed, and complete pairing.

**Note:** As part of this process, peripherals automatically update their firmware to ensure they are running a supported version compatible with the RMP-100. Devices that complete pairing will no longer show a *Not Paired* state.

#### About Non-Pairable Devices

Non pairable devices are network endpoints that the RoomSuite Modular System can detect on the A/V LAN, but are not treated as RoomSuite peripherals and are not paired to the room. Examples include, Dante ceiling array microphones or installer laptops connected to RMP 100 ports 2â8 or QIO VEN4 ports 1â4. These devices do not count against supported peripheral limits and do not require pairing, but they may still be used for audio routing, control, or configuration via RoomSuite Modular System or third party tools (such as Dante Controller, Sennheiser Control Cockpit, or Shure Designer).

### What Happens During Pairing

Before device discovery starts, be aware that:

* Newly connected peripherals will initially appear as Not Paired.
* You may rename devices before completing pairing.
* Peripherals may automatically update their firmware during pairing.
* Devices switch from Not Paired to Paired once the process finishes.

#### You Decide When You Will Run Room System Optimization (RSO)

* RSO is not automatic. Go to Audio > Optimization.
* You can complete pairing first, then initiate RSO when you are ready.
* RSO will analyze room size and acoustics and allow you to override recommended values

### Let's Begin

1. **Connect the Configuration Computer to RMP-100**.

   * Connect a configuration computer to the AUX A port on the RMP-100.
2. **Connect All Required Minimum Hardware**.

   * 1 x RMP-100
   * 1 x QIO-VEN4
   * 1 x NL Loudspeaker

   **RMP-100 Connection**

   Use the included RMP-100 power supply to connect one end to the RMP-100 Power In connector and the other end of the power supply to an AC power outlet.

   **QIO-VEN4 Connection**

   Connect **QIO-VEN4 PoE In** to **RMP-100 Port 1**.
3. **Connect Your Peripherals**.

   Physically connect peripherals to either the RMP-100 or the QIO-VEN4.

   * Loudspeakers, Microphones, (Q SYS NM-T1 microphone or Dante ceiling array microphone.), Cameras, Touch panels, Displays (HDMI), Optional devices such as occupancy sensors or RS 232 controlled displays.
   * Connect Q-SYS peripherals to **RMP-100 Ports 2â8** or **QIO VEN4 Ports 1â4**.
4. **Power On the System**.

   During initial boot, the displays connected to RMP-100 HDMI Out 1/2 show AUX A and AUX B network settings.

   * AUX A is enabled by default.
   * AUX B is disabled by default and can be enabled later.

   **Note:** The network settings are only displayed on screen for about 60 seconds during the boot-up process. After that, once the system loads for the first time, the only way to see that screen again is to power cycle the RMP-100. This is the only way to get the IP Address to access the web interface for the first time.

   * Enter the **AUX A IP address** in a web browser to open RoomSuite Modular System.
   * Navigate to Get Started on the Devices menu to begin basic configuration.
5. **Discovery and Automatic Pairing**.

   Once required wired connections are complete and power is on, from the Devices page, RMP-100 automatically begins Discovering Devices on its A / V LAN. A list of all detected peripherals is displayed. After devices are discovered, they appear visually in the interface, mapped to the specific ports where they are physically connected.

   **Note:** **Naming Devices During Discovery**. Before confirming the detected device list, you may rename peripherals to make them easier to identify in the RoomSuite Modular System. Naming devices at this stage improves clarity during setup, optimization, and ongoing management. The names you assign will appear throughout the interface, including on the Devices page, in Room System Optimization (RSO), and in presets. Once names are set, continue with pairing.
6. **Confirm whether the list is complete**.

   * Confirm: The system pairs all devices and proceeds.
   * Rescan: The system returns to the welcome screen and re-attempts discovery.

   At this point, your collaboration space will be online and ready for basic use with the RoomSuite Modular System.

## Optional Connections

#### MTR / Zoom Room Integration

* Connect RMP-100 USB C to the MTR/ZR compute device.
* Connect RMP-100 HDMI Out 1 to the computeâs HDMI input.
* Additional HDMI sources can be connected to RMP-100 HDMI 2

**Note:** Audio is not supported on HDMI Input 2.

* Connect HDMI outputs from MTR/ZR to your room displays.

#### BYOD Integration

* For laptops with Thunderbolt / DisplayPort Alt Mode:

Connect laptop â QIO-VEN4 USB-C

* For laptops without Alt Mode:

Connect USB â QIO-VEN4 USB-C

Connect HDMI â QIO-VEN4 HDMI In

* Connect RMP-100 HDMI Out 1 to your display.
* For dual displays, connect HDMI Out 2 (mirrors Output 1).

**Note:** If using MTR or Zoom Room, ensure the Conferencing Compatibility Mode found on the upper right-side of the Devices page matches your environment (default is BYOD).

#### Additional Optional HardwareConnections

* Occupancy sensor â RMP-100 GPIO
* RS-232 compatible display â RMP-100 RS-232-port

## Unsupported Connections

These connections are present on the hardware, but not supported.

* RMP-100: USB-A, Antenna
* QIO- VEN4: USB-A, 3.5 mm headset

## Room Devices Summary Banner

The top of the Devices page shows a summary banner that describes the overall device state for the current room system.

#### Paired Status

#### Paired

Displays a green indicator when all required RoomSuite Modular System-compatible peripherals for the room are discovered and paired.

#### Last Paired

Shows the date and time of the last successful pairing operation. Helpful when confirming new hardware changes have been recognized by the system.

#### Optimization Status

Indicates whether the system has been through Room System Optimization (RSO) for this device set. Use this in combination with the Optimization page (Room Setup > Audio > Optimization) to know if you still need to run optimization after updating devices.

#### Conferencing Compatibility Mode

Defines the type of conferencing experience the room is designed for and is selected during initial setup, but can also be adjusted later if the roomâs intended use changes. Modes include:

**BYOD (Bring Your Own Device)** â The room is optimized for users who bring their own laptops.

* Users connect their laptop to the QIO-VEN4 USB-C port, or to USB-C + HDMI if the laptop does not support DisplayPort Alt Mode.

* The RMP-100 HDMI output connects directly to the room display.
* RoomSuite Modular System provides in room AV controls and manages the connected peripherals automatically.

**Microsoft Teams Rooms / Zoom Rooms** â The room uses a dedicated conferencing appliance running Microsoft Teams Rooms or Zoom Rooms software.

* The RMP-100 HDMI output connects to the MTR / ZR compute HDMI input.
* The MTR / ZR compute HDMI output then connects to the room display.
* The native Teams or Zoom interface functions as the primary user interface.
* RoomSuite Modular System provides a coordinated "second page" experience for additional AV controls, such as camera selection, audio adjustments and display management.
* These rooms can still support BYOM (Bring Your Own Meeting) scenarios when configuredâallowing users to connect a laptop and use the RoomSuite Modular System even in an MTR / ZR deployment.

**Note:** Since Conferencing Compatibility Mode influences both the underlying design and the roomâs touch interface, it is one of the first items to confirm on the Devices page when you bring a new room online or repurpose an existing space.

#### Edit Button

Enables full modification of the Device page. When edits are complete, click Save.

## Device Groups

Below the Room Devices summary banner, the page is divided into device groups. Each group corresponds to a physical component of the RoomSuite Modular System. This grouping makes it easier to see what is connected and how each part is functioning.

### RMP-100 Processor

The RMP-100 is the main processing component of the system. It powers the setup, manages audio and video routing, and connects to the conferencing Host PC running Microsoft Teams Rooms or Zoom Rooms. Its built-in PoE+ switch can power a variety of Q-SYS components, including NL, NC, and NM endpoints, as well as third-party microphones. It also provides HDMI outputs, USB-C, and integration points for sensors and RS-232-capable displays.

#### Summary Banner for the RMP-100 Processor

#### Device Name

The user assigned or factory assigned name of the RMP-100. This identifies the processor currently being managed.

#### Device Model

Indicates the hardware type detected.

#### Peripheral Count

Shows how many peripherals are currently associated with this processor.

#### Non-Pairable Devices Button

A button that opens a list of devices detected on the room network that cannot be paired or managed through RoomSuite Modular System. These are typically unsupported devices, network endpoints, or devices outside the RoomSuite ecosystem.

#### Power Indicator

A live power-usage readout showing the current power draw over the maximum available power budget.

#### Expand / Collapse Arrow

Arrow allows you to expand or collapse the device's full detail view.

#### RMP-100 Processor Grid

The grid displays all available A / V LAN ports on the RMP-100 processor and shows the connection status of each port. Each tile represents a physical Ethernet port, labeled numerically to match the port numbering on the hardware chassis.

**Note:** Network-connected, non-PoE, non-pairable devices, such as laptops, will not appear in the grid.

When a supported device is connected to a port, the tile shows:

* The device icon
* The device type.
* The model name.
* Status indicators (e.g., OK or Offline).
* Optional ID toggle control for locating a device.

Empty tiles are labeled as such, indicating unused ports and thus, available capacity for additional peripherals.

#### RMP-100 Video IN

The Video IN section for the RMP-100 is the control center for managing HDMI inputs on the processor. It doesnât just list ports, it tells you how each input is being used and whether itâs ready for your conference workflow.

This area is where you validate that HDMI ports are correctly enabled and named, ensuring clarity when matching physical connections to the system design. It also gives you control over which inputs are permitted for content sharing, aligning the hardware configuration with your chosen conferencing compatibility mode, whether BYOD, Microsoft Teams Rooms, or Zoom Rooms. When combined with the Room Devices Summary Banner, the Video IN table provides a complete picture of your video sources, confirming not only that they are physically connected, but they are also properly configured for the intended meeting experience.

**Tip:** After enabling / disabling HDMI sources, check this table before starting optimization or troubleshooting. It ensures your inputs are live, properly named, and aligned with your conferencing workflow.

#### Type

Identifies the physical video input type, with icon and label, so you know which port you are working with, HDMI-IN 1 or HDMI-IN 2.

#### Status

Indicates if a video source is currently detected. For example, Not Present means that nothing is plugged-in or no active source is detected at that input.

#### Capability

Lists the maximum resolution and audio capability for that input. For example, 1080p60 / Audio.

#### Name

Friendly name for the input, like HDMI In (1) or HDMI In (2) makes it easier to match what you see on the page with the actual hardware.

#### Meeting Source

Determines which input is available as the content source when a user selects Meet on the roomâs touch controller. This setting is only used when the system is operating in BYOD mode.

* Each input row includes a checkbox that designates that input as the meeting source.

* Only one input can be selected at a time. Selecting a different input automatically clears the previous selection.
* You may also leave both inputs unselected if you do not want any meeting source available in BYOD mode.

When an input is selected as the Meeting Source, it becomes the content source option presented to the user on the controller during a meeting.

#### Enable

A per-input on / off toggle that controls whether the input is active in the RoomSuite Modular System design, even if it is physically connected.

* ON - The input is active and available to the RoomSuite Modular System.
* OFF - The input is disabled in the RoomSuite Modular System design, even if physically connected.

#### Link

The Link toggle on the RMP-100 Video In section controls whether the two HDMI inputs are treated as one combined video source or as two separate video sources in RoomSuite Modular System.

When Link is ON:

* The two HDMI inputs on the RMP-100 are used together as a single source.
* You assign one friendly name for the combined input.
* On the Touch Panel UCI, this appears as one video source tile.

This mode is intended for setups where one device uses both HDMI inputs, such as:

* Room PC - HDMI Output 1 -> RMP-100 HDMI Input 1
* Room PC - HDMI Output 2 -> RMO-100 HDMI Input 2

When Link is OFF:

* Each HDMI input on the RMP-100 is treated as its own video source.
* You assign separate friendly names for each input.
* On the Touch Panel UCI, the inputs appear as two distinct video source files.

This mode is intended for setups where two different devices are connected, such as:

* Blu-ray Player - HDMI Output -> RMP-100 HDMI Input 1
* Document Camera - HDMI Output -> RMP-100 HDMI Input 2

#### RMP-100 Video Out

The Video OUT section summarizes how the RMP-100 feeds video in the room and ensures it is properly configured.

#### Type

Shows the output connector type and label, such as HDMI OUT 1 or HDMI OUT 2. This helps you identify which physical port corresponds to each display, making it easier to match the system view with the actual hardware.

#### Status

Indicates if a display is detected by checking Extended Display Identification Data (EDID) presence. For example, Not Present means no active display or EDID signal is detected. This is critical for troubleshooting because if the system doesnât see the display, content wonât appear even if the cable is connected.

#### Capability

Lists the maximum format the output supports (e.g., 1080p60). Knowing this ensures your display can handle the resolution and refresh rate for high-quality video in your conferencing workflow.

#### Resolution

Shows the resolution and frame rate currently configured or detected, such as 1920x1080p60 (actual resolution depends on your display and configuration). This helps confirm that the display is operating at the expected quality level and matches your room design.

#### Name

Friendly name for the destination, like Left Display or Right Display. Clear naming reduces confusion when managing multiple outputs and ensures consistency across the system design and physical setup.

#### Enable

A per-input on / off toggle that controls whether the input is active in the RoomSuite Modular System design, even if it is physically connected.

* ON - The input is active and available to the RoomSuite Modular System.
* OFF - The input is disabled in the RoomSuite Modular System design, even if physically connected.

#### RMP-100 USB

The USB section for the RMP 100 shows how USB audio endpoints are presented to the host PC. This is useful because the USB configuration determines how audio flows between the room system and the conferencing platform, ensuring the correct devices are active for your conferencing compatibility mode.

#### Type

USB functional role:

â¢ USB-Speakerphone â A composite USB audio device designed for conferencing. This role combines microphone and speaker functions so the host PC sees the room system as a single, integrated audio endpoint.

â¢ USB-Sound Card â A simple audio I/O device for recording and playback.

#### Connected

Indicates whether a USB host is currently connected to that function, Yes / No. If Yes, this confirms that the physical USB link between the RMP-100 and the Host PC is active. If No, the system cannot pass audio to the conferencing platform, even if everything else is configured correctly.

#### Active

Whether the room system is actively using this USB function, Yes/No. If Yes, The USB role (e.g., USB Speakerphone or USB Sound Card) is actively engaged and passing audio to or from the host PC. This means the room system is using that function for the meeting. If No, the USB role is not in use, even if the host PC is physically connected. This could happen if the conferencing compatibility mode doesnât require that role or if the input is disabled in the configuration.

### QIO-VEN4 Expander

The QIO-VEN4 is the A / V and connectivity expander component. This device extends connectivity to user touchpoints, such as at the conference table. It supports Bring Your Own Device (BYOD) connections via USB-C and HDMI, and adds extra ports for Q-SYS peripherals. The QIO-VEN4 acts as the expansion unit for user interaction and additional A / V devices. Additionally, up to three QIO-VEN4 expanders can be used.

#### Summary Banner for the QIO-VEN4 Expander

#### Device Type

Displays the functional category of the device.

#### Model

Displays the specific detected hardware model.

#### Peripheral Count

Indicates how many peripherals are currently connected through this device.

#### Power Indicator

A live power-usage readout showing the current power draw over the maximum available power budget.

#### Expand / Collapse Arrow

Arrow allows you to expand or collapse the device's full detail view.

#### QIO-VEN4 Expander Grid

The QIO‑VEN4 Expander Grid displays the status of all available device ports on the QIO‑VEN4 expander and shows which peripherals are connected to each port. This grid provides a visual representation of the expanderâs four network ports. For larger rooms, you can have a maximum of 3 expanders per room.

**Note:** Network-connected, non-PoE, non-pairable devices, such as laptops, will not appear in the grid.

When a supported device is connected to a port, the tile shows:

* The device icon.
* The device type.
* The model name.
* Status indicators (e.g., OK or Offline).
* Optional ID toggle control for locating a device.

Empty tiles are labeled as such, indicating unused ports and thus, available capacity for additional peripherals.

#### QIO-VEN4 Video IN

The Video IN section for the QIO-VEN4 group focuses on BYOD connectivity (USB-C and HDMI), where users typically plug their devices to connect directly at the table without depending entirely on the RMP-100 processor for video. These inputs provide convenience for users and enable flexible meeting workflows.

Use this area to confirm that the QIO‑VEN4 inputs are ready for BYOD devices, and that the combined USB‑C/HDMI‑In input toggle is enabled. Since both connectors share a single enable / disable control, ensure the input is turned on and labeled clearly for end users.

**Note:** If a laptop will be used for meetings and content sharing and does not support DisplayPort Alt Mode, the user must connect both the USB‑C cable and the HDMI cable to achieve full audio / video functionality and device control.

#### Type

Identifies the physical video input type, with icon and label, so you know which port you are working with, USB-C - IN or HDMI-IN.

#### Status

Indicates if a video source is currently detected. For example, Not Present means that nothing is plugged-in or no active source is detected at that input.

#### Capability

Indicates the maximum supported resolution and audio. For example, 1080p60 / Audio. This confirms the input meets quality requirements for video and audio, ensuring smooth BYOD experience.

#### Resolution

Shows the resolution and frame rate currently configured or detected. Displays N/A when no source is present; shows active resolution when connected.

#### Name

Friendly label, such as Laptop to reduce confusion for end users and technicians making it easy to identify which input is which during setup or troubleshooting.

#### Enable

A per-input on / off toggle that controls whether the input is active in the RoomSuite Modular System design, even if it is physically connected.

* ON - The input is active and available to the RoomSuite Modular System.
* OFF - The input is disabled in the RoomSuite Modular System design, even if physically connected.

#### QIO-VEN4 USB

#### Type

USB functional role:

â¢ USB-Speakerphone â A composite USB audio device designed for conferencing. This role combines microphone and speaker functions so the host PC sees the room system as a single, integrated audio endpoint.

â¢ USB-Sound Card â A simple audio I/O device for recording and playback.

#### Connected

Indicates whether a USB host is currently connected to that function, Yes / No. If Yes, this confirms that the physical USB link between the RMP-100 and the Host PC is active. If No, the system cannot pass audio to the conferencing platform, even if everything else is configured correctly.

#### Active

Whether the room system is actively using this USB function, Yes / No. If Yes, The USB role (e.g., USB Speakerphone or USB Sound Card) is actively engaged and passing audio to or from the host PC. This means the room system is using that function for the meeting. If No, the USB role is not in use, even if the host PC is physically connected. This could happen if the conferencing compatibility mode doesnât require that role or if the input is disabled in the configuration.
