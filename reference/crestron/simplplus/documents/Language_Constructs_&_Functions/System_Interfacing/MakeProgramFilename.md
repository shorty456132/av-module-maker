# MakeProgramFilename

Name:

MakeProgramFilename

Syntax:

MakeProgramFilename

Description:

Takes in the filename (which would be the program path or anything that the user wants) and prepends that with the Program ID Tag. The Program ID Tag is specified in the Header of the SIMPL program.

For example: if running in program and the user passes in "\Simpl\App01\MyProgram" as the filename and the Program ID Tag is set to "HVAC" then this function would return "\Simpl\App01\HVAC_MyProgram".

NOTE: In the 2 Series, Program ID Tags are not used, so the same name is returned.

Example:

FUNCTION MyFunc()

{

// SIMPL Program ID Tag is set to "HVAC

PRINT( “ProgramFileName = %s”, MakeProgramFilename("\\\Simpl\\\App01\\\MyProgram") );

// prints: "\Simpl\App01\HVAC_MyProgram"

}

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v <> and above

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/MakeProgramFilename.htm*
