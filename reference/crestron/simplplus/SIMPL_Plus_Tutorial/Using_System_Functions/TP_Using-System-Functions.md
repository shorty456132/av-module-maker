# Using System Functions

In order to make programming in SIMPL+ simpler and more powerful, the concept of functions is introduced. A function is essentially a more complicated programming task that has been predefined and given a name. Many of the examples in previous sections of this document have used special types of functions called system functions (or built‑in functions). To employ system functions, use the following format.

returnValue = FunctionName(Parameter1, Parameter2,...); 

The above syntax is called a function call, because it tells the function to cause/perform an action. Notice that there are three elements to a function call. First, it is identified by `FunctionName`, which must be unique for every system function. The function name itself is followed by a comma‑separated parameter list enclosed in parentheses. Each function may have a fixed number of parameters, a variable number of parameters, or no parameters at all. These parameters provide the means to supply information to a function. For example, the itoa function converts an integer value into its ASCII equivalent, which is very useful for creating strings to control switchers. The single parameter to this function would be the integer value that needs to be converted. Parameters can be any valid SIMPL+ expression. Consider the statements:

returnValue = itoa(154); // constant param  
returnValue = itoa(input_num); // variable param  
returnValue = itoa(x*5-4); // general expression param 

All are valid function calls.

The variable to the left of the equal sign in the above function calls is used to hold the return value of the function. This value can be either an integer or a string, depending on the nature of the function. Clearly, if a given function returns an integer value, an integer variable must be used to accept this value and a string variable for those functions that return strings. In the itoa examples shown above, the return value is the ASCII string which represents the number being converted. Thus, `returnValue` in this case must be a string variable.

Some functions do not return any values at all. Thus it is not reasonable to assign a variable to a function as shown above. In addition, when using functions that do return values, sometimes the return value may not be needed. In both cases, use the `Call` keyword:

Call FunctionName(Parameter1, Parameter2, ...); 

In this case, if the function being called does return a value, it is ignored.

Be aware as well that some functions may need to return more than one value. Since functions can only have at most a single return value, there are some functions that modify the values of the parameters that are passed to it.

SIMPL+ provides a large number of system functions, which are listed under a number of categories in the latest revision of the SIMPL+ Language Reference Guide. Many of these system functions are used as examples throughout this manual.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Using_System_Functions/TP_Using-System-Functions.htm*
