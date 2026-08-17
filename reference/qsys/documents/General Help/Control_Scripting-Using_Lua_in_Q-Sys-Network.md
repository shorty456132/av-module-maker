# Network

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Network.htm

# Network

Use the Network commands to return the full host name and IP address of a specified host, or obtain a table of network interface names and their IP addresses.

[Network.GetHostByName](javascript:void(0))

Return an object with the name (.name) and addresses (.addresses) of a specified host, where .addresses is a table of strings.

### Syntax

Network.GetHostByName('*host*')

### Arguments

*host* : The host name for which to obtain network information.

### Example

```lua
local ghbn = Network.GetHostByName('localhost')  
print("GetHostByName("..ghbn.name..")")  
for _, item in ipairs(ghbn.addresses) do  
  print("-"..item)  
end
```

#### Debug Output

```lua
GetHostByName(US-MYCOMPUTER-123.mydomain.com)
-127.0.0.1
```

[Network.Interfaces](javascript:void(0))

Return a table of network interface names (.Interface) and the IP address (.Address), MAC address (.MACAddress), broadcast address (.BroadcastAddress), gateway (.Gateway), and netmask (.Netmask) for each.

### Syntax

Network.Interfaces()

### Example

```lua
local ni = Network.Interfaces()  
for _, item in ipairs(ni) do  
  print("-"..item.Interface, " = \n IP ", item.Address,"\n MAC",item.MACAddress,"\n Broadcast",  
  item.BroadcastAddress,"\n Gateway",item.Gateway,"\n Netmask",item.Netmask)  
end
```

#### Debug Output

```lua
-LAN A	 = 
 IP 	192.0.2.50	
 MAC	00:01:99:98:A1:A9	
 Broadcast	192.0.3.200	
 Gateway	192.0.3.199	
 Netmask	255.255.255.0
```
