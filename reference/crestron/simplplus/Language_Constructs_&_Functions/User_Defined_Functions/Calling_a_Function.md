# Calling a Function  
  
When calling a function where the return is being used, the syntax is:

<variable> = <function_name>([argument_list]);

For example,

INTEGER X, ANALOG1, ANALOG2;

STRING Q$[20], B$[50];

X = ComputeChecksum(Analog1, Analog2);

Q$ = DoSomething(Analog1, B$);

Are legal.

If the return is not going to be used, or there is no return (in the case of a FUNCTION), the syntax is:

<CALL> <function_name>([argument_list]);

For example,

CALL DoSomethingElse(); (X-Generation or 2-Series)

or

DoSomethingElse() ; (2-Series only)

NOTE: (X-Generation only) Functions do not support recursion, i.e. the code in the body of a function may not contain a call to that function.

NOTE: The keyword, CALL, is required in the X-Generation control system, and optional in the 2-Series control system. CALL may not be used when calling non-user defined functions. For example: CALL Print( str, "abc" ); // Illegal

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/User_Defined_Functions/Calling_a_Function.htm*
