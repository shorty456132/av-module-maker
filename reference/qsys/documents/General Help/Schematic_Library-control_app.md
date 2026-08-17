# Q-SYS Control App (iOS)

> Source: https://help.qsys.com/Content/Schematic_Library/control_app.htm

# Q-SYS Control App (iOS)

Use the Q-SYS Control App to wirelessly control any element of your Q-SYS system from an iPhone or iPad device. You can select a User Control Interface (UCI) from a list of discovered UCIs on your network, and then control that UCI just as you would on a Q-SYS touch screen.

**Tip:** Before using the app, refer to the [User Control Interface (UCI) Design Overview](user_control_interface.htm) topic to learn how to build and deploy a UCI.

[Requirements â Version 3.4.x](javascript:void(0))

* Version 3.4.x of the iOS app is required with Q-SYS 9.1.x and later. Download and install the app from the [App Store](https://itunes.apple.com/us/app/q-sys-control/id417461920?mt=8).
* The app is installable on any iOS device (iPhone, iPad) running iOS version 12.0 or later. For the best app performance, use the latest iOS version available. For users running the app on iOS version 14.0+, the app may no longer discover Cores on the network. This is due to changes in multicast support at the iOS level. As a workaround, configure [Hard Link IP Addresses](#Hard) in the app to communicate with the desired Cores. A fix is being investigated.
* For increased system compatibility, we recommend enabling the [Allow Insecure Networking](#Allow) setting. (This communication method is the default behavior for firmware v9.1.0 and earlier.) This recommendation will no longer be applicable once iOS app v3.5 releases.
* The app requires that the Q-SYS UCI Viewers - Windows and iOS network service is enabled in Core Manager > Network > Services (or remotely from Q-SYS Reflect). To learn how to enable or disable network services on the Q-SYS Core processor, see the [Network > Services](../Core_Manager/Core_Management/Network_Services.htm) topic.

[Configure Settings](javascript:void(0))

Go to your iOS device Settings menu and select "Q-Sys Control" from the list.

### Q-SYS Control Settings

#### UCI Viewer Mode

Similar to the [UCI Viewer App (Windows)](uci_viewer_app.htm), this displays UCIs from designs that include the [Status/Control (UCI Viewer)](uci_viewer.htm) component. When enabled, only designs with included UCI Viewers display in the list.

#### Enable Keyboard

When enabled, an on-screen keyboard appears for knobs and faders when they are tapped. Note that Text Fields always display the on-screen keyboard, regardless of this setting.

#### Allow Insecure Networking

When enabled, the app uses HTTP and unencrypted TCP to communicate with the Q-SYS Core processor. Enabling this setting is required for Q-SYS firmware versions that donât support HTTPS and TLS control connections (version 7.0 and earlier).

### UCI Filtering

#### Design Filter

This is a wild card -based filter for design names. Only Designs that match the filter are displayed in the app. Use question marks (?) for single character wild cards and asterisks (\*) for multiple character wild cards. For example, the filter 'Room \*' would match any designs that start with 'Room'.

#### UCI Filter

This works the same as for Design Filters, but for UCI names (or UCI Viewer names, depending on the UCI Viewer Mode property).

### Hard Link IP Addresses

#### IP 1-8

Configure up to eight IP addresses of remote Q-SYS Core processors. To learn more, see [Remote Connectivity](../Networking/Remote_Connectivity.htm).

[Use the App](javascript:void(0))

1. Open the app to see a list of UCIs (or UCI Viewers, if enabled in the app's Settings) from designs running on the local network or on remote Cores (if configured in Settings > Hard Links).
2. Tap a UCI or UCI Viewer name to open the UCI.
3. Tap the UCI to toggle and adjust controls as you would on a TSC touch panel. Rotate your iOS device to switch between portrait and landscape mode.
4. Swipe left to return to the list of UCIs.

[Create Shortcuts](javascript:void(0))

You can create a shortcut to open the app to a specific UCI, which can save you time if you always need to connect to a particular UCI or UCI Viewer name.

1. On your iOS device, open the Shortcuts app.
2. Tap + to create a new Shortcut.
3. Tap Add Action.
4. Tap Open URLs.
5. Name the Shortcut and enter the URL for the UCI or UCI Viewer. See [URL Rules](#URL) below for the proper URL format.
6. Assign a custom color and glyph.
7. Add the Shortcut to the home screen. You can now assign a custom icon, if desired.

**Tip:** Once your Shortcut is created, use Siri to open your UCI. Just say, "Hey Siri, <shortcut name>" or "Hey Siri, open <shortcut name>".

### URL Rules

Whether in a Shortcut, an e-mail, or in a browser, the prefix `qsys://` prompts the Q-SYS Control app to open. The body of the URL then points to the specific design name and UCI or UCI Viewer name.

* Use this format to open a UCI by name:

  `qsys://?design=<design_name>&page=<uci_name>`
* Use this format to open a UCI Viewer by name:

  `qsys://?design=<design_name>&viewer=<viewer_name>`

**Note:** Replace any spaces in either the design name or UCI name with the '+' character.

For example, this URL would open a UCI called 'Super Fancy UCI' from a design called 'My Design':

`qsys://?design=My+Design&page=Super+Fancy+UCI`

[Troubleshooting](javascript:void(0))

If your desired UCI or UCI Viewer name does not appear for selection in the app, check the following in the app's iOS Settings:

* Make sure the Local Network setting is enabled, which allows the app to communicate with the network.
* Try creating a Hard Link directly to the Core's IP address.
* Check that the Design Filter and UCI Filter settings aren't inadvertently filtering out your UCI name.
