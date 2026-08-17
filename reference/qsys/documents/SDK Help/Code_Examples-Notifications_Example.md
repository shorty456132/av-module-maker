# Notifications

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Notifications_Example.htm

# Notifications

These are examples for using the Notifications object in Lua. Notifications are a mechanism in which scripts within the same design can communicate with each other and sync control changes without having to wire the individual control pins. [Documentation of the Notifications Class is found here](https://q-syshelp.qsc.com/#Control_Scripting/Using_Lua_in_Q-Sys/Notifications.htm).

[Text Controller Setup](javascript:void(0))

### Controls

Open an instance of Q-SYS Designer Software and drag in a Text Controller component. Add the following controls (see screenshot):

* Subscribe: toggle button
* Send: trigger button
* SendID: text box
* SendString: text box
* Incoming: LED
* ReceiveID: text box
* ReceiveString: text box

Next, copy the Example Code to the Text Controller and duplicate it so you have two identical components and scripts.

[Notifications Example Code](javascript:void(0))

```lua
-- Control Aliases  
subscribed     = Controls.Subscribe  
send           = Controls.Send  
transmitId     = Controls.SendID  
transmitString = Controls.SendString  
incoming       = Controls.Incoming  
receiveId      = Controls.ReceiveID  
receiveString  = Controls.ReceiveString  
  
-- Variables  
noteid         = ""  
  
-- Functions  
-- Send a notification at the specified transmit id  
function Send()  
  local transmit = transmitString.String  
  if #transmit > 0 then  
    Notifications.Publish(transmitId.String,transmit)  
  end  
end  
  
-- This function is called whenever a Notification that matches the id is sent from another script  
function Receive(id,data)  
  receiveString.String = data  
  -- Flash the incoming LED for 1 second  
  incoming.Boolean = true  
  Timer.CallAfter(  
    function()  
      incoming.Boolean = false  
    end,  
    1)  
end  
  
-- This function subscribes to notifications for the specified receive id  
function Subscribe()  
  local id = receiveId.String  
  local state = subscribed.Boolean  
  if state then -- subscribe when the control is toggled high  
    if #id > 0 then  
      noteid = Notifications.Subscribe(id,Receive)  
    end  
  else          -- unsubscribe when toggled low  
    if noteid ~= nil then  
      Notifications.Unsubscribe(noteid)  
      receiveString.String = ""  
    end  
  end  
end  
  
-- EventHandlers  
send.EventHandler       = Send  
receiveId.EventHandler  = Subscribe  
subscribed.EventHandler = Subscribe  
  
-- Initialization  
function Initialization()  
  if #transmitId.String == 0 then transmitId.String = "Enter ID" end  
  Subscribe()  
end  
  
Initialization()
```

[Using the Example](javascript:void(0))

### Running or Emulating the Design

Push the Design to a Core and Run or simply Emulate. In one Text Controller's SendID, enter ID 1. In the other, enter ID 2. Use the SendID values to enter the ReceiveID, and then enter unique strings for the SendString control in each component. Now, toggle the Subscribe controls high and press Send. See the screenshot for control setup reference.
