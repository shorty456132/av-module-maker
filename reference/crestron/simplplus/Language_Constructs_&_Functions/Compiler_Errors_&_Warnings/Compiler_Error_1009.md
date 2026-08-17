# Compiler Error 1009

syntax error: Missing structure member: '<identifier>'

Structure does not contain member: '<identifier>'

Variables contained within structures are required when using structures within an expression or statement. When using structures, the ‘dot’ notation is required to specify a structure’s variable.

The notation is as follows: <structure_name>.<member_variable>

Structure arrays are as follows: <structure_name>[index].<member_variable>

The following are examples of this error:

STRUCTURE MyStruct

{

INTEGER x;

INTEGER x2[10];

}

Function MyFunc( INTEGER x )

{

INTEGER i;

MyStruct struct;

MyStruct structArr[10];

i = struct.x; // ok

struct.x = 5; // ok

struct.x2[2] = 5; // ok

structArr[1].x2[2] = 5; // ok

Call MyFunc( i ); // ok

Call MyFunc( struct.x ); // ok

Call MyFunc( structArr[1].x ); // ok

Call MyFunc( struct.x2[1] ); // ok

i = struct; // error – structure variable not specified

struct = i; // error – structure variable not specified

Call MyFunc( struct ); // error – structure variable not specified

i = struct.z; // error – structure variable does not exist

struct.z = 5; // error – structure variable does not exist

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1009.htm*
