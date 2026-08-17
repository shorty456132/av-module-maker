# SNMP Query

> Source: https://help.qsys.com/Content/Schematic_Library/snmp_query.htm

# SNMP Query

Use this component to monitor up to 16 OIDs obtained from an SNMP-enabled device's MIB file. You can set conditions for monitoring each OID.

**Note:** In the SNMP model, Q-SYS acts as the SNMP Manager, while the device you intend to monitor runs an SNMP Agent that allows for monitoring.

[Prerequisites](javascript:void(0))

To monitor a device using the SNMP Query component, you need the Object Identifiers (OIDs) for the device you intend to monitor. If you don't know the OIDs for the managed objects within the MIB, use a MIB browser to view the OIDs. For example, these are the OIDs for the "firmware" category managed objects in the Q-SYS MIB:

Object: firmwareMajorVersion  
OID: `.1.3.6.1.4.1.1536.1.1.2.1.0`

Object: firmwareMinorVersion  
OID: `.1.3.6.1.4.1.1536.1.1.2.2.0`

Object: firmwareBuildVersion  
OID: .`.1.3.6.1.4.1.1536.1.1.2.3.0`

**Tip:** MIB browsers are available for download from the Internet.

[Getting Started](javascript:void(0))

1. Drag the SNMP Query component into your schematic.
2. Configure the SNMP Query properties. See [Properties](#Properti).
3. Drag the Status/Control component into your schematic.
4. Run your design.
5. Double-click the SNMP Query component to open the control panel.
6. Configure the Host Info and OIDs. See [Controls](#Controls).
7. Click Start.
8. Check the Status box for the SNMP query results. For more information, see [Controls](#Controls).

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Schematic Examples](javascript:void(0))

### Example 1: Status = OK

In this example, the conditions have been satisfied for all listed OIDs, so the overall Status is 'OK'.

### Example 2: Status = Fault

In this example, the Trigger Value for OID 2 (1806) is no longer equivalent to the Last Value (1906), so the OID Error LED glows red. Because a single OID is producing an error condition, the overall SNMP query Status is now 'Fault'.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### SNMP Query Properties

#### OID Count

Select how many OIDs to monitor, from 1 to 16.

#### Version

Select v2c (default) or v3, depending on the how your SNMP-enabled device is configured.

#### Auth Type

For v3 only, select the authorization type:

* NoAuth: (Default) Only a Username is required for authorization.
* AuthNoPriv: A Username and Auth Passkey is required for authorization. Select an SNMP Auth Protocol â details below.
* AuthPriv: A Username, Auth Passkey, and Priv Passkey are required for authorization. Select both an SNMP Auth Protocol and SNMP Priv Protocol â details below.

#### Auth Protocol

Select the type of authorization protocol for the AuthNoPriv and AuthPriv authorization types, either MD5 (default) or SHA.

#### Priv Protocol

Select the type of privacy protocol for the AuthPriv authorization type, either AES (default) or DES.

[Controls](javascript:void(0))

### Host Info

#### Host Name

Specify the IP address of the SNMP-enabled device on your network.

#### Community (v2c only)

Specify the community string of the device, as configured in the device's SNMP setup.

#### Username (v3 only)

Specify the SNMP v3 username string of the device, as configured in its SNMP setup.

#### Auth Passkey (v3 only)

The SNMP v3 authorization passkey is required whenever the Auth Type property is set to AuthNoPriv or AuthPriv.

#### Priv Passkey (v3 only)

The SNMP v3 privacy passkey is required only when the Auth Type property is set to AuthPriv.

#### Query Interval

Specify how often to query the SNMP-enabled device for OID value changes, from 10.0ms to 10.0s (default is 1.00s).

### OIDs

#### OID 1-16

Specify the OID string for the managed object you intend to monitor - for example:

`.1.3.6.1.4.1.1536.1.1.2.1.0`

#### Last Value

The OID's reported value from the last polling interval is shown in this text box.

#### Comparison Operator

For each listed OID, select the condition that determines whether the OID Error control is true or false. For all selections other than Present, you must then enter a comparative Trigger Value â see below.

* Present: The condition is satisfied if the OID is present. (There is no comparative Trigger Value.)
* == is equivalent to
* > is greater than
* < is less than
* >= is greater than or equal to
* <= is less than or equal to
* != is not equal to

#### Trigger Value

In this text box, specify a value for comparison to the Last Value.

#### OID Error

This LED glows red if the comparison between the Last Value and Trigger Value is false. This produces a 'Fault' status.

#### Start

Click this button to start an SNMP query of all listed OIDs and return an overall Status â see below.

### Status

The indicated status is determined by the overall OID Error state for all listed OIDs:

* If all OIDs have an OID Error state of 'false' (meaning all OIDs have satisfied their Comparison Operator conditions), the Status shows as 'OK'.
* If any OIDs have an OID Error state of 'true' (meaning at least one OID has not met the Comparison Operator condition), the Status shows as 'Fault'.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Community | (text) | | | Input / Output |
| Auth Passkey | (text) | | | Input |
| Auth User | (text) | | | Input / Output |
| Comparison Operator | - | Present  ==  >  <  >=  <=  != | - | Input / Output |
| Host Name | (text) | | | Input / Output |
| Last Value *n* | (text) | | | Input / Output |
| OID *n* | (text) | | | Input / Output |
| Priv Passkey | (text) | | | Input / Output |
| Query Interval | 0.01 to 10 | 10.0ms to 10.0s | 0.00 to 1.00 | Input / Output |
| Start | 0  1 | disabled  enabled | 0  1 | Input / Output |
| Status | (text) | | | Output |
| Trigger Value *n* | (text) | | | Input / Output |
