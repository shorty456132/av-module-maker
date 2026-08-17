# Log

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Log.htm

# Log

Use the Log object to write messages and errors to the Q-SYS Core processor's system log file.

[Log.Message](javascript:void(0))

Write a log message to the Core's log file.

### Syntax

Log.Message("Your message here")

### Example

```lua
Log.Message("The user pressed the button")
```

[Log.Error](javascript:void(0))

Write an error message to the Core's log file.

### Syntax

Log.Error("Error description here")

### Example

```lua
Log.Error("The user pressed an invalid page code")
```
