# Compile Output Files

Compiling SIMPL+ modules will result in several output files being written into the project folder. These files will appear both in the module's project folder and into a temporary folder called SPlsWork. The files written are as follows:

The SIMPL+ Module's project directory will contain the following files:

<module>.usp - SIMPL+ User Module (Never Deleted)

<module>.usl - SIMPL+ User Library (Never Deleted)

<module>.ush - SIMPL+ User Module Header File (Never Deleted - File is written upon SIMPL+ Module compilation)

SPlusWork Directory will contain the following files:

<module>.inf - SIMPL+ Module Information File (Remains after a successful compilation)

<module>.spl - SIMPL+ intermediary file (Remains after a successful compilation)

<module>.h - SIMPL+ intermediary file (Remains after a successful compilation)

<module>.o - SIMPL+ intermediary file (Remains after a successful compilation)

<module>.c - SIMPL+ intermediary file (Deleted after SIMPL+ Module compilation)

SIMPL+ Modules are only compiled if the module has not been changed since the last successful compilation. The compiler is optimized not to recompile a module during the build process once it is has been compiled successfully. SIMPL+ Libraries and modules contained within User Macros are not optimized in this manner and they will always be recompiled for each build process. Selecting "Build All" from the SIMPL+ Build Menu will force the module and all included libraries to be recompiled.

---
*Source: https://help.crestron.com/simpl_plus/Content/Programming_Environment/Compile_Output_Files.htm*
