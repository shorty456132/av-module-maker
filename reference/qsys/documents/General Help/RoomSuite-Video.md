# Video

> Source: https://help.qsys.com/Content/RoomSuite/Video.htm

# Video

The Video section in RoomSuite Modular System lets you configure how cameras, displays, and video sources behave in your meeting space. This section ensures that participants, presenters, and shared content all appear correctly on in room displays and to remote meeting participants.

The following pages shape how you adjust your roomâs visual experience:

* Cameras â Position and tune up to two paired Q SYS cameras, configure image quality, enable auto framing, and create camera presets for the touch panel.
* Video Endpoints â Manage displays and video sources, including display control via Serial, Ethernet, or CEC (Consumer Electronics Control).

## Cameras

The Cameras page is where you configure how each camera in your room is aimed, how it looks, and how it behaves during meetings. You can also select, rename, save, or load presets.

**Note:** You can pair and configure up to two NC series models cameras in the same room. If no cameras are paired, a yellow notification banner appears: No Devices Paired â Camera controls are unavailable.

Supported Camera Models

RoomSuite Modular System supports the following NC series cameras:

* NC-90-G2
* NC-12x80
* NC-20x60

**Note:** Pairing must be completed in Devices before camera controls are enabled. For more information on how to pair devices see, [Devices](Devices.htm) page.

### Camera Settings

**Note:** You may only see the Position Presets page, and none of the other camera controls, when no supported camera is connected.

#### Model-Specific Differences

While all supported cameras share core functionality, the following model-specific differences apply depending on which camera model is paired with the system.

* **Auto Framing detection**: On NC 90, Auto Framing uses both **face and skeletal detection**, which can help keep people framed even when their face is partially turned. NC-12x80 and NC-20x60 use **face-based Auto Framing**.
* **Additional AI modes (NC 90 only)**: NC 90 introduces two extra AI modes â **Active Speaker Framing** and **Tile View** â in addition to standard Auto Framing. These modes are not available for NC-12x80 or NC-20x60.
* **Far End Audio Detect (NC 90 only)**: NC 90 provides a **Far End Audio Detect** feature that works with its AI modes to avoid reacting to remote audio coming from in room speakers. This feature is not for NC-12x80 or NC-20x60.

#### Position Cameras

Once supported cameras are paired, the camera controls allow you to position, focus, and invert each paired camera while watching a high-quality preview.

#### Camera Image Settings

Adjusts how the camera image looks. By default, auto white balance is selected. You can use a grey card to perform One Button Correction to calibrate the white balance based on your roomâs lighting.

#### Save and Recall Camera Position Presets

Allows you to save and recall camera position to a named position preset that is then displayed on the touch panel UCI. Only named presets appear on the touch panel.

#### Position Presets

The Position Presets section lets you save and recall camera position presets. Each preset stores the current camera position(s) for the paired cameras. When you give a preset a name, that preset name is displayed on the roomâs touch panel UCI. Only named presets appear on the touch panel.

#### To Create or Update a Position Preset

1. From the Position Presets section, choose a preset slot.
2. Adjust the camera position as necessary.
3. Enter a Preset Name.
4. Save the preset to store the camera position with that name.

#### To Recall a Preset

* From Select a preset, choose a preset, and click Load.
* Or, from the roomâs touch panel, tap the preset name to move the camera to the stored position.

## Video Endpoints

Within Video Endpoints, the Display pane lets you configure how each room display is controlled by setting the connection type (Serial / Ethernet / CEC), entering the control commands for power and input selection, and choosing a default display input. You can configure these settings separately for the Left Display and Right Display tabs.

#### Commands Table

The Commands table defines how RoomSuite Modular System controls the selected display for common actions such as powering the display on and off or selecting inputs.

**Note:** The Commands table is available only for Serial and Ethernet connections. When CEC is selected, the table is not shown since CEC control is automatic and does not require custom command entries.

Each row represents a display function, and each column shows how that function is implemented for the current display and connection type, Serial or Ethernet.

Use this table to:

* See which display functions are available for this display.
* Enter or adjust the commands used to control the display (for connection types that support custom commands).
* Verify that commands are configured correctly by sending them from the configuration interface when a test control is available.

#### Commands Table - Function column

Lists the supported display functions that can be controlled, such as Power On, Power Off, Input 1â4.

#### Commands Table - Command column

Editable text fields where you enter the command string to send for each Function.

#### Commands Table - End of Line column

Control (icon/drop down) where you specify the end of line characters used when sending each command.

#### Commands Table - Trigger column

Test buttons that send the corresponding command to the display so you can verify the display works.

### Serial Connection Type

#### Baud Rate (Bps)

Select the serial baud rate used. Choose a value to match the displayâs control protocol.

#### Data Bits

Select the number of data bits for the serial connection. Choose a value to match the displayâs control protocol.

#### Parity

Select the parity setting for the serial connection. Choose a value to match the displayâs control protocol.

#### Stop Bits

Select the number of stop bits for the serial connection when using Serial control. Choose a value to match the displayâs control protocol.

#### Connection Status

Read only text indicating the current status.

#### Default Display Input

Drop down that selects which input source for the display after reboot.

### Ethernet Connection Type

#### IP Address

Enter the IP address assigned to the display on the AV/control network. The value must match the displayâs network configuration.

#### Mac Address

For use with displays that require Wake on LAN for Ethernet Power On commands.

#### Port

This is the TCP or UDP port on which the display accepts control connections or messages. The correct port value is defined by the display manufacturerâs control documentation.

#### Connection Status

Read only text indicating the current status.

#### Default Display Input

Drop down that selects which input source for the display after reboot.

### CEC Connection Type

Select CEC when the display is controlled over the same connection that carries its audio / video signal and supports CEC. No separate IP or serial communication settings are required when using CEC control.
