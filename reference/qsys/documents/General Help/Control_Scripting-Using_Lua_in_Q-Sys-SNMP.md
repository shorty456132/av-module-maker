# SNMP

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/SNMP.htm

# SNMP

Use the SNMP library in Lua to monitor OIDs obtained from an SNMP-enabled device's MIB file.

**Note:** In the SNMP model, Q-SYS acts as the SNMP *Manager*, while the device you intend to monitor runs an SNMP *Agent* that allows for monitoring.

[SNMPSession.New](javascript:void(0))

Create a new SNMP session.

**Note:** Do not scope your SNMP locally. This causes the object to be managed by Lua's garbage collector, which may lead to its removal even if it is still in use.

### Syntax

SNMPSession.New(*type*)

### Arguments

*type*

`SNMPSessionType.V2c` : Instantiate an SNMP v2 session.

`SNMPSessionType.V3` : Instantiate an SNMP v3 session.

### Example

```lua
snmp_session = SNMPSession.New(SNMP.SessionType.v3)
```

[setHostName](javascript:void(0))

Specify the host to which to connect.

### Syntax

setHostName("*hostname*")

### Arguments

*hostname* : String. The target host name.

### Example

```lua
snmp_session:setHostName("mydevice")
```

[setAuthType](javascript:void(0))

For SNMP v3 only, set the authorization type for the session.

### Syntax

setAuthType(*type*)

### Arguments

*type*

`SNMP.AuthType.NoAuth` : No authorization type and no privacy type.

`SNMP.AuthType.AuthNoPriv` : Authorization with no privacy.

`SNMP.AuthType.AuthPriv` : Both authorization and privacy.

### Example

```lua
snmp_session:setAuthType(SNMP.AuthType.AuthNoPriv)
```

[setAuthProt](javascript:void(0))

For SNMP v3 only, set the authorization protocol for the session.

### Syntax

setAuthProt(*type*)

### Arguments

*type*

`SNMP.AuthProtocol.NoAuth` : Disable the authorization protocol.

`SNMP.AuthProtocol.MD5` : Enable the MD5 authorization protocol.

`SNMP.AuthProtocol.SHA` : Enable the SHA authorization protocol.

### Example

```lua
snmp_session:setAuthProt(SNMP.AuthProtocol.MD5)
```

[setPrivProt](javascript:void(0))

For SNMP v3 only, set the privacy protocol for the session.

### Syntax

setPrivProt(*type*)

### Arguments

*type*

`SNMP.PrivProtocol.NoPriv` : Disable the privacy protocol.

`SNMP.PrivProtocol.AES` : Enable the AES privacy protocol.

`SNMP.PrivProtocol.DES` : Enable the DES privacy protocol.

### Example

```lua
snmp_session:setPrivProt(SNMP.PrivProtocol.DES)
```

[setUserName](javascript:void(0))

For SNMP v3 only, set the user name for the session.

### Syntax

setUserName("*username*")

### Arguments

*username* : String. The user name for the session.

### Example

```lua
snmp_session:setUserName("MD5User")
```

[setPassPhrase](javascript:void(0))

For SNMP v3 only, set the authorization pass phrase for the session.

### Syntax

setPassPhrase("*passphrase*")

### Arguments

*passphrase* : String. The pass phrase for the corresponding user name.

### Example

```lua
snmp_session:setPassPhrase("My Demo Password")
```

[setPrivPassPhrase](javascript:void(0))

For SNMP v3 only, set the privacy pass phrase for the session.

### Syntax

setPrivPassPhrase("*privpass*")

### Arguments

*privpass* : String. The privacy pass phrase for the session.

### Example

```lua
snmp_session:setPrivPassPhrase("password")
```

[setCommunity](javascript:void(0))

For SNMP v2 sessions only, set the community name for the session.

### Syntax

setCommunity("*community*")

### Arguments

*community* : String. The community name for the session.

### Example

```lua
snmp_session:setCommunity("demopublic")
```

[startSession](javascript:void(0))

Initiate the connection to the corresponding session.

### Syntax

startSession()

### Example

```lua
snmp_session:startSession()
```

[getRequest](javascript:void(0))

Request an object ID (OID) and pass the response to a Lua callback.

### Syntax

getRequest("*oid*", *callback*)

### Arguments

*oid* : String. The object ID to request.

*callback* : The Lua callback to which to pass the response.

### Example

```lua
function myCallback(dataout)  
      for k,v in pairs(dataout) do  
        print(k,v)  
      end  
  end  
  
  snmp_session:getRequest(".1.3.6.1.2.1.1.3.0", myCallback)
```

[setRequest](javascript:void(0))

Set a new value for a specified OID.

### Syntax

setRequest("*oid*", "*new\_value*", *type*, *callback*)

### Arguments

*oid* : String. The object ID to set in the request.

*new\_value* : String. The new value to which to set the specified object ID.

*type*

