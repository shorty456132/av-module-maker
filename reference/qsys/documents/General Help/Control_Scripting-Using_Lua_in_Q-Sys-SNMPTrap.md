# SNMPTrap

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/SNMPTrap.htm

# SNMPTrap

Use the SNMPTrap library in Lua to receive trap notifications from an SNMP-enabled device.

**Note:** In the SNMP model, Q-SYS acts as the SNMP *Manager*, while the device you intend to monitor runs an SNMP *Agent* that allows for monitoring.

[SNMPTrap.New](javascript:void(0))

Create a new SNMP trap listener.

### Syntax

SNMPTrap.New("*trap\_name*")

### Arguments

*trap\_name* : String. The name of the trap listener session.

### Example

```lua
snmp_trap = SNMPTrap.New("snmp_trap")
```

[startSession](javascript:void(0))

Begin a trap listening session.

### Syntax

startSession()

### Example

```lua
snmp_trap:startSession()
```

[EventHandler](javascript:void(0))

Assign a Lua callback for successful SNMP events.

### Requests

**RequestID** : Integer. The request ID for bookkeeping purposes.

**OID** : String. The object ID for the response.

**Value** : String. The string representation for the current state of the object ID.

**HostName** : String. The host name for the response.

### Example

```lua
snmp_object.EventHandler = function(response)  
    print(response.OID)  
    print(response.Value)  
end
```

[ErrorHandler](javascript:void(0))

Assign a Lua callback for unsuccessful SNMP events.

### Requests

**Error** : String. The error message for the request.

### Example

```lua
snmp_object.ErrorHandler = function(response)  
    print(response.Error)  
end
```
