# #HELP_BEGIN … #HELP_END

Name:

#HELP_BEGIN … #HELP_END

Syntax:

#HELP_BEGIN

Help Text Line 1

Help Text Line 2

etc.

#HELP_END

Description:

The #HELP_BEGIN, #HELP_END pair makes it easier to create help since each line does not need a separate #HELP directive. When F1 is hit either on the symbol in the Symbol Library, in either the Program View or the Detail view, the help text will be displayed. If this directive or #HELP is not present, the help text shown is "NO HELP AVAILABLE". Note that the text will show up exactly as typed between the begin/end directives (including blank lines).

Example:

#HELP_BEGIN

This is help line 1.

This is help line 3.

#HELP_END

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_HELP_BEGIN_%E2%80%A6__HELP_END.htm*
