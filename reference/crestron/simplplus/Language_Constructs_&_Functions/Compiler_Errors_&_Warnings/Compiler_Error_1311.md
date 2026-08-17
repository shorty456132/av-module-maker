# Compiler Error 1311

declaration error: Undefined Wait Label: '<identifier>'

Missing, invalid or already defined Wait label: '<identifier>'

Wait Statements can be given a label as an optional argument. This label must be a unique name and more than one wait statement cannot share the same label name. The label name can then be used in the Pause, Cancel and Resume wait functions. All labels must already be declared in within a wait statement before any Pause, Cancel or Resume wait statement can reference it.

The following are examples of this error:

FUNCTION MyFunc()

{

CancelAllWaits(); // ok

CancelWait( MyWaitLabel ); // error – MyWaitLabel has

// not been declared yet

Wait( 500 ) // ok – Label is not required

{

}

Wait( 500, MyWaitLabel ) // ok – MyWaitLabel is unique

{

}

Wait( 500, MyWaitLabel ) // error – MyWaitLabel has already

// been used

{

}

CancelWait( AnotherWaitLabel ); // error – AnotherWaitLabel has

// not been declared yet

Wait( 500, AnotherWaitLabel ) // ok – AnotherWaitLabel is unique

{

}

CancelWait( AnotherWaitLabel ); // ok

PauseWait( MyWaitLabel ); // ok

ResumeWait( MyFunc ); // error – MyFunc is not a valid

// wait label

ResumeWait( someLabel ); // error – someLabel does not exist

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1311.htm*
