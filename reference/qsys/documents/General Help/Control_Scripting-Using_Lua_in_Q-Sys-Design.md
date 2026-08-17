# Design

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Design.htm

# Design

Use the Design functions to return design status and inventory information.

[Design.GetStatus](javascript:void(0))

Return a status table containing design information.

### Syntax

Design.GetStatus()

### Arguments

None

### Returns

**Note:** The returns are contained within a table.

`.DesignName` : The name of the design file.

`.Platform` : Emulator | *Core model*

`.IsRedundant` : true | false

`.DesignCode` : A unique code assigned to the design.

### Example

```lua
for k,v in pairs(Design.GetStatus()) do  
  print("Design."..k.." = "..tostring(v))  
end
```

#### Debug Output: Design Running in Emulation Mode

```lua
Design.DesignName = My Wonderful Design
Design.Platform = Emulator
Design.IsRedundant = false
Design.DesignCode = UKDk4bcbiXXS
```

#### Debug Output: Design Running on Q-SYS Core

```lua
Design.IsRedundant = false
Design.Platform = Core 110f
Design.DesignCode = uQFstX85kuLD
Design.DesignName = My Wonderful Design
```

[Design.GetInventory](javascript:void(0))

Return a table of design inventory information, and the details for each inventory item.

### Syntax

Design.GetInventory()

### Arguments

None.

### Returns

`.Type` : The category of the inventory item.

`.Name` : The name of the inventory item.

`.Location` : The location of the inventory item, as specified in the design file.

`.Model` : The model of the inventory item.

`.Status.Message` : The text status of the inventory item.

`.Status.Code` : The numeric status of the inventory item.

### Example

```lua
print("Design.GetInventory() includes the following data for each Inventory item:")  
for k,v in pairs(Design.GetInventory()) do  
  for a,b in pairs(v) do  
    print("\tDesign.GetInventory()."..a)  
  end  
  break  
end  
print(" ")  
for k,v in pairs(Design.GetInventory()) do  
  print("Inventory: Type:"..v.Type,"Name:"..v.Name,"Loc:"..v.Location,"Model:"..v.Model)  
  print("\t"..v.Name.." Status Msg: \t"..v.Status.Message,"Status Code: "..math.floor(v.Status.Code))  
end
```

#### Debug Output

```lua
Design.GetInventory() includes the following data for each Inventory item:
	Design.GetInventory().Model
	Design.GetInventory().Location
	Design.GetInventory().Type
	Design.GetInventory().Status
	Design.GetInventory().Name
 
Inventory: Type:Processor	Name:MyCore110f	Loc:Rack A3	Model:Core110f
	MyCore110f Status Msg: 	Fault - Audio Clock Set Events	Status Code: 2
Inventory: Type:Streaming I/O	Name:AES67-RX-1	Loc:Default Location	Model:AES67 Receiver
	AES67-RX-1 Status Msg: 	Fault - LAN A: PTP Grandmaster Mismatch : LAN B: No Network Link	Status Code: 2
```

**Note:** If the device is a Core running Q-SYS Designer 9.4 or later, the âTypeâ will display âProcessorâ as depicted in the example. However, if the device is a Core that is running Q-SYS Designer 9.3 or earlier, the type will display âCoreâ.
