# UCI Viewer App (Windows)

> Source: https://help.qsys.com/Content/Schematic_Library/uci_viewer_app.htm

# UCI Viewer App (Windows)

The Q-SYS User Control Interface (UCI) Viewer is a stand-alone, Windows based application used to discover and run Q-SYS UCIs over a local area network.

For information about designing UCIs, see [User Control Interface (UCI) Design Overview](user_control_interface.htm).

[Installation](javascript:void(0))

The Q-SYS UCI Viewer for Windows is available on the QSC website as part of the Q-SYS software download. It is highly recommended that you download and install the same version UCI Viewer as your Q-SYS Designer.

1. On the Windows PC that is going to run the UCI Viewer, locate the download file (for example, Q-Sys\_Uci\_Viewer\_Installer\_x.x.xxx.exe), and double-click the file.
2. Or, download the file from the web site listed above. During the download process you are prompted to run or save the file. Select Run.
3. Follow the instructions given during the installation process.

[Run the UCI Viewer](javascript:void(0))

1. Ensure that the PC on which the UCI Viewer will run is connected to the same local area network as the Core.

**Note:** For remote access, refer to the section titled "Remote Access with Q-SYS UCI Viewer" below.

2. Select Start > All Programs > Q-SYS UCI Viewer > Q-SYS UCI Viewer. The UCI Viewer interface displays.
3. Select the UCI Viewer type (under the tool bar). You can select UCI Viewers to get a list of UCIs that are assigned to a UCI Viewer Status/Control component, or select one UCIs by name. Running a UCI using the UCI Viewer component displays the UCI status, and allows a certain amount of control of the UCI from Q-SYS Designer. Refer to the [UCI Viewer Status/Control component](uci_viewer.htm) topic for details.
4. In the UCI Browser (left-side pane), is a list of all Available UCIs running in a design on any Core connected to the Q-LAN network. In addition, if you are Emulating a design with a UCI, and running the UCI Viewer on the same PC, the Emulated UCI is listed. The UCIs are sorted by design name, then UCI name.

**Note:**  Hover over the Current Design name to see information about the Core running the design, or the PC Emulating the design.

5. Select the desired UCI. The UCI displays as designed.

### Auto Start

If you want a UCI to automatically run when Windows starts:

1. Create a bookmark (see table below) for the UCI
2. Create a Windows Shortcut to the bookmark
3. Copy or Cut and Paste the shortcut into the Windows Startup directory: C:\Users\user\_name\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
4. When Windows is restarted, the UCI automatically starts.

[UCI Viewer Interface](javascript:void(0))

Because the UCI Viewer is a stand-alone Windows application that connects with Q-SYS, it supports standard Windows input methods. You can interact with the interface using a mouse or touchscreen, and take advantage of multi-button press slidingâpress and hold a button, then slide your finger or mouse over other buttons to change their states to match the first button pressed.

Platform-level horizontal scrolling is supported here to navigate layouts that extend beyond the visible workspace. You can scroll horizontally using any of the following input methods:

