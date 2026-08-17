# Microsoft Teams Room (MTR)

> Source: https://help.qsys.com/Content/Schematic_Library/spe_uci.htm

# Microsoft Teams Room (MTR)

You can integrate Q-SYS with a Microsoft Teams Room compute (PC) and room console. Integration of a Q-SYS system into a Microsoft Teams Room requires multiple Q-SYS software elements. Read this topic to understand what software elements are required, and to follow step-by-step guidance on getting your Teams Room integration up and running.

**Tip:** To learn about the strategic alliance between QSC and Microsoft Teams, to see examples of spaces featuring Teams Room with Q-SYS integration, and to read application documentation, go to the [Q-SYS + Microsoft Teams](https://www.qsys.com/alliances-partnerships/microsoft-teams/) page on the Q-SYS website.

[Overview and Requirements](javascript:void(0))

Click an element to learn more.

[Q-SYS Designer](javascript:void(0))

Q-SYS Designer Software version 9.0.0 and later is required.

[Teams Sample Design](javascript:void(0))

This sample design file enables Q-SYS to meet Microsoft Teams Room experience expectations, including audio DSP signal flow, DSP settings, room type optimization, and loudspeaker configuration optimization. The design file can be augmented with other DSP and control programming as long as the required signal flow remains intact.

The Teams Sample design is available in Q-SYS Library and includes the Mobile Device Companion App, Q-SYS Webhooks, and Teams UCI Style â each described separately below.

[Mobile Device Companion App](javascript:void(0))

The Mobile Device Companion App is a UCI embedded in the Teams Sample Design. Use it to fine-tune and optimize the DSP parameters in the design based on room acoustics.

Access the Mobile Device Companion App using a mobile device with network access to the Core. This could be via the HTML5 UCI viewer in Core Manager or from the Q-SYS Control app for iOS devices.

**Tip:** If you adjust the DSP settings in the Mobile Device Companion App and later change your mind, you can easily start over in the companion app and repeat the process with the default Teams-certified settings.

[Teams UCI Style](javascript:void(0))

The Teams UCI Style is included with the Teams Sample Design and also available for download separately via Q-SYS Library. Use it to apply CSS classes to controls in a native Q-SYS UCI. The CSS Style automatically applies colors, fonts, and control style information to match the Teams Room aesthetic.

To see a list of Teams style classes and examples for each, refer to the CSS Class Reference in the [UCI Styles](uci_styles.htm) topic.

[Q-SYS Control for MTR](javascript:void(0))

Q-SYS Control for MTR is an application, installed on the Microsoft Teams Room compute via .exe installer, that allows the Teams Room console to display any Q-SYS UCI deployed on the Core â typically for room control. An icon appears on the Teams Room touch panel to switch over to Room Control mode to view the Q-SYS UCI. You can then switch back to the native Teams Room console display when ready.

The Q-SYS Control for MTR .exe installer is included with the Q-SYS Designer Software download and also available separately from the Q-SYS [Software and Firmware](https://www.qsys.com/resources/software-and-firmware/) website.

[Q-SYS MTR Component](javascript:void(0))

The Q-SYS MTR Component connects to the Q-SYS Control for MTR application running on the Microsoft Teams Room compute. Use it to obtain the status of that connection and define what UCI is displayed on the Microsoft Teams Room console.

[Setup](javascript:void(0))

Follow these steps in order to get your Q-SYS system integrated with a Microsoft Teams Room. Before proceeding:

* Consult your network administrator and the [Microsoft Teams Deployment Overview](https://docs.microsoft.com/en-us/microsoftteams/rooms/rooms-deploy) (provided by Microsoft) for details on getting your Microsoft Teams Room compute device running.
* If the site uses a proxy service, ensure that the proxy service is configured to allow proxy bypass.

**Tip:** Watch the [Integrating Microsoft Teams Rooms into Q-SYS](https://www.youtube.com/watch?v=G8LQkc4BTGA) video from QSC Training for an overview of the integration process.

[Install Q-SYS Designer Software v9.0+](javascript:void(0))

Download and install Q-SYS Designer version 9.0.0 and later from the Q-SYS [Software and Firmware](https://www.qsys.com/resources/software-and-firmware/) website.

[Install Q-SYS Control for MTR on the Microsoft Teams Room compute](javascript:void(0))

The Q-SYS Control for MTR .exe installer is included with the Designer download bundle. Or, you can download separately from the Q-SYS [Software and Firmware](https://www.qsys.com/resources/software-and-firmware/) website. Follow this procedure to install the application on the Microsoft Teams Room compute.

**Note:** Install the application on the Teams Room compute, not the PC running Q-SYS Designer Software.

1. Ensure that the Teams Rooms platform is already installed and running on the Teams Room compute.
2. Copy the Q-SYS Control for MTR Installer.exe file to a thumb drive.
3. Insert the thumb drive into a USB port on the Microsoft Teams Room compute.
4. On the Teams Room console, tap More > Settings.
5. On the User Account Control prompt, type the Administrator password, and then tap Yes. If you do not know the password, consult your IT administrator.
6. On the Settings page, tap Windows Settings.
7. In the lower left corner, tap the Administrator user and log in with the Administrator password.
8. In Windows, use File Explorer to navigate to the USB thumb drive.
9. Double-tap the .exe installer file.
10. Follow the prompts to install the Q-SYS Control for MTR application and reboot the Microsoft Teams Room compute.

[Download the Teams Sample Design](javascript:void(0))

In Q-SYS Designer, go to Tools > Open Q-SYS Library (or click  from the toolbar) to find, select, and download the Teams Sample Design.

[Deploy the Teams Sample Design](javascript:void(0))

Go to File > Open Sample Design and select the Teams Sample Design to open. Then, select File > Save to Core & Run (or press F5) to deploy the design to the Core.

**Tip:** For help with saving designs to the Core, see the [Loading and Saving Designs](load_from_core.htm) topic.

[Set the Q-SYS Core as the Default Microphone and Speakers](javascript:void(0))

On the Teams Room console:

1. Tap More > Settings.
2. Enter the system password.
3. Select Peripherals from the left pane.
4. In the center window, select "Echo Canceling Speakerphone (Core110f)" for the Microphone, Speaker, and Default Speaker boxes.
5. Tap Save and Exit to go back to the main control window.

[Set Up the Sennheiser TeamConnect Ceiling Mic](javascript:void(0))

The Sennheiser TCC2 is a ceiling-mounted dynamic beamforming microphone that supports Dante for audio transport. The Sennheiser Control Cockpit software is required to begin the setup process. With your PC and the TCC2 Ethernet PoE/Ctrl port connected to the network switch, the browser-based Control Cockpit interface uses mDNS to detect and identify the TCC2.

1. Click the Devices tab.
2. Select the TCC2 mic to open its properties.
3. Click the Ethernet tab to configure its IP address, and then click Save.

   **Note:** Make a note of the mic's IP address, as you will use it later in the setup process when configuring the Teams Sample Design.
4. Click the Audio tab. The Source Detection section shows the current focus of the TCC2 automatic beam-steering, which can be tracked in real time. Click Edit to manually configure vertical and horizontal exclusion zones, which prevents detection of noise and sounds in these zones â for example, from ceiling-mounted AC vents, projector fans, doors, and credenzas.

   **Tip:** In some reverberant environments, applying an exclusion zone directed toward the front of the room and in the direction of the video display can improve AEC performance. Refer to the Sennheiser TeamConnect Ceiling 2 instruction manual for more information.

[Set Up the Selected Microphone](javascript:void(0))

The setup procedure varies depending on the microphone selected. Use the manufacturer's recommended procedures and software to deploy their microphone properly.

[Configure the Teams Sample Design](javascript:void(0))

With the Teams Sample Design running on the Core, follow the Room Setup steps in the design:

#### Step 1: Network Interface

Select the correct network interface that will be used to load the companion app. This will provide the correct network address via the QR code in order to load the Mobile Device Companion App.

#### Step 2: Microphone Dante Receive

Configure the communication parameters for the selected microphone:

*Dante receive*: Select the appropriate Dante device and channel for the microphone.

#### Step 3: Microphone Dante Transmit

Configure the communication parameters for the selected microphone:

*Dante transmit*: To send audio back to the microphone as a reference, specify a unique channel name for this purpose. Then, use Dante Controller software to route that channel from the Core back to the microphone.

#### Step 4: Loudspeaker Model

Select the model of NL Series PoE loudspeakers in use. Add the correct model into the inventory window and drag them into the design. You will need to remove the previous models and reconnect the wiring to the new models.

#### Step 5: Microphone LED Sync

Configure the communication parameters for the selected microphone:

*Control IP address*: Specify the microphone's control IP address, which is obtainable from the selected manufacturer's microphone software.

#### Step 6: Microsoft Teams Room Compute

This configures the MTR component in the sample design.

* MTR IP address: Specify the IP address of the PC that is running the Microsoft Teams Rooms software. This is visible on the idle screen of the Q-SYS Control for MTR application when you switch to the Room Controls view (when the application is not connected to the Core).
* Room Console UCI: Select the UCI from the design file to display on the Teams Room console. For now, you can leave this set to the room controls sample UCI.

#### Step 7: Mobile Device Companion App

From a mobile device with network access to the Q-SYS Core:

1. Scan the QR code to load the Mobile Device Companion App. (Alternatively, you can open Core Manager, navigate to the User Control Interfaces page, and select the "Companion App" UCI.)
2. Follow the instructions to fine-tune the audio settings for your specific room.
3. At the end of the process, save the settings.

[Configure the Teams Sample Design](javascript:void(0))

With the Teams Sample Design running on the Core, follow the Room Setup steps in the design:

#### Step 1: Room Name

Type a unique name/identifier for the room.

#### Step 2: Loudspeaker Type

Select where your room's loudspeaker's are installed, Ceiling or Surface. This selection determines the options for Loudspeaker Model.

#### Step 3: Loudspeaker Model

For each output, select the installed QSC loudspeaker model.

#### Step 4: Microphone

Configure the communication parameters for the Sennheiser TCC2 microphone:

* Control IP address: Specify the microphone's control IP address, which is obtainable from the Sennheiser Control Cockpit software.
* Dante receive: Select the appropriate Dante device and channel for the microphone.
* Dante transmit: To send audio back to the microphone as a reference, specify a unique channel name for this purpose. Then, use Dante Controller software to route that channel from the Core back to the microphone.

#### Step 5: Microsoft Teams Room Compute

This configures the MTR component in the sample design.

* MTR IP address: Specify the IP address of the PC that is running the Microsoft Teams Rooms software. This is visible on the idle screen of the Q-SYS Control for MTR application when you switch to the Room Controls view (when the application is not connected to the Core).
* Room Console UCI: Select the UCI from the design file to display on the Teams Room console. For now, you can leave this set to the room controls sample UCI.

#### Step 6: Webhook

Paste the unique Webhook URL for the Teams Room. This allows the Core to post messages in a Teams channel about design status, including whether audio parameters have been adjusted and may be impacting system performance or are using certified settings.

#### Step 7: Mobile Device Companion App

From a mobile device with network access to the Q-SYS Core:

1. Scan the QR code to load the Mobile Device Companion App. (Alternatively, you can open Core Manager, navigate to the User Control Interfaces page, and select the "Companion App" UCI.)
2. Follow the instructions to fine-tune the audio settings for your specific room.
3. At the end of the process, save the settings. This generates a Webhook message that commissioning is complete for the room.

[Build a Room Controls UCI](javascript:void(0))

Build a Q-SYS UCI to display on the Teams Room console for users to control and monitor camera selection and positioning, displays, HVAC, shades, mic and loudspeaker meters, etc.

**Tip:** You can modify the Room Controls sample UCI (included with the Teams Sample Design) for your own application.

1. Disconnect from the running Teams Sample Design (F7).
2. From the navigation pane, click User Control Interfaces.
3. Click  to create a new UCI.
4. Add controls to the UCI. For information about creating UCIs, see [User Control Interface (UCI) Design Overview](user_control_interface.htm).
5. From the navigation pane, select your UCI name.
6. From the User Control Interface Properties, select "Teams" as the Style. (The Teams style is included with the Teams Sample Design.)
7. For each control (text box, button, etc.), assign a CSS Class Name from the drop-down menu. To see a list of Teams style classes and examples for each, refer to the CSS Class Reference in the [UCI Styles](uci_styles.htm) topic.

**Tip:** The Teams style CSS classes automatically apply the colors, fonts, and control style information to match the Microsoft Teams Rooms aesthetic.

[Test the Room Controls UCI](javascript:void(0))

1. Save and run the Teams Sample Design to the Core, which now includes your Q-SYS room controls UCI.
2. On the Teams Room console, switch to Room Controls by tapping the fader icon in the bottom right corner. The Q-SYS UCI should display.

   **Tip:** If you are in a call, you can switch to Room Controls by tapping the . . . icon at the bottom of the screen and then tapping Room Controls.

[(Optional) Adjust Advanced Configuration Controls](javascript:void(0))

The Teams Sample Design includes an Advanced Configurations section for tweaking the audio, video, and control components for your specific room. Double-click a component's icon to understand the effects of changing its controls.

**Note:** The Q-SYS sample design file includes audio signal flow and processing settings that meet Microsoft Teams Rooms certification. We recommend using this design file. If you cannot, you should ensure that the signal integrity and gain structure is maintained to meet Microsoft Teams Rooms performance expectations.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### UCI Assignment

When set to Static (default), only the UCI as specified in Properties is displayed on the Teams Room console. When set to Dynamic, you can select the UCI while the design is running.

#### UCI

This field displays only when the UCI Assignment is set to Static. Use the pull-down list to select the UCI assigned to display on the Teams Room console. The UCI selection cannot be changed while the design is running.

[Controls](javascript:void(0))

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### IP Address / Host

Specify the IP address of the PC that is running the Microsoft Teams Rooms software.

#### UCI

If the UCI Assignment property is set to Dynamic, select the UCI from the design file to display on the Teams Room console. If the UCI Assignment property is set to Static, this control only shows the selected UCI as configured in the UCI property.

#### Page

Select the UCI page to display on the Teams Room console.

#### UCI Visible

LED indicates whether the Room Controls screen is active on the Microsoft Teams Room console.

#### Show

When triggered, the Room Controls screen is shown with the currently assigned UCI on the Microsoft Teams Room console.

#### Hide

Hide functionality is supported with Q-SYS Designer Software version 9.5 and later and the Q-SYS Control for MTR app version 9.5 and later. When triggered, the Room Controls screen is hidden on the Microsoft Teams Room console.

**Note:** There is a brief delay between pressing the Hide button and the UCI Visible LED indicating the current status.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Current Page | (text) | | | Input / Output |
| Current UCI | (text) | | | Output |
| Hide UCI | (trigger) | | | Input / Output |
| MTR IP Address | - | *nnn*.*nnn*.*nnn*.*nnn* | - | Input / Output |
| Show UCI | (trigger) | | | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| UCI Visible | 0  1 | false  true | 0  1 | Output |
