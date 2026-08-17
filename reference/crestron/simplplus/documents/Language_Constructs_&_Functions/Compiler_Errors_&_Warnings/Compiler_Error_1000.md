# Compiler Error 1000

syntax error: '<identifier>' already defined

The specified identifier was declared more than once. A variable can only be declared once within it’s function scope. The same identifier cannot be used for more than one declaration type.

NOTE: Scope refers to the level at which an Event, user-defined function or statement resides. Having a global scope means that the function or variable can be called or accessed from anywhere within the program. A local scope means that the variable can only be accessed from within the event or function that it resides in.

  * Make sure the identifier has not been declared as another declaration type, user-defined function, or structure definition.




The following are examples of this error:

INTEGER i;

INTEGER i; // error – i is already defined as an INTEGER

STRING i[100]; // error – i is already defined as an INTEGER

STRUCTURE myStruct

{

INTEGER i; // ok – i is a member variable of myStruct

}

INTEGER_FUNCTION MyFunc( INTEGER x, INTEGER y )

{

INTEGER i; // ok

INTEGER i; // error - i is already defined as a local INTEGER

INTEGER x; // error – x is already defined as a function

// parameter, which makes it a local

// variable in this function

}

FUNCTION MyFunc() // error – MyFunc() is already defined

// as an INTEGER_FUNCTION

{

}

FUNCTION AnotherFunc( INTEGER x, INTEGER y ) // ok – x and y are

// local to this function

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1000.htm*
