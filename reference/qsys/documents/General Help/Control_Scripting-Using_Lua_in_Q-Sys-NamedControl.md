# NamedControl

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/NamedControl.htm

# NamedControl

The methods in NamedControl are used to read or set the values of Named Controls.

|  |  |  |
| --- | --- | --- |
| Methods | | |
| Name | Arguments | Description |
| .SetString | Control name, string | Class static. Sets control with specified Control name to specified string value. If Control name does not exist an error is raised. |
| .GetString | Control name | Class static. Returns string of control with specified Control name. If Control name does not exist an error is raised. |
| .SetPosition | Control name, position, optional ramp time | Class static. Sets control with specified Control name to specified position. The ramp time is optional, and is in seconds. If Control name does not exist an error is raised. |
| .GetPosition | Control name | Class static. Returns position of control with specified Control name. If Control name does not exist an error is raised. |
| .SetValue | Control name, value, optional ramp time | Class static. Sets control with specified Control name to specified value. The ramp time is optional, and is in seconds. If Control name does not exist an error is raised. |
| .GetValue | Control name | Class static. Returns value of control with specified Control name. If Control name does not exist an error is raised. |
| .Trigger | Control name | Class static. Triggers control with specified Control name. If Control name does not exist an error is raised. |

### Example

```lua
NamedControl.SetValue("CustomControlsInteger1", 7, 15)  -- Set value of a named integer control to 7, ramp 15 seconds  
NamedControl.GetString("CustomControlsTextdisplay1")  --Get string value of a control  
NamedControl.Trigger("CustomControlsTrigger1")  --Triggers a controlled trigger button
```
