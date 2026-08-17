# SocketReceive

Name:

SocketReceive

Syntax:

SocketReceive ClientVariable

{

// user code for routine

// make sure that the buffer is empty so we can receive new data ClearBuffer(UDP_Variable.SocketRxBuf);

}

NOTE: ClientVariable used as an example. ServerVariable and UDP_Variable also apply.

Description:

The RECEIVE event is called when a TCP_CLIENT, TCP_SERVER or UDP_SOCKET socket receives data. The Rx$ field of the [SOCKET_STRUCT](<Direct_Socket_Access_Functions_Overview.htm>) contains the data.

(See also [THREADSAFE](<../Events/THREADSAFE.htm>))

NOTE: The RECEIVE event is comparable to a CHANGE event on the Rx$ field of the socket structure.

NOTE: Due to the nature of UDP traffic, each UDP datagram must be processed before the next can be received. For SIMPL+, this means that the buffer must be emptied before the next packet can be received. Please use the ClearBuffer() SIMPL+ routine for this.

Parameters:

ClientVariable: the socket variable declared in the input/output section.

ServerVariable: the socket variable declared in the input/output section.

UDP_Variable: the socket variable declared in the input/output section

Example:

In the case of Direct Socket Access Functions and events, the example code is best when viewed in the context in which it applies. For that reason, the example code for this event can be viewed by clicking [here](<Direct_Socket_Access_Example_Code.htm>). A scrolling pop up will open for your convenience.

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Direct_Socket_Access/SocketReceive.htm*
