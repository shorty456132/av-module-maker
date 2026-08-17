# Working with Data (Variables)

Programming is really the manipulation of data. Examples of data in a program are the `switcher` input and output numbers, the name of the next speaker and the amount of time left before the system shuts down automatically. This section covers the different data types available in SIMPL+.

## Input/Output Types

Input/output variables are used to transfer data between SIMPL+ modules and the surrounding SIMPL program. Each input or output variable in SIMPL+ is connected directly to a signal in the SIMPL program. SIMPL programmers should already be familiar with the three signal types available in that language: digital, analog, and serial. The table below takes a closer look at the type of data conveyed by these signal types.

SIMPL Signal Styles Signal Type | Data | Example  
---|---|---  
Digital | Single bit | Button push/release  
Analog | 16-bit (0 to 65,535) | Volume level  
Serial | Up to 255 bytes | Serial data input from a COM port  
  
This table illustrates that digital signals only transfer a single bit of information between SIMPL+ and SIMPL. Of course this makes sense, as digital signals only have two possible states (on and off). Obviously, analog and serial signals allow the transfer of much more information per signal. Depending on the application, it may be more convenient to generate an analog signal in SIMPL and connect it to a SIMPL+ program, rather than connecting a large number of digital signals and setting some variable based on which was pressed last (though both methods should work).

### Digital Inputs/Outputs

Digital signals comprise the bulk of signals in a typical SIMPL program. In SIMPL+ they are used mainly to trigger events on the rising‑ or falling‑ edge of the signal, though they can also be used in expressions.

The state (or value) of a digital signal is always either 1 or 0 (also referred to as On or Off). In SIMPL+, assigning a value of 0 to a digital signal turns it Off. Assigning it any non-zero value will turn it On (for clarity, in most cases, use the value 1).

### Analog Inputs/Outputs

Analog signals are used in SIMPL to accomplish tasks for which digital signals are inadequate. Typical examples include volume control and camera pan/tilt control. In SIMPL+, analog signals take on even greater importance since they provide an easy way of transferring data (16 bits at a time) into and out of SIMPL+ modules.

In SIMPL+, analog signals are treated much as they are in SIMPL. They are 16-bit numbers that can range between 0 and 65,535 (unsigned) or ‑32768 and +32,767 (signed). Signed and unsigned numbers are discussed in detail in Working with Data (Variables).

### String Inputs/Outputs and Buffer Inputs

Perhaps the greatest advantage that SIMPL+ provides is related to string handling. In SIMPL, serial data can be generated dynamically and placed on serial signals. However, one problem that arises is due to the transient nature of these signals. Simply put, serial signals are invalid except for the time between when they are created and when they reach the next symbol. With careful programming this does not cause problems, but it requires a good understanding of SIMPL.

SIMPL+ makes working with serial data much simpler by storing this data into temporary string variables. When a serial signal is connected to a SIMPL+ module and the SIMPL program causes data to be sent via this signal, the SIMPL+ program copies the data from this signal into local memory. The data is kept there until the SIMPL program changes it.

By storing the serial data into a string variable, SIMPL+ programmers can now perform tasks on strings that were difficult or impossible with SIMPL alone. For example, it is easy to evaluate a string and then add a `checksum` byte on the end to insert or remove characters from a string, or to parse information out of a string for use elsewhere. Functions that are designed to work explicitly with string signals and string variables are discussed in detail in the latest revision of the SIMPL+ Language Reference Guide.

Serial data is also unique in that unlike digital or analog signals, the data may not appear at one time, but instead it can stream in (e.g., if it comes from a COM port). This raises an interesting problem, namely, what happens if a command string coming in from a device is not picked up as one piece, but rather is broken up into two or more pieces? The problem arises in that a string input is completely replaced each time new data is detected on the input. To account for this, an alternate type of serial input type may be used, the buffer input. The buffer input differs from the string input in that serial data that comes in is appended onto data that already exists in the buffer, instead of replacing it. This type of behavior is critical for performing sophisticated string parsing and manipulation when dealing with streaming data. Refer to [Working with Strings](<../Working_With_Strings/TP_Working-with-Strings.htm>) for a detailed discussion of buffer inputs.

