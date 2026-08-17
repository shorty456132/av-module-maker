# Compiler Error 1606

construct error: Statement must be contained within a loop statement

The ‘break’ and 'continue' statements can only be used with a loop construct. Valid loop constructs are While loops, Do-While loops and For loops. The compiler encountered this function outside of one of these event functions.

The following are examples of this error:

FUNCTION MyFunc()

{

INTEGER I;

for ( i = 1 t 10 )

{

break; // ok

}

while (1)

{

continue; // ok

}

do

{

break; // ok

} until (1);

if (1)

{

break; // error – break cannot exist within an ‘if’ statement

}

}

EVENT

{

break; // error – TerminateEvent should be used instead

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1606.htm*
