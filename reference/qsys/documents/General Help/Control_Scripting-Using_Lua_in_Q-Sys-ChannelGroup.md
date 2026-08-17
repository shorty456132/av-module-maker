# ChannelGroup

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/ChannelGroup.htm

# ChannelGroup

Used when a Control Script is located inside a Channel Group.  The .Index property is used to determine which Channel Group is currently selected.

| Properties | | |
| --- | --- | --- |
| Name | Attributes | Comment |
| .Index | Read Only | Integer value, 1-n, indicates which channel of the Channel Group, 0 indicated not in Channel Group.  If multiple groups are selected, the index of the first group is returned. |

### Example

|  |
| --- |
| print("This script is running within Channel Group number: "..ChannelGroup.Index) |
