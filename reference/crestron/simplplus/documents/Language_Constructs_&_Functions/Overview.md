# Language Constructs & Functions Overview

Functions take one or more comma separated parameters and return a result. The following template shows how each language construct and function is explained.

Name:

The name used to refer to the construct or function.

Syntax:

The SIMPL+ specific language requirements for this particular construct or function. This section demonstrates exactly how to enter the statement in a SIMPL+ program.

For completeness, the general syntax for SIMPL+ functions is shown below:

<Return Value Type> FunctionName(<Parameter 1 Type> [,

<Parameter 2 Type> ...]);

The Types are described as STRING, INTEGER, LONG_INTEGER, SIGNED_INTEGER, and SIGNED_LONG_INTEGER.

If a STRING is specified as a return type, a STRING or STRING_OUTPUT variable may be used.

If an INTEGER or LONG_INTEGER is specified as a return type, an INTEGER, LONG_INTEGER, ANALOG_OUTPUT or DIGITAL_OUTPUT may be used.

If a STRING is specified as a parameter, a STRING, STRING_INPUT, BUFFER_INPUT or literal string (i.e. "Hello") may be used.

If an INTEGER, LONG_INTEGER, SIGNED_INTEGER or SIGNED_LONG_INTEGER is specified as a parameter, an INTEGER, LONG_INTEGER, ANALOG_INPUT, ANALOG_OUTPUT, DIGITAL_INPUT or DIGITAL_OUTPUT may be used. A literal integer (i.e. 100) may also be used. Note that for DIGITAL_OUTPUT values, a value of 0 is equivalent to digital low, and any other value is a digital high.

Description:

General overview of what this function does.

Parameters (applies to functions only):

Specifics on each of the parameters listed.

Return Value (applies to functions only):

What values are placed in the return variable. Error conditions are also described here. Error conditions are results that occur if one or more of the input values does not have values that are legal for that function.

Example:

A code example of how this function is typically used.

Version:

The version of SIMPL+ in which the construct or function was made available and any revision notes about differences between various versions of SIMPL+. All constructs and functions are available in all subsequent versions except where noted.

Control System:

The control system platform for which the function is valid. Unless specified, the construct or function is valid for both X-Generation (eg., CEN-TVAV, CNMSX-AV/PRO, CNRACKX/-DP) and 2-Series control systems. SIMPL+ is not available in the control systems preceding the X generation - CNMS, CNRACK/-D/-DP, CNLCOMP/-232, and ST-CP

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Overview.htm*