`SNMP.SNMPDataType.unknown`

`SNMP.SNMPDataType.integer32`

`SNMP.SNMPDataType.unsigned32`

`SNMP.SNMPDataType.unsigned_integer32`

`SNMP.SNMPDataType.timeticks`

`SNMP.SNMPDataType.ip_address`

`SNMP.SNMPDataType.object_id`

`SNMP.SNMPDataType.octet_string`

`SNMP.SNMPDataType.hex`

`SNMP.SNMPDataType.decimal`

`SNMP.SNMPDataType.bit_string`

`SNMP.SNMPDataType.integer64`

`SNMP.SNMPDataType.unsigned64`

`SNMP.SNMPDataType.float32`

`SNMP.SNMPDataType.double64`

*callback* : The Lua callback to which to pass the response.

### Example

```lua
function myCallback(dataout)  
      for k,v in pairs(dataout) do  
        print(k,v)  
      end  
  end  
  
  snmp_session:setRequest(".1.3.6.1.2.1.1.5.0", "new_switch_name", SNMP.SNMPDataType.octet_string, myCallback)
```

[EventHandler](javascript:void(0))

Assign the Lua callback for successful SNMP events.

### Responses

**RequestID** : Integer. The request ID for bookkeeping purposes.

**OID** : String. The object ID for the response.

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

Assign the Lua callback for unsuccessful SNMP events.

### Responses

**Error**: String. The error message for the request.

Values that may be returned:

* Time Out
* Send Failed
* Sec Error
* SNMP Error
* No Such Instance
* No Such Object

### Example

```lua
snmp_object.ErrorHandler = function(response)  
    print(response.Error)  
end
```

[Example Using SNMP V3](javascript:void(0))

The following example requests a set of OIDâs from a remote Core. One OID is fetched every 5 seconds.

**Note:** For this example to work, the Core being connecting needs to be configured so SNMP V3 is enabled (the default is disabled).

```lua
QueryList = {  
  '.1.3.6.1.4.1.1536.1.1.2.1.0',      
  '.1.3.6.1.4.1.1536.1.1.2.2.0',     
  '.1.3.6.1.4.1.1536.1.1.2.3.0',     
      
  '.1.3.6.1.4.1.1536.1.2.2.1.1.0',    
     
  '1.3.6.1.4.1.1536.1.2.2.2.1.1.1',     
  '1.3.6.1.4.1.1536.1.2.2.2.1.1.2',     
  '1.3.6.1.4.1.1536.1.2.2.2.1.1.3',     
  '1.3.6.1.4.1.1536.1.2.2.2.1.1.4',  
  '1.3.6.1.4.1.1536.1.2.2.2.1.1.5',     
  '1.3.6.1.4.1.1536.1.2.2.2.1.1.6',  
  '1.3.6.1.4.1.1536.1.2.2.2.1.1.7',     
    
  '1.3.6.1.4.1.1536.1.2.2.3.1.1.1',  
  '1.3.6.1.4.1.1536.1.2.2.3.1.1.2',     
  '1.3.6.1.4.1.1536.1.2.2.3.1.1.3',  
  '1.3.6.1.4.1.1536.1.2.2.3.1.1.4',     
  '1.3.6.1.4.1.1536.1.2.2.3.1.1.5',  
}  
listPtr = 1  
  
snmp_session = SNMPSession.New(SNMP.SessionType.v3) -- Create a new SNMP session.  
snmp_session:setHostName('192.168.1.100') -- Type in the Host Name  
snmp_session:setAuthType(SNMP.AuthType.AuthNo)  
snmp_session:setAuthProt(SNMP.AuthProtocol.NoAuth)  
snmp_session:setPrivProt(SNMP.PrivProtocol.NoAuth)  
snmp_session:setUserName('defaultuser')  
snmp_session:setPassPhrase('')   
snmp_session:setPrivPassPhrase('')  
  
snmp_session.EventHandler = function(response)  
  print("OID Start")  
  for k,v in pairs(response) do  
    print(k,v)  
  end  
  print("OID End")  
end  
  
snmp_session.ErrorHandler = function(response)  
  print("Err Start")  
  for k,v in pairs(response) do  
    print(k,v)  
  end  
  print("Err End")  
end  
  
snmp_session:startSession()  
  
function myCallback(dataout)  
  print("Data Start")  
  for k,v in pairs(dataout) do  
    print(k,v)  
  end  
  print("Data End")  
end  
  
function requestSNMP()  
  print("Send",listPtr,QueryList[listPtr])  
  snmp_session:getRequest(QueryList[listPtr], myCallback)  
  if (listPtr == #QueryList) then  
    listPtr = 1   
  else   
    lisPtr = listPtr + 1  
  end  
end  
  
  
OIDpoll_timer = Timer.New()  
OIDpoll_timer.EventHandler = requestSNMP  
OIDpoll_timer:Start(5)
```
