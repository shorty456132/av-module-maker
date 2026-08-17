# THREADSAFE

Name:

THREADSAFE

Syntax:

THREADSAFE EVENT { }

THREADSAFE PUSH <variable_name> { }

THREADSAFE RELEASE <variable_name> { }

THREADSAFE CHANGE <variable_name> { }

THREADSAFE SOCKETCONNECT <variable_name> { }

THREADSAFE SOCKETDISCONNECT <variable_name> { }

THREADSAFE SOCKETRECEIVE <variable_name> { }

THREADSAFE SOCKETSTATUS <variable_name> { }

Description:

When using the THREADSAFE keyword before an event (such as PUSH, RELEASE, CHANGE) the event is prevented from retriggering, until the entire code block in the event has executed.

Events prevented from triggering WILL be dropped.

Please be aware, that the value of the digital (in case of PUSH and RELEASE) or Analog/Serial (in case of CHANGE) can still change while the THREADSAFE event is running. The THREADSAFE keyword will eliminate the need for adding a programmatic Semaphore to the body of the event.

NOTE: Events prevented from triggering WILL be dropped

Example:

DIGITAL_INPUT DigInp;

THREADSAFE PUSH DigInp

{

// code

}

NOTE: The above example is equivalent to this:

DIGITAL_INPUT DigInp;

INTEGER semaphore;

FUNCTION Main

{

semaphore = false;

}

PUSH DigInp

{

If( semaphore = false )

{

semaphore = true;

// code

semaphore = false;

}

}

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: v3.02.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Events/THREADSAFE.htm*
