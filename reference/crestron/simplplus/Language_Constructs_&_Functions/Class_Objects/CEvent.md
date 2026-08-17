# CEvent

**Name:**

CEvent

**Syntax:**

CEvent event;

**Description:**

Event is a synchronization primitive which allows threads to communicate with each other by signaling. The CEvent is signaled on startup. A thread waits on the event by calling “Wait” with the specified timeout ( -1 for infinite). The timeout is specified in milliseconds and is the time that the thread will wait before returning.

Please use the return value to ensure that the thread has access to the event before continuing. Once the CEvent has been signaled, it will wake up the first thread which is blocked on this event. Once that thread has been awakened, the event is reset and subsequent calls on the “Wait” will block and return an error (if a finite timeout is specified) until the event gets signaled again. The event is signaled using the “Set” call.

**Class Members:**

class CEvent

{

FUNCTION Close();

SIGNED_LONG_INTEGER Reset();

SIGNED_LONG_INTEGER Set();

SIGNED_LONG_INTEGER Wait( SIGNED_LONG_INTEGER timeOutInMs );

}

**Class Member Description:**

**Close**

This function should be invoked when the program is done using the event. This will free out all the associated resources.

**Set**

The set function sets the state of the event to be signaled and will wake up a single thread. If there are no waiting threads, the event remains signaled until a thread attempts to wait on it, or until its Reset method is called. Calling a Set on an event which is already set does not do anything.

The function returns a 1 if successful or 0 if failed.

**Reset**

The Reset function is used to set the state of the event to be non-signaled.

The function returns a 1 if successful or 0 if failed.

**Example:**

DIGITAL_INPUTtest1,test2;

CEvent myEvent;

Function ShowEventUsage()

{

INTEGER retVal;

// Wait on the event to happen.

// By default the event is signaled so the first time we come into this function the event will be signaled and we

// will fall through. Subsequent calls will block until the event is signaled using the Set method

// The wait takes a timeout parameter in milliseconds. Pass a -1 for an INFINITE WAIT and a 0 for no timeout

do

{

print(" Waiting for event to get signaled \r\n");

retVal = myEvent.Wait(-1);

if (retVal = 1)

print(" Event signaled \r\n");

else

print(" Event wait failed - Event not signaled \r\n");

} until (0);

}

PUSH test1

{

INTEGER retVal;

retVal = myEvent.Set();

print(" Signaling event Now. Returned %ld \r\n", retVal);

}

RELEASE test1

{

}

PUSH test2

{

}

RELEASE test2

{

}

Function Main()

{

WaitForInitializationComplete();

// Invoke the function - event will be triggered once since it is set on startup

ShowEventUsage();

}

**Version:**

X Generation: N/A

2-Series: N/A

3-Series: SIMPL v4.02.02+

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Class_Objects/CEvent.htm*
