# User Defined Functions

The previous section details how to use system functions in SIMPL+. When programming, there may be a need to create functions of your own to simplify your programs. These functions are called user‑defined functions. User‑defined functions perform exactly like system functions with the only exception in that they must be defined before they are used.

## Function Definitions

Since user‑defined functions are created by the user (the SIMPL+ programmer), the user must make sure that the SIMPL+ compiler knows about these functions before the program tries to call them. This is accomplished by creating a function definition, which is different from a function call. Remember from the discussion of system functions that a function call is used to invoke a function. A function definition tells the SIMPL+ compiler what the function does.

User functions are used for several reasons. It is not desirable to create one function that performs every task for the entire program. To help better organize program modules, creating several smaller functions makes programming easier to read and understand, and debug. User‑defined functions can also be called by any other function. Rather than have the same programming logic written out in several functions, one function can be defined with this logic and then called by any other function within the module. This will also greatly reduce the module’s size.

To help the reusability of functions, any number of variables can be passed to functions. Variables are passed to functions through the function’s argument list. This is also called parameter passing, or function arguments. Function arguments can be thought of as passing a value into a function. Other variables or literal values can be passed to function arguments. Function arguments are another way of defining local variables. The difference between declaring a local variable within the function and declaring one as part of the parameter list is that the function argument will have the value of the calling function’s variable copied into it.

It is also useful for a function to return a value. A function might be written to compute a value. Another function might want to perform a task and return an error code that can be evaluated by the calling function. Functions can only return at most one value, namely integers or strings. When defining a function, the returning value will determine what type of function to declare. The different types of functions are: `FUNCTION`, `INTEGER_FUNCTION` and `STRING_FUNCTION`. For the 2‑series and newer compilers, `LONG_FUNCTION`, `SIGNED_INTEGER`, and `SIGNED_LONG_FUNCTION` are also available.

The syntax of a SIMPL+ function call is as follows:

FUNCTION MyUserFunction( [parameter1][, parameter2][, parametern] )  
{  
<statements>}

INTEGER_FUNCTION MyUserIntFunction( [parameter1][, parameter2][, parametern] )  
{  
<statements>}

STRING_FUNCTION MyUserStrFunction( [parameter1][, parameter2][, parametern] )  
{  
<statements>}

The `FUNCTION` keyword is used to tell the SIMPL+ compiler that what follows is the definition of a function and not a function call. The `FUNCTION` keyword also specifies that there will be no return value for this function. `INTEGER_FUNCTION` and `STRING_FUNCTION` specify that an integer or string value will be returned as the result of the function. These keywords are also called the function type.

The next keyword is a name provided by the SIMPL+ programmer that will become the name for this user function (called the function name). Be sure to use a unique name and not an existing SIMPL+ keyword, system function, or a previously declared variable name. Otherwise, a compile syntax error will result.

Following the function name is the function’s argument list. If no arguments are needed within this function, then the list can remain empty. Otherwise, a parameter is defined by giving a variable type and name (i.e., `INTEGER myIntArgument`). One or more functions are possible by separating each with a comma.

Function definitions are global to the SIMPL+ module in which they are defined. That is, any event function, the `Function Main`, or even another user‑defined function can call a user‑defined function that has been defined in the same SIMPL+ module. Functions defined in other modules are not accessible.

When calling a function, it is critical not only that that function has been defined in the SIMPL+ module, but also that this function definition occur before the line of code which calls the function. For example, consider the following.

INTEGER x; 

PUSH someSignal  
{  
call MyUserFunction1();  
x = MyUserFunction2( x, 10 );} 

FUNCTION MyUserFunction1()  
{  
print("This is MyFunction1 runnning!\n");} 

INTEGER_FUNCTION MyUserFunction2( INTEGER arg1, STRING arg2 )  
{  
print("This is MyFunction2 runnning!\n");} 

This code causes a compile error, because the function `MyUserFunction1` has been called before it has been defined. This can easily be remedied by reversing the order:

INTEGER x;

FUNCTION MyUserFunction1()  
{  
print("This is MyFunction1 runnning!\n");}

INTEGER_FUNCTION MyUserFunction2( INTEGER arg1, STRING arg2 )  
{  
print("This is MyFunction2 runnning!\n");}

PUSH someSignal  
{  
call MyUserFunction1();  
x = MyUserFunction2( x, 10 );}

This program compiles without any problems. Due to this dependence on order, the SIMPL+ module template that appears each time a new program is created provides a place to put function definitions. Notice that this section comes after the input/output and variable definitions, but before the event and main functions. Following the layout suggested by the template should prevent most of these errors.

## Defining Local Variables In Functions

