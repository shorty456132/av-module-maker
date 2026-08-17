# Compiler Error 1607

construct error: GetLastModifiedArrayIndex may return an ambiguous

signal index

If an event function (EVENT, PUSH, CHANGE, RELEASE) is acting on more than one input array signal, the specific array will not be able to be determined based on the index returned from GetLastModifiedArrayIndex(). In order to use GetLastModifiedArrayIndex() for multiple input signal arrays, a separate event function will have to be defined for each array.

The following are examples of this error:

DIGITAL_INPUT digIn[10];

ANALOG_INPUT anlgIn[10];

PUSH digIn

{

INTEGER i;

i = GetLastModifiedArrayIndex(); // ok – index from digIn

}

PUSH anlgIn

{

INTEGER i;

i = GetLastModifiedArrayIndex(); // ok – index from anlgIn

}

CHANGE digIn, anlgIn

{

INTEGER i;

i = GetLastModifiedArrayIndex(); // error – ambiguous result

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1607.htm*
