# System

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/System.htm

# System

Use the System functions to return Q-SYS environment information.

[System.BuildVersion](javascript:void(0))

Returns the build version number of Q-SYS environment.

### Syntax

System.BuildVersion

### Example

If the current Q-SYS environment version is 7.1.0:

```lua
print (System.BuildVersion)
```

#### Debug Output

```lua
0
```

[System.LockingId](javascript:void(0))

Returns the Q-SYS Core's Locking ID, which is used for Q-SYS feature license activation. For more information, see [Licensing](../../Core_Manager/Core_Management/Licensing.htm).

### Syntax

System.LockingId

### Example

```lua
print (System.LockingId)
```

#### Debug Output

```lua
*1AB2CDEFG3HI4J5
```

[System.IsEmulating](javascript:void(0))

Returns a Boolean indicating whether the design is emulating or running on a Core.

### Syntax

System.IsEmulating

### Example

```lua
if System.IsEmulating  
then print("System is emulating.")  
end  
  
print(System.IsEmulating)
```

#### Debug Output

```lua
System is emulating.
true
```

[System.MajorVersion](javascript:void(0))

Returns the major version number of Q-SYS environment.

### Syntax

System.MajorVersion

### Example

If the current Q-SYS environment version is 7.1.0:

```lua
print (System.MajorVersion)
```

#### Debug Output

```lua
7
```

[System.MinorVersion](javascript:void(0))

Returns the minor version number of Q-SYS environment.

### Syntax

System.MinorVersion

### Example

If the current Q-SYS environment version is 7.1.0:

```lua
print (System.MinorVersion)
```

#### Debug Output

```lua
1
```

[System.Version](javascript:void(0))

Returns the complete version number of Q-SYS environment.

### Syntax

System.Version

### Example

If the current Q-SYS environment version is 7.1.0:

```lua
print (System.Version)
```

#### Debug Output

```lua
7.1.0
```
