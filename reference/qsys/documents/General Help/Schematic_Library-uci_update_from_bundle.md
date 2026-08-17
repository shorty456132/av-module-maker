# Update UCI From Bundle

> Source: https://help.qsys.com/Content/Schematic_Library/uci_update_from_bundle.htm

# Update UCI From Bundle

Use Update UCI from Bundle when you want to update an existing UCI with something you previously created and exported from another computer. This is useful when you want to be able to re-apply a UCI import to update a version without modifying your control links.

**Note:** If you need to export the UCI design first, please visit the topic.

[Adding a UCI to the Design](javascript:void(0))

1. Select **User Control Interfaces** from the left-side pane.
2. Click  and select **New User Control Interface**.
3. Select the new UCI (for example, "Interface 1").
4. In the right-side pane, under Properties, configure the UCI as desired. See [Update UCI From Bundle](#Web_Control_Interface_Properties).
5. In the middle pane, select **Page 1**.
6. Navigate to **Tools** and select **Update UCI From Bundle**.
7. A File-Open dialog box opens where you can navigate to the exported .uci file on your computer or external hard drive.
8. Once you select the .uci file, that custom UCI will show up in **User Control Interfaces**.
9. In the right-side pane, under **Properties**, configure the UCI page, including its **Title**. See [Update UCI From Bundle](#Page).
10. To add additional control elements to the UCI page to build your UCI. See [Update UCI From Bundle](#Building_a_User_Control_Interface).
11. To add more pages, see [Update UCI From Bundle](#Working).
12. To configure layering within a page, see [Update UCI From Bundle](#Add_Layers).

[Troubleshooting](javascript:void(0))

[Update UCI From Bundle is Grayed Out](javascript:void(0))

If you notice the Update UCI From Bundle options is disabled (grayed out), it could be because you have not yet chosen to add a new UCI design. To fix it, click  and select **New User Control Interface**.

[Resolving Orphans](javascript:void(0))

Orphaned controls are indicated in the UCI window with a red question mark. Orphaned controls can occur when the source control in the schematic has been removed, or you have remapped the controls in your UCI from one component to another that does not match, leaving some controls unmapped.

You can easily resolve orphans by following the steps in [Relink UCI Controls [BETA]](uci_control_relink.htm) or [Remap UCI Controls [BETA]](uci_control_remap.htm).
