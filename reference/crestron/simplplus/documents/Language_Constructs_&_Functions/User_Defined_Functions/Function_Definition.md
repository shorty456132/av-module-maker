# Function Definition

<function_type> <function_name> ([argument list])

{

<statements>

[RETURN <expression>;]

}

The table shown below demonstrates what <function_type> may be, what it means, and what data may be returned to the caller. Note that in all cases, a RETURN is not required, as the system defaults it to a shown specified value.

<function type> |  MEANING |  RETURN VALUE  
---|---|---  
FUNCTION |  Returns no data to the caller. |  No RETURN  
INTEGER_FUNCTION |  Returns an integer value to the caller. |  INTEGER expression (default 0)  
LONG_INTEGER_FUNCTION |  Returns a long integer value to the caller. |  LONG_INTEGER expression (default 0)  
SIGNED_INTEGER_FUNCTION |  Returns a signed integer value to the caller. |  SIGNED_INTEGER expression (default 0)  
SIGNED_LONG_INTEGER_FUNCTION |  Returns a signed long integer value to the caller. |  SIGNED_LONG_INTEGER expression (default 0)  
STRING_FUNCTION |  Returns a string value to the caller. |  STRING expression (default "")

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/User_Defined_Functions/Function_Definition.htm*
