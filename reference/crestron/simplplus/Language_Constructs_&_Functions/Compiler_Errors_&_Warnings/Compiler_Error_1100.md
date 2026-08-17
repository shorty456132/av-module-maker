# Compiler Error 1100

fatal error: Statement outside of function scope

User-defined functions, Events, and compiler directives can only be defined at a global level.

NOTE: Scope refers to the level at which an Event, user-defined function or statement resides. Having a global scope means that the function or variable can be called or accessed from anywhere within the program. A local scope means that the variable can only be accessed from within the event or function that it resides in.

Variables can have either a global or local scope.

The following are examples of this error:

INTEGER i;

STRING str[100];

#DEFINE_CONSTANT myConst 1 // ok

#DEFINE_CONSTANT myConst 2; // error – semicolon is not needed

i = 5; // error – variables can only be used within a

// function or event

Call MyFunc(); // error – functions can only be called from

// another function or event

; // error – a semicolon is valid statement (which

// does nothing), and is not contained

// within a function or event

{ // error – braces only signify a group of

// statements within a function or

// construct (i.e.: if-else, while, etc)

INTEGER x;

INTEGER y;

}

Print( “outside of everything” ); // error – statement is

// not contained within

// a function or event

FUNCTION MyFunc() // ok

{

}

Function Main() // ok – Function Main gets called automatically

// at the start of the program

{

i = 5; // ok

str = “”; // ok

Call MyFunc(); // ok

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1100.htm*
