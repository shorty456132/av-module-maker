# Snapshot

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Snapshot.htm

# Snapshot

Use the Snapshot methods to view, load, and save snapshots in the running design.

[Snapshot.GetNames()](javascript:void(0))

Returns a table of snapshots in the design.

### Syntax

Snapshot.GetNames()

### Arguments

None

[Snapshot.Load()](javascript:void(0))

Loads a snapshot with the provided name and bank with an optional ramp time.

### Syntax

Snapshot.Load(*'name'*, *bank*, [*ramp*])

### Arguments

*name* : String. The name of the snapshot bank, in quotes, from which to load the snapshot - for example, 'MySpecialBank'.

*bank* : Integer that identifies a snapshot within a snapshot bank - for example, 7. The range is 1 to the number of snapshots in the bank, inclusive.

*ramp* : Optional. Double. Ramp time, in seconds, when loading the snapshot - for example, 8.5.

[Snapshot.Save()](javascript:void(0))

Saves a snapshot with a provided name and bank.

### Syntax

Snapshot.Save(*'name'*, *bank*)

### Arguments

name : String. The name of the snapshot bank to which to save the snapshot - for example, 'MyVerySpecialBank'.

bank : Integer. Identifies a snapshot within a snapshot bank - for example, 4. The range is 1 to the number of snapshots in the bank, inclusive.
