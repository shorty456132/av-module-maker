# Configurator

> Source: https://help.qsys.com/Content/Hardware/0017_Configurator.htm

# Configurator

Use Q-SYS Configurator to discover all Q-SYS networked Cores and peripherals and configure Q-SYS PTZ cameras. Q-SYS Configurator is included with Q-SYS Designer Software and accessible from the Tools menu.

**Note:** Beginning with Q-SYS version 9.0, [Peripheral Manager](../Peripheral_Manager/PeripheralManager_Overview.htm) replaces many of the configuration and management functions formerly found in Q-SYS Configurator. Q-SYS PTZ cameras are still managed directly within Configurator. Q-SYS Core processors running firmware version 8.0 and later are managed with [Core Manager](../Core_Manager/CoreManager_Overview.htm).

[Device Status](javascript:void(0))

Discovered Q-SYS devices are shown in the left pane with a status icon. A flashing icon means that an ID button has been pushed, either on the physical device or in Q-SYS Core Manager or Peripheral Manager.

A green square means that your PC and device can communicate. Hover over the square to see the device's IP address.

A blue square means that the device is initializing. Select the device to reveal its known IP addresses.

A red square means that the device is discoverable, but your PC cannot communicate with it. Click the device to reveal its discovered IP addresses. To communicate with the device, try placing your PC on the same subnet as the device.

[Sorting and Searching](javascript:void(0))

* Use the Group By buttons to sort devices by Category, Model, or both.
* Use the Search field to show only those devices matching a text string.
* Click the  and  icons to expand or collapse individual groups or the entire list of discovered devices.

[Troubleshooting](javascript:void(0))

### "Current Password Invalid" error

If you receive a "Current Password Invalid" error when resetting a PTZ camera's password, make sure the new password does not exceed 31 characters.

### Devices appear and disappear from the Configurator window

* If Q-SYS devices disappear from the Q-SYS Configurator window after they have previously appeared, try disabling IGMP snooping on the network switch.
* If Q-SYS devices appear and disappear from Q-SYS Configurator repeatedly over the course of several minutes, it indicates the presence of an IGMP querier, but the IGMP snooping member expiration settings on a network switch are set to be shorter than the interval of queries from the querier. For example, if an IGMP querier sends queries every 300 seconds, yet the IGMP snooping rules are defined to remove members from multicast group tables after 125 seconds, devices will disappear for 175 seconds until the next query is sent.

**Note:** See the [Multicast Traffic](../Networking/Multicast_Traffic.htm) topic for information about IGMP requirements for Q-SYS networks.

### PTZ-IP Cameras: Cannot obtain DHCP address after changing from Static to Auto mode

In Q-SYS Configurator, if you change a Q-SYS PTZ-IP Series camera's IP address from Static to Auto, the camera may be assigned a link-local (169.254.x.x) address instead of a DHCP server-assigned address. This can occur if the camera has not previously been assigned an address by a DHCP server.

Workaround: Reboot the camera for the change to take effect. With the camera still selected in Q-SYS Configurator, click the cog icon (top-right corner) and select Reboot Camera.

**Note:** This issue does not affect NC Series cameras.
