# #IF_SERIES3

Name:

# IF_SERIES3

Syntax:

#IF_SERIES3 <statements> [ #ELSE <statements> ] #ENDIF

Description:

When compiling for different control system targets, it might be desirable to have each target execute a different portion of code. Reasons for this might be new or obsolete functions or different performance characteristics in each control system. Using this compiler directive will cause the compiler to only include the statements for the 3-series control system. The #ELSE block is optional and may be used if a different set of code should be executed when the 3-series is not the target control system.

NOTE: During a compilation for 4-series control systems SIMPL will issue a warning whenever a #IF_SERIES3 directive is found.  
  
As any logic contained in the #IF_SERIES3 block WILL NOT be compiled for 4-series control systems make sure that logic intended for 4-series control system is outside of the #IF_SERIES3 block.  


Example:

#IF_SERIES3

Function FunctionOne()

{

}

#ENDIF

#IF_SERIES3

Function FunctionTwo()

{

}

#ELSE

Function FunctionThree()

{

}

#ENDIF

Function FunctionFour()

{

#IF_SERIES3

// some code

#ELSE

// some other code

#ENDIF

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/_IF_SERIES3.htm*
