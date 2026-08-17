# PARAMETER_PROPERTIES

Parameters in SIMPL+, have certain attributes by default (see [INTEGER_PARAMETER](<../Declarations/INTEGER_PARAMETER.htm>), [LONG_INTEGER_PARAMETER](<../Declarations/LONG_INTEGER_PARAMETER.htm>), [SIGNED_INTEGER_PARAMETER](<../Declarations/SIGNED_INTEGER_PARAMETER.htm>), [SIGNED_LONG_INTEGER_PARAMETER](<../Declarations/SIGNED_LONG_INTEGER_PARAMETER.htm>), [STRING_PARAMETER](<../Declarations/STRING_PARAMETER.htm>) for more information) 

Parameters may be further restricted by declaring parameter Properties. The general format is below.

NOTE: Note all combinations below can or should be used at the same time.

Syntax:

#BEGIN_PARAMETER_PROPERTIES parameter_variable[, parameter_variable ...]

propValidUnits= unitString or unitDecimal|unitHex|unitPercent|unitCharacter|unitTime|unitTicks;

propDefaultUnit=unitString or unitDecimal or unitHex or unitPercent or unitCharacter or unitTime or unitTicks;

propDefaultValue=default_value or "default_value";

propList={ "value","label" },{ "value","label" };

propBounds=lower_bound , upper_bound;

propShortDescription= "status_bar_hint_text";

#BEGIN_PROP_FULL_DESCRIPTION

line_1

...

line_n 

#END_PROP_FULL_DESCRIPTION

#BEGIN_PROP_NOTES

line_1

...

line_n

#END_PROP_NOTES

#END_PARAMETER_PROPERTIES

NOTE: The values unitString unitDecimal or unitHex or unitPercent or unitCharacter or unitTime or unitTicks used with propValidUnits and propDefaultUnit are actual keywords and should be specified accordingly.

NOTE: The keywords used to describe the properties ValidUnits, DefaultUnits, DefaultValue, List, Bound, ShortDescription, FullDescription and Notes are prefixed by the word "prop" in this directive (e.g., propValidUnits. propDefaultUnit, etc.). This applies only to this directive.

NOTE: The keywords used to describe the units Decimal, Hex, Percent, Character, Time and Ticks are prefixed by the word "unit" in this directive (e.g., unitDecimal. unitString, etc.). This applies only to this directive.

Description:

The parameter properties directive is used to restrict the behavior of parameters, similar to the way property sheets are used in SIMPL to modify the behavior of module parameters during data entry time (i.e. when a programmer is using the module and entering data into the parameter fields).

The "parameter_variable" is the identical name used when declaring one of the 5 parameter types. If the parameter is an array type, the [] notation is not used, just the name. Multiple parameters may be given the same property block by listing them separated by commas.

NOTE: If the variables are arrayed elements, the usual [ ] notation should not be used.

The parameters that are introduced to SIMPL+ by this directive are similar in form and function to their existing namesakes. For example, SIGNED_INTERGER_PARAMETER possesses the same basic attributes as SIGNED_INTEGER. The new parameters are:

Parameters:

