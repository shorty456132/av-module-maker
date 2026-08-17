# Compiler Error 1608

construct error: Missing library file name

A filename was not found following the compiler directive, #USER_LIBRARY or #CRESTRON_LIBRARY. This filename must be enclosed within quotation marks. The file extension (.usl or .csl) should NOT be used when specifying the filename.

The following are examples of this error:

#USER_LIBRARY “MyUserLib” // ok

#CRESTRON_LIBRARY “EvntSched” // ok

#USER_LIBRARY MyUserLib // error – missing quotation marks

#USER_LIBRARY MyUserLib.usl // error – missing quotation marks and

// extension is not allowed

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1608.htm*