* Touchpad Gestures: Use side-to-side (two finger swipes on supported trackpads.
* Mouse Wheel: Hold the Shift key while scrolling vertically with a mouse wheel.
* Native HID Devices: Use devices with dedicated horizontal scroll support (e.g., horizontal scroll wheels).
* Scroll Bar: Use mouse or arrow keys to drag the bar.

[Controls](javascript:void(0))

#### UCI Selection Panel (show / hide)

Clicking this icon shows or hides the UCI Selection panel. The default is show.

#### Full Screen

Clicking this icon enters or exits the UCI Viewer full-screen mode.

* The UCI Viewer full-screen mode is different from the Windows full-screen mode in that while in the UCI Viewer full-screen mode, the title bar is not shown. In Windows full-screen, the title bar and controls are shown.
* When in full-screen mode, you can press the Esc button to exit the full-screen view.
* If the UCI Selection Panel is visible in full-screen mode, you can hide or size it by grabbing the separator bar between the UCI and the UCI Browser and sliding it to the desired position. If you opened the UCI Viewer with a Bookmark, and the Bookmark file did not "Show the UCI Browser", you cannot open it in that bookmark mode.
* If you opened the UCI Viewer with a Bookmark, and the Bookmark file did not "Show the Toolbar", you cannot open the Toolbar in that bookmark mode.

#### Touchscreen Control Mode (On / Off)

Click this button to change the UCI display to Touchscreen Control mode. In Touchscreen Control mode, hovering and text entry are disabled, the mouse cursor is not visible. When the UCI Viewer is in Touchscreen Control mode, the login screen is a pin-pad instead of a dialog box.

Touchscreen Control mode does not disable the mouse cursor over the toolbar, or the UCI Selection Panel.

Touchscreen Control Mode is persistent. If you enable Touchscreen Control mode, close the UCI Viewer then reopen it, Touchscreen Control Mode is still enabled. However, Bookmark settings take precedence.

You can save a UCI in Touchscreen Control mode as part of a Bookmark.

#### Bookmark

Clicking this icon saves information about the currently running UCI, and the desired view of the UCI Viewer.

1. Click the Bookmark icon. The Save Bookmark dialog box displays
2. Click the checkbox for one or more of the following options:

* **Show Full Screen**
  - When you open the Bookmark file, the UCI is automatically displayed in full-screen mode.
* **Show Toolbar**
  - the Toolbar is included in the display when the Bookmark file is opened.
* **Show UCI Browser**
  - The UCI Browser (left-side pane) is included in the display when the Bookmark file is opened.
* **Touchscreen Control Mode**
  - When the Bookmark file is opened, the UCI displays in Touchscreen Control Mode.

3. **File**
   - The path and filename of the Bookmark file. The extension for the file is *.quci*.   
   You can type the path and filename, or click the ellipsis button to navigate to a directory, then type the filename.
4. Click **Save** to save the Bookmark file, or **Cancel** to exit without saving.
5. After the file is saved, you can double click the Bookmark file and the UCI Viewer opens with the UCI, and view selections you defined.

#### Toolbar (Hide)

Click the Toolbar button to hide the toolbar.

Right-click, or touch-and-hold (Win 7/8) a menu displays. Click or touch Toolbar to restore the Toolbar.

#### Settings and Hard Links

Clicking this button will open a dialog box within the UCI Viewer App interface, allowing you to adjust certain settings and configurations.

* **Hard Links** - View the IP address(es) of connected Q-SYS devices within the software interface. This feature includes a checkbox next to each IP address, which you can check or uncheck to toggle the connectivity of that specific IP address. Checking the box enables the connection of the IP address, while unchecking it hides the IP disconnects from that device.
* **+ / -**  - The plus and minus signs represent options for connecting or disconnecting from a device's IP address within the Q-SYS system. Clicking the plus sign initiates a connection to the specified IP address, enabling communication and interaction with the device. Conversely, clicking the minus sign terminates the connection to that IP address, effectively ending communication with the device and severing the link established between them.
* **Mode** - Allows users to select between UDP or HTTP communication protocols.
* **Close** - Closes the dialog box and returns to the UCI Viewer.
* **Maximum Live Video Streams** - Determines the maximum number of concurrent live video streams that can be processed or displayed within the system at any given time. (Default is 2).
* **Right click (Mouse) / Long Press (Touch) Disabled Checkbox** - When checked, it disables the context menu from appearing. When unchecked, it allows the context menu to appear, permitting right-clicking with a mouse or performing a long press on a touchscreen interface to trigger the context menu as usual.

#### Help

Click this button to access the offline help file for guidance in the UCI Viewer App interface.

#### Info

Clicking this button provides info within the Q-SYS UCI Viewer interface. When pressed, it triggers the opening of a dialog box that displays the version number.

#### Multi-touch Mode (On / Off)

Click to toggle Multitouch mode, which allows for UCI Viewer to recognize more than one point of contact (touch) at a time. Disable Multitouch for better compatibility with touchscreen PC devices such as Microsoft Surface.

[Remote Access with Q-SYS UCI Viewer](javascript:void(0))

See [Remote Connectivity](../Networking/Remote_Connectivity.htm).
