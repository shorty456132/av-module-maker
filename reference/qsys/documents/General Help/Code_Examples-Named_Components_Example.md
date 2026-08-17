# Named Components

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Named_Components_Example.htm

# Named Components

These are examples for using the Named Components object in Lua. The Component object allows access to Named Components in the design. [Documentation of the Component object is found here](https://q-syshelp.qsc.com/#Control_Scripting/Using_Lua_in_Q-Sys/Component.htm).

[Design Setup](javascript:void(0))

### Controls

Open an instance of Q-SYS Designer Software and drag in a Gain component and a Control Script component.

On the Control Script component, set the input pin and output pin properties both to 0.

Make the Gain component a Named Component by giving its block a custom name, "Main Gain". Simply select the Gain component and type "Main Gain", and then press Enter to complete. The name has been applied correctly if the text in the box is italicized (see screenshot).

Next, add the following code to the control script.

[Named Components Example Code](javascript:void(0))

```lua
-- First, we set the component to a variable  
mixer = Component.New("Main Gain")  
  
-- Step through all of the controls and their names  
-- Add an event handler to each one so that whenever a control changes, it prints the controls name and its current value  
for k,v in pairs(mixer) do  
  v.EventHandler = function(ctl)  
    print(k,ctl.Value)  
  end  
end  
  
-- We can also just get all of the controls at once  
ctrls = Component.GetControls("Main Gain")  
  
-- The values in "ctrls" will be returned as a table  
for k,v in pairs(ctrls) do  
  print("=============================================================")  
  --print out each entry in the table.  
  print(k,v)  
  
  -- You can be more specific by indexing to the exact property you want. This prints the controls name  
  print(v.Name)  
  
  for l,m in pairs(v) do  
    -- This will print out all the metadata of each control  
    print(l,m)  
  end  
end
```

[Using the Example](javascript:void(0))

### Running or Emulating the Design

Push the design to a Core and Run or simply Emulate. When initially run, the debug window for the code will display the data from the Named Component. Changing a value of any of the controls in the Named Component will cause the code to print out what control was changed and what its new value is.
