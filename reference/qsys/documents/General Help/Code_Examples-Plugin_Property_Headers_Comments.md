# Plugin Property Headers and Comments

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Plugin_Property_Headers_Comments.htm

# Plugin Property Headers and Comments

Starting in Q-SYS Designer Software v9.10, you can define Headers and Comments for properties defined in a plugin. Headers are useful for grouping similar or related properties together under a single Header. Comments allow for conveying relevant information such as a default value or accepted range to an end user.

[Example Code](javascript:void(0))

```lua
function GetProperties()  
  local props = {}  
  table.insert(  
    props,  
    {  
      Name = "Input Count",  
      Type = "integer",  
      Value = 8,  
      Min = 2,  
      Max = 32,  
      Comment = "Range: 2-32"  
    }  
  )  
  table.insert(  
    props,  
    {  
      Name = "Output Count",  
      Type = "integer",  
      Value = 8,  
      Min = 1,  
      Max = 32,  
      Comment = "Range: 1-32"  
    }  
  )  
  table.insert(  
    props,  
    {  
      Name = "Type",  
      Type = "enum",  
      Value = "Mono",  
      Choices = {"Mono", "Stereo", "Multi-channel"},  
      Header = "Channels"  
    }  
  )  
  table.insert(  
    props,  
    {  
      Name = "Count",  
      Type = "integer",  
      Value = 8,  
      Min = 2,  
      Max = 64,  
      Comment = "Range: 2-64",  
      Header = "Channels"  
    }  
  )  
  return props  
end  
  
function RectifyProperties(props)  
  props["Count"].IsHidden = (props["Type"].Value ~= "Multi-channel")  
  return props  
end
```

[Result](javascript:void(0))
