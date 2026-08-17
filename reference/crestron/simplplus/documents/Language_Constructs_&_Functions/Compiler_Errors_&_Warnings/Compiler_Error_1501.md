# Compiler Error 1501

function argument error: Argument <arg_num> cannot be passed by value

In SIMPL+, arrays can only be passed by reference. The keyword, ByVal, cannot be used within a function’s argument list in conjunction with arrays. A copy of an individual element within an array must first be copied into an INTEGER or STRING variable and then that variable can be passed.

Pass by Reference – The function will act directly on the variable that was passed as the argument. Any changes to the variable within the called function the will be reflected within the calling function.

Pass by Value – The function creates a local copy of the source variable. Any changes to this local copy are not reflected in the source variable that was originally passed to the function. The source variable will still retains it’s original value from before the function was called.

The following are examples of this error:

FUNCTION MyFunc( ByVal INTEGER intArr[] ) // error – arrays cannot be

// passed by value

{

}

FUNCTION MyFunc( ByVal STRING strArr[] ) // error – arrays cannot be

// passed by value

{

}

FUNCTION MyFunc( ByVal INTEGER intArr[][] ) // error – arrays cannot be

// passed by value

{

}

FUNCTION MyFunc( ByVal STRING strArr[][] ) // error – arrays cannot be

// passed by value

{

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1501.htm*
