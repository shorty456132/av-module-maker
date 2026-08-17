# Compiler Error 1612

construct error: Category Name can only be assigned to custom category #46. Category #<category_number> found"

Custom category names can only be assigned to category “46”. A different category number was found.

The following are examples of this error:

#CATEGORY “46” “My Custom Category”// ok – “46” is the custom category number

#CATEGORY 6 “My Custom Category”// error – 6 is not the custom

category number

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1612.htm*