### Signal Scope

Signals are global throughout the entire SIMPL program and to any SIMPL+ program to which they are connected. In a SIMPL+ program, the values of digital, analog, and string inputs are read (their values can be evaluated). However, their values cannot be changed from within the SIMPL+, thus they are considered read‑only. Buffer inputs can be read from and modified.

Digital and analog output signals in SIMPL+ can be read and modified. String outputs can be modified, but cannot be read back. To understand this, the user must realize what is being seen when looking at the contents of an output variable in a SIMPL+ program. The value of any output is the value of the signal as seen by the outside SIMPL program at that instant. This is critical considering that SIMPL+ does not necessarily propagate outputs to the SIMPL program each time they are changed in the program. As a general rule, assume that analog and serial outputs are propagated at the time they are assigned new values. However, digital signals are not propagated until a task switch occurs.

This explains reading values of analog and digital outputs, but why is it that string outputs cannot be read? The reason has to do with the nature of serial signals in SIMPL. Namely that these signals do not actually store strings in them, but rather point to locations in memory where a string exists. Since the data stored at a particular location in memory can change at some later time, there is no guarantee that the string data is still there. As a result, SIMPL+ does not allow a string output to be examined.

Examine the following code example.

DIGITAL_OUTPUT d_out;  
ANALOG_OUTPUT a_out;  
STRING_OUTPUT s_out; 

PUSH someEvent  
{  
d_out = 1; // set this digital output to ‘on’   
a_out = 2000; // set this analog output to 2000  
s_out = "hello"; // set this string output to "hello" 

if (d_out = 1) // this WILL NOT be true until the Print ("d_out is on\n"); // next task-switch

if (a_out = 2000) // this WILL be true Print ("a_out = 2000");

if (s_out = "hello") // this WILL NOT be true due to the Print ("s_out is hello"); // nature of serial signals

ProcessLogic(); // force a task-switch

if (d_out = 1) // NOW this is true Print ("d_out is on\n");   
}

Function Main() // initialization  
{  
d_out=0;  
a_out = 0;}

In this example, the digital output, `d_out`, and the analog output,` a_out`, are set to `0` on system startup in the `Function Main`. In the `push` function, the first conditional `if` statement evaluates to `False` because the digital output signal, `d_out`, is considered `Off` until this value is propagated to the SIMPL program. With digital outputs, this does not happen until the SIMPL+ program performs a task switch. The analog and string outputs, on the other hand, are propagated as soon as they are assigned new values. Thus the second `if` condition evaluates to `True` and the subsequent `print` statement is executed. The third `if` statement can still evaluate to `False`, however, due to the nature of serial signals in SIMPL, as previously described.

Notice the `ProcessLogic` function call in the last example. This function forces a task switch from SIMPL+ to the SIMPL logic processor. This causes the digital signal to be propagated out to the SIMPL program. The next time the logic processor passes control back to this SIMPL+ program, it picks up where it left off. As a result, the fourth `if` condition evaluates to True, thus executing the print statement.

Note: The `if` language construct is described in detail in [Controlling Program Flow: Branching](<../Controlling_Program_Flow_Branching/TP_Controlling-Program-Flow-Branching.htm>). Evaluation of True and False expressions are covered in [Operators, Expressions, and Statements](<../Operators,_Expressions_and_Statements/TP_Operators, Expressions, and Statements.htm>). 

## All About Variables

In addition to input and output signals, additional variables can be declared that are only used inside the SIMPL+ program. That is, the outside SIMPL program has no knowledge of these variables and no access to them. These variables are critical for use as temporary storage locations for calculations.

Unless otherwise specified with a compiler directive, all variables in SIMPL+ are volatile, which means that they do not remember their values if power is lost. The compiler directive, `#DEFAULT_NONVOLATILE`, can be used to change this behavior so that the variable's values are retained after power is lost. Notably, it is generally a good idea to explicitly initialize variables to some value before using them, except in the cases where it becomes necessary to take advantage of their non‑volatility. An obvious place to do this is in `Function Main`.

