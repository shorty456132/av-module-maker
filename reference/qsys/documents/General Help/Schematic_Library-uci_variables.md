# Working with UCI Variables

> Source: https://help.qsys.com/Content/Schematic_Library/uci_variables.htm

# Working with UCI Variables

The Variables tab allows you to set certain Variables that you can later reference in your UCI Script. This feature allows you to modify the UCI script as changes are made to the Variables tab.

**Note:** UCI Variables can run `.Value` and `.EventHandler`.

**Tip:** You must be in Emulate mode or Running the design on a Core for the feature to be interactive.

[Adding Variables](javascript:void(0))

1. Select a UCI name from the User Control Interfaces section of the left-side pane.
2. Select the Variables Tab.
3. Click  to add a Variable to the selected page.
4. Choose what type of Variable you wish to use. You can select **String**, **Number**, **Boolean**, **Color**.
   * **String**: Insert your text field.
   * **Number**: Insert any number. You can use the up / down arrows to select a number, or manually type in a number.
   * **Boolean**: Check-box field to allow for a Boolean.
   * **Color**: Pops up with the Color Picker box to choose a color.

[Updating Variables](javascript:void(0))

1. Select a UCI name from the User Control Interfaces section of the left-side pane.
2. Select the Variables Tab.
3. Choose what type of Variable you wish to update.
4. Make the necessary changes, (i.e., changing the color, or updating the string, etc.).

**Note:** You must click away from the Variable that you updated in order for the changes to take effect. For instance, if you have a Variable Name as "Room123", and change it to "Room456", you must click out of the Variable box in which you typed. Enter/Return keys do not force the change.

[Deleting Variables](javascript:void(0)) 

1. Select a UCI name from the User Control Interfaces section of the left-side pane.
2. Select the Variables Tab.
3. Click  to delete the selected Variables.

[Access Variables Globally](javascript:void(0)) 

You can access variables globally, either from another UCI or a regular Text controller script.

```lua
-- get room_name variable of some UCI  
room_name = Uci.GetVariable("Interface 1", "room_name")  
  
-- change it to something else  
Uci.SetVariable("Interface 1", "room_name", "Updated room name")
```

[Importing and Exporting UCI Variables](javascript:void(0)) 

Visit the [Import and Export UCI Variables](uci_variables_import_and_export.htm) topic to learn how to import and export UCI Variables.

[Using UCI Variables with CSS Integration](javascript:void(0))

Using UCI Variables with CSS Integration makes customizing a UCI even easier by pulling in predefined colors, icons, etc. from a CSS Style (to learn more about CSS Styles, see the [UCI Styles](uci_styles.htm) topic).

**Note:** Examples 1 and 2 are best when you already have the source classes defined in your style sheet. Example 3 is best when you need to assign icons using source Variables.

**Tip:** When using a UCI variable to override CSS Content, add quotes around the text if it contains spaces or other special character.

[Example 1: Changing Color](javascript:void(0))

**Note:** Only use CSSColor Variables for CSS. CSS expects RGBA, whereas Designer colors are ARGB.

In the following video, the root style.css file contains root background, primary, secondary colors, and button radius size.

After choosing the Style sheet, those root preferences automatically import. However, we can easily change that information.

[
Your browser does not support the video tag.
](../Resources/Multimedia/Changing_Colors_Variables.webm)

[Example 2: Changing Icons](javascript:void(0))

The root file also contains predefined button icons for Mac, DVR, and PC.

Using this predefined information, the example below quickly and effortlessly imports the same icons once the variable name matches.

[
Your browser does not support the video tag.
](../Resources/Multimedia/Change_Icons_Variables.webm)

The `EventHandler` on the UCI Script assigns the specific button to what the Variable Value is set to.

[Example 3: Changing Icons Using Source Variable](javascript:void(0))

The CSS Style sheet contains `source_Variable` to easily assign icons.

With the `source_Variable` defined, another portion of the UCI script details what icon will be placed into that variable.

[
Your browser does not support the video tag.
](../Resources/Multimedia/Var-changing_icons.webm)

[Scripting with UCI Variables](javascript:void(0))

In the following examples, we are using a small UCI equipped with *Volume Up*, *Volume Down*, and *Mute* buttons as well as a *Gain* meter. Additionally, we have two Variables:

* `RoomName` is defined by the string: `Example Room`
* `GainBlock` is defined by the string: `Example Gain`

[Example 1: Gain Functionality](javascript:void(0)) 

```lua
function GetLevel() -- get current gain level  
  Controls.Vol_Lvl.Position = MyGain["gain"].Position  
end  
  
function SetVolUp(state) -- press/release gain stepper increase  
  if MyGain["stepper.increase"]~= nil then   
    MyGain["stepper.increase"].Boolean = state  
  else  
    print ("Gain isn't linked.")  
  end  
end  
  
function SetVolDn(state) -- press/release gain stepper decrease  
  if MyGain["stepper.decrease"]~= nil then   
    MyGain["stepper.decrease"].Boolean = state  
  else  
    print ("Gain isn't linked.")  
  end  
end  
  
function GetMute() -- get current mute state  
  Controls.Vol_Mute.Boolean = MyGain["mute"].Boolean  
end  
  
function SetMute() -- set gain mute state to UCI mute state  
  if MyGain["mute"]~= nil then   
    MyGain["mute"].Boolean = Controls.Vol_Mute.Boolean  
  else  
    print ("Mute isn't linked.")  
  end  
end  
  
function SetGainBlock()  
  local compName = Uci.Variables["GainBlock"].String -- get component name from UCI variable  
  MyGain = Component.New(compName)          -- link to gain block  
  
  if MyGain["gain"] ~= nil then             --check that this component has a gain control  
    MyGain["gain"].EventHandler = GetLevel  -- subscribe for level FB  
    GetLevel()                              -- get current level FB  
  end  
  if MyGain["mute"] ~= nil then             --check that this component has a gain control  
    MyGain["mute"].EventHandler = GetMute   -- subscribe for mute FB  
    GetMute()                               -- get current mute FB  
  end                                         
end  
  
Controls.Vol_Mute.EventHandler = SetMute  
  
Controls.VolUp.EventHandler = function(ctl)  
  SetVolUp(ctl.Boolean)  
end  
  
Controls.VolDn.EventHandler = function(ctl)  
  SetVolDn(ctl.Boolean)  
end  
  
Uci.Variables["GainBlock"].EventHandler = SetGainBlock -- update gain block connection if variables changes  
  
SetGainBlock() -- set gain on initial script start
```

[Example 2: String Functionality](javascript:void(0))

```lua
function SetRoomName()  
  Controls.Btn_RoomName.Legend = Uci.Variables["RoomName"].String  
end  
  
Uci.Variables["RoomName"].EventHandler = SetRoomName -- update room name if variables changes  
  
SetRoomName() -- set room name on initial script start
```
