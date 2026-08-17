# CMutex

**Name:**

CMutex

**Syntax:**

CMutex mutex;

**Description:**

Mutex is a synchronization primitive that grants exclusive access to the shared resource to only one thread.  If a thread acquires a mutex, the second thread that wants to acquire that mutex is suspended until the first thread releases the mutex.

A mutex object is a synchronization object whose state is set to signaled when it is not owned by any thread and non-signaled when it is owned.  Only one thread at a time can own a mutex object. A mutex is available on startup and can be grabbed using the WaitForMutex call.  The thread that owns a mutex can request the same mutex in repeated calls to WaitForMutex without blocking its execution. However, the thread must call the ReleaseMutex method the same number of times to release ownership of the mutex.

**Class Members:**

class CMutex

{

FUNCTION Close();

FUNCTION ReleaseMutex();

SIGNED_LONG_INTEGER WaitForMutex();

}

**Class Member Description:**

**Close**

This function should be invoked when the program is done using the mutex. This will free all the associated resources.

**ReleaseMutex**

This function is invoked to release the mutex. If the calling thread does not own the mutex then an exception is thrown.

**WaitForMutex**

This function is used to get access to the mutex. This is a blocking call and the thread will block until it can get access to the mutex. Once a thread has access to the mutex, it can call the WaitForMutex function repeatedly without blocking. However, the thread must call the ReleaseMutex method the same number of times to release ownership of the mutex.

While one thread has access to the mutex, another thread will block infinitely until it gets access to the mutex.

**Example:**

DIGITAL_INPUTtest1,test2;

CMutex myMutex;

CEvent myEvent;

PUSH test1

{

INTEGER retVal;

// By default the mutex is not owned by the callee - Use WaitForMutex to grab the mutex. There is no timeout for the WaitForMutex function

// Use ReleaseMutex to release the mutex

// Mutex is used to provide mutual exclusion across two functions. If one thread has the mutex another one cannot

// We need to release the mutex from within the same thread which obtained the mutex

print(" Inside callback for test1 - Try grabbing the mutex \r\n");

myMutex.WaitForMutex();

print(" Inside callback for test1 - Obtained mutex. Now waiting now event which will tell us to release the mutex \r\n");

// Wait for an event to be signaled, then we can then release the mutex

myEvent.Wait(-1);

print(" Releasing the mutex now \r\n");

myMutex.ReleaseMutex();

}

RELEASEtest1

{

print(" Setting the event now which will tell the thread to release the mutex \r\n");

myEvent.Set();

}

PUSHtest2

{

print(" Inside callback for test2 - Try grabbing the mutex \r\n");

myMutex.WaitForMutex();

print(" Inside callback for test2 - Obtained mutex Now waiting now event which will tell us to release the mutex \r\n");

// Wait for an event to be signaled, then we can then release the mutex

myEvent.Wait(-1);

print(" Releasing the mutex now in callback 2\r\n");

myMutex.ReleaseMutex();

}

RELEASEtest2

{

try

{

print(" Inside release callback for test2 - Release the mutex \r\n");

// Release mutex throws an exception if we are trying to release a mutex which we do not own

// This will throw an exception

myMutex.ReleaseMutex();

print(" Inside release callback for test2 - Released the mutex \r\n");

}

catch

{

// This is expected since the thread which owns the mutex has to release it

print(" Exception thrown %s \r\n", GetExceptionMessage());

// Now set the event so that we can release the mutex

myEvent.Set();

}

}

FunctionMain()

{

WaitForInitializationComplete();

// Invoke the function - event will be triggered once since it is set on startup

myEvent.Reset();

}

**Version:**

X Generation: N/A

2-Series: N/A

3-Series: SIMPL v4.02.02+

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Class_Objects/CMutex.htm*