Parameter |  Similar to:  
---|---  
Non-Arrayed |   
[INTEGER_PARAMETER](<../Declarations/INTEGER_PARAMETER.htm>) |  [INTEGER](<../Declarations/INTEGER.htm>)  
[SIGNED_INTEGER_PARAMETER](<../Declarations/SIGNED_INTEGER_PARAMETER.htm>) |  [SIGNED_INTEGER](<../Declarations/SIGNED_INTEGER.htm>)  
[LONG_INTEGER_PARAMETER](<../Declarations/LONG_INTEGER_PARAMETER.htm>) |  [LONG_INTEGER](<../Declarations/LONG_INTEGER.htm>)  
[SIGNED_LONG_INTEGER_PARAMETER](<../Declarations/SIGNED_LONG_INTEGER_PARAMETER.htm>) |  [SIGNED_LONG_INTEGER](<../Declarations/SIGNED_LONG_INTEGER.htm>)  
[STRING_PARAMETER](<../Declarations/STRING_PARAMETER.htm>) |  [STRING](<../Declarations/STRING.htm>)  
Arrayed |   
[INTEGER_PARAMETER](<../Declarations/INTEGER_PARAMETER.htm>) |  [INTEGER](<../Declarations/INTEGER.htm>)  
[SIGNED_INTEGER_PARAMETER](<../Declarations/SIGNED_INTEGER_PARAMETER.htm>) |  [SIGNED_INTEGER](<../Declarations/SIGNED_INTEGER.htm>)  
[LONG_INTEGER_PARAMETER](<../Declarations/LONG_INTEGER_PARAMETER.htm>) |  [LONG_INTEGER](<../Declarations/LONG_INTEGER.htm>)  
[SIGNED_LONG_INTEGER_PARAMETER](<../Declarations/SIGNED_LONG_INTEGER_PARAMETER.htm>) |  [SIGNED_LONG_INTEGER](<../Declarations/SIGNED_LONG_INTEGER.htm>)  
[STRING_PARAMETER](<../Declarations/STRING_PARAMETER.htm>) |  [STRING](<../Declarations/STRING.htm>)  
  
NOTE: The STRING parameters only set properties for propDefaultValue, propList, propShortDescription, propFullDescription and propNotes. All other values will be ignored.

The following values are set by this directive:

Values:

NOTE: If the parameter variable specified in a property block is an array, the attributes in the block will be applied to all elements of the array.

Value |  Description  
---|---  
propValidUnits |  This is the default value that will be shown in the parameter field in SIMPL. If there is no default value specified, there will be no default value shown in SIMPL. STRING_PARAMETERs: The value must be encased in double-quotes, however the double quotes will not show in SIMPL. All other parameter types: The default must have a unit that is expressed in the propValidUnits list. It is specified in the following format: |  Parameter |  Valid Unit Example  
---|---  
unitDecimal |  25d  
unitHex |  25h  
unitPercent |  25%  
unitCharacter |  'A'  
unitTime |  25s  
unitTicks |  25t  
  
Therefore if propValidUnits=unitHex | unitDecimal, then only "h" and "d" constants would be accepted. Any others (e.g., 25%) would be rejected. If nothing is specified, then this field should be assumed to be unitString|unitDecimal| unitHex|unitPercent|unitCharacter|unitTime| unitTicks (i.e. all types).  
  
propDefaultUnits |  This describes the behavior of what SIMPL will do with the parameter when a programmer types in a value and hits enter (without explicitly entering a type, i.e. they enter 25 and not 25d) or type in a value and move off the parameter field without typing a type. STRING_PARAMETERs: propDefaultUnits can only be set to unitString, however it is implied as it is the only legal value in this case. All other parameter types: propDefaultUnits is a subset of what is specified in propValidUnits, and must be one of unitDecimal, unitHex, unitPercent, unitCharacter, unitTime or unitTicks. If this value is not specified, then it will be taken from–in the following order–propDefaultValue, propBounds, propList and propValidUnits. NOTE: This parameter must occur after propValidUnits or a compilation error will occur.  
propDefaultValue |  If this is a STRING_PARAMETER, it can be either left out or set to unitString. If this is a numeric parameter, it can be any bitwise OR separated list of a combination of any or all of unitString, unitDecimal, unitHex, unitPercent, unitCharacter, unitTime or unitTicks strings. These string units consist of a number suffixed with a single character or a single character surrounded by single quotes: |  Parameter |  Valid Unit Example  
---|---  
unitDecimal |  25d  
unitHex |  0x25  
unitPercent |  25%  
unitCharacter |  'A'  
unitTime |  25s  
unitTicks |  25t  
  
