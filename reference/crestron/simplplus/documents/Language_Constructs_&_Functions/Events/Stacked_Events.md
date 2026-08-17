# Stacked Events

Stacked Events

Refers to multiple CHANGE, PUSH, or RELEASE functions followed by a single block of code (complex statement).

NOTE: Only CHANGE, PUSH, or RELEASE functions are used in stacked events. If necessary, refer to the descriptions of each function for details.

A typical event statement may appear as:

PUSH var1, var2

{

// code

}

SIMPL+ allows event stacking, which allows a block of code to be called from different CHANGE, PUSH, or RELEASE statements. An example is:

STRING_INPUT A$[100];

DIGITAL_INPUT IN1, IN2, IN3, IN4;

ANALOG_INPUT LEVEL;

ANALOG_INPUT PRESETS[5];

PUSH IN1

PUSH IN2

CHANGE IN3, LEVEL, A$, PRESETS

RELEASE IN3, IN4

{

// code

}

This allows one piece of code to execute from many different types of event statements.

NOTE: An input signal can be used in more than one event function. The order of execution is as follows:   
The order for a PUSH:  
PUSH statements in the order they appear in the source.  
CHANGE statements in the order they appear in the source EVENT statement.   
  
The order for a RELEASE:  
RELEASE statements in the order they appear in the source.  
CHANGE statements in the order they appear in the source EVENT statement.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Events/Stacked_Events.htm*
