# Monitoring Proxy

> Source: https://help.qsys.com/Content/Schematic_Library/monitoring_proxy.htm

# Monitoring Proxy

Use the Monitoring Proxy component to allow a third-party device to report its status to the Status > Inventory list, which is viewable not only in Q-SYS Core Manager, but remotely in Q-SYS Reflect. In addition, you can use the component to trigger custom log events â for example, from a scripting component.

**Note:** Monitoring proxies are considered peripherals. When the total number of peripherals, including monitoring proxies, reaches the maximum allowed for each Core, a red bar or compile error might be thrown in Check Design.

[Use Cases](javascript:void(0))

* Monitoring Proxy allows a third-party device to become an Inventory item in your design. When you connect Monitoring Proxy to an upstream Status control pin, that status is then viewable locally in Core Manager and remotely in Q-SYS Reflect.
* Monitoring Proxy also allows you to submit log entries for the third-party device to the Core's Event Log. Events from Monitoring Proxy are then viewable in the Q-SYS Reflect Event Log.

**Tip:** Log output from scripting components (for example, [Block Controller](device_controller.htm)) and entries submitted to the Event Log from the [Event Logger](event_logger.htm) component do not appear in Q-SYS Reflect Event Log. Use Monitoring Proxy to allow logging from these components in Q-SYS Reflect.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Status Input

By default, Monitoring Proxy includes a single input control pin. Wire this pin to an upstream component's Status control pin. The Status Input pin receives the complete, extended status from the upstream component and passes it to Status > Inventory list in Core Manager and Q-SYS Reflect. For more information, see [Controls](#Controls).

### Output Pins

This component does not have standard output pins.

[Configuration Overview](javascript:void(0))

To configure Monitoring Proxy to send the status of a third-party device to the Status > Inventory list in Core Manager and Q-SYS Reflect:

1. From the Inventory > Control menu, select Monitoring Proxy.
2. Define your third-party device's Name (for example, "Conf-Room-TV"), Manufacturer (required), Model (required), and Type. See [Properties](#Properti).
3. Drag the Monitoring Proxy's Status/Control component into the schematic.
4. Wire the Status Input pin to the Status pin of an upstream component. For example, this could be an upstream Monitor category component (Ping, SNMP Query) or a script you have written for this third-party device.
5. Press F5 to save your design to the Core and run it.
6. Double-click the Monitoring Proxy component to open its control panel. The Status field indicates your third-party device status, which is now being sent to the Status > Inventory list in Core Manager and, with a subscription, Q-SYS Reflect.

**Tip:** You can also submit custom log entries to the Core's Event Log. To learn how, see [Schematic Examples](#Examples).

[Schematic Examples](javascript:void(0))

### Monitor a Third-Party Device's Network Connectivity

In this example, Monitoring Proxy is used to check the status of a network-connected TV. A [Ping](ping.htm) component is configured to check the TV's network connectivity every second. If the ping is successful, the status is reported as OK. If the ping fails, a Fault is generated, indicating that the device may be having an issue. The device status is sent to the Core's Status > Inventory list, which is easily viewed locally in Core Manager and remotely in Q-SYS Reflect.

### Monitor Device Status and Send Log Entries

In this example, a Ping component monitors the TV's network connectivity (as with the previous example), and a Block Controller component is configured to control the TV and write log entries to the Event Log. The following Monitoring Proxy control pins are used:

