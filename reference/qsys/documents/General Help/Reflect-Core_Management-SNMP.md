# Network > SNMP

> Source: https://help.qsys.com/Content/Reflect/Core_Management/SNMP.htm

# Network > SNMP

SNMP allows you to manage and/or monitor devices on the Q-LAN network for conditions that may need attention. With a third-party Management Information Base (MIB) browser, you can poll any Q-SYS Core, which returns its status as well as the status of any Q-SYS peripheral devices included in the running design. Additionally, third-party devices monitored via Q-SYS Reflect-enabled plugins or the Monitoring Proxy component also report their statuses via the Core using SNMP.

**Note:** SNMP is disabled by default on new Q-SYS Core processors and those that have been factory reset.

## Configuring SNMP Access

Depending on the MIB browser you select, you can access the Q-SYS information using SNMP v2c and/or SNMP v3.

**Note:** The parameters you specify in Network Services > SNMP must be the same values you specify in the MIB browser.

Click Edit to modify SNMP access parameters.

[Version 2C](javascript:void(0))

* Access: Select SNMP v2c access is Disabled, Read Only, or Read/Write.
* Community: Specify the v2c community text string.

[Version 3](javascript:void(0))

* Access: Select whether SNMP v3 access is Disabled, Read Only, or Read/Write.
* User: The SNMP v3 username string.
* Security Level: Select from:
  + No Authorization â Only a username is required.
  + Authorization No Privacy â Requires a password, and allows selection of an Auth Protocol.
  + Authorization and Privacy â Adds another layer of security using a Privacy Password and Encryption.
* Password: The password for authorization, which is encrypted and masked. The password must be a minimum of 8 characters.
* Auth Protocol: The protocol for encrypting the signature attached to the SNMP message, either MD5 or SHA.
* Privacy Password: This password is used with the 'Authorization and Privacy' security level, which encrypts the entire SNMP message. The password is encrypted and masked, and must be a minimum of 8 characters.
* Encryption: Select an encryption type, either DES or AES.

## Loading the MIB File

Load the Q-SYS MIB into a MIB browser to access the Q-SYS SNMP objects by name. You can put the MIB anywhere as long as the MIB browser has access to the location.

You can obtain the MIB file from:

* The Q-SYS Designer installation directory: `C:\Program Files\QSC\Q-SYS Designer\SNMP`
* The QSC website (https://www.qsc.com) â search for "MIB".

## Supported Third-Party MIBs

* NET-SNMP-MIB
* NET-SNMP-FRAMEWORK-MIB
* NET-SNMP-EXTEND-MIB
* SNMPv2-MIB
* SNMP-MPD-MIB
* SNMP-USER-BASED-SM-MIB
* SNMP-VIEW-BASED-ACM-MIB
* UCD-SNMP-MIB
* UCD-DLMOD-MIB

## Inventory Table

Each device in the Q-SYS design's Inventory has an entry with the following objects:

* invDeviceName (Read Only) â the name of the Inventory device
* invDeviceType (Read Only) â the type of Inventory device (Core, Peripheral, Page Station, Amplifier, etc. )
* invDeviceModel (Read Only) â the specific model of the Inventory device
* invDeviceLocation (Read Only) â the Location of the Inventory device
* invDeviceStatus (Read Only) â the Status string
* invDeviceStatusValue (Read Only) â the Status value. (See [Status](../Status.htm#Statuses) for possible values.)

## Snapshot Table

Each Snapshot Bank has an entry with the following objects:

* ssSnapshotName (Read Only) â the Name of the Snapshot Bank.
* ssSsTotalSnapshots (Read Only) â the total available snapshots in the Snapshot Bank.
* ssActiveSnapshot (Read/Write) â Sets the active Snapshot.
* ssRampTimeSec (Read/Write) â Sets the time it takes for the controls to reach the saved position or value (in seconds).

**Note:** For all other Q-SYS SNMP objects, see the MIB file.