The concept of local variables was introduced in the section [Working with Data (Variables)](<../Working_With_Data/TP_Working-with-Data-\(Variables\).htm#All>). In this section we will discuss the topic in greater detail and present a number of examples.

What is a local variable? A local variable is a variable (i.e. an integer or string) with a limited life span and limited scope. You can think of global variables as being immortal. That is, for as long as the control system is plugged in and the program is running, global variables retain their values unless a programming statement modifies them. In addition, global variables can be accessed (either to use their value or to modify them) anywhere in a SIMPL+ program. Here is a simple example:

DIGITAL_INPUT go;  
INTEGER i,j,k; // define 3 global integers

FUNCTION sillyFunction()  
{  
i = j * 2;  
k = i ‑ 1;}

FUNCTION anotherSillyFunction()  
{  
j = i + k;}

PUSH go  
{  
i = 1;  
j = 2;  
k = 3;  
Print("i = %d, j = %d, k = %d\n", i, j, k);  
Call sillyFunction();  
Print("i = %d, j = %d, k = %d\n", i, j, k);  
Call anotherSillyFunction();  
Print("i = %d, j = %d, k = %d\n", i, j, k);}

In this program, it should be clear to see that both of the functions defined, as well as the push event, have access to the three global integers `i`, `j`, and `k`.

Local variables, on the other hand, can only be accessed within the function in which they are defined. If another user‑defined function or event function tries to access a local variable defined elsewhere, a compiler error will be generated. In addition, as soon as the function completes execution, all of the functions' local variables are destroyed. This means that any value they contained is lost. The next time this function is called the local variables are re‑created.

Creating local variables is identical to creating global variables, except that the declaration statement is placed inside of the function definition, as follows:

FUNCTION localExample()  
{  
INTEGER i, count, test;  
STRING s[100], buf[50];}

## Passing Variables to Functions as Arguments

The last section describes how to make your programs easier to read and maintain by defining variables local to functions. However, this does not change the fact that by their very nature most functions require access to one or more variables that have been declared elsewhere in the program, either as global variables or as local variables in a different function. The question is, how can your function access these variables.

As we have already seen, global variables are available everywhere in a program, thus you can simply use such variables to share data between functions and the rest of the program. This is considered bad programming practice, however, and often leads to programs that are hard to read and even harder to debug. Functions can also access any input/output signals defined in the program, but as these signals can be thought of as global variables, this too is not considered good programming practice.

Instead of using global variables to share data, we instead use the concept of passing arguments (also known as parameters) into functions. Arguments can be thought of as an ordered list of variables that are passed to a function by the calling function (the term calling function simply refers to the scope of the code statement which calls the function in question). To define a function’s parameters, you list them inside the parentheses following the function name. A typical function definition would look like this:

FUNCTION some_function (INTEGER var1, INTEGER var2, STRING var3)  
{  
INTEGER localInt;  
STRING localStr[100];

var1 = var1 + 1;  
localInt = var1 + var2;  
localStr = left(var3, 10); }

Notice that the function shown above has three arguments, named `var1`, `var2`, and `var3`. `var1` and `var2` are integers, while `var3` is a string. Shown below is an example of how to call this function from elsewhere in your program:

Call some_function( intVal1, 5+1, stringVal1); 

Here we are assuming that the variable `intVal1` has been defined as an integer earlier in the program, as has the string variable, `stringVal1`. Also note that the second argument is a constant, and not a variable at all. This simply means that inside `some_function`, the value of `var2` will be set to `6`.

### ByRef, ByVal, and ReadOnlyByRef

When defining a function’s argument list, there are optional keywords you can use which give you greater control over the behavior of the arguments. These keywords are ByRef, ByVal, and ReadOnlyByRef.

What do these keywords mean? Essentially they describe the way that SIMPL+ passes variables to the function. When a function argument is defined as ByRef, any variable that is passed to this argument will pass enough information about itself to allow the function to modify the value of the original variable. The term ByRef is used because we say a reference to the original variable is passed to the function. This reference can be thought of the memory location where the original variable lives. When a function argument is defined as ByVal, only the value of the variable and not the variable itself is passed to the function, so the original variable cannot be modified within the function. As an example, below is a function, which takes two strings as arguments. It inserts one string into the other at a specified character location:

Note: When passing STRING arguments by value, you only need to specify the ByVal keyword for 2-series modules. 3-Series and 4-Series STRINGS are passed by value by default, unless ByRef is used.

2-Series Example:

FUNCTION insertString(ByRef STRING string1, ByVal STRING string2, ByVal INTEGER position)

{

STRING leftpart[20], rightpart[20];

leftpart = left(string1,position);

rightpart = right(string1,position);

string1 = leftpart + string2 + rightpart; }

3-series and 4-Series Example:

FUNCTION insertString(ByRef STRING string1, STRING string2, ByVal INTEGER position)

{

STRING leftpart[20], rightpart[20];

leftpart = left(string1,position);

rightpart = right(string1,position);

string1 = leftpart + string2 + rightpart; }

In this example, note that only the first string argument, string1, was defined as ByRef.

## Functions That Return Values

To this point all user‑defined functions we have discussed have had one thing in common: when the functions are finished executing they do not return a value to the calling code. This statement is ambiguous, because some of the functions do modify the values of their arguments, and thus these modified variables can be used by the calling procedure. However, the term return value is used to describe the core value, which is returned from the function to the calling procedure. Many system functions discussed earlier in this manual have return values. For example, here are some statements that use the return values of functions:

String1 = itoa(int1);  
position = find(“Artist”,CD_data);  
int3 = max(int1, int2); 

For clarity, here are some example statements using system functions that do not have return values:

Print(“Variable int1 = %d\n”,int1);  
ProcessLogic();  
CancelWait(VCRWait); 

It should be clear that, at least as far as system functions go, whether or not a function returns a value depends largely upon what that function is designed to do. For example, the `itoa` function would not be very valuable if it did not return a string, which could then be assigned to a variable, or used inside of an expression. On the other hand, the `Print` function simply outputs text to the console for viewing, and thus no return value is needed.

Allowing a user‑defined function to return a value is extremely useful, as it allows such functions to be used in flexible ways, such as inside of an expression. To enable a function to return a value, use a modified version of the function keyword, as shown below:

STRING_FUNCTION strfunc1(); //function returns a string  
INTEGER_FUNCTION intfunc1(); //function returns an integer  
FUNCTION func1(); //function has no return value 

Clearly, functions defined using the `STRING_FUNCTION` keyword will return a string value, and those defined using the `INTEGER_FUNCTION` keyword will return an integer value. Function declared using the `FUNCTION` keyword would have no return value.

Once a function has been declared using the appropriate function type, it is the responsibility of the programmer to ensure that the proper value is returned. This is accomplished using the return function. To illustrate this, examine the following function example, which raises one number to the power determined by the second argument, and returns the result.

INTEGER_FUNCTION power(INTEGER base, INTEGER exponent)  
{  
INTEGER i, result;

if (base = 0)   
return (0);

else if (exponent = 0)  
return (1);

else {  
result = 0; // initialize result  
for (i = 1 to exponent)  
result = result + result * base;

return (result);}}

To use this function in a program, simply call the function just like you would any built‑in system function. Here are a few usage examples:

Print(“5 raised to the power of 3 = %d\n”,power(5,3)); x = power(y,z); 

As a second example, we shall build a function which appends a simple `checksum` byte onto the end of a string. As was mentioned earlier in this manual, `checksum`s are used by many devices to provide a basic form of error checking. In this example, the `checksum` is formed by simply adding up the values of each byte in the command string and then appending the equivalent ASCII character of the result onto the string itself. If the `checksum` value is larger than a single byte (255 decimal), we simply ignore the overflow and use the lower 8-bits of the result.

DIGITAL_INPUT control_device1, control_device2;  
STRING_OUTPUT device1_out, device2_out;  
STRING device1_cmd[20], device2_cmd[20], tempCmd[20];

STRING_FUNCTION appendChecksum(STRING command)  
{  
INTGEGER checksum, i; // define local variables

checksum = 0; // initialize variable

for (i = 1 to len(command)) // calculate the sum   
checksum = checksum + byte(command,i);

return(command + chr(checksum)); //append the byte }

PUSH vcr_play  
{  
vcr_out = appendChecksum(“PLAY”);}

PUSH vcr_stop  
{  
vcr_out = appendChecksum(“STOP”);}

In this example, the system function, `byte`, is used inside the function to get the numeric value of each byte in the string. After the `checksum` has been calculated, the `chr` function is used to append the corresponding ASCII character to the end of the command string. Realize that this example is useful for just one (very simple) type of `checksum`.

## Function Libraries

You are likely to find that the longer you program in SIMPL+ the more you will need to repeat code you have already written. For example, a function that converts the temperature from Celsius to Fahrenheit might come in handy in more than one job.

Clearly, code that has many applications is best placed inside of a function. Remember, however, that unlike system functions, which are globally available, user‑defined functions are only available inside of the SIMPL+ program in which they exist. If you need to use a user‑defined function in more than one SIMPL+ program, you must copy and paste it from one program to another. While this technique works, it can lead to problems when, for example, you find a bug in the function and fix it one program but forget to change it elsewhere.

To solve this problem, SIMPL+ has introduced the concept of function libraries. Simply put, a function library is a collection of user‑defined functions placed in a separate file. A library can consist of only a single function, or can consist of every function you have ever written. More likely, you will organize your libraries so that each one contains related functions. For example, you may create a string handling library, which consists of a number of functions that perform useful operations on stings.

Once a function has been included inside of a function library, it now becomes accessible to all SIMPL+ modules that are made aware of it. To make a SIMPL+ program aware of a particular library, you must use the `#USER_LIBRARY`. To include a user library within a SIMPL+ module, the syntax is as follows:

#USER_LIBRARY "MyStringFunctionLib" 

Note that the file extension (.usl in this case) is left out. The above example refers to the function library called `MyStringFunctionLib.usl`. Any number of user libraries can be included within a SIMPL+ module.

Special function libraries that are created by Crestron and made available to all customers can be used in a similar manner. The only difference is the use of the `#CRESTRON_LIBRARY` compiler directive in place of `#USER_LIBRARY`. Crestron function library files end with the extension .csl.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/User_Defined_Functions/TP_User-Defined-Functions.htm*
