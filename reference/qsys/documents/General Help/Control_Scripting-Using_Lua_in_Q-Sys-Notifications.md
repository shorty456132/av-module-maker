# Notifications

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Notifications.htm

# Notifications

Use the following methods to subscribe to a notification, publish a notification with specified data, and unsubscribe from a notification. This allows scripts running within the same Core to communicate with each other using control wiring or [Component](Component.htm).

### Methods

| Name | Attribute/Arguments | Comment |
| --- | --- | --- |
| noteid = Notifications.Subscribe() | name, function | Subscribe to a notification with a given name.   * **noteid**: The token to use when unsubscribing from a notification. * **name**: The name of the notification. * **function**: The callback to call when the named notification is triggered. The signature is function( name, data ). |
| Notifications.Publish() | name, data | Publish a named notification with given data. The data can be either a Lua table or a string.  **Note:** You cannot call the Notifications.Publish() method inside a Notifications.Subscribe() callback. This will raise a Lua error. |
| Notifications.Unsubscribe() | noteid | Unsubscribe from a notification with the specified noteid. |

[Example](javascript:void(0))

In this example, two [Scriptable Controls](../../Schematic_Library/scriptable_controls.htm) components are configured - Thing 1 and Thing 2. Control wiring connects exposed Code control pins. Thing 1 is subscribed to receive notifications from Thing 2 and vice versa. When the Send button is pushed on one component, the other receives the Send String text and the Received LED illuminates. If the Unsubscribe button is pushed, notifications are no longer received from the other component.

See the table below for the complete Lua code example from each Scriptable Controls component. All Notifications methods are used in this example.

**Note:** In Q-SYS Designer version 7.2 and higher, the [Text Controller](../../Schematic_Library/device_controller_script.htm) component replaces Scriptable Controls.

| Thing 1 | Thing 2 |
| --- | --- |
| ```lua send = Controls.Send txstr = Controls["Send String"] txid = Controls["Notify ID"] rxled = Controls.Received rxstr = Controls["Receive String"] rxid = Controls["Receive ID"] sub = Controls.Subscribed unsub = Controls.Unsubscribe  local noteid  function RXHandler(name,data)   print(string.format("Notification Name: \"%s\"\t Data: \"%s\"",name,data))   rxstr.String = data   rxled.Boolean = true   Timer.CallAfter(function() rxled.Boolean = false end, 1) end  function Subscribe()   local id = rxid.String   if #id>0 then     noteid = Notifications.Subscribe( id, RXHandler )     if noteid then       sub.Boolean = true     end   end end rxid.EventHandler = Subscribe Subscribe()  send.EventHandler = function()   local tx = txstr.String   if #tx>0 and #txid.String>0 then     Notifications.Publish( txid.String, tx )   end end  unsub.EventHandler = function()   if noteid~=nil then     Notifications.Unsubscribe(noteid)     sub.Boolean = false     rxstr.String = ""     rxid.String = ""   end end ``` | ```lua send = Controls.Send txstr = Controls["Send String"] txid = Controls["Notify ID"] rxled = Controls.Received rxstr = Controls["Receive String"] rxid = Controls["Receive ID"] sub = Controls.Subscribed unsub = Controls.Unsubscribe  local noteid  function RXHandler(name,data)   print(string.format("Notification Name: \"%s\"\t Data: \"%s\"",name,data))   rxstr.String = data   rxled.Boolean = true   Timer.CallAfter(function() rxled.Boolean = false end, 1) end  function Subscribe()   local id = rxid.String   if #id>0 then     noteid = Notifications.Subscribe( id, RXHandler )     if noteid then       sub.Boolean = true     end   end end rxid.EventHandler = Subscribe Subscribe()  send.EventHandler = function()   local tx = txstr.String   if #tx>0 and #txid.String>0 then     Notifications.Publish( txid.String, tx )   end end  unsub.EventHandler = function()   if noteid~=nil then     Notifications.Unsubscribe(noteid)     sub.Boolean = false     rxstr.String = ""     rxid.String = ""   end end ``` |
