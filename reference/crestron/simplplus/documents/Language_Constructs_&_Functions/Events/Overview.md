# Events Overview

SIMPL+ is an event driven language. There are eight functions, or event handlers, which deal with activating events in a given SIMPL+ program; CHANGE, CONNECT, DISCONNECT, EVENT, PUSH, RECEIVE, RELEASE and STATUS.

Event |  Description  
---|---  
[CHANGE](<CHANGE.htm>) |  The CHANGE event is called when a DIGITAL_INPUT transitions from low to high or high to low, or when an ANALOG_INPUT or STRING_INPUT changes.  
[EVENT](<EVENT.htm>) |  Executes the defined <statements> anytime one of the inputs to the SIMPL+ symbol changes. It is similar to having a CHANGE statement listed for every input, and each change is set up to execute a common block of code.  
[PUSH](<PUSH.htm>) |  PUSH is executed when a DIGITAL_INPUT transitions from low to high.  
[RELEASE](<Release.htm>) |  RELEASE is executed when a DIGITAL_INPUT transitions from high to low.  
[SOCKETCONNECT](<../Direct_Socket_Access/SocketConnect.htm>) |  The SOCKETCONNECT event is called when a socket connection is completed on a TCP_CLIENT or TCP_SERVER variable.  
[SOCKETDISCONNECT](<../Direct_Socket_Access/SocketDisconnect.htm>) |  The SOCKETDISCONNECT event is called when a TCP_CLIENT or TCP_SERVER socket is disconnected.  
[SOCKETRECEIVE](<../Direct_Socket_Access/SocketReceive.htm>) |  The SOCKETRECEIVE event is called when a TCP_CLIENT or TCP_SERVER socket receives data.  
[SOCKETSTATUS](<../Direct_Socket_Access/SocketStatus.htm>) |  The SOCKETSTATUS event is called when the status of a TCP_CLIENT or TCP_SERVER socket changes.  
[THREADSAFE](<THREADSAFE.htm>) |  When using the THREADSAFE keyword before an event (such as PUSH, RELEASE, CHANGE) the event is prevented from retriggering, until the entire code block in the event has executed. Events prevented from triggering WILL be dropped.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Events/Overview.htm*
