# Remote Connectivity

> Source: https://help.qsys.com/Content/Networking/Remote_Connectivity.htm

# Remote Connectivity

You can remotely connect to a Q-SYS Core processor over the internet. Read this topic to understand the requirements for remote connectivity.

[Connectivity Requirements](javascript:void(0))

To establish remote connectivity, itâs essential to implement a secure network connection between local and remote networks, typically by utilizing a VPN or a comparable solution. Directing incoming traffic to specific devices is not recommended, as this practice may introduce security vulnerabilities. For instance, port forwarding via NAT is not supported due to these security concerns.

You may need to configure network firewalls to allow communication on the following ports:

* Q-SYS Designer requires TCP port 443 and HTTPS Hard Links to communicate with the target Q-SYS Core processor.
* Q-SYS UCI viewers (Windows app and iOS app) require TCP port 443 (supervisory functions), TCP port 1704 (control messaging), and UDP port 6504 (discovery) to communicate with the target Q-SYS Core.
* The remote PC must be able to exchange ICMP (ping) echo messages with the Q-SYS Core. There are separate firewall settings to enable or filter these messages.

### External Control

* External control systems can connect to the Q-SYS Core on TCP port 1702 (Q-SYS External Control Protocol - ASCII) or TCP port 1710 (Q-SYS Remote Control Protocol - JSONRPC).
* External controllers can communicate with a Q-SYS Core via any of its network interfaces. For more information, see [Network Interfaces, Services, & Protocols](Interfaces_Services.htm).
* Quality of Service (QoS) configuration is not required for external control.
* The external controller does not need to reside on the same LAN network as Q-SYS peripherals. It only needs to communicate with the Q-SYS Core over the network.

To learn more about external control, see [External Control APIs](../External_Control_APIs/External_Control_APIs_Overview.htm).

[Testing Connectivity](javascript:void(0))

You can test network connectivity by pinging the Q-SYS Core from your PC using the Windows command line interface (cmd.exe) and the Core's IP address. The format is `ping ip_address`. For example:

`ping 123.45.6.789`

If you get a good response â for example, "`Reply from 123.45.6.789: bytes=32 time<1ms TTL=64`" â you have the proper connectivity.

[Creating Hard Links](javascript:void(0))

You can configure Q-SYS Designer, Q-SYS UCI Viewer, and the Q-SYS Control iOS app to discover and connect to a remotely located Q-SYS Core. A Hard Link is the IP address of the Core to which you wish to connect. You may include multiple IP addresses. Note that the Q-SYS Administrator application uses the Hard Links as configured in Q-SYS Designer or Q-SYS UCI Viewer.

**Note:** Do not create Hard Links if your device can already discover the Q-SYS Core â that is, receive multicast packets from the Core.

[Creating Hard Links in Q-SYS Designer](javascript:void(0))

1. Close any open instances of the UCI Viewer.
2. Select File > Preferences > Hard Links from the Q-SYS Designer main menu.
3. To create a new hard link:
   1. Click the  button at the bottom of the dialog box.
   2. Enter the IP address of the Core to which to connect.
   3. Click OK to save the new IP address.
4. To manage existing hard links:
   * To edit a hard link, double-click an existing entry and specify a new IP address.
   * To delete an existing hard link, select a hard link and click the  button.
   * To toggle a hard link on or off, select or deselect the check box. This is useful when moving between network locations.
5. Select the Mode for all hard links: UDP or HTTPS.
6. After creating the required IP addresses, close all open instances of Q-SYS Designer. You can then:
   1. Reopen Q-SYS Designer, and connect to the Core using Load from Core and Connect or Save to Core and Run.
   2. Open the Q-SYS UCI Viewer, and then select a UCI from the UCI Browser.

[Creating Hard Links in Q-SYS UCI Viewer](javascript:void(0))

1. Close any open instances of Q-SYS Designer.
2. Open Q-SYS UCI Viewer.
3. Within the toolbar, click  (Edit Hard Links).
4. To create a new hard link:
   1. Click the  button at the bottom of the dialog box.
   2. Enter the IP address of the Core to which to connect.
   3. Click OK to save the new IP address.
5. To manage existing hard links:
   * To edit a hard link, double-click an existing entry and specify a new IP address.
   * To delete an existing hard link, select a hard link and click the  button.
   * To toggle a hard link on or off, select or deselect the check box. This is useful when moving between network locations.
6. Select the Mode for all hard links: UDP or HTTPS.
7. Close the Hard Links window, and then select a UCI from the UCI Browser.

[Creating Hard Links on an iOS Device](javascript:void(0))

1. Select Settings on the device
2. Under Apps, select Q-SYS Control. The Hard Link IP addresses list displays
3. Touch one of the IP address lines. The keyboard displays
4. Enter the IP address of the Core to which to connect. You must enter the periods along with the numbers.
5. You can continue adding IP addresses as required.
6. When you are finished, close the keyboard, and the settings menu.
7. Start the Q-SYS Control App. A list of available UCIs displays.
8. Select the one you wish to run.
