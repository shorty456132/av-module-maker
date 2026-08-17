# Target Selection

When compiling a SIMPL+ module at least one target control system type needs to be selected for the SIMPL+ module to compile successfully. Starting with SIMPL v. 4.14.xx the default target selections for a new SIMPL+ module are 3-Series AND 4-series control systems.. Note that on open, existing SIMPL+ modules will also target 4-Series control system class by default..

For example, if a SIMPL+ module was previously targeting 2-Series only, it will target 2-Series and 4-Series when opened in SIMPL v. 4.14.xx and later.

Selecting a target implies that the module MUSTwork for that target and any statements that are not valid for that target are NOT permitted. It does NOT mean that the module won't work for other targets. For example, most SIMPL+ modules targeting 4-Series control systems can be uploaded and expected to work on 3-Series control systems as well.

NOTE: A SIMPL+ module can be added to the SIMPL program only if that module targets the control system present in the SIMPL program;  
  
If the SIMPL+ module does NOT target the control system present in the SIMPL program, the SIMPL+ module cannot be added to SIMPL program.  


Changes to the targeted control system types can be made via the SIMPL+ toolbar or from the **Build** menu.

Target Selection from the toolbar

When one or more target options are selected (buttons appear "pressed"), the control system type target is included during compilation; when an option is NOT selected, the control system target type is NOT included during compilation.

In the example below only the 4-Series control systems target is selected, thus only the 4-Series control system target will be included when compiling:

Additionally, target selection can be specified from the **Build** menu:

Target Selection from the Build Menu

When one or more target options are selected (checkmark is displayed), the control system type target is included during compilation; when an option is NOT selected, the control system target type is NOT included during compilation.

NOTE: In older versions of SIMPL+, the settings for the target types were system-wide. Those settings applied to all SIMPL+ modules that were opened and were not specific to the active module being edited.   
  
In SIMPL+ version 3.00 and later, the target type setting is specific only to the active module being edited and saved within that module. The toolbar buttons reflect the target type of the active module within the SIMPL+ environment.

NOTE: If a program is compiled for the wrong type of control system, an error message may appear when attempting to upload, and the program must be re-compiled.

.

**See also:**

[IF_SERIES2](<../Language_Constructs_&_Functions/Encoding/_IF_SERIES2.htm>)

[IF_SERIES3](<../Language_Constructs_&_Functions/Encoding/_IF_SERIES3.htm>)

[IF_SERIES4](<../Language_Constructs_&_Functions/Encoding/_IF_SERIES4.htm>)

---
*Source: https://help.crestron.com/simpl_plus/Content/Programming_Environment/Target_Selection.htm*
