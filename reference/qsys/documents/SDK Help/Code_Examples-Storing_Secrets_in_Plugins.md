# Storing Secrets in Plugins

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Storing_Secrets_in_Plugins.htm

# Storing Secrets in Plugins

## Use case

In many plugins, a password or key might be needed to authenticate with a device or service. This is considered a secret and should be obfuscated in the UI of the plugin. This means that the string needs to be stored outside of that control so that it is still accessible to the script between script restarts. The best practice is to store the value in an embedded componentâs control. Controls of embedded components can only be accessed by the plugin in which they are embedded and, like all other controls, the values are retained as part of the design state.

## Where do I start?

### Start with the storage

To start, add a âCustom Controlsâ component to your plugin. See [Embedded Components](../Standards_Definitions/Embedded_Components.htm) to learn more about adding components to your plugin. In this example, we are only adding one but you can increase `count_1` to match your needs â for example, if you had a password and a persistent token to keep track of. A benefit to using a Custom Controls component is the ability to define other controls to persistently store other internal values as well without exposing extra controls to the user.

```lua
function GetComponents(props)  
  local components = {}  
  table.insert(  
    components,  
    {  
      Name = "SecretStorage", -- Name of the component to be used in your runtime  
      Type = "custom_controls",  
      Properties = {  
        type_1 = 13, -- Text Edit  
        count_1 = 1 -- Number of text edits with control name of text.n, where n is the index  
      }  
    }  
  )  
  return components  
end
```

### How do I access the component and its controls?

QDS will add your Component to the global scope of your runtime using the name you defined earlier. In our example, it is called `SecretStorage`. We can access the controls the same way you would use [Component.New()](https://help.qsys.com/#Control_Scripting/Using_Lua_in_Q-Sys/Component.htm).

```lua
MySecret = SecretStorage["text.1"] -- alias for the control where our secret is stored.  
  
-- To store a value, assign a String to the control  
MySecret.String = "Dont tell anyone this"  
  
-- To recall the String, call its .String value  
print(MySecret.String)
```

### How can I easily obfuscate the password after the user enters it?

You can easily obfuscate the secret by using a gsub operation on the string value of the control to replace all characters with a \* after storing its value.

```lua
SecretEntry.EventHandler = function(ctrl)  
  MySecret.String = ctrl.String -- Store the secret  
  ctrl.String = ctrl.String:gsub(".", "*") -- Obfuscate the secret to the user  
end
```

## OK, what does the complete code look like?

Here is an entire example plugin that stores a single secret and will print it to the console when the trigger is pressed.

Secret Storage Complete Example

```lua
PluginInfo = {  
    Name = "Embeded Secret Example",  
    Version = "1.0",  
    BuildVersion = "1.0.0.0",  
    Id = "56c56b94-72eb-4868-aca0-534b216e01cd",  
    Description = "This is an example to show how to store secrets in a plugin.",  
}  
  
function GetColor(props)  
  return { 102, 102, 102 }  
end  
  
function GetPrettyName(props)  
  return "Embeded Secret Example\n" .. PluginInfo.BuildVersion  
end  
  
pagenames = {"main"}  
  
function GetPages(props)  
  local pages = {}  
  for ix,name in ipairs(pagenames) do  
    table.insert(pages,{name = pagenames[ix]})  
  end  
  return pages  
end  
  
function GetProperties()  
  local props = {}  
  return props  
end  
  
function GetControls(props)  
  local controls = {}  
  table.insert(  
    controls,  
    {  
      Name = "SecretEntry",  
      ControlType = "Text",  
      PinStyle = "Both",  
      UserPin = true  
    }  
  )  
  table.insert(  
    controls,  
    {  
      Name = "PrintSecret",  
      ControlType = "Button",  
      ButtonType = "Trigger",  
      PinStyle = "Input",  
      UserPin = true  
    }  
  )  
  return controls  
end  
  
function GetControlLayout(props)  
  local layout   = {}  
  local graphics = {}  
  --[[ Layout File Contents ]]  
  table.insert(  
    graphics,  
    {  
      Type = "Label",  
      Text = "Enter your secret here:",  
      Size = {120, 16},  
      Position = {0, 0},  
      HTextAlign = "Right"  
    }  
  )  
  layout["SecretEntry"] = {  
    Style = "Text",  
    Size = {100, 16},  
    Position = {120, 0}  
  }  
  table.insert(  
    graphics,  
    {  
      Type = "Button",  
      Text = "Print Secret:",  
      Size = {120, 16},  
      Position = {0, 20},  
      HTextAlign = "Right"  
    }  
  )  
  layout["PrintSecret"] = {  
    Style = "Button",  
    ButtonStyle = "Trigger",  
    Size = {36, 16},  
    Position = {120, 20}  
  }  
  return layout, graphics  
end  
  
function GetComponents(props)  
  local components = {}  
  table.insert(  
    components,  
    {  
      Name = "SecretStorage", -- Name of the component to be used in your runtime  
      Type = "custom_controls",  
      Properties = {  
        type_1 = 13, -- Text Edit  
        count_1 = 1 -- Number of text edits with control name of text.n, where n is the index  
      }  
    }  
  )  
  return components  
end  
  
--Start event based logic  
if Controls then  
  -- Control Alias  
  MySecret = SecretStorage["text.1"]  
  SecretEntry = Controls.SecretEntry  
  PrintSecret = Controls.PrintSecret  
    
  function Initialize()  
    SecretEntry.String = MySecret.String:gsub(".", "*") -- show the user if a secret is stored on script start  
  end  
    
  SecretEntry.EventHandler = function(ctrl)  
    MySecret.String = ctrl.String -- Store the secret  
    ctrl.String = ctrl.String:gsub(".", "*") -- Obfuscate the secret to the user  
  end  
    
  PrintSecret.EventHandler = function(ctrl)  
    print("Your secret is '"..MySecret.String.."'") -- Print the secret to the console  
  end  
    
  Initialize()  
end
```
