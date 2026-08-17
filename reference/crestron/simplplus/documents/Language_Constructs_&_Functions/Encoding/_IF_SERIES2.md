# #IF_SERIES2

Name:

# IF_SERIES2

Syntax:

#IF_SERIES2 <statements> [ #ELSE <statements> ] #ENDIF

Description:

When compiling for different control system targets, it might be desirable to have each target execute a different portion of code. Reasons for this might be new or obsolete functions or different performance characteristics in each control system. Using this compiler directive will cause the compiler to only include the statements for the 2-series control system. The #ELSE block is optional and may be used if a different set of code should be executed when the 2-series is not the target control system.

Example:

#IF_SERIES2

Function FunctionOne()

{

}

#ENDIF

#IF_SERIES2

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

#IF_SERIES2

// some code

#ELSE

// some other code

#ENDIF

}

Version:

X Generation: Not Supported

2-Series: 

3-Series:

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/_IF_SERIES2.htm*
