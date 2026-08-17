# Attero Tech Zip4

> Source: https://help.qsys.com/Content/Schematic_Library/Attero_Tech_extension_Zip4.htm

# Attero Tech Zip4

Use this extension to connect to and control the Zip4 or Zip4-3G Dante/AES67 four-zone paging station (Attero Tech by QSC).

**Note:** See the [Zip4 product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/attero-tech-paging-stations/zip4/) or [Zip4-3G product page](https://www.qsys.com/systems/products/q-sys-ecosystem/products-peripherals-accessories/attero-tech/attero-tech-paging-stations/zip4-3g/) on the QSC website for product information and documentation.

[Compatibility](javascript:void(0))

The extension is compatible with Q-SYS Designer version 8.4 and above and Attero Tech firmware version 1.5 (Zip4) and 1.4 (Zip4-3G) and above. For best results, use the latest Attero Tech firmware.

[Requirements](javascript:void(0))

* It is recommended that a static IP address be assigned to the device. If the network uses a DHCP server, the DHCP server should be configured to assign a reserved IP address for each Zip4.
* Each instance of the extension controls a single Zip4 device. Your design requires the same number of extensions as there are Zip4 devices to control.
* The Zip4 extension requires an instance of the PA Router component in your design. Configure the PA Router to ensure that one station is available for each Zip4 extension in your design. For example, here are two Zip4 extensions with the [Auto Cancel](#Auto) property enabled:

[Connection Setup](javascript:void(0))

1. In the NIC field, select the interface through which the extension will communicate to control the device.
2. Specify the Station ID number. Each instance of the Zip4 extension requires a unique Station ID. The Station ID must match the audio input on the PA Router that receives audio from the Zip4. For instance, if the Zip4 extension is wired to the PA Router to Station 3 Audio, the Station ID must show '3'.
3. In the IP field, specify the IP address of the device and press Enter.

The extension will automatically attempt a connection. The "Connected" LED glows green once a connection is established. If the extension loses its connection to the device, it will attempt to re-establish the connection every 5 seconds.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Default Zone

Determines what happens if a page is initiated with no zone groups selected. If set to âNoâ (default), nothing happens. If set to âYesâ, a page is made to an additional âdefaultâ zone thatâs configured with its own set of paging parameters.

#### Auto Cancel

Allows a âDelayedâ type page to be canceled if audio level remains below a certain level for a given period. For this option to work, the incoming audio must be routed through the plug-in from the receiver.

#### Multi Zone Select

Specifies if multiple group buttons can be selected simultaneously for a page. When set to âNoâ, only a single zone group can be selected at one time.

#### Security

Sets the security mode on the Zip4. In âOpenâ mode (default), the Zip4 can be used at any time without restriction for a page. In âSecuredâ mode, the unit is protected with a 3-digit pin which must be entered first before a change can be made.

#### Show Debug

Select 'Yes' to show the Debug Output window. For details, see [Debug Output](debug_output.htm).

[Controls](javascript:void(0))

The Zip4 extension is designed to work similarly to the Q-SYS Virtual Paging Station component. Many of the configuration options are the same as those seen in the VPS.

**Note:** Some of the configuration for paging is completed within Q-SYS Administrator. Plug-ins do not automatically pick up changes made within Q-SYS Administrator. Each Zip4 extension must be manually updated to get the latest settings by clicking the Refresh button.

### Button/Zone Config

Each button on the Zip4 can be assigned a zone group that comprises a single zone or a specific group of zones of the PA Router. Assignment is completed using the combo boxes below each button. To ensure correct operation, the name of each tag and zone must be unique. A button can be left unassigned if it is not required. Pressing a group button on the device that has no assigned zone or tag has no effect.

The group buttons in the extension mirror the state of the group buttons on the device to which the extension is connected. When a zone button is pressed, it toggles the selected state of that zone group. The zone group indicator turns green if the zone is selected.

During operation, if pages elsewhere in the system affect any of the assigned zone groups on this device, they are marked "busy" and the zone group indicator turns red. If the zone group is both selected and busy, the group indicator turns yellow.

**Note:** When selecting tags for remote zones (Core-To-Core paging) in the drop-down, certain issues may arise. These include the loss of tag selection whenever the plugin is restarted, such as during a Core reboot or when the design is restarted or pushed, and differences in how the Zone LED for the remote zone functions compared to local zone LEDs. To mitigate these issues, it is recommended to create an additional local zone in the PA Router that remains unconnected and assign the remote tag solely to this local zone. This approach prevents the remote tag from being removed upon plugin startup and ensures that the remote zone's LED functions consistently with those of local zones.

### Paging Config

Each page uses the parameters defined in the Paging Config section of the extension. If the Default Zone property is set to yes, a second set of parameters is also shown that relates purely to the default zone pages. Therefore, the default page can be set up differently from regular group pages.

#### Page Mode

Configures the page mode to one of three different options: Live, Delay or Auto. Live pages connect the microphone directly to the output so any speech is heard live. Delayed pages are first recorded and then played back later to the required zones. âAutoâ will activate a live page if possible and switch to a âdelayedâ page if the required zones are busy.

#### Priority

Determines the importance of a particular page. The options available are based on the priority configuration set using Q-SYS Administrator.

#### Max Page Time

Sets the time limit on the maximum length of a page. Options are "Not Limited", "30 Seconds", "60 Seconds", "90 Seconds", "120 Seconds", and "240 Seconds".

#### Preamble Dir, Msg

The preamble fields enable pages to be prefixed with a common audio clip. Q-SYS Core processor DSPs contain some default audio clips. If a custom clip is required, this must be preloaded into the DSP beforehand using Q-SYS Administrator. The âDirectoryâ field lists all folders that contain supported audio files that can be used as a preamble. The âblankâ option represents the ârootâ folder, which contains default audio files. The âMsgâ field lists the supported audio files within the selected directory that can be used. If the âMsgâ field is empty, no preamble is played for a page.

**Note:** Empty folders or folders not containing supported audio files are not included in the âDirâ drop-down list.

### Brightness

These controls configure the brightness of the various indicators on the Zip4. There are separate controls for the red LEDs, Green LEDs, and the backlight. Values range from 0 (off) to 255 (fully on).

### Auto Cancel

These controls only appear when the âAuto Cancel" property is set to âYesâ. Auto cancel only works on pages that record the message for later playback. The recorded page can be canceled by keeping the audio level below the specified threshold for a specified amount of time. The threshold and the time are both configurable. If successfully canceled, the âReadyâ indicator turns green even though the âPTTâ button remains pressed.

### Security

These controls only appear when the âSecurityâ property is set to âYesâ. With security enabled, the device appears to be off with all backlights and indicators turned off. The unit activates if the correct 3-digit pin is entered. The unit automatically locks itself after a specified time has passed with no button activity.

#### Lock button

Immediately locks the connected Zip4.

#### Unlock button

Immediately unlocks the connected Zip4.

#### Code entry

Three drop downs allow selection of the 3-digit pin. Once the code is selected, click **Apply**.

#### Timeout

Select the number of minutes of button inactivity that have to elapse before the device locks itself. Range is 1 minute to 30 minutes.

### Status

#### PTT button

State of PTT button on device.

#### Ready indicator

Mirrors the state of the âReadyâ indicator on the device. Turns green if the device is ready to accept a page. Shows yellow if the page is being recorded.

#### Busy indicator

Indicates the paging system is busy and cannot currently be used.

#### Auto Cancel indicator

Only visible when the âAuto Cancelâ property is enabled. Briefly flashes green if the auto cancel is activated.

#### Status field

Indicates the state of any page as reported by the PA Router to the extension.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Device | | | | |
| Connected | 0  1 | false  true | 0  1 | Output |
| Identify | 0  1 | false  true | 0  1 | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Zone |  |  |  |  |
| 1-4 | 0  1 | false  true | 0  1 | Output |
| Zone Group |  |  |  |  |
| 1-4 | (text) | | | Input / Output |
| Zone LED |  |  |  |  |
| 1-4 | 0  1 | false  true | 0  1 | Output |
| Busy LED | 0  1 | false  true | 0  1 | Output |
| Disable[1](#Use) | 0  1 | disabled  enabled | 0  1 | Input / Output |
| PTT | 0  1 | false  true | 0  1 | Output |
| Ready LED | 0  1 | false  true | 0  1 | Output |

###### 1. Use this control pin to enable or disable the extension in your design. When Disabled is set to enabled (value of 1), the Connection Status changes to "Not Present - Disabled".
