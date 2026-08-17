# #IF_DEFINED … #ENDIF

Name:

#IF_DEFINED … #ENDIF

Syntax:

#IF_DEFINED <constant_name>

<code>

#ENDIF

Description:

Results in compilation of the <code> only if <constant_name> has previously been defined. This construct is generally useful for putting in code for debugging purposes, giving the ability to easily turn the debugging on and off during compilation.

Example:

#DEFINE_CONSTANT DEBUG 1

DIGITAL_OUTPUT OUT$;

INTEGER I;

FOR(I=0 to 20)

{

#IF_DEFINED DEBUG

PRINT("Loop index I = %d\n", I);

#ENDIF

OUT$ = ITOA(I);

}

The value of the loop is printed only if the DEBUG constant is defined. In order to prevent compilation of the code, delete the line that defines the constant or comment it out.

Version:

X Generation: SIMPL v1.50.06

2-Series: SIMPL v2.01.05 and later

See also [IsSignalDefined](<../System_Interfacing/IsSignalDefined.htm>)

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_IF_DEFINED_%E2%80%A6__ENDIF.htm*
