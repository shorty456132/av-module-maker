# Compiler Error 1602

construct error: Switch statement contains 'default' without 'case' labels

The Switch and CSwitch constructs must contain ‘case’ statements if the ‘default’ statement is to be used. The ‘default’ statement is optional.

The following are examples of this error:

FUNCTION MyFunc( INTEGER x )

{

Switch ( x )

{

case (1): // ok

{

}

default: // ok

{

}

}

CSwitch ( x )

{

case (1): // ok

{

}

default: // ok

{

}

}

Switch ( x )

{

default: // error – no Case statement in Switch

{

}

}

CSwitch ( x )

{

default: // error – no Case statement in Switch

{

}

}

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1602.htm*
