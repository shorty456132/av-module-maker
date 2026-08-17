# Compiler Error 1017

**syntax error: ** **SIMPL# Classes and Structures are case-sensitive: **

**‘ <variable_name>’  
**

All code within SIMPL# Libraries is case-sensitive, therefore upper case and lower case characters are distinct. All class, structure and variable calls and references from SIMPL+ must use the same case as that used within the SIMPL# code.

The datatype (class or structure name) and class/structure members within the SIMPL# Library are case-sensitive. The variable declared within the SIMPL+ module is not case-sensitive.

For example, the classes, ‘MyClass’ and ‘myClass’ are different.

The following are examples of this error:

SIMPL# Library

// SimplSharpLibrary.clz

public class MyClass

{

public int intVar;

public int IntFunction();

}

public struct tagMyStruct

{

public string myString;

}

SPlusModule.usp

// UserModule.usp

#USER_SIMPLSHARP_LIBRARY "SimplSharpLibrary"

MyClass class1; // ok – matching case

myclass class2; // error – case doesn’t match

tagMyStruct myStruct1; // ok – matching case

TagmyStruct myStruct2; // error – case doesn’t match

FUNCTION MyFunction ( STRING str )

{

class1.intVar = 1; // ok – intVar is the same case

CLASS1.intVar = 2; // ok – CLASS1 is not case-sensitive.

It is the variable declared

within SIMPL+ (not SIMPL#).

intVar is case-sensitive since

it is a SIMPL# structure

member.

myfunction( myStruct1.myString ); // ok, myfunction is a

function declared within

SIMPL+

class1.INTFUNCTION(); // error – INTFUNCTION is case-sensitive.

Should be IntFunction

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1017.htm*
