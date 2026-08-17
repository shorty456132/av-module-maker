# UCI

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Uci.htm

# UCI

Use the UCI API functions to programmatically control and modify user control interfaces in Q-SYS.

[Script the UCI](javascript:void(0))  

The UCI Script tab contains a familiar interface for authoring Lua code specific to the selected UCI. This makes it easy to duplicate a UCI and update the new one (i.e., modify the script) with different parameters. One use case, for example, is having multiple UCIs with differing Layer and Shared Layer visibility settings.

**Note:** Some Lua methods are not supported â see [Unsupported Lua methods](#Unsuppor) for details. When referencing the [UCI](#) Lua methods in your UCI script, it will not work if you define the `UCI_Name` variable because the script is local to the UCI and its name.

### Examples

[Setting UCI Layer Visibility](javascript:void(0))

**Note:** When using the `UCI.SetLayerVisibility` within a UCI script, you must drop the argument of `UCI_Name`.

Here is a simple UCI script that sets layer visibility.

```lua
timer0 = Timer.New()  
   
   
timer0.EventHandler = function()  
  Uci.SetLayerVisibility('Page 1', 'Layer 1', false, 'fade')  
  Timer.CallAfter(function()  
      Uci.SetLayerVisibility('Page 1', 'Layer 1', true, 'fade')  
    Uci.SetLayerVisibility('Page 1', 'Layer 2', false, 'left')  
   
    Timer.CallAfter(function()  
        Uci.SetLayerVisibility('Page 1', 'Layer 2', true, 'left')  
    Uci.SetLayerVisibility('Page 1', 'Layer 3', false, 'right')  
   
      Timer.CallAfter(function()  
          Uci.SetLayerVisibility('Page 1', 'Layer 3', true, 'right')  
    Uci.SetLayerVisibility('Page 1', 'Layer 4', false, 'top')  
   
        Timer.CallAfter(function()  
            Uci.SetLayerVisibility('Page 1', 'Layer 4', true, 'top')  
    Uci.SetLayerVisibility('Page 1', 'Layer 5', false, 'bottom')  
   
          Timer.CallAfter(function()  
              Uci.SetLayerVisibility('Page 1', 'Layer 5', true, 'none')  
   
          end,1)  
        end,2)  
      end,2)  
    end,2)  
  end,2)  
end  
   
   
timer0:Start(10)
```

[Setting UCI Shared Layer visibility](javascript:void(0))

This line instructs the a Shared Layer in a UCI to become hidden with a fade transition.

```lua
Uci.SetSharedLayerVisibility('Shared Layer 1', false, 'fade')
```

### Unsupported Lua methods

Some Lua methods are not supported in UCI scripts, including methods from the following libraries. If you use these methods in the UCI Script tab, you will see this error in the Debug Output window: "This feature is unavailable in UCI Controller."

**Note:** These Lua methods are not supported in the UCI Scripts tab.

|  |  |
| --- | --- |
| * `Bonjour`* `Curl`   * `dir`   * `Email`   * `http`   * `HttpClient`   * `icmp`   * `imap`   * `lua_reflect`   * `loop_player` | * `Midi` * `Ping`* `Serial`   * `socket`   * `snmp`   * `Ssh`   * `TcpSocket`   * `udp`   * `usb`   * `UdpSocket` |

[Uci.GetVariable](javascript:void(0))

Retrieves the value of a variable that has been set in the UCI.

### Syntax

Uci.GetVariable( *UCI\_Name*, *Variable\_Name* )

### Arguments

*UCI\_Name* : The UCI from which you want to retrieve the variable.

*Variable\_Name* : The name of the variable you want to retrieve from the specified UCI.

[Uci.LogOff](javascript:void(0))

Enable the ability to log off from a specified TSC touchscreen controller or UCI Viewer.

**Note:** Uci.LogOff can log out only if PIN security is enabled in Q-SYS Core Manager. For more information, see [User Control Interfaces](../../Core_Manager/System_Management/User_Control_Interfaces.htm).

### Syntax

Uci.LogOff( *TSC\_Name* )

### Arguments

*TSC\_Name* : The name of the TSC touchscreen controller or UCI Viewer.

### Example

```lua
-- Control Alias  
TSC = Controls.TSC_Name -- This textbox should contain the name of the TSC or UCI Viewer Inventory instance  
  
-- UCI Log Off  
Controls["Log Me Out"].EventHandler = function()  
  print("Uci.LogOff() can only log out if PIN security is enabled on the panel")  
  Uci.LogOff(TSC.String)  
end
```

[Uci.SetLayerVisibility](javascript:void(0))

Set whether and how a layer is made visible within a specified UCI name and page.

**Note:** When using the `UCI.SetLayerVisibility` within a UCI script, you must drop the argument of `UCI_Name`. For an example, under Script the UCI, see [Setting UCI Layer Visibility](#Setting).

### Syntax

Uci.SetLayerVisibility( *UCI\_Name*, *Page\_Name*, *Layer\_Name*, *Visibility*, *Transition\_Type* )

### Arguments

*UCI\_Name* : String. The name of the UCI.

*Page\_Name* : String. The name of the UCI page.

*Layer\_Name* : String. The name of the UCI layer.

*Visibility* : true | false

*Transition\_Type* : "none" | "fade" | "left" | "right" | "bottom" | "top"

### Example

```lua
--Set Layer Visibility  
trans = Controls.Transition  
trans.Choices = {"none","fade","left","right","bottom","top"}  
if #trans.String==0 then trans.String = "none" end  
for ix,layer in ipairs{"The Top Layer","The Middle Layer","The Bottom Layer"} do  
  Controls[layer].EventHandler = function(ctl)   
    Uci.SetLayerVisibility( "Main UCI", "Page 1", layer, ctl.Boolean, trans.String )  
  end  
  Uci.SetLayerVisibility( "Main UCI", "Page 1", layer, Controls[layer].Boolean, trans.String )  
end
```

[Uci.SetPage](javascript:void(0))

Set which UCI page to display on a TSC touchscreen controller or UCI Viewer.

### Syntax

Uci.SetPage( *TSC\_Name*, *Page\_in\_UCI* )

### Arguments

*TSC\_Name* : The name of the TSC touchscreen controller or UCI Viewer.

*Page\_in\_UCI* : The UCI page to show.

### Example

```lua
-- Control Alias  
TSC = Controls.TSC_Name -- This textbox should contain the name of the TSC or UCI Viewer Inventory instance  
  
-- Set UCI Page  
for key,ctl in ipairs(Controls.Page) do  
  ctl.EventHandler = function()  
    local TSC_Name = TSC.String  
    Uci.SetPage(TSC_Name,"Page "..key)  
  end  
end
```

[Uci.SetScreen](javascript:void(0))

Set the screen status of a TSC touchscreen controller or UCI Viewer.

### Syntax

Uci.SetScreen( *TSC\_Name*, *State* )

### Arguments

*TSC\_Name* : The name of the TSC touchscreen controller or UCI Viewer.

*State* : "On" | "Off" | "Dim"

### Example

```lua
-- Control Alias  
TSC = Controls.TSC_Name -- This textbox should contain the name of the TSC or UCI Viewer Inventory instance  
  
-- Set Screen  
for _,state in pairs{"On","Off","Dim"} do  
  Controls[state].EventHandler = function()  
    local TSC_Name = TSC.String  
    Uci.SetScreen(TSC_Name,state)  
  end  
end
```

[Uci.SetSharedLayerVisibility](javascript:void(0))

Set whether and how a shared layer is made visible within a specified UCI name and page.

Uci.SetSharedLayerVisibility is similar to UciSetLayerVisibility, but because Shared Layers can exist on multiple UCI pages, there is no argument for Page\_Name. For more information about Shared Layers, see [User Control Interface (UCI) Design Overview](../../Schematic_Library/user_control_interface.htm#Add_Layers).

**Note:** In UCI scripts, `Uci.SetSharedLayerVisibility` must be called without the `UCI_Name` parameter. For details and sample code, under Script the UCI, see [Setting UCI Shared Layer Visibility](#Setting2).

### Syntax

Uci.SetSharedLayerVisibility( '*UCI\_Name*', '*Layer\_Name*', *Visibility*, *Transition\_Type* )

### Arguments

*UCI\_Name* : String. The name of the UCI.

*Layer\_Name* : String. The name of the UCI layer.

*Visibility* : true | false

*Transition\_Type* : "none" | "fade" | "left" | "right" | "bottom" | "top"

[Uci.SetUCI](javascript:void(0))

Set which UCI to display on a TSC touchscreen controller or UCI Viewer.

**Note:** To avoid errors when using the Uci.SetUCI function, the **UCI Assignment** property for the TSC touchscreen controller or UCI Viewer must be set to "Dynamic". For more information, see [Status/Control (Touch Screen)](../../Schematic_Library/touch_screen_status.htm) and [Status/Control (UCI Viewer)](../../Schematic_Library/uci_viewer.htm).

### Syntax

Uci.SetUCI( *TSC\_Name*, *UCI\_Name* )

### Arguments

*TSC\_Name* : The name of the TSC touchscreen controller or UCI Viewer.

*UCI\_Name* : String. The name of the UCI.

### Example

```lua
-- Control Alias  
TSC = Controls.TSC_Name -- This textbox should contain the name of the TSC or UCI Viewer Inventory instance  
  
-- Set UCI  
Controls["Main UCI"].EventHandler = function() local  
  TSC_Name = TSC.String   
  Uci.SetUCI(TSC_Name,"Main UCI")  
end  
Controls["Other UCI"].EventHandler = function()  
  local TSC_Name = TSC.String  
  Uci.SetUCI(TSC_Name,"Other UCI")  
end
```

[Uci.SetVariable](javascript:void(0))

Sets the Value of a Variable within a UCI.

### Syntax

Uci.SetVariable( *UCI\_Name*, *Variable\_Name*, *Value* )

### Arguments

*UCI\_Name* : The name of the UCI where the variable is defined.

*Variable\_Name* : The name of the variable you want to set.

*Value* : The value to assign to the variable.

[Uci.ShowDialog](javascript:void(0))

Display a dialog in a UCI that contains a title, message, and button selection list.

### Syntax

Uci.ShowDialog( *UCI\_Name*, *DialogTable* )

### Arguments

*UCI\_Name* : String. The name of the target UCI for which to display the dialog.

*DialogTable* : A table consisting of the following elements

Title = "*UCI dialog titlebar string*",

Message = "*Dialog message string*",

Buttons = { "*Button\_String*", "*Button\_String*", "*Button\_String*", "*etc.*" }

The button list is a table consisting of strings â one string per desired response button.

Handler = *EventHandler\_Function*

The EventHandler Function receives an integer index of which button was pressed. The EventHandler argument is zero-based, so add 1 to the integer to match a Lua table entry. See example.

### Example

In this example, the ShowDialog control and event handler activates the dialog. The UCIDialogHandler event handler function calls the WhichButton control to provide feedback of which button was pushed, defined by a list of strings (ButtonText).

```lua
ButtonText = {  
  "Button 1 was pushed",  
  "Button 2 was pushed",  
  "Button 3 was pushed",  
}  
  
function UCIDialogHandler(choiceInt)  
  print(choiceInt,ButtonText[choiceInt+1])  
  Controls.WhichButton.String = ButtonText[choiceInt+1]  
end  
  
function ShowDialog()  
  Uci.ShowDialog(   
    "Main UCI",  
    {  
      Title = "UCI Dialog Titlebar",  
      Message = "Which button would you like to push?",  
      Buttons = {  
        "Button 1",  
        "Button 2",  
        "Button 3",  
      },  
      Handler = UCIDialogHandler,  
    }  
  )  
end  
  
Controls.ShowDialog.EventHandler = ShowDialog
```
