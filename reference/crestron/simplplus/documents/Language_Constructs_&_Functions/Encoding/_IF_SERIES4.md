# 

# #IF_SERIES4

Name:

# IF_SERIES4

Syntax:

#IF_SERIES4 <statements> [ #ELSE <statements> ] #ENDIF

Description:

When compiling for different control system targets, it might be desirable to have each target execute a different portion of code. Reasons for this might be new or obsolete functions or different performance characteristics in each control system. Using this compiler directive will cause the compiler to only include the statements for the 4-series control system. The #ELSE block is optional and may be used if a different set of code should be executed when the 4-series is not the target control system.

The #IF_SERIES4 keyword is ignored and the SIMPL+ module should compile without issues when the SIMPL+ module target control system class is any of the following:

  * 2-Series only
  * 3-Series only
  * 2-Series and 3-Series



Example:

#IF_SERIES4

Function FunctionOne()

{

}

#ENDIF

#IF_SERIES4

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

#IF_SERIES4

// some code

#ELSE

// some other code

#ENDIF

}

Version:

4-Series: SIMPL v. 4.14.xx

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/_IF_SERIES4.htm*
