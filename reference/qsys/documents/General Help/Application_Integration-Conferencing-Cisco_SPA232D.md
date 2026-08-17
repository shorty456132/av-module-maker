# Cisco SPA232D

> Source: https://help.qsys.com/Content/Application_Integration/Conferencing/Cisco_SPA232D.htm

# Cisco SPA232D

Follow these recommendations when integrating a Cisco SPA232D Analog Telephone Adapter with Q-SYS.

## Introduction

This topic covers the use of the SPA232D in the role of analog telephone adapter (ATA) from an analog telephone network to the Q-SYS softphone, shown below:

## Configuration

To configure the SPA232D Analog Telephone Adapter (ATA), you will need an AC mains power outlet and a computer with a wired Ethernet port and up-to-date web browser. You may need Internet access to download a firmware update.

1. Plug the power supply (provided with the ATA) into an AC mains outlet and plug its DC output connector into the DC power jack on the ATA.
2. Connect the POTS line to the green LINE port. Using a standard Ethernet cable, connect the computerâs network port to the yellow ETHERNET port.
3. Set the computerâs network interface to obtain an IP address from a DHCP server.
4. If the computer has any other network interface cards (NICs), such as WiFi, additional wired ports, etc., disable them for the time being.
5. The computer should automatically obtain the IP address 192.168.15.100 from the DHCP server in the ATA.
6. Open a web browser and navigate to the IP address 192.168.15.1. The web interface page of the ATA should appear.

   **Note:** If the browser cannot connect to the web interface, do a factory reset on the ATA. To do so, insert a thin pointed object (e.g., a pin, a straightened paper clip, et al) into the red hole labeled RESET. Press the recessed button inside and hold it until the power LED on the ATA starts flashing (this should take less than 10 seconds). Release the button and allow the ATA to run until the power LED is solid. Then, disconnect power for several seconds and re-connect it. This will reboot the ATA with factory default settings. Once the power LED stays solid, try connecting the browser to 192.168.15.1 again. You might need to refresh the browser several times.
7. Take note of the firmware version displayed on the login page. If it is older than version 1.4.1, locate and download the latest update from Cisco so you can apply it later. It downloads as a .zip file, so you will have to unzip it to a .bin file.
8. Log in to the web interface. The factory default credentials are admin (user name) and admin (password).
9. If you need to update the firmware, go to Administration > Firmware Upgrade. Select the .bin file and follow the instructions on the web interface page. When the update is uploaded and applied, the ATA will restart. Allow it to finish restarting before proceeding.
10. Go to Administration > Management > User List and click the pencil icon to the right of the admin account. Change the admin password to something secure other than admin. You may also change the admin user name. Click Submit.
11. Go to Administration > Management > Web Access Management and select these options:

    * Admin Access: Enabled
    * Web Utility Access: Check both HTTP and HTTPS
    * Remote Management: Enabled
    * Web Utility Access: HTTP
    * Remote Upgrade: Enabled
    * Allowed Remote IP Address: Any IP Address
    * Remote Management Port: 80

    Click Submit.
12. Go to Network Setup > Internet Settings. Change the Connection Type to Static IP and set a valid Internet IP address, subnet mask, and default gateway for the network. Click Submit.

    **Note:** The static IP address ensures that a Q-Sys Smartphone can always reach the ATA. Do not enter a temporary IP address here; use only the ATAâs permanent WAN address.
13. Go to Network Settings > Basic Setup > Network Service and change Networking Service to Bridge. Click Submit. The ATA will reboot to implement these settings, which may take longer than two minutes. While it reboots, continue with steps 14 and 15.
14. Adjust the computerâs IPv4 settings to allow access to the Core and the ATAâs WAN IP address, which was set in an earlier step.
15. Disconnect the ATA from the computerâs network port. Connect both the ATA and the computer to the same switch and VLAN that the Q-SYS Core processor is connected to.
16. In the web browser, use the ATAâs WAN IP address to access its web interface. The web interface should appear once the unit finishes rebooting. You might need to refresh the browser. When the page appears, log in using the new credentials.
17. Go to the Quick Setup page.

    1. Under HandsetâOutgoing DECT Line Selection, clear the check box to the right of All Handsets (see figure). This will clear all the check boxes in the left column, under DECT Line 1.
    2. Under HandsetâIncoming DECT Line Selection, clear all the check boxes in the All row, and clear the check box at the bottom of the All Handsets column (see figure).

       Click Submit. Wait for the web interface page to return.
18. Click the Voice tab.

    **Tip:** To save time, assign all the following settings, then click Submit once at the end.

    |  |  | Parameter | Setting |
    | --- | --- | --- | --- |
    | Line 1 |  | Line | No |
    | PSTN | SIP Settings | SIP Port | 5060 |
    |  | Proxy and Registration | Proxy | Enter the Q-SYS Core processor's Softphone IP address (this address is  assigned in the Softphones tab of Q-SYS Core Manager) |
    |  |  | Register | No |
    |  |  | Make Call Without Reg | Yes (default value) |
    |  |  | Ans Call Without Reg | Yes (default value) |
    |  | Audio Configuration | Preferred Codec | G711u |
    |  |  | G729a Enable | No |
    |  |  | DTMF Process INFO | No |
    |  |  | DTMF Tx Method | AVT (this is Ciscoâs term for out-of-band DTMF RTP events) |
    |  | Dial Plans | Dial Plan 8 | (`S0<:nnnn`)  where *nnnn* is a four- to 10-digit number. You will have to use this same number as the User Name telephone number in Step 22.  You may use the same number as the POTS line, if you wish, but it is not required. |
    |  | VoIP-To-PSTN  Gateway Setup | DECT Line Caller DP | None |
    |  | PSTN-To-VoIP  Gateway Setup | PSTN Caller Default DP | 8 |
    |  | PSTN Timer Values  (sec) | PSTN Answer Delay | 2 |
    |  | International Settings | FXO Country Setting | Select the appropriate country from the list, if not US |

    Click Submit. The ATA will restart.
19. Because the ATA is operating with networking bridged, you may switch the network connection at this point from the yellow Ethernet port to the blue Internet port. Either port will work for accessing the ATA, but the blue port has a network activity indicator LED, while the yellow one does not.
20. If you wish to save a backup file of this configuration, click on the Administration tab. Go to Config Management > Backup Configuration.

    Click Backup to download the configuration file.

    **Note:** The SPA232D configuration file is not in editable text form.
21. In Q-SYS Core Manager, click the Softphones tab. Select the Softphone instance you wish to assign the ATA to.
22. Apply these settings to the Softphone:

    | Option | Setting |
    | --- | --- |
    | User Name | Enter the phone number assigned in the Dial Plan 8 setting in Step 18. |
    | CID Name | Enter the Caller ID name that Q-Sys should report to the gateway. |
    | Proxy | Enter the WAN IP address assigned to the ATA in Step 12. |
    | Register With Proxy | No |
    | Call Start Tone | Choose one:  Yes = When a call connects, a short tone is produced.  No = No tone is produced when a call connection is made. |
