# Compiler Error 1506

function argument error: 0, 1 or 2 constant expected for argument 1

The function, MakeString, can contain a 0, 1, 2 as the first argument. This tells the control system to output the resulting string to a specific destination. An integer value other than 0, 1 or 2 was encountered as the first argument of MakeString().

The different destinations are as follows:

0: Computer Port, same as PRINT.

1: CPU (same functionality as the SendPacketToCPU function)

2: Cresnet Network (same functionality as the SendCresnetPacket function).

The following are examples of this error:

FUNCTION MyFunc( INTEGER x, STRING str )

{

Call MyFunc( 1, “abc” ); // ok

Call MyFunc(); // error – 2 arguments are expected

Call MyFunc( 1 ); // error – argument 2 is missing

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1506.htm*
