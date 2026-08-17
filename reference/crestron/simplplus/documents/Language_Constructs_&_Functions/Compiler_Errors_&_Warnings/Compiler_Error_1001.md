# Compiler Error 1001 

syntax error: Undefined variable: '<identifier>'

Undefined function ‘<identifier>’

The specified identifier was not declared.

All variables and user-defined functions must be declared before they are used. They must be declared either globally or within the same function scope. Variables from one program are not accessible from another program.

NOTE: Scope refers to the level at which an Event, user-defined function or statement resides. Having a global scope means that the function or variable can be called or accessed from anywhere within the program. A local scope means that the variable can only be accessed from within the event or function that it resides in.

  * Make sure the identifier is spelled correctly

  * Make sure the identifier has not been declared locally within another function

  * When using structures, make sure the proper ‘dot’ notation is being used when accessing the structure’s variables (see example below)




The following are examples of this error:

INTEGER i;

STRUCTURE myStruct

{

INTEGER structMember;

INTEGER structArrMember[10];

}

myStruct struct;

myStruct structArr[10];

FUNCTION MyFunc( INTEGER x )

{

INTEGER k;

i = 1; // ok

k = 3; // ok

x = 4; // ok

struct.structMember = 5; // ok – proper ‘dot’ notation

struct.structMember[1] = 6; // ok – proper ‘dot’ notation

structArr[1].structMember = 7; // ok – proper ‘dot’ notation

structArr[1].structArrMember[2] = 8; // ok – proper ‘dot’ notation

j = 2; // error – j is not declared

structMember = 10; // error – improper ‘dot’ notation

structMember[1] = 11; // error – structMember is not an array

k = AnotherFunc(); // error – AnotherFunc() was not

// declared previously

}

INTEGER_FUNCTION AnotherFunc()

{

k = 5; // error – k is a local variable of MyFunc()

x = 6; // error – x is a local variable of MyFunc()

Call MyFunc(); // ok

Call MyFunk(); // error – spelling error

return (1);

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1001.htm*
