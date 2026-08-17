# Crypto Object

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Crypto_Example.htm

# Crypto Object

These are code examples for using the Crypto object to encode or decode Base64, MD5, and CRC16 compute and to create a hash with or without a key using MD5, SHA1, SHA256 or SHA512.

[Base64](javascript:void(0))

### Text Controller Setup

Drag in a Text Controller and name it Crypto B64. Add a Combo Box named **Options**, two Text Boxes named **Input** and **Output**, and a Toggle button named **Padding** (see screenshot).

Next, copy the Example Code to the Text Controller.

[Base64 Example Code](javascript:void(0))

```lua
-- Aliases  
Options = Controls.Options  
Input = Controls.Input  
Output = Controls.Output  
Padding = Controls.Padding  
  
  
-- Constants  
Options.Choices = {"Encode","Decode"}  -- choices for the type of compute  
  
  
-- Functions  
function OptionsEntered()  -- returns true when Option is selected and there is data in the Input field  
  return Options.String ~= "" and Input.String ~= ""  
end  
  
function ProcessData()  -- function to process the text in the Input field  
  if OptionsEntered() then   
    if Options.String == "Encode" then   
      Output.String = Crypto.Base64Encode(Input.String, Padding.Boolean)  -- output the Base64 result to the Output field  
    else   
      Output.String = Crypto.Base64Decode(Input.String)  -- output the Base64 result to the Output field  
    end  
  end  
end  
  
function Initialization()  -- function called at the start of runtime  
  if Options.String == "" then Options.String = "Encode" end  -- set the Option field if blank on runtime  
end  
  
  
-- EventHandlers  
Options.EventHandler = ProcessData  -- calls ProcessData when the Options EventHandler is called  
Input.EventHandler = ProcessData  -- calls ProcessData when the Input EventHandler is called  
Padding.EventHandler = ProcessData  -- calls ProcessData when the Padding EventHandler is called  
  
  
-- Start at runtime  
Initialization()  -- calls Initialization at the start of runtime
```

### Using the Example

In the **Options** Combo Box, select âEncodeâ or âDecodeâ. Enter the string you would like to encode or decode into the **Input** Text Box and the result will populate in the **Output** box. The **Padding** Toggle will add a â=â character to the start and end of the result.

[Crypto Compute](javascript:void(0))

### Text Controller Setup

Drag in a Text Controller and name it Crypto Compute. Add a Combo Box named **Options** and two Text Boxes named **Input** and **Output** (see screenshot).

Next, copy the Example Code to the Text Controller.

[Crypto Compute Example Code](javascript:void(0))

```lua
-- Aliases  
Options = Controls.Options  
Input = Controls.Input  
Output = Controls.Output  
  
  
-- Constants  
Options.Choices = {"MD5","CRC16"}  -- choices for the type of compute  
  
  
-- Functions  
function OptionsEntered()  -- returns true when Option is selected and there is data in the Input field  
  return Options.String ~= "" and Input.String ~= ""  
end  
  
function ProcessData()  -- function to process the text in the Input field  
  if OptionsEntered() then   
    if Options.String == "MD5" then   
      Output.String = Crypto.MD5Compute(Input.String)  -- output the MD5 result to the Output field  
    else   
      Output.String = Crypto.CRC16Compute(Input.String)  -- output the CRC16 result to the Output field  
    end  
  end  
end  
  
function Initialization() -- function called at the start of runtime  
  if Options.String == "" then Options.String = "MD5" end  -- set the Option field if blank on runtime  
end  
  
  
-- EventHandlers  
Options.EventHandler = ProcessData  -- calls ProcessData when the Options EventHandler is called   
Input.EventHandler = ProcessData  -- calls ProcessData when the Input EventHandler is called  
  
  
-- Start at runtime  
Initialization()  -- calls Initialization at the start of runtime
```

### Using the Example

In the **Options** ComboBox, select âMD5â or âCRC16â. Enter the string you would like to process into the **Input** Text box, and the result will populate in the **Output** box.

[Crypto Hash](javascript:void(0))

### Text Controller Setup

Drag in a Text Controller and name it Crypto Hash. Add two Combo Boxes named **Options** and **Algorithm** and three Text Boxes named **Input**, **Key** and **Output** (see screenshot).

Next, copy the Example Code to the Text Controller.

[Crypto Hash Example Code](javascript:void(0))

```lua
-- Aliases  
Options = Controls.Options  
Algorithm = Controls.Algorithm  
Input = Controls.Input  
Key = Controls.Key  
Output = Controls.Output  
  
  
-- Constants  
Options.Choices = {"Digest","HMAC"}  -- choices for the type of compute  
Algorithm.Choices = {"md5","sha1","sha256","sha512"}  -- choices for the algorithm used to compute  
  
  
-- Functions  
function OptionsEntered()  -- returns true when Option is selected and there is data in the Input field  
  return Options.String ~= "" and Input.String ~= "" and Algorithm.String ~= "" and Key.String ~= "Enter Key"  
end  
  
function ProcessData()  -- function to process the text in the Input field  
  if Options.String == "Digest" then   
    Key.IsDisabled = true  -- disables Key control since the input is not needed  
    Key.String = "N/A"  
    if OptionsEntered() then Output.String = Crypto.Digest(Algorithm.String,Input.String) end  -- output the MD5 result to the Output field  
  else   
    Key.IsDisabled = false  -- enables Key control since the input is needed  
    if Key.String == "N/A" then Key.String = "Enter Key" end  
    if OptionsEntered() then Output.String = Crypto.HMAC(Algorithm.String,Key.String,Input.String) end  -- output the CRC16 result to the Output field  
  end  
end  
  
function Initialization() -- function called at the start of runtime  
  if Options.String == "" then Options.String = "Digest" end  -- set the Option field if blank on runtime  
  if Algorithm.String == "" then Algorithm.String = "md5" end  -- set the Algorithem field if blank on runtime  
  ProcessData()  
end  
  
  
-- EventHandlers  
Options.EventHandler = ProcessData  -- calls ProcessData when the Options EventHandler is called  
Input.EventHandler = ProcessData  -- calls ProcessData when the Input EventHandler is called  
Key.EventHandler = ProcessData  -- calls ProcessData when the Key EventHandler is called  
Algorithm.EventHandler = ProcessData  -- calls ProcessData when the Algorithm EventHandler is called  
  
  
-- Start at runtime  
Initialization()  -- calls Initialization at the start of runtime
```

### Using the Example

In the **Options** Combo Box, select âDigestâ or âHMACâ. In the **Algorithm** Combo Box, select âMD5â, âSHA1â, âSHA256â or âSHA512â. Next, if a key is required, enter the key into the **Key** Text Box (the control will be disabled if it cannot be used). Enter the string you would like to process into the **Input** Text Box, and the result will populate in the **Output** box.
