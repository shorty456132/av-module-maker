# Compiler Error 1605

construct error: Function can only be contained within an event

The function, TerminateEvent, can only be used within a PUSH, CHANGE, RELEASE or EVENT statement. The compiler encountered this function outside of one of these event functions.

The following are examples of this error:

DIGITAL_INPUT digIn;

EVENT

{

TerminateEvent; // ok

}

PUSH digIn

{

TerminateEvent; // ok

}

RELEASE digIn

{

TerminateEvent; // ok

}

CHANGE digIn

{

TerminateEvent; // ok

}

FUNCTION MyFunc()

{

while (1)

{

TerminateEvent; // error – TerminateEvent is not within

// an event function

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1605.htm*
