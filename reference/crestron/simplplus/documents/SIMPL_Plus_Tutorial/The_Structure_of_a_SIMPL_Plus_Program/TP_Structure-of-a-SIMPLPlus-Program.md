# The Structure of a SIMPL+ Program

What are the different elements that make up a SIMPL+ program? This section provides an overview of the code structure, given in the typical order that they are used.

## Compiler Directives

Compiler directives should come at the beginning of the program, and they are used to provide explicit instructions to the compiler. As such, these elements are not part of the SIMPL+ language itself. These directives are distinguished from actual SIMPL+ code by preceding them with a pound sign (`#`).

Currently there are thirty compiler directives, nineteen of which are provided in the template file that is created when a new program is started. The compiler directives are as follows.

  * **`#SYMBOL_NAME` ‑**Allows the user to specify the name that SIMPL uses for this module. If this directive is left out, the filename will be used by default.
  * **`#HINT` ‑** Provides text that appears in the SIMPL status bar whenever the module icon is clicked on.
  * **`#CATEGORY` ‑** (SIMPL+ 3.0 and later) Specifies the SIMPL symbol tree category number for this SIMPL+ module, which controls where the SIMPL+ module is listed in the symbol tree in Program Manager. Selecting **Edit** > **Insert Category** from the menu will display a list of available categories to choose from and automatically insert the selected category in to the program module.
  * **`#DEFAULT_VOLATILE` ‑** (SIMPL+ 3.0 and later) Specifies that all program variables will retain their values if hardware power is lost. If neither the **`#DEFAULT_VOLATILE`** nor **`#DEFAULT_NONVOLATILE`** are specified, the compiler will default all variables declared within the SIMPL+ module as nonvolatile.
  * **`#DEFAULT_VOLATILE` ‑** (SIMPL+ 3.0 and later) Program variables will not retain their value if hardware power is lost.
  * **`#HELP_BEGIN / #HELP_END` ‑** Allows online help to be entered for this module. This text appears when the user selects the module and presses F1 from within SIMPL.
  * **`#DEFINE_CONSTANT` ‑** Allows constant numeric/string values to be assigned to alphanumeric names. This is extremely useful for writing changeable and readable code.



This last compiler directive deserves more discussion, since using constant definitions are a very important part of writing readable code. To illustrate this, examine the following example.

