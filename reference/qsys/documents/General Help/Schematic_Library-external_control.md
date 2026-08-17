# Named Controls

> Source: https://help.qsys.com/Content/Schematic_Library/external_control.htm

# Named Controls

After controls are made available for external control, a third-party system can change or monitor the settings of the available controls as required. This procedure describes how to make controls available for external control. In order to test the control logic, the controls must be available for external control.

[Select Controls](javascript:void(0))

You can select and use controls from components in your Schematic for [external control systems](../External_Control_APIs/External_Control_APIs_Overview.htm), [Control Change Commands](../Administrator/Commands.htm), and [Control Scripts](control_script_2.htm).

1. Open your Q-SYS Designer file.
2. Make sure the design is in the design mode. (F7)
3. Click the **Named Controls** accordion bar in the left pane of the Q-SYS workspace. The **Named Controls** list displays and is empty in new designs.
4. Double-click the Schematic Element for which you want to make the controls available. The Control Panel displays.
5. Select one or more controls that you want to make available and drag them into the **Named Controls** list. You can press Ctrl+A to select all the controls. When you press Ctrl+A, all the non-control items are selected as well, but are ignored by Q-SYS when dragged into the list.
6. As you drag controls into the **Named Controls** list, the list is populated with the control's name, for example, **CrossoverLowBandGain**. The name is used by the external system to access this control.
7. To help you identify controls already in the Named Controls list, each control you place in the list is marked graphically in the Control Panel by a small gray circle on the lower right corner of the control in the Control Panel from which it came. This identifier is available only in the Design mode.
8. Rename the control if desired. [Naming the Controls](#NamingtheControls)  below.
9. When you have completed selecting and renaming the controls. Test the control logic. Refer to [Test External Controls over Telnet](../External_Control_APIs/ECP/Test_External_Controls.htm).

[Naming the Controls](javascript:void(0)) 

In order for the external system to access the controls, they have to be named.

To rename a control, use your mouse to select the control you want to change, then click directly on the name, and type new name.

* When a control is placed in the **Named Controls** list, Q-SYS gives it a name using the component from which it came, and the type of control, for example **CrossoverLowBandGain**.
* If you add the same control from another component, Q-SYS adds a sequential number to the name for example, **CrossoverLowBandGain1**.
* Each control in the design can have a single Named Control reference. Dragging in a control from a component that already has a reference in Named Controls will have no effect.
* You can use the default naming convention, or create your own.
* The names are case-sensitive. If they are all entered in the same case, there is less of a chance of making mistakes in the commands from the external system or **Control Scripts**. (The Control Change Commands display a list of the Named Controls for selection.)
* Some components can be named in the Properties of the component for example the Audio Player. When you place one of the controls from a "named" component, that name is added to the Named Control name. Most components don't have this capability, so you might want to add another identifying characteristic to the name of the Named Control. Either way, you can use Find (Ctrl+F) to find (or match) the component and a control.
* If you create a name with spaces, and are using the Q-SYS External Control Protocol, the name must be enclosed in double quotes when sending commands to Q-SYS.

[Sorting and Grouping Names](javascript:void(0))

When you add controls to the Named Controls list, they are always added at the end of the list in a group. This allows you to easily rename them after they are added - you don't have to locate them. After adding controls from several components, all controls are in the order in which they were added. You can rename them and they are still in the order added.

* You can select another accordion button, for example, Snapshots, then reopen the Named Controls accordion, the controls are now sorted alphabetically.
* Click the {} icon in the Named Controls accordion bar. The controls are now grouped by the component from which they came.
* Click the {} icon again, and the names are sorted alphabetically.
* The sorting and grouping are case-insensitive.

[Finding Controls](javascript:void(0))

With a large number of **Named Controls** it may be difficult to determine which control in which component belongs to a control listed in the Named Controls list.

1. Select the control in the component's **Control Panel**, and press **Ctrl+F**. The Find dialog box displays.
2. Select **Find By Context** from the drop-down list.
3. If there is an associated Named Control for the selected control, a link displays similar to " **Jump to Named Control** 'CrossoverLowBandGain1'". Click the link. The associated control is located in the Named Controls list.
4. To find the control from the Named Controls list, select the control in the Named Controls list, press Ctrl+F, then click the displayed link.

[Copying Components with Named Controls](javascript:void(0))

When a component has controls in the Named Control list, and you copy that control, when you paste the control, a dialog appears asking you if you want to create Named Controls for the copy. If yes, Named Controls are automatically placed in the Named Control list with a sequence number at the end of each control to differentiate them from the original Named Controls.

[Listing (Extracting) Named Controls](javascript:void(0))

You can list the controls, and information about the controls, you have placed in the Named Controls list in an XML file. This is primarily designed for importing into [Medialon](http://www.medialon.com/download/show_mxm/mxmQSCAudioQSys/mxmQSCAudioQSys.htm) software.

1. From the main menu, select **Tools** > **Extract Named Controls...** the Windows Save As dialog displays.
2. Select a location from the **Save in:** drop-down list.
3. Type a name for the file in the Flin name: field.
4. Click the Save button.

You can view the file using an editor of your choice, for example, Notepad. The format of the file is:

```lua
<?xml version="1.0" encoding="utf-8"?>  
<Design DesignName="untitled" CompileGUID="">  
<Snapshots>  
<Snapshot Name="Global" Count="1" />  
</Snapshots>  
<ExternalControls>  
<Control Id="External ID 1" ControlId="gain" ControlName="Master Gain" ComponentId="UnWnJflUXrJ-XKRhYfh;" ComponentName="Delay" ComponentLabel="" Type="Float" Mode="RW" MinimumValue="-100" MaximumValue="20" Size="1" />  
</ExternalControls>  
</Design>
```

### Explanation of External Control Fields

* Control Id â The user-defined name in the Named Controls list.
* ControlId â The Q-SYS system name for the control.
* ControlName â The name of the control as it is in the component's control panel.
* ComponentId â Randomly generated unique Id for the component from which the control came.
* ComponentName â The Q-SYS system name for the component from which the control came.
* ComponentLabel â The user-defined label for the component.
* Type â The type of control, can be: Float, Integer, Boolean, Trigger, enum or String
* Mode â The write state of the control. Can be: RW (read / write) or R (read only)
* MinimumValue â The minimum value of which the control is capable. The Type must be Float or Integer.
* MaximumValue â The maximum value of which the control is capable. The Type must be Float or Integer.
* Size â 1, unless the control is a vector control ( like meters ) - then it will be the size of the vector.
