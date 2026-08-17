# Compiler Error 1400

assignment error: Illegal Assignment

Assignments in SIMPL+ require that the value being assigned to a variable must equate to the same type as that variable. Integer variables can only be assigned integer values and string variables can only be assigned a string value.

  * If a complex assignment is being made, make sure that all parenthesis are matched. In other words, all opening parenthesis must have a matching closing parenthesis.

  * When comparing 2 strings (‘=’, ‘<’, ‘>=’, etc.), the resulting value is an integer

  * Input variables (DIGITAL_INPUT, ANALOG_INPUT, STRING_INPUT and BUFFER_INPUT) cannot be assigned a value.




The following are examples of this error:

INTEGER x, y;

STRING str[100], str2[100];

DIGITAL_INPUT digIn;

DIGITAL_OUTPUT digOut;

ANALOG_OUTPUT anlgOut;

FUNCTION MyFunc()

{

str = “abc”; // ok

str = “abc” + “def”; // ok

str = str2; // ok

x = 1; // ok

x = digOut; // ok

x = (str = str2); // ok

x = 5 * (1 + (str > str2)); // ok

digOut = x; // ok

digOut = 5; // ok

digOut = anlgIn; // ok – both are integer types

x = str; // error – str does not equate to

// an integer

// atoi() should be used

digIn = 1; // error - digIn is an input variable

str = 5; // error – 5 is an integer

// MakeString() should be used

str = str2 = “abc”; // error = str2 = “abc” is an equality

// test, not an assignment

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1400.htm*
