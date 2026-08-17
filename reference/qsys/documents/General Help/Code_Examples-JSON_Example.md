# JSON Object

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/JSON_Example.htm

# JSON Object

These are examples for using the JSON object in Lua to encode/decode and read and write JSON files.

[Encode/Decode](javascript:void(0))

### Methods

Refer to the [RapidJSON](https://q-syshelp.qsc.com/#Control_Scripting/Using_Lua_in_Q-Sys/RapidJSON.htm) topic in Q-SYS Help for a list of methods and their descriptions.

### Text Controller Setup

Drag in a Text Controller and name it JSON Encode/Decode. Add a Combo Box named **Type**, three Text Boxes named **Input**, **Name** and **Version**, and a Text Indicator named **Output** (see screenshot).

Next, copy the Example Code to the Text Controller.

[JSON Encode/Decode Example Code](javascript:void(0))

```lua
-- Include  
rapidjson = require("rapidjson")  -- include the rapidjson library  
  
  
-- Aliases  
Name = Controls.Name  
Version = Controls.Version  
Type = Controls.Type  
Input = Controls.Input  
Output = Controls.Output  
  
  
-- Constants  
JSONChoices = {"Encode","Decode"}  -- combobox choices  
  
  
-- Functions  
function ShowJSONVersion()  -- gets and prints JSON version to text boxes  
  Name.String = rapidjson._NAME  -- get rapidjson name  
  Version.String = rapidjson._VERSION  -- get rapidjson version  
end  
  
function SetJSONChoices()  -- set the combobox choices  
  Type.Choices = JSONChoices  
  if Type.String == "" then Type.String = "Select Encode or Decode" end  
end  
  
function ProcessData()  -- process the string in the Input textbox  
  if Input.String ~= "" and Type.String ~= "Select Encode or Decode" then  
    if Type.String == "Encode" then   
      Output.String = rapidjson.encode(Input.String)  -- encode the string in the Input textbox   
    elseif Type.String == "Decode" then   
      local data,err = rapidjson.decode(Input.String)  -- decode the string in the Input textbox  
      Output.String = data==nil and err or tostring(data)  -- prints data if valid or err if error  
    end   
  end  
end  
  
function Initialization()  -- function called at the start of runtime  
  ShowJSONVersion()  
  SetJSONChoices()  
  ProcessData()  
end  
  
  
-- EventHandlers  
Type.EventHandler = ProcessData  -- calls process data when Type EventHandler is called  
Input.EventHandler = ProcessData  -- calls process data when Input EventHandler is called  
  
  
-- Start at runtime  
Initialization()  -- calls Initialization at the start of runtime
```

### Using the Example

In the **Type** Combo Box, select âEncodeâ or âDecodeâ. Enter the string you would like to encode or decode into the **Input** Text Box and the result will populate in the **Output** box. The **Name** and **Version** Text Boxes will populate at the start of the script.

[Read/Write](javascript:void(0))

### Text Controller Setup

Drag in a Text Controller and name it JSON Read/Write Files. Add two Text Boxes named **Input** and **Name**, a Combo Box named **Location**, and a Text Indicator named **Output** (see screenshot).

Next, copy the Example Code to the Text Controller.

[JSON Read/Write Example Code](javascript:void(0))

```lua
-- Include  
rapidjson = require("rapidjson")  -- include the rapidjson library  
  
  
-- Aliases  
Name = Controls.Name  
Location = Controls.Location  
Input = Controls.Input  
Output = Controls.Output  
  
  
-- Constants  
Locations = {"media", "design"}  -- location choices  
Location.Choices = Locations  -- set location choices to the Location combobox  
TestJSON = "{\"test\":test,\"Foo\":bar}"  -- test JSON string that can be used  
Warning = "Cannot write JSON file in emulation mode"  -- warning used when in emulation  
  
  
-- Functions  
function WriteJSON(location)  -- write JSON file  
  print("write json")  
  local location = Location.String  
  local name = Name.String  
  rapidjson.dump(Input.String, location.."/"..name)  -- write JSON file to the location file path  
  Timer.CallAfter(function() ReadJSON(location) end,.5)  -- call the ReadJSON function after .5 seconds and pass location  
end  
  
function ReadJSON(location)  -- read JSON file  
  print("read json")  
  local name = Name.String  
  Output.String = tostring(rapidjson.load(location.."/"..name))  -- read JSON file and print it in the Output textbox  
end  
  
function Emulation(state)  -- function to set controls disabled and throw warnings if in emulation modee  
  Input.IsDisabled = state  --  IsDisabled state driven by emulation state  
  Location.IsDisabled = state  --  IsDisabled state driven by emulation state  
  if state then Input.String, Location.String = Warning, Warning end  -- throw warnings if in emulation mode  
end  
  
function Initialization()  -- function called at the start of runtime  
  if Location.String == "" or Location.String == Warning then Location.String = "media" end  -- set Location string if blank  
  if System.IsEmulating then -- conditional that calls Emulation() passing the emulation state and calls WriteJSON if not emulating  
    Emulation(true)  
  else  
    Emulation(false)  
    WriteJSON()  
  end  
end  
  
  
-- EventHandlers  
Input.EventHandler = WriteJSON  
Location.EventHandler = WriteJSON  
  
-- Start at runtime  
Initialization()  -- calls Initialization at the start of runtime
```

### Using the Example

In the **Location** Combo Box, select âmediaâ or âdesignâ. Enter the name of the file in the **Name** Text Box and the file contents in the **Input** Text Box. The data from **Input** will be saved as **Name** in the **Location** folder on the Q-SYS Core processor.

**Note:** This file example does not work in Emulation mode.
