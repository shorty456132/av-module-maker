# Q-SYS UCI Viewer App (Android)

> Source: https://help.qsys.com/Content/Schematic_Library/control_app_android.htm

# Q-SYS UCI Viewer App (Android)

Use the Q-SYS Control App to wirelessly control any element of your Q-SYS system from an Android phone or tablet. You can select a User Control Interface (UCI) from a list of discovered UCIs on your network, and then control that UCI just as you would on a Q-SYS touch screen.

**Tip:** Before using the app, refer to the [User Control Interface (UCI) Design Overview](user_control_interface.htm) topic to learn how to build and deploy a UCI.

[Requirements](javascript:void(0))

* Android 10 is the minimum supported OS.
* The Q-SYS UCI Viewer App for Android requires Q-SYS Designer Software version 10.0.x or later.

[Installation](javascript:void(0))

The Q-SYS UCI Viewer App for Android can be downloaded and installed from the [Google Play Store](https://play.google.com/store/apps/details?id=com.qsc.qsysuciviewer). The .apk (Android Executable) will also be available on the Q-SYS website.

[App Performance](javascript:void(0))

* The Android UCI Viewer application is rendering the UCI using the devices internal web browser.
* The performance of the UCI is directly related to capabilities of the hardware + the capabilities of the on-board web browser.
* The UCI performance will always be equivalent to opening the same UCI in the hardwareâs default web browser.

[Use the App](javascript:void(0))

Upon launching the app, it automatically opens to the UCI Selection screen. However, tapping the three lines  on the left side will reveal the side pane, providing access to the UCI Display and Settings menus.

### UCI Selection

1. Open the app to see a list of UCIs (or UCI Viewers, if enabled in the app's Settings) from designs running on the local network or on remote Cores (if configured in Settings > Hard Links).
2. Tap a UCI or UCI Viewer name to open the UCI.
3. Tap the UCI to toggle and adjust controls as you would on a TSC touch panel. Rotate your Android device to switch between portrait and landscape mode.
4. Swipe left to return to the list of UCIs.

### UCI Display

The UCI Display tab shows the currently selected UCI.

### Settings

Provides various options to access and customize the app's functionality. For more information, see [Configure Settings](#Configur).

[Configure Settings](javascript:void(0))

Open the Q-SYS UCI Viewer (Android) application and select Settings from the three lines on the left side.

### Q-SYS UCI Settings

### UCI Filtering

#### Design Filter

This is a wild card -based filter for design names. Only Designs that match the filter are displayed in the app. Use question marks (?) for single character wild cards and asterisks (\*) for multiple character wild cards. For example, the filter 'Room \*' would match any designs that start with 'Room'.

#### UCI Filter

This works the same as for Design Filters, but for UCI names (or UCI Viewer names, depending on the UCI Viewer Mode property).

### Hard Link IP Addresses

#### IP 1-7

Configure up to seven IP addresses of remote Q-SYS Core processors. To learn more, see [Remote Connectivity](../Networking/Remote_Connectivity.htm).

[Create Shortcuts](javascript:void(0))

You can create a shortcut to open the entire application.

1. After installing the Q-SYS UCI Viewer (Android) application, swipe up from the home screen to access the App Drawer.
2. Find the Q-SYS UCI Viewer application.

3. Long-press on the app's icon.
4. Click on 'Add to Home'.

[Troubleshooting](javascript:void(0))

If your desired UCI or UCI Viewer name does not appear for selection in the app, check the following in the app's Settings:

* Make sure the Local Network setting is enabled, which allows the app to communicate with the network.
* Try creating a Hard Link directly to the Core's IP address.
* Check that the Design Filter and UCI Filter settings aren't inadvertently filtering out your UCI name.