* Log Entry (Input): Receives the log entry text from the script output.
* Severity (Input): Receives the severity text from the script output. See [Controls](#Controls) for valid severity strings.
* Trigger (Input): Receives the trigger signal from the script to submit the log entry to the Event Log.
* Ready (Output): The Ready LED determines if the Monitoring Proxy can receive a log entry. This is fed back into the script as a condition of triggering a log event only when the LED's value is '1' (string is 'true'). See [Controls](#Controls) to understand what determines the Ready state.

**Tip:** See the [Scripting Example](#Scriptin) for details of using a scripting component to monitor and send log event entries for a third-party device.

[Scripting Example](javascript:void(0))

This example shows the details of how a scripting component communicates with Monitoring Proxy for status monitoring and event logging.

### Control Elements

A Text Controller ("Status and Events") includes the following control elements:

#### Text Boxes

* Monitoring Proxy Component Name: Required custom name given to the Monitoring Proxy component to allow for scripted control.
* Device Name: Text applied to the beginning of each Event Log entry statement.
* Status: Selects the Status condition to report in Core Manager and Q-SYS Reflect.
* Status Message: Optional message to report with a Status condition.
* Event Severity: Selects the Severity associated with the Event Log entry.
* Event Log Entry: Message to follow the Device Name for an Event Log entry.

#### Input Controls and Pins (Trigger Buttons)

These pins connect to control components as needed to trigger updates in Core Manager and Q-SYS Reflect.

* Update Status: Updates the device status to the set parameters.
* Send Event: Sends an event to the Event Log with the set parameters.

#### Output Controls and Pins (Status Indicator)

* Monitor Status: This pin connects to the Status Input pin of the Monitoring Proxy component.

**Note:** The device status displayed in Core Manager or Q-SYS Reflect defaults to OK when rebooting the Core or after deploying a design to the Core.

### Status and Events (Text Controller) Script

This is the example script from the Text Controller component's script editor window.

```lua
--Initialize Named Component control---------------------------------------------------  
Monitor = Component.New(Controls["Monitoring Proxy Component Name"].String)  
  
--Intialize Status table---------------------------------------------------------------  
StatusState = { OK = 0, COMPROMISED = 1, FAULT = 2, NOTPRESENT = 3, MISSING = 4, INITIALIZING = 5 }  
  
--Initialize Combo Box selection options-----------------------------------------------  
for i = 1,16 do  
  Controls["Status"][i].Choices = { "OK","COMPROMISED", "FAULT", "NOTPRESENT", "MISSING", "INITIALIZING"}  
  Controls["Event Severity"][i].Choices = { "normal","warning", "error"}  
end  
  
  
--Update the reported status in Core Manager-----------------------------------------------  
function ReportStatus(State, Message)  
  if StatusState[State] == nil and message == nil then  
    Monitor.status.Value = StatusState[CurrentState]  
    Monitor.status.String = CurrentMessage  
  elseif StatusState[State] then  
    CurrentState = State  
    CurrentMessage = Message  
    Monitor.status.Value = StatusState[State]  
    Monitor.status.String = Message  
  end  
end  
  
--Update Monitoring Proxy when the Ready state changes---------------------------------------  
function CheckProxy(bool)  
  print("CheckProxy() has been called")  
  if bool then  
    ReportStatus("OK","")  
  else  
    ReportStatus("INITIALIZING","Proxy not ready")  
  end  
end  
  
--Send Event to Event Log in Core Manager-----------------------------------------------  
function SendEvent(Severity, Entry)  
  if Severity ~= "" and Entry ~= "" then  
    Monitor["severity"].String = Severity  
    Monitor["log.entry"].String = Controls["Device Name"].String.." : "..Entry  
    Monitor.trigger:Trigger()  
    Timer.CallAfter(ReportStatus,0.1)  
  end  
end  
  
--Set the inital state after a reboot/redeploy  
if Monitor.ready.Boolean == true then  
  ReportStatus("OK","")  
end  
  
--Update Status when Update Status pressed---------------------------------------------------  
for i = 1,16 do  
  Controls["Update Status"][i].EventHandler = function ()  
    ReportStatus(Controls["Status"][i].String, Controls["Status Message"][i].String)  
  end  
end    
  
--Send Event to Event Log when pressed-------------------------------------------------------  
for i = 1,16 do  
  Controls["Send Event"][i].EventHandler = function ()  
    SendEvent(Controls["Event Severity"][i].String, Controls["Event Log Entry"][i].String)  
  end  
end    
  
--Check the status of the Monitoring Proxy----------------------------------------------------  
Monitor.ready.EventHandler = function ()  
  CheckProxy(Monitor.ready.Boolean)  
end
```

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### Connection Status

#### Status

This is the complete text string status of the wired, upstream component. It includes at least one of the seven basic statuses, plus any extended details, if applicable.

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### Log Entry

When you press the Trigger button, this is the text string that is placed in the Core's event log under the Message column.

#### Severity

When you press the Trigger button, this is the severity level that is placed in the Core's event log for the event â normal, error, or warning. Note that "default" equates to "Normal" severity. For more information on statuses, see [Status](../Core_Manager/Status.htm).

#### Trigger

Click to submit the Log Entry, including its defined Severity.

#### Ready

The LED glows green when the Monitoring Proxy is ready to receive a log entry. No more than four log entries per second per component are allowed. When this limit is reached, the Ready LED turns off until the next one-second period.

**Tip:** If you are using a script to trigger log events, expose the Ready control pin and wire it to your script to validate that the Monitoring Proxy can accept additional log entries.

### Device Properties

#### Manufacturer

Specify the third-party device manufacturer. This is visible in the Status > Inventory list in Core Manager. For more information, see [Status](../Core_Manager/Status.htm).

#### Model

Specify the model of the third-party device, which is shown in the Status > Inventory list for identification purposes in Core Manager. For more information, see [Status](../Core_Manager/Status.htm).

#### Type

From the drop-down menu, select a hardware category that best fits the third-party device. The Type you choose is shown in the Status > Inventory list for identification. For more information, see [Status](../Core_Manager/Status.htm).

#### Other

If none of the **Type** categories is suitable, select 'Other', and then specify your own category.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Log Entry | (text) | | | Input / Output |
| Manufacturer | (text) | | | Input / Output |
| Model | (text) | | | Input / Output |
| Other | (text) | | | Input / Output |
| Ready | 0  1 | false  true | 0  1 | Input / Output |
| Severity | - | default  error  warning | - | Input / Output |
| Status | 0  1  2  3  4  5 | OK (Green)  Compromised (Orange)  Fault (Red)  Not Present (Gray)  Missing (Red)  Initializing (Blue) | - | Output |
| Trigger | (trigger) | | | Input / Output |
| Type | - | AudioIO  Unknown  Interface  Display  Projector  Amplifier  Camera  Microphone  Power  ControlIO  Speaker  DigitalSignage  MediaPlayer  MediaServer  Network  VideoDistribution  VideoSwitching  Conferencing  CaptureDevice  Presentation  Lighting  HVAC  Shades  Sensors  Calendar  Other | - | Input / Output |
