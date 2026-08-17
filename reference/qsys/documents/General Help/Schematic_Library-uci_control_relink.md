# Relink UCI Controls [BETA]

> Source: https://help.qsys.com/Content/Schematic_Library/uci_control_relink.htm

# Relink UCI Controls [BETA]

Use the Relink UCI Controls tool to easily reassign the control IDs for multiple UCI controls in a single click. This tool requires the need to relink controls on an individual basis using the "Relink Controls" function, as documented in [Transferring Settings from one Control to Another](../Q-SYS_Designer/Using_the_Schematic/using_controls.htm#Transfer).

**Note:** This is a BETA tool. Though it is functional, it is not feature complete.

[When would I use this tool?](javascript:void(0))

In a nutshell, this tool allows you to point the controls in a UCI to any of the controls in your schematic. You can queue up changes for multiple controls and then submit the updates in a single click. Here are some use cases:

* New UCI: You have an existing UCI for the control of one room and you want to copy that UCI to make a new one for a different room. You've configured new components in your schematic for audio and video control that need to be linked to the new UCI â for example, a new Softphone Status/Control component pin pad. With this tool, you can simply select the new Softphone Status/Control component to use with the new UCI.
* New UCI Page or Layer: You've created a new page or layer within a UCI to handle a different set of controls tied to new components in your schematic. To make relinking easier, you can view the controls in the UCI by Page Name or by Page and Layer Name.
* **Same Component Control Relink**: You want to relink individual controls within the same component. For example, you have a UCI button that toggles HDMI1 on an HDMI I/O Decoder component and another that toggles HDMI2. You want to swap these so that the UCI button for HDMI1 now toggles HDMI2 and vice versa.
* Resolving Orphaned Controls: You've made changes to your schematic that have resulted in multiple orphaned controls (indicated with red question marks) in your UCI. These need to be relinked to new controls.

[Relinking Components Overview](javascript:void(0))

Use this procedure to relink the UCI controls from one component to another component.

1. From the Design Elements > User Control Interfaces panel, select a UCI.
2. From the menu, click Tools > Relink UCI Controls.
3. A list of components appears. These are the components from your schematic that have controls in the selected UCI. From the list, click the component name whose controls you want to link to another component.
4. From the drop-down menu, select a new component. A green check mark icon  indicates that the component is the same type as the existing component and all controls will be relinked to the new component. However, if there is no green check mark icon, it means that the new component is a different type and that some controls do not match between them. You can still relink the component, but with the option to:
   * Cancel: Don't relink any controls.
   * Relink Matching Controls: Listed controls will stay linked to the current component.
   * Relink All: Listed controls will be orphaned.

[Example: New UCI Component Relink](javascript:void(0))

In this example, we copy / paste the UCI components from Room 1 to create a new UCI for Room 2. Since the controls for the new UCI are linked by default to the schematic components for Room 1, we use the UCI Control Relink tool to point the Room 2 UCI controls to the separate speaker Status components intended for Room 2.

[
Your browser does not support the video tag.
](../Resources/Multimedia/RelinkComponents_RelinkTool.webm)

[Relinking Individual Components Using Link Icon](javascript:void(0))

Use this procedure to add the UCI controls from one component to another component.

**Note:** Only toolbox based controls have the option to be linked. If your design does not have toolbox based UCI controls, you will not see anything that can be linked.

1. From the Design Elements > User Control Interfaces panel, select a UCI.
2. From the Toolbox Tab, select the type of control you want and drag it into your UCI.
3. Assign the type of control using the UCI Text Field Properties on the right side pane.
4. Once you have the components added to your UCI, switch back to the Layers Tab.
5. A Link Icon with a circle and a line through itwill indicate that the component is not currently linked to a control.
6. Click on the icon to link the component to the design. See [Example: Relinking Components Using Link Icon](#Example:).

[Example: Relinking Components Using Link Icon](javascript:void(0))

In this example, we copy / paste the Status LED Icons from Room 1 UCI onto a secondary Room 2 UCI. Since the controls for the new UCI are linked by default to the schematic components for Room 1, we use the UCI Relink Icon on the Layers Tab to point the Room 2 UCI controls to the separate Status components intended for Room 2.

[
Your browser does not support the video tag.
](../Resources/Multimedia/UCI_Relink_RelinkingIcons.webm)

[Un-linking Individual Components](javascript:void(0))

Use this procedure to remove the UCI controls from one component to another component. This is useful in case you have previously and erroneously linked a component to something different.

**Note:** Only toolbox based controls have the option to be linked. If your design does not have toolbox based UCI controls, you will not see anything that can be linked.

1. From the Design Elements > User Control Interfaces panel, select a UCI.
2. From the Toolbox Tab, select the type of control that was erroneously linked.
3. Click on the Link Icon and then click Remove Link.

[Example: Un-linking Components Using Link Icon](javascript:void(0))

In this example, we started with [Example: Relinking Components Using Link Icon](#Example:) but then realized, one of the components, the Amp Status is erroneously showing Speaker 1 Status. By clicking on Remove Link, we can then follow [Relinking Individual Components Using Link Icon](#Relinkin) as necessary.

[
Your browser does not support the video tag.
](../Resources/Multimedia/UCI-Unlinking_LinkIcon.webm)

[Resolving Orphans](javascript:void(0))

Orphaned controls are indicated in the UCI window with a red question mark. In the relink UCI Controls tool, they are indicated with a red flag icon. Orphaned controls can occur when the source control in the schematic has been removed, or you have relinked the controls in your UCI from one component to another that does not match, leaving some controls unlinked. You can easily resolve orphans in the Relink UCI Controls tool.

1. From the Design Elements > User Control Interfaces panel, select a UCI.
2. From the menu, click Tools > Relink UCI Controls.
3. Components with orphaned controls are noted with a red flag  icon. Click the component name (for example, "gain") to select a Schematic Page and new component to which to link the orphaned controls.
4. Click Ok to save your changes.

[Example: Resolving Orphaned Components](javascript:void(0))

In this example, we have the Amp and DCIO components placed in the design in Room 1; however, they became orphaned in Room 2. Using Relink UCI Controls, we are able to resolve the orphaned components by pointing it to Room 2.

[
Your browser does not support the video tag.
](../Resources/Multimedia/ResolvingOrphans_RelinkUCI.webm)

[Tips and Tricks](javascript:void(0))

[Error: All Items Have Been Filtered Out](javascript:void(0))

When using Tools > Relink UCI Controls, you receive an error that all items have been filtered out, it could be due to two of the following reasons:

* The controls might need to be relinked in the Toolbox Tab.
* Your design does not consist of any toolbox controls.

[Finding Linked Controls in the UCI](javascript:void(0))

From the list of linked controls within a component, click a control's icon to find it in your UCI.

[
Your browser does not support the video tag.
](../Resources/Multimedia/FindingMappedComponents_RelinkUCI.webm)

[Viewing and Filtering Controls](javascript:void(0))

Use the toolbar to:

* Expand and collapse the list of controls.
* Group the list by page name or page and layer name.
* Search for controls by name.
* Show or hide only controls that have been orphaned.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_View_Filter.webm)
