# Compiler Error 1329

**declaration error: Class name exists in one or more namespaces. **

**Fully-qualified name must be specified: ‘<class_name>’**

SIMPL# Libraries can contain multiple namespaces, each of which can contain one or more classes. Class names do not have to be unique when used in different namespaces. For example, namespaceA and namespaceB can each contain a class named, ‘MyClass’.

Using the example above, if SIMPL+ were to declare a variable of type, ‘MyClass’, the compiler would not know which namespace to use and would result in an ambiguous declaration. For SIMPL+ to resolve this error, the fully-qualified name must be specified.

Fully-qualified names are represented by specifying both the namespace and class name, using the dot-notation to separate them. The SIMPL+ declaration would be: ‘namespaceA.MyClass <variable_name>’.

The following are examples of this error:

SIMPL# Library

// SimplSharpLibrary.clz

namespace MyNamespace1

{

public class MyClass

{

public int intVar();

}

}

namespace MyNamespace2

{

public class MyClass

{

public int intVar();

}

}

SPlusModule.usp

// UserModule.usp

#USER_SIMPLSHARP_LIBRARY "SimplSharpLibrary"

MyClass class1; // error – compiler doesn’t know

whether MyClass is from

MyNamespace1 or MyNamespace2

MyNamespace1.MyClass class1; // ok – fully-qualified name is used

MyNamespace2.MyClass class2; // ok – fully-qualified name is used

FUNCTION MyFunc()

{

Class1.intVar = 1; // ok – use SIMPL+ variable as normal

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Error_1329.htm*
