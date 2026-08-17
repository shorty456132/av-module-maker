# Ping

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Ping.htm

# Ping

Use the Ping library in Lua to check whether a device is reachable on the network.

**Note:** The Lua Ping library requires that you run Q-SYS Designer as administrator ("Run as administrator" option in Windows) when emulating your design. If you see a non-terminating "Socket failed to open" error message in the debug window, re-launch Designer as administrator.

[Ping.New](javascript:void(0))

Create a new ping object.

### Syntax

Ping.New("*target\_host*")

### Arguments

*target\_host* : The hostname to ping.

### Example

```lua
ping_object = Ping.New("www.qsys.com")
```

[start](javascript:void(0))

Begin the ping session.

### Syntax

start(*single\_shot*)

### Arguments

*single\_shot* : Bool. Set to **true** if you want only a single ping attempt.

### Example

```lua
ping_object:start(false)
```

[stop](javascript:void(0))

Stop the ping session.

### Syntax

stop()

### Example

```lua
ping_object:stop()
```

[setTimeoutInterval](javascript:void(0))

Set the timeout for waiting for a ping response.

### Syntax

setTimeoutInterval(*interval*)

### Arguments

*interval* : Double. The timeout duration, in seconds.

### Example

```lua
ping_object:setTimeoutInterval(10.0)
```

[setPingInterval](javascript:void(0))

Set the interval for retrying after a ping request.

### Syntax

setPingInterval(*interval*)

### Arguments

*interval* : Double. The interval duration, in seconds.

### Example

```lua
ping_object:setPingInterval(10.0)
```

[EventHandler](javascript:void(0))

Assign a Lua callback for successful ping events.

### Responses

**ElapsedTime** : Long. The amount of time for the ping to occur, in microseconds.

**HostName** : String. The hostname that was pinged.

### Example

```lua
ping_object.EventHandler = function(response)  
    print(response.HostName)  
    print(response.ElapsedTime)  
end
```

[ErrorHandler](javascript:void(0))

Assign a Lua callback for unsuccessful ping events.

### Responses

**Error** : String. The description of the error.

**HostName** : String. The hostname that was pinged.

### Example

```lua
ping_object.ErrorHandler = function(response)  
    print(response.HostName)  
    print(response.Error)  
end
```

[Examples](javascript:void(0))

[Example 1: Successful Ping](javascript:void(0))

In this simple example, a ping request is sent to a live host every 5 seconds until the script is stopped. The response includes the host name that was pinged, as well as the amount of time for the ping to occur (in microseconds).

```lua
myping = Ping.New("www.qsys.com")  
myping:start(false)  
myping:setPingInterval(5.0)  
myping.EventHandler = function(response)  
  print(response.HostName)  
  print(response.ElapsedTime)  
end  
myping.ErrorHandler = function(response)  
  print(response.HostName)  
  print(response.Error)  
end
```

#### Debug Output

```lua
2020-03-24T23:32:08.679	Starting Script
2020-03-24T23:32:08.781	www.qsys.com
2020-03-24T23:32:08.781	25
2020-03-24T23:32:13.892	www.qsys.com
2020-03-24T23:32:13.892	27
2020-03-24T23:32:18.993	www.qsys.com
2020-03-24T23:32:18.994	25
2020-03-24T23:32:24.089	www.qsys.com
2020-03-24T23:32:24.089	23
2020-03-24T23:32:29.184	www.qsys.com
2020-03-24T23:32:29.184	23
2020-03-24T23:32:34.280	www.qsys.com
2020-03-24T23:32:34.280	23
2020-03-24T23:32:39.377	www.qsys.com
2020-03-24T23:32:39.377	24
```

[Example 2: Unsuccessful Ping (Single attempt)](javascript:void(0))

In this example, the `start()` function is set to 'true', meaning that the ping request only runs a single time. The request is made to a bad host name, so the response includes the returned error.

```lua
myping = Ping.New("www.qsc.c")  
myping:start(true)  
myping:setPingInterval(5.0)  
myping.EventHandler = function(response)  
  print(response.HostName)  
  print(response.ElapsedTime)  
end  
myping.ErrorHandler = function(response)  
  print(response.HostName)  
  print(response.Error)  
end
```

#### Debug Output

```lua
2020-03-24T23:22:29.895	Starting Script
2020-03-24T23:22:29.897	www.qsc.c
2020-03-24T23:22:29.897	Send echo failed.
```
