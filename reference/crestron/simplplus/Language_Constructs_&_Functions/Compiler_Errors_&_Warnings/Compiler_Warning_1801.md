# Compiler Warning 1801

compiler warning: 'TerminateEvent' statement will only terminate current

Wait statement's function scope

When Wait Statements are embedded within one another, the TerminateEvent, will only terminate the corresponding Wait Statement of the same scope. It will NOT terminate any Wait Statements that are of a different scope.

Wait Statements are similar to event functions (EVENT, PUSH, CHANGE, RELEASE) in that they execute in their own program thread. The control system can have many threads executing at the same time; each thread runs concurrent with one another.

Scope refers to the level at which an Event, user-defined function or statement resides. Having a global scope means that the function or variable can be called or accessed from anywhere within the program. A local scope means that the variable can only be accessed from within the event or function that it resides in.

The following are examples of this warning:

FUNCTION MyFunc( INTEGER x )

{

Wait( 500, MyLabel1 )

{

Wait( 300, MyLabel2 )

{

TerminateEvent; // warning – this will only terminate

// the Wait Statent, MyLabel2.

// MyLabel1 will continue to

// execute

}

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Warning_1801.htm*