NOTE: For unitHex, the value will actually appear as (in this example) 25h in SIMPL. In SIMPL+ it must be specified with a leading '0x' and no 'h' suffix.  
  
propList |  This provides a drop-down list for a parameter. The list will show the contents of the "Label" field, but when compiled, the choice in the "Label" field is converted to the value specified in the appropriate Val field. This directive is valid for all parameter types. For example: if propList={0x25,"Address1"}, {0x26,"Address2"} then a drop-down list is shown containing 2 choices: "Address1 [25h]" and "Address2 [26h]". If the Address1 is chosen, when the program is compiled, the parameter passed is actually 25h. The units for the values must be a unit that is expressed in the propValidUnits list. NOTE: Since the label field is in double quotes, spaces and commas are legal. Values should be entered as show in the following table: |  Parameter |  Valid Unit Example  
---|---  
unitDecimal |  25d  
unitHex |  0x25  
unitPercent |  25%  
unitCharacter |  'A'  
unitTime |  25s  
unitTicks |  25t  
  
NOTE: If propList and propBounds are both specified, propList will take priority and propBounds will be ignored.

NOTE: If a propList is used, a propDefaultValue may still be expressed, but it MUST be one of the values entered in the prop list.

NOTE: For unitHex, the value will actually appear as (in this example) 25h in SIMPL. In SIMPL+ it must be specified with a leading '0x' and no 'h' suffix.  
  
propBounds |  This allows the programmer a range of values that can be typed in when using the parameter field by specifying upper_bound and lower_bound. The units must be expressed in the propValidUnits list.  This directive is not valid for STRING_PARAMETER types. For example: If upper_bound=25d and lower_bound=1000d, then SIMPL will restrict the type-in values to between 25d and 1000d. NOTE: For unitHex, the value will actually appear as (in this example) 25h in SIMPL. In SIMPL+ it must be specified with a leading '0x' and no 'h' suffix.  
propShortDescription |  This provides a single string for the status bar hint in SIMPL and when ALT+F3 is performed on a parameter.  
#BEGIN_PROP_FULL_DESCRIPTION #END_PROP_FULL_DESCRIPTION |  The text entered in this field becomes the Parameter Properties text and is a more elaborate description. This is only seen in SIMPL when the user performs an ALT+F3 on the parameter. Multiple lines can be entered.   
#BEGIN_PROP_NOTES #END_PROP_NOTES |  The text entered in this field becomes the Parameter Properties text and is a more elaborate description. This is only seen in SIMPL when the user performs an ALT+F3 on the parameter. Multiple lines can be entered.   
  
NOTE: Examples of valid and invalid parameter properties can be found [here](<../../Examples.htm>).

NOTE: For propDefaultValue: if the user enters a value in a parameter field and then moves away from that field, the value will be assumed to be that of the specified units (if any). Therefore entering 26 in the field will assume 26 seconds if propDefaultUnit=unitTime, etc.

NOTE: For propList: the Label field is contained in double quotes and therefore allowed to contain any character including spaces and commas.

Example:

DIGITAL_INPUT trig;

INTEGER_PARAMETER DelayTime;

STRING_INPUT MyString[20];

STRING_PARAMETER DeviceCode[33];

#BEGIN_PARAMETER_PROPERTIES DelayTime

propValidUnits=unitTime|unitTicks

propBounds=25s,36s;

propDefaultValue=26s;

#END_PARAMETER_PROPERTIES

#BEGIN_PARAMETER_PROPERTIES DeviceCode

propDefaultValue="35"

#END_PARAMETER_PROPERTIES

push trig

{

String LocalString[50];

Delay(DelayTime);

LocalString = MyString + "Stuff" + DeviceCode;

print("the string is %s, The DeviceCode is %s", LocalString, DeviceCode);

}

Version:

SIMPL Version 2.10.00 or later

SIMPL+ Version 3.03.00 or later

Control System:

2 Series Only, CUZ 4.00 or later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/PARAMETER_PROPERTIES.htm*
