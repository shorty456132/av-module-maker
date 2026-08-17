# #DIGITAL_EXPAND

Name:

#DIGITAL_EXPAND

Syntax:

#DIGITAL_EXPAND <value>

Description:

This provides a way to expand, or add, inputs and/or outputs for a specified symbol. It is useful when you want to expand the number of outputs for a given input, expand the number of inputs for a specific output, expand both the inputs and outputs or for a variety of other combinations.

NOTE: Expansion directives can only be used in conjunction with an array input.

Values:

Value |  Description  
---|---  
Separately |  This is the default value and allows for expansion of both inputs and outputs, in no particular order, on a given symbol.  
OutputsWithParams |  This allows a single input to be expanded into a number of outputs.  
InputsWithOutputs |  This allows the combined expansion of inputs and outputs. If you add an input, an output is also automatically added.  
InputsWithParams |  This allows the expansion of the number of inputs for a single output.  
AllWithAny |  This allows for the expansion of both inputs and outputs, but unlike InputWithOutputs, the relationship between inputs and outputs doesn't have to be one to one.  
PWithIxorO |  This allows for the expansion of either inputs or outputs.  
  
Example:

#DIGITAL_EXPAND OutputsWithParameters InputsWithOutputs

A single input would be expanded into a specified number of outputs.

Version:

SIMPL+ Version 2.10.00 or later

Control System:

2-Series Only

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_DIGITAL_EXPAND.htm*
