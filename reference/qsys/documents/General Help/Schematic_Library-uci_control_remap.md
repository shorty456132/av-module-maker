# Remap UCI Controls [BETA]

> Source: https://help.qsys.com/Content/Schematic_Library/uci_control_remap.htm

# Remap UCI Controls [BETA]

Use the Remap UCI Controls tool to easily reassign the control IDs for multiple UCI controls in a single click. This tool eliminates the need to remap controls on an individual basis using the "Remap Controls" function (formerly "Transfer Control ID"), as documented in [Transferring Settings from one Control to Another](../Q-SYS_Designer/Using_the_Schematic/using_controls.htm#Transfer).

**Note:** This is a BETA tool. Though it is functional, it is not feature complete.

[When would I use this tool?](javascript:void(0))

In a nutshell, this tool allows you to point the controls in a UCI to any of the controls in your schematic. You can queue up changes for multiple controls and then submit the updates in a single click. Here are some use cases:

* New UCI: You have an existing UCI for the control of one room and you want to copy that UCI to make a new one for a different room. You've configured new components in your schematic for audio and video control that need to be mapped to the new UCI â for example, a new Softphone Status/Control component pin pad. With this tool, you can simply select the new Softphone Status/Control component to use with the new UCI.
* New UCI Page or Layer: You've created a new page or layer within a UCI to handle a different set of controls tied to new components in your schematic. To make remapping easier, you can view the controls in the UCI by Page Name or by Page and Layer Name.
* Component Swap: You want to remap multiple UCI controls tied to one type of component to a similar component with some matching control types â for example, swapping a Gain component for a Gain Ramp component, where many of the controls match.
* **Same Component Control Remap**: You want to remap individual controls within the same component. For example, you have a UCI button that toggles HDMI1 on an HDMI I/O Decoder component and another that toggles HDMI2. You want to swap these so that the UCI button for HDMI1 now toggles HDMI2 and vice versa.
* Resolving Orphaned Controls: You've made changes to your schematic that have resulted in multiple orphaned controls (indicated with red question marks) in your UCI. These need to be remapped to new controls.

[Remapping Components](javascript:void(0))

Use this procedure to remap the UCI controls from one component to another component.

1. From the Design Elements > User Control Interfaces panel, select a UCI.
2. From the menu, click Tools > Remap UCI Controls.
3. A list of components appears. These are the components from your schematic that have controls in the selected UCI. From the list, click the component name whose controls you want to map to another component.
4. From the drop-down menu, select a new component. A green check mark icon  indicates that the component is the same type as the existing component and all controls will be remapped to the new component. However, if there is no green check mark icon, it means that the new component is a different type and that some controls do not match between them. You can still remap the component, but with the option to:

   * Cancel: Don't remap any controls.
   * Remap Matching Controls: Listed controls will stay mapped to the current component. See [Example: Component Swap](#Example:2).
   * Remap All: Listed controls will be orphaned. See [Example: Resolving Orphaned Individual Controls](#Example:).

[Example: New UCI Component Remap](javascript:void(0))

In this example, we copy/paste the Softphone UCI for Room 1 to create a new UCI for Room 2. Since the controls for the new UCI are mapped by default to the schematic components for Room 1, we use the UCI Control Remap tool to point the Room 2 UCI controls to the separate Mixer and Softphone components intended for Room 2.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_Example_New_UCI.webm)

[Example: Component Swap](javascript:void(0))

In this example, a UCI contains controls for a Gain component, including Gain level, Mute, Invert, and Bypass. We want to re-map these UCI controls to a new Gain Ramp component. However, because Gain Ramp does not contain Bypass or Invert controls, we must choose how to resolve them. In this case, we'll remap only the controls that match (Mute and Current Gain), which will keep the unmatched controls (Bypass and Invert) still mapped to the existing Gain component.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_Component_Swap.webm)

[Remapping Individual Component Controls](javascript:void(0))

Use this procedure to remap controls within the same component:

1. From the Design Elements > User Control Interfaces panel, select a UCI.
2. From the menu, click Tools > Remap UCI Controls.
3. A list of components appears. These are the components from your schematic that have controls in the selected UCI. From the list, click the drop-down arrow next to the component name whose controls you want to remap.
4. A list of controls appears. Use the drop-down arrows to point the UCI control to a different control within the component.
5. Click Ok to save your changes.

[Example: Individual Control Remap](javascript:void(0))

In this example, we have a UCI that controls the AV output from an NV-32-H Network Video Endpoint. Originally, AV1 was the output from an Amazon FireTV and AV2 was the output from a Roku stick. However, someone recently disconnected and reinserted these devices and swapped them. Now, the UCI control for the FireTV turns on the Roku and vice versa. There's an easy way to fix this! Simply use the Remap UCI Controls tool to swap the AV outputs to which the UCI is pointed.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_Ind_Control.webm)

[Resolving Orphans](javascript:void(0))

Orphaned controls are indicated in the UCI window with a red question mark. In the Remap UCI Controls tool, they are indicated with a red flag icon. Orphaned controls can occur when the source control in the schematic has been removed, or you have remapped the controls in your UCI from one component to another that does not match, leaving some controls unmapped. You can easily resolve orphans in the Remap UCI Controls tool.

1. From the Design Elements > User Control Interfaces panel, select a UCI.
2. From the menu, click Tools > Remap UCI Controls.
3. Components with orphaned controls are noted with a red flag  icon. Click the component name (for example, "gain") to select a schematic Page and new component to which to map the orphaned controls.
4. Click Ok to save your changes.

[Example: Resolving Orphaned Component Controls](javascript:void(0))

In this example, a simple UCI contains Gain component controls. However, that Gain control was deleted from the design and replaced with a new one ("MyNewGain"), leaving the UCI controls orphaned. We use the Remap UCI Controls tool to remap all the orphaned controls to the new Gain component in one click.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_Resolve_Orphans.webm)

[Example: Resolving Orphaned Individual Controls](javascript:void(0))

In this example, we swapped a Gain component for a Gain Ramp component and selected to Remap All controls, which left the Bypass and Invert controls orphaned. We will remap those controls to new controls within the Gain Ramp component: Ramp to A and Ramp to B.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_Resolve_Ind_Orphans.webm)

[Tips and Tricks](javascript:void(0))

[Finding Mapped Components in the Schematic](javascript:void(0))

From the list of mapped components, click a component's icon to find it in your schematic.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_Find_Mapped_Components.webm)

[Finding Mapped Controls in the UCI](javascript:void(0))

From the list of mapped controls within a component, click a control's icon to find it in your UCI.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_Find_Controls.webm)

[Viewing and Filtering Controls](javascript:void(0))

Use the toolbar to:

* Expand and collapse the list of controls.
* Group the list by page name or page and layer name.
* Search for controls by name.
* Show or hide only controls that have been orphaned.

[
Your browser does not support the video tag.
](../Resources/Videos/UCI_Control_Remap_View_Filter.webm)
