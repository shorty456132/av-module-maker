# Compiler Warning 1802

compiler warning: #CATEGORY_NAME defined more than once.

Using: #CATEGORY_NAME "<number>"

Only one category name is allowed for each SIMPL+ module. If the compiler directive, #CATEGORY, is found more than once within a SIMPL+ module, the compiler will use the category number from the last occurrence of the compiler directive.

The following are examples of this warning:

#CATEGORY “1”

#CATEGORY “2”

FUNCTION MyFunc()

{

}

#CATEGORY “3” // this is the resulting category number

// for this SIMPL+ module

FUNCTION AnotherFunc()

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Warning_1802.htm*
