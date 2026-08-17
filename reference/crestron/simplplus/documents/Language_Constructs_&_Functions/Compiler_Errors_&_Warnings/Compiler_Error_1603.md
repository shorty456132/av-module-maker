# Compiler Error 1603

construct error: #CATEGORY does not exist: '<categorgy_number>'.

Defaulting to Category Type, ""32"" (Miscellaneous).

The category number for this compiler directive was not found or was not a valid category number within the Symbol Tree Category List within SIMPL. The category number must be enclosed in quotation marks.

Selecting Edit | Insert Category from the SIMPL+ menu will display the list of valid category numbers and give the option for this compiler directive to be automatically inserted into the SIMPL+ module.

The following are examples of this error:

#CATEGORY “6” // ok – “6” is the category number

// for Lighting

#CATEGORY “Lighting” // error – the category number, “6”,

// should be used instead of

// the category symbol name

#CATEGORY 6 // error – the category number should

// be enclosed in quotation marks

#CATEGORY 99 // error – invalid category number

#DEFINE_CONSTANT MyCategory 6

#CATEGORY MyCategory // error – cannot substitute category

// number with #DEFINE_CONSTANTs

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1603.htm*
