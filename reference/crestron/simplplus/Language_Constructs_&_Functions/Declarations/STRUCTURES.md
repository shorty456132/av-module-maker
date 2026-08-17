# STRUCTURES

A structure is a collection of one or more variables grouped together under a single name. These variables, called structure fields or members, may consist of both integer and string datatypes. Structures help organize related data because they allow variables to be grouped together as a unit instead of as separate entities.

Structure datatypes can be defined globally within a SIMPL+ module (*.usp file) and/or within a SIMPL+ library (*.usl file). Variables of a defined structure datatype may be declared both globally and locally and passed as function arguments. Structures are always passed to functions by reference. INTEGER, LONG_INTEGER, SIGNED_INTEGER, SIGNED_LONG_INTEGER and STRING are the only SIMPL+ datatypes allowed to be used as structure member fields. INTEGER and LONG_INTEGER can include 1 and 2 dimensional arrays. String arrays are not permitted.

The syntax for defining a structure is as follows:

STRUCTURE struct_name

{

type member1;

type member2;

.

.

.

type memberN;

};

The keyword, STRUCTURE, tells the compiler that a new datatype is being defined. Each type is one of the SIMPL+ datatypes, INTEGER, LONG_INTEGER, SIGNED_INTEGER, SIGNED_LONG_INTEGER or STRING. struct_name is the name for the structure that will be used as the new datatype.

Declaring a variable of a structure datatype is as follows:

struct_name var_name;

An example of a structure would be an entry in a phone book. The phone book contains many entries, all containing the same three pieces of information: the person’s name, address and phone number. The structure would be defined as follows:

STRUCTURE PhoneBookEntry

{

STRING Name[50];

STRING Address[100];

STRING PhoneNumber[20];

};

PhoneBookEntry OneEntry;

PhoneBookEntry Entry[500];

In this example, the name, PhoneBookEntry, is the datatype defined that will encapsulate the structure fields, Name, Address and PhoneNumber. Two variables are then defined to be of this datatype. The variable, OneEntry, is a variable that contains one instance of the datatype, PhoneBookEntry. The variable, Entry, is then defined to be an array of the datatype, PhoneBookEntry consisting of 501 individual instances, namely Entry[0] to Entry[500].

To access a structure’s field, the structure’s declared variable name is used, followed by a period (also known as the ‘dot’ or ‘dot operator’), then followed by a structure member variable name.

From the example above, accessing the Name field from the declared variable would be written as follows:

OneEntry.Name

or

Entry[5].Name

Using this in a SIMPL+ statement might look as follows:

If ( OneEntry.Name = "David" )

Return;

If ( Entry[5].Name = "David" )

Return;

Passing structures as function arguments is as follows:

FUNCTION myFunction ( PhoneBookEntry argOneEntry,

PhoneBookEntry argEntry[] )

{

if ( argOneEntry.Name = "David" )

return;

if ( argEntry[5].Name = "David" )

return;

}

Version:

X Generation: Not Supported

2-Series: SIMPL v2.02.10 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Declarations/STRUCTURES.htm*
