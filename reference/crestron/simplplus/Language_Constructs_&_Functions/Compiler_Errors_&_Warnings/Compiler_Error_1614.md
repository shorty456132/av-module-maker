# Compiler Error 1614

construct error: SocketGetStatus can only be used with a SOCKETSTATUS event.

SocketGetStatus can only be used within the SOCKETSTATUS event. It cannot be used inside any other declared function or event type.

The following are examples of this error:

SOCKETSTATUS MyServer

{

SIGNED_INTEGER Status;

Status = SocketGetStatus(); // ok

}

SOCKETRECEIVE MyServer

{

SIGNED_INTEGER Status;

Status = SocketGetStatus(); // error

}

Function MyFunc()

{

SIGNED_INTEGER Status;

Status = SocketGetStatus(); // error

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1614.htm*
