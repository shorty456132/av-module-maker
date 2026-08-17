# Compiler Warning 1019

compiler warning: Logic excluded as a result of #if_series3 directive

SIMPL+ module(s) contain the #IF_SERIES3 directive. When compiling for 4-Series control systems any logic within the #IF_SERIES3 directive block will be excluded from compilation which may result in loss of functionality.

Review the logic contained within the #IF_SERIES3 directive and make sure that it doesn't include any logic intended for 4-series control systems.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Warning_1019.htm*
