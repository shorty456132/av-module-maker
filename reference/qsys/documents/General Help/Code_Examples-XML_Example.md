# XML Object

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/XML_Example.htm

# XML Object

This is a code example for using the XML library to convert an XML string to a Lua table and to look through an XML string to find and return a tag or attribute.

## Text Controller Setup

Drag in a Text Controller and name it XML. Add four Text Boxes named **Input**, **Output**, **Find**, and **Found**. (see picture below).

Next, copy the Example Code to the Text Controller.

[XML Example Code](javascript:void(0))

```lua
-- Include  
require("LuaXML") -- require the LuaXML lib so it can be referenced  
  
  
-- Aliases  
Input = Controls.Input  
Output = Controls.Output  
Find = Controls.Find  
Found = Controls.Found  
  
  
-- Variables  
XML = ""  
  
  
-- Functions  
function EncodeXML()  -- function to encode xml data into a lua table  
  if Input.String ~= "" then -- make sure there is input data  
    XML = xml.eval(Input.String) -- encode input string to lua table and assign to var XML  
    Output.String = tostring(XML) -- convert the XML lua table to a string so it can be read  
  end  
end  
  
function FindMatch() -- see if a tag or attribute exists in a XML lua table  
  if Find.String ~= "" and XML ~= "" then -- make sure the find string and XML var have data  
    local found = tostring(xml.find(XML,Find.String)) -- convert the found XML data to a string and assign to var found  
    if found == "nil" then -- ensure found has data (nil means could not find string)  
      Found.String = "NO MATCH" -- found is nil so no match is printed in the Found textbox  
      print("NO MATCH")  
    else  
      Found.String = found -- found has data (found the string) and print it in the Found textbox  
      print("FOUND: "..found)  
    end  
  end  
end  
  
function Initialization() -- first function called on start of the script  
  EncodeXML()  
  FindMatch()  
end  
  
  
-- EventHandlers  
Input.EventHandler = EncodeXML -- call EncodeXML everytime the Input EventHandler is called  
Find.EventHandler = FindMatch -- call FindMatch everytime the Find EventHandler is called  
  
  
-- Start at Runtime  
Initialization() -- call this function on the start of the script
```

## Using the Example

In the **Options** Combo Box, select âEncodeâ or âDecodeâ. Enter the XML string into the **Input** Text Box and the result will populate in the **Output** Text Box. In the **Find** Text Box, enter the tag or attribute for which to search the XML string. If found, it populates in the **Found** Text Box.