PUSH vcr_select  
{  
switcher_input = 3;  
switcher_output = 2; // video projector}  


PUSH dvd_select  
{  
switcher_input = 4;  
switcher_output = 2; // video projector} 

In this example it should be clear that the value of the variable `switcher_input` is being set to `3` if the **VCR** button is pressed or `4` if the **DVD** button is pressed. In both cases the variable, `switcher_output` is set to `2`, which is the output connected to the video projector. Presumably, these variables would be used somewhere else in the program to generate a command string to control a switcher. Using numbers in a small and simple program like this still produces a relatively readable program. Even so, a couple of problems should become evident. For one thing, if the switcher configuration is changed, and the inputs and outputs are rearranged, the user must carefully go through the program and change all the appropriate values for the switcher input and output. Secondly, in a larger program this technique becomes very hard to read. After all, the number 3 has no intrinsic relationship to a VCR.

Examine the following equivalent program, which uses constant definitions in place of actual numbers.

#DEFINE_CONSTANT VCR_INPUT 3  
#DEFINE_CONSTANT DVD_INPUT 4  
#DEFINE_CONSTANT VPROJ_OUTPUT 2 

PUSH vcr_select  
{  
switcher_input = VCR_INPUT;  
switcher_output = VPROJ_OUTPUT; // video projector}

PUSH dvd_select  
{  
switcher_input = DVD_INPUT;  
switcher_output = VPROJ_OUTPUT; // video projector}

Note the use of capital letters for the constant definitions. This is not required, but it makes it clear to see the difference between variables and constants when reading through a program (but of course is not useful if all caps are used for the rest of the program). Not only is this version of the program easier to read, even for a small example, but it is obvious that changing a numeric value in one place (the `#DEFINE_CONSTANT`) can affect the value everywhere in the program.

## Include Libraries

Libraries are a way of grouping common functions into one source file to enable modularity and reusability of source code. Libraries are different from modules in that they do not contain a starting point (`Function Main`), and cannot interact with the control system (through I/O signals and events). Libraries can include other libraries, but cannot include a SIMPL+ module. Only functions and defined constants are allowed to be declared and defined within libraries. Global variable declarations are not allowed. Functions, however, can contain local variables. Other advantages are:

  1. Modularity. SIMPL+ programs can grow to be large and can be better organized by taking sections of code and placing them into a **User‑Library**. It is best to create libraries that contain sets of related functions. For example, a library might be created that contains only functions that perform certain math related functions. Another library might be created that contains functions performing special string parsing routines.
  2. Reusability. As modules are written, it is common for SIMPL+ modules to need pieces of functionality that were previously written in other modules. These common and repeatedly portions of code can be extracted and placed into one or more libraries. Once placed into a library, one or more SIMPL+ modules can include and make use of them.



SIMPL+ modules include libraries using the following syntax:

#USER_LIBRARY “<library_name>”  
#CRESTRON_LIBRARY “<library_name>” 

Note that `library_name` is the name of the library without the file extension. **User‑Libraries** are libraries that the end user writes. These can exist either in the SIMPL+ module’s project directory or in the User SIMPL+ directory (set in SIMPL).

**Crestron‑Libraries** are provided from Crestron and are contained within the Crestron Database.

## Variable Declarations

Variables can be thought of as storage areas to keep data. When writing all but the most basic of programs, users need to use variables to store values.

Any variable used in a SIMPL+ program must be declared before it is used. This also tells the operating system how much space must be reserved to hold the values of these variables. This section describes the different types of variables in SIMPL+ and how to define them.

. 

### Inputs, Outputs, and Parameters

SIMPL+ programs communicate with the SIMPL program in which they are placed through input and output variables and through parameter values. This is similar in concept to the Define Arguments symbol used in SIMPL macros. Input variables can be of three types: digital, analog, and string types. These correspond directly to the same signal types in SIMPL and the buffer input, which is a special case of the string input. Output variables can only be of the digital, analog, or string variety.

Input variables are declared using the following syntax.

DIGITAL_INPUT <dinput1>,<dinput2>,…<dinputn>;  
ANALOG_INPUT <ainput1>,<ainput2>,…<ainputn>;  
STRING_INPUT <sinput1>[size],<sinput2>[size],...<sinputn>[size];  
BUFFER_INPUT <binput1>[size],<binput2>[size],...<binputn>[size];

Note: For more information on the `buffer_input`, refer to [Working with Strings](<../Working_With_Strings/TP_Working-with-Strings.htm>).

Digital and analog output variables are declared in the same way, except the word input is replaced with output, as shown below. String output variables do not include a size value. There is no output version of the buffer variable.

DIGITAL_OUTPUT <doutput1>,<doutput2>,…<doutputn>;  
ANALOG_OUTPUT <aoutput1>,<aoutput2>,…<aoutputn>;  
STRING_OUTPUT <soutput1>,<soutput2>,…<soutputn>; 

The inputs and outputs declared in this way govern the appearance of the SIMPL+ symbols that are presented via SIMPL. The order of the signal declarations is important only within signal types; in SIMPL, digital signals always appear at the top of the list, followed by analogs, and then serials.

### 

###    
Variables

In addition to the input and output variables described in the last section, the user can define and use variables that are only seen by the SIMPL+ program. That is, the SIMPL program, which holds this module has no knowledge of these variables. In addition, any other SIMPL+ modules that are included in the SIMPL program would not have access to these variables.

[Working with Data (Variables)](<../Working_With_Data/TP_Working-with-Data-\(Variables\).htm>) discusses variables in much more detail. For now, understand how to declare them. Declaring variables tells the SIMPL+ compiler how much memory to put aside to hold the workable data.

These variable declarations are very similar to input/output declarations. However, instead of digital, analog, and serial (string and buffer) types, integer and string variables are also available with the `INTEGER` and `STRING` datatype. Integers are 16 bit quantities. For the 2‑series and 3‑series control systems, 32 bit quantities are supported with the `LONG_INTEGER` datatype. Both `INTEGER` and `LONG_INTEGER` are treated as unsigned values. Signed versions for both of these datatypes are available by using the `SIGNED_INTEGER` and `SIGNED_LONG_INTEGER` datatypes. The following example illustrates how each of these datatypes can be used within a program module:

INTEGER intA, intB, intC;  
STRING stringA[10], stringB[20];  
LONG_INTEGER longintA, longIntB;  
SIGNED_INTEGER sintA, sintB;  
SIGNED_LONG_INTEGER slongIntA; 

It is important to realize that all variables declared in this manner are non‑volatile. That is, they remember their values when the control system reinitializes or even if the power is shut off and then turned back on. Since input/output variables are attached directly to signals defined in the SIMPL program, they do not have this property unless the signals they are connected to are explicitly made non‑volatile through the use of special symbols.

### 

### Structures

Sometimes sets of data are needed rather than individual pieces. Variables store a piece of data, but are not related to other variables in any way. Structures are used to group individual pieces of data together to form a related set. Before structures can be used, a structure definition must be defined. Defining a structure is really defining a custom datatype (such as `STRING`s and `INTEGER`s). Once this new type (the `STRUCTURE`) is defined, variables of that type can be declared. The following example illustrates how a structure can be defined and used within a program module:

STRUCTURE PhoneBookEntry  
{  
STRING Names[50];  
STRING Address[100];  
STRING PhoneNumber[20];  
INTEGER Age;};  


PhoneBookEntry OneEntry;  
PhoneBookEntry Entry[500];

To access a variable within a structure, the structure’s declared variable name is used, followed by a period (also known as the dot or dot operator), followed by the structure member variable name. For example:

PUSH BUTTON  
{  
OneEntry.Names="David";  
OneEntry.Address="100 Main Street";  
OneEntry.PhoneNumber="800 555‑5555";  
OneEntry.Age="30";

Entry[5].Names="Andrew";  
Entry[5].Address="15 Volvo Drive";  
Entry[5].PhoneNumber="201 767‑3400";  
Entry[5].Age="23";}

## 

##    
User-Defined Functions

In programming, it is common to reuse the same code over and over again. For example, when writing a program to generate strings (to control a device), there may be a need to calculate a checksum byte. Once the code to calculate this byte is formulated, paste it in to the program after each instance where a command string is created.

Note: The term `checksum` byte is commonly used in serial communications to represent a byte (or bytes) that is appended to a command string. This byte is calculated from the other characters in the string using some specified algorithm. `checksum` bytes are used to provide error-checking when communicating between devices.

This technique has many flaws. First, the program can grow unnecessarily large and become hard to manage and debug. Second, if there is a need to change the code, it must be changed every place it was used, which is time consuming and error prone.

The solution is to create user‑defined functions to perform common tasks. A user‑defined function is very similar to a built‑in function like `Date` or `MakeString`, with some important exceptions.

To invoke a user‑defined function, use the following syntax:

CALL MyUserFunction(); 

## Event Functions

Event functions make up the heart of most SIMPL+ programs. Since a well-designed control system is event‑driven in nature, most code is activated in response to certain events when they occur. Event functions allow the user to execute code in response to some change that has occurred to one or more of the input signals feeding the SIMPL+ module from the SIMPL program.

Two things must be realized about event functions. They can be used with input variables only (not with locally defined variables). Also, they are only triggered by the operating system at the appropriate time (that is, they cannot be called manually by the programmer).

Like everything else in the control system, event functions are multi‑tasking. That is, an event can be triggered even if another event in the same SIMPL+ module is already processing. As described in [Understanding Processing Order](<../Understanding_Processing_Order/TP_Understanding-Processing-Order.htm>), this only happens if events are triggered on the same logic wave, or if one event function has caused a task switch.

The structure of an event function is as follows.

event_type <input list>  
{  
<statements>} 

In SIMPL+ there are three basic event types that can occur: Push, Release, and Change. In addition to these three is a fourth type simply called Event. These event types are discussed in the following subsections.

### 

###    
Push and Release Events

Push and Release events are valid only for `DIGITAL_INPUT` variables. The Push event is triggered when the corresponding digital input goes from a low to a high state (positive‑ or rising‑edge). The Release event occurs when the signal goes from a high to a low (negative‑ or falling‑edge). For example, the following code sends a string to a camera unit to pan left when the left button is pressed and then send a stop command when the button is released.

DIGITAL_INPUT cam_up, cam_down, cam_left, cam_right;  
STRING_OUTPUT camera_command;

PUSH cam_left  
{  
camera_command = "MOVE LEFT";}

RELEASE cam_left  
{  
camera_command = "STOP";}

Note: This example assumes that the camera unit being controlled continues to move in a given direction until a stop command is issued. Some devices function this way, but others do not. 

### 

###    
Change Events

Change events can be triggered by digital, analog, string, or buffer inputs. Anytime the corresponding signal changes its value, the Change event will be triggered. For digital signals, this means that the event will trigger on both the rising and falling edges (push and release). For buffer inputs, this event triggers any time another character is added to the buffer.

The following example sends a command to a CD player to switch to a different disc whenever the analog input `disc_number` changes value.

ANALOG_INPUT disc_number;  
STRING_OUTPUT CD_command; 

CHANGE disc_number  
{  
CD_command = "GOTO DISC " + itoa(disc_number);}

This program uses the `itoa` function to convert the analog value in `disc_number` into a string value which can be concatenated onto `CD_command`. The string concatenation operator (`+`) and system functions (i.e., `itoa`) are discussed in later sections of the manual and in the latest revision of the SIMPL+ Language Reference Guide.

### 

###    
Compound Events

Sometimes it is desired to have the same (or similar) action occur when any of a number of events occur. For example, there may be a need to generate a switcher command string each time any of a group of **output** buttons are pressed.

Compound events can be created in two ways. One way is to provide a list of input signals separated by commas in the event function declaration. Refer to the following example.

PUSH button1, button2, button3  
{  
<statements>}

A second form of compound event occurs when combining different types of events into a single function. For example, there may be a need to execute some code when a button is pushed or the value of an analog signal changes. To accomplish this, stack the event function declarations, as follows.

CHANGE output_value  
PUSH button1, button2  
{  
<statements>} 

A useful feature of SIMPL+ event functions is that a single input can have more than one event function defined for it. This makes it possible to write one event function for a specific input only and another event function for a group of inputs. Refer to the following example.

PUSH button1  
{ // code here only runs when   
// button1 goes high  
} 

PUSH button1, button2, button3  
{ // this code runs when any of  
// these inputs goes high  
} 

### 

###    
The Global Event

A special form of event exists, which is triggered anytime any of the inputs to the SIMPL+ module changes. This is simply a shortcut for having to build a compound event manually which includes all the inputs separated by commas in a `CHANGE` event declaration. Access this special event function by using the `EVENT` keyword, as follows.

EVENT  
{ // this code runs anytime anything   
// on the input list changes  
} 

Be careful when using this global event function. If the user has a SIMPL+ program in which a change on any input causes the same code to execute, this type of event is useful. However, if additional inputs are added at a later time, remember that this event function exists, and it is caused when these new inputs change as well. This may not be desirable.

## 

##    
Function Main

`Main` is a special case of a user‑defined function. The `Main` function is executed when the control system initializes (boots up) and is never called again. In many cases, the `Main` function is used to initialize variables; it may not contain any statements at all.

However, in some cases, a loop may be placed in the `Main` function to perform a continuous action. Refer to the following example, and note that this example uses a `while` loop construct, which is discussed in [Controlling Program Flow: Loops](<../Controlling_Program_Flow_Loops/TP_Controlling-Program-Flow-Loops.htm>).

Function Main()  
{  
Integer x;  
String LocalString[50000];

x = 0;

While (1)

{//<do something forever> code in here runs continuously

LocalString = GatherByLength(2, MyDelimitedString, GATHER_TIMEOUT);

If(Len(LocalString) = 0)//timeout occurred  
{  
ClearBuffer(MyDelimitedString);  
Print "Timeout occurred in Delimited string. \n");  
Break:  
}//code to work with received string}}

This loop runs continuously for as long as the control system is on. If a construct like this is used, it is recommended that a `ProcessLogic` or `Delay` function in the loop be included to allow the logic processor a chance to handle the rest of the system. If one of these statements is not included, the operating system forces a task switch at some point in time. These concepts are discussed in detail in [Understanding Processing Order](<../Understanding_Processing_Order/TP_Understanding-Processing-Order.htm>).

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/The_Structure_of_a_SIMPL_Plus_Program/TP_Structure-of-a-SIMPLPlus-Program.htm*