SIMPL+ allows for two different types of variables: integers and strings. In addition, variables of either type may be declared as one‑ or two‑dimensional arrays. The following sections explain these topics in detail.

### Integers

Integers contain 16‑bit whole numbers. That is, they can range between 0 and 65,535 (unsigned, refer to paragraph after example) and cannot contain a decimal point. SIMPL programmers may recognize that this range is identical to that of analog signals. This is because analog signals are also treated as 16‑bit values.

Integers are declared as follows:

INTEGER <int1>, <int2>,…,<intn>; 

Depending on how they are used, integers can either be unsigned or signed. Unsigned integers have values between 0 and 65,535. Signed integers have values between ‑32768 and +32767.

In reality, there is no difference between a signed and unsigned integer, the difference is solely in how the control system views them. That is, for any given value, that number can be thought of as either being a signed number or an unsigned number. Depending upon which operations are perform on a number, the control system decides whether to treat that number as signed or unsigned.

When an integer has a value of between 0 and 32767, it is identical whether it is considered signed or unsigned. However, numbers above 32767 may be treated as negative numbers. If they are, they will have a value of x ‑65536, where x is the unsigned value of the number. This means that the value 65,535 has a signed value of ‑1, 65534 is ‑2, etc. This scheme is referred to as two’s complement notation.

Why is all this signed/unsigned discussion important? Well, in most cases, it can be ignored and things work out fine. However, for those instances when it does make a difference, it pays to understand how to debug programs that are not working as expected.

In control system programming, often there is not a need for negative numbers (e.g., how often is a switcher switched to input number ‑12 ?). As a result, the most common operations treat integers as unsigned and it becomes necessary to use special signed operators or functions when treating numbers as signed. The table after this paragraph lists operators and functions that are unsigned and those that are signed. Any operators or functions that are not shown here do not need special consideration.

Unsigned/Signed Operators and Functions  Description | Unsigned Operators/Functions | Signed Operators/Functions  
---|---|---  
Less than | < | S<  
Less than or equal to | <== | S<=  
Greater than | > | S>  
Greater than or equal to | >= | S>=  
Integer division | / | S/  
Maximum | Max() | SMax()  
Minimum | Min() | SMin()  
  
Examine the following:

INTEGER j, k; 

