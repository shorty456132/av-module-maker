# #IF_NOT_DEFINED … #ENDIF

Name:

#IF_NOT_DEFINED … #ENDIF

Syntax:

#IF_NOT_DEFINED <constant_name>

<code>

#ENDIF

Description:

Results in compilation of the <code> only if <constant_name> has not been previously defined. This construct is generally useful for putting in code for debugging purposes, giving the ability to easily turn the debugging on and off during compilation.

Example:

#DEFINE_CONSTANT DEBUG 1

DIGITAL_OUTPUT OUT$;

INTEGER I;

FOR(I=0 to 20)

{

#IF_DEFINED DEBUG

PRINT("Loop index I = %d\n", I);

#ENDIF

#IF_NOT_DEFINED_DEBUG

OUT$ = ITOA(I);

#ENDIF

}

The value of the loop is only printed if the DEBUG constant is defined. The output OUT$ is only generated if the debug constant is not defined (if debug mode is not turned on). In order to generate "release" code, the debug constant can be deleted or commented out.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_IF_NOT_DEFINED_%E2%80%A6__ENDIF.htm*
