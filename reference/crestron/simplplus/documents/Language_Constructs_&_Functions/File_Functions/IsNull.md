# IsNull

**Name:**

IsNull

**Syntax:**

INTEGER IsNull( <class_object> )

**Description:**

IsNull can be used to determine whether or not a class or class member variable is valid.

**ReturnValue:**

IsNull will return 1 if the class or class member variable has not been properly initialized, 0 otherwise.

**Example:**

CMutex myMutex;

FUNCTIONInit()

{

INTEGER retVal;

if ( !IsNull(myMutex) )

{

myMutex.WaitForMutex();

}

else

{

print(" myMutex is initialized!\r\n");

}

}

**Version:**

X Generation: N/A

2-Series: N/A

3-Series: SIMPL v4.02.02+

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/IsNull.htm*