Function Main()  
{  
j = 2;  
k = -1; // this is the same as k = 65535

if (j > k) // this will evaluate to FALSEPrint( “j is bigger as unsigned numbers\n” );

if (j S> k) // this will evaluate to TRUEPrint( “j is bigger as signed numbers\n” );}

In this example, the first condition, `j > k`, evaluates to `False` and the `Print` statement does not execute. This is because the `>` operator performs an “unsigned greater than” operation. If both `j` and `k` are converted to unsigned values, `j` remains at `2`, but `k` becomes `65,535`, and thus `k` is obviously not smaller than `j`.

The second condition, `j S> k`, evaluates to `True`, because this time the “signed greater than” operator was used.

Examine one more example:

INTEGER a, b, c, d;

Function Main()  
{  
a = 100;  
b = ‑4;

c = a / b; // c = 0 (100/65532)  
d = a S/ b; // d = ‑25 (100/‑4)} 

Notice that `c` calculates to `zero` because the `/` operator is unsigned. It treats the variable `b` as `+65,532`. Since the `/` operator truncates the decimal portion of the result, `c` becomes `zero`. In regard to the variable `d`, since the signed division operator `S/` was used, `b` is treated as `‑4` and the result is `‑25`.

A final note regarding signed/unsigned integers, if an operation results in a number that is greater than 65,535 that number overflows and the value wraps around again starting at zero. This allows certain operators (e.g. +, ‑, and *) to operate with no regard to sign (the result is accurate when thinking of the numbers as signed or unsigned). This also means that when trying to add (or multiply) two unsigned numbers and the result is greater than 65,535, the answer may not be what is expected.

### Strings

String variables are used to hold multiple characters in a single variable. The term string is used to illustrate the act of stringing together a number of characters to produce words, sentences, etc. Typically strings in SIMPL+ are used to hold things such as serial commands, database records, and so on.

Strings are declared as follows:

STRING <string1[size]>, <string2[size]>,…,<stringn[size]>; 

The number in square brackets following the variable name defines the size of the string variable. When declaring strings, choose a size that is large enough to hold any amount of data that might be needed, but that is not overly large so as to waste space. That is, it is unnecessary to set the variable size to 100 characters when a given variable in an application does not contain more than 50 characters.

Working with strings is not unlike working with other variable or signal types. To assign a value to a string, for example, do the following:

STRING myString[50];  
myString = "Tiptoe, through the tulips\n"; 

In the example above, a variable called `myString` is declared, which can contain up to 50 characters of data. The value, `Tiptoe, through the tulips\n`, is the value being assigned to the variable. The double-quotation marks surrounding the data defines a literal string expression. That is, a string expression which is defined at compile‑time (when the program is compiled) and cannot change during run-time (while the program is running). Also note the `\n` at the end of this string literal. This represents a newline, or a carriage return followed by a line feed. This character combination is used often, so a shortcut was developed. For a complete list of similar shortcuts, refer to the latest revision of the SIMPL+ Language reference Guide. Finally, note that the square brackets were not included after the variable name, as was done when it was declared. When assigning a value to a string, that value is always assigned starting at the first character position.

It is important to note that the length of the this value does not exceed total length allocated for `myString` (in this case, 50 characters). If the declared variable is not large enough to hold the data being assigned to it, the data is truncated to as many characters as the string can hold. Also, when the program is being executed, a string overflow error will be reported within the control system’s error log.

The example above is useful, but does not really begin to tap the enormous string‑generating capabilities of SIMPL+. A common task in control system programming is the control of an audio/video matrix switch. To control such a router, often it is necessary to specify the input and output which make up the desired matrix crosspoint. As an example, assume the device to be controlled expects to see a command in a format, shown as follows:

IN<input#>OUT<output#><CR><LF>

This protocol allows the input and output to be specified as numbers. For example, to switch `input 4` to `output 10`, the command would be as follows:

IN4OUT10<CR><LF>

Where `<CR><LF>` represents the carriage return and line feed characters. Obviously, for a router of any significant size, the number of possible crosspoints can grow very large. Thus creating a literal string expression for each case would be very inefficient. Instead, build the control string dynamically as the program runs. An easy way to do this is through the use of the string concatenation operator (`+`). Note that this is identical to the addition operator, but the SIMPL+ compiler is smart enough to know whether integers are added or string expressions are concatenated.

This is addressed in the following code:

DIGITAL_INPUT do_switch;  
STRING_OUTPUT switcher_out[10];  
INTEGER input, output; 

PUSH do_switch  
{   
switcher_out = "IN" + itoa(input) + "OUT" + itoa(output) + "\n";}

In this example, the `+` operator is used to concatenate multiple string expressions. The itoa function has been used, which converts an integer value (in this case from analog input signals) into a string representation of that number (e.g. 23 becomes “23”).

There is an alternate way to build strings in SIMPL+. The `MakeString` function provides functionality similar to the concatenation operator, while providing a bit more power and flexibility. The following line is equivalent to the concatenation statement above:

MakeString( switcher_out, "IN%dOUT%d\n", input, output ); 

This syntax is a bit more confusing. The first argument to the `MakeString `function, `switcher_out`, is the destination string. This is where the resulting string created by `MakeString` is placed. The second argument, the part embedded in double-quotation marks, is the format specification. This determines the general form of the data.

Notice how the constant parts of the string are entered directly. The interesting thing about the format specification is the `%d` sequences, which are known as type specifiers.

### Variable Scope

Variable declarations in a SIMPL+ program can be either global or local. Global variables are defined in the Define Variables section of the code, and exist throughout the entire SIMPL+ program. This means that any event function or user‑defined function can reference and modify global variables. When the value of a global variable is being set or modified, it is reflected throughout the entire program.

Local variables are defined inside a function declaration and exist only inside that particular function. In other words, if a local variable, `byteCount`, were defined inside of a function, `CalcChecksum`, any reference to `byteCount`, outside of the scope of this function (e.g. in another function) will result in a compiler syntax error. Note that different functions can use the same variable names when defining local variables. Take a look at the following example:

// simple function to add up all the bytes in a  
// string and append the sum as a single byte   
// onto the original string.  
String_Function CalcChecksum(STRING argData)  
{  
INTEGER i, checksum; 

checksum = 0;

for (i = 1 to len(argData))  
checksum = checksum + byte(argData,i);

return (argData + chr(checksum));} 

In this example, `i` and `checksum` are local variables that only exist inside the function, `CalcChecksum`. This example also introduces an additional way to implement a local variable: by passing it as an argument to the function, as was done with the `STRING` variable, `argData`. The concept of local variables and argument passing is discussed in detail in the section [User Defined Functions](<../User_Defined_Functions/TP_User-Defined-Functions.htm>).

While the use of global variables may seem simpler, local variables can help keep your programs better organized and easier to debug. A significant disadvantage of global variables is that you must be careful each time you use or modify a variable that it does not have an adverse effect on another part of the program. Since local variables can only be used inside of a function, this is not a concern.

## Arrays

When `INTEGER` or `STRING` variables are declared, the user may also declare them as one‑ or two‑dimensional (Integers only) arrays. An array is a group of data of the same type arranged in a table. A one‑dimensional array can be thought of as a single row with two or more columns, while a two-dimensional array can be thought of as a table with multiple rows . In SIMPL+, arrays are declared as follows.

INTEGER myArray1[15] // 1-D integer array with 16 elements   
INTEGER myArray2[10][3] // 2-D integer array with 11x4 elements   
STRING myArray3[50][8] // 1-D string array with 9 elements 

The first two examples above define `1D` and `2D` integer arrays, respectively. The last example looks like it declares a `2D` array of strings, yet the comments states that it actually declares a `1D` array of strings. Recall that in Working with Data (Variables), it was necessary to define the maximum size of the string in square brackets, which is the same notation used for arrays. So, in the example above, nine-element array of 50‑byte strings is being declared. The user cannot declare a `2D` array of strings in SIMPL+.

Another question should have come to mind from the above examples. That is, why does declaring `myArray1[15]` create an array with 16 elements instead of 15? The answer is that array elements start at 0 and go to the declared size (15 in this case). This fact makes for an easy transition to SIMPL+ for programmers of other languages (some of which start at 0 and others which start at 1). That is, if the user is comfortable with treating arrays as starting with element 0, then the user can continue programming in this manner. If however, the user has used languages, which treat the first element in an array as element 1, then the user may want to use that notation instead.

To reference a particular element of an array when programming, use the variable name followed by the desired element in square brackets. Using the arrays declared in the example above, the following statements are all valid in SIMPL+.

j = 5; // set an integer variable to 5   
myArray1[3] = j; // set the 3rd element of the array to 5   
myArray1[j*2] = 100; // set the 10th element of the array   
// to 100

myArray2[j][1] = k; // set the j,1 element of myArray2 to   
// the value of k

m = myArray2[j][k-1]; // set the variable m to the value in   
// the j,k‑1 element of myArray2

myArray3[2] = "test"; // set the 3rd element of the string  
// myArray3 to "test"

From these examples, it should be clear that the user may use constants, variables, or expressions (discussed in [Operators, Expressions, and Statements](<../Operators,_Expressions_and_Statements/TP_Operators, Expressions, and Statements.htm>)) inside of the brackets to access individual array elements. Array elements can appear on either side of the assignment (`=`) operator. That is they can be written to (left side) or read from (right side). Of special interest is the notation used for storing a value into the string array `myArray3`. Notice that only one set of brackets was used here even though two sets of brackets are needed when declaring the array. Remember that the first set of brackets in the declaration specified the size (in characters) of each string element. Also recall from earlier in this section, that the size field is not included when referring to strings. For example, refer to the following.

myString = "hello!"; // we do not use the size brackets here   
// to assign a value to a string variable

As a result, when working with string arrays, only use one set of brackets, which refer to the array element, not the string size.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Working_With_Data/TP_Working-with-Data-%28Variables%29.htm*
