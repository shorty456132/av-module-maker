# Compiler Errors and Warnings Overview

Of all the possible problems that a program can have, compiler errors and warnings may be the easiest to remedy. This is because the compiler reveals both the nature and location of the problems it encounters. The only task left to the developer is to recognize exactly what the compiler means and make the necessary changes.

The following list provides the most common causes of compiler errors:

  * Missing a semi-colon at the end of a statement

  * Having a semi-colon where it does not belong (e.g., before an opening brace of a compound statement)

  * Trying to use a variable that has not been declared, or misspelling a variable

  * Attempting to assign a value to an input variable (digital, analog, string, or buffer)

  * Syntax errors




If multiple error messages are received when compiling the program, it is recommended that you work with the first one before attempting to fix the rest. Many times, a missing semi-colon at the beginning of a program can confuse the compiler enough that it thinks there are many more errors. Fixing the first error may clear up the rest.

The SIMPL+ program compiler errors and warnings are grouped into several categories, as shown in the following table. Errors are listed in numerical order; the numbers are linked to detailed descriptions of the errors.

Compiler Errors and Warnings

CATEGORY |  NUMBER |  MESSAGE TEXT  
---|---|---  
Syntax Errors |  [1000](<Compiler_Error_1000.htm>) |  '<identifier>' already defined  
|  [1001](<Compiler_Error_1001.htm>) |  Undefined variable: '<identifier>'  
Undefined function ‘<identifier>’  
|  [1002](<Compiler_Error_1002.htm>) |  Missing '<token>'  
|  [1003](<Compiler_Error_1003.htm>) |  Incorrect type '<decl_type>', expected type(s):  
'<decl_type1[,decl_type2] [,decl_typen]>'  
Incorrect type, expected type(s):  
'<decl_type1[,decl_type2][,decl_typen]>'  
|  [1004](<Compiler_Error_1004.htm>) |  Unmatched symbol: '<identifier>'  
|  [1005](<Compiler_Error_1005.htm>) |  Unexpected symbol in compiler directive: '<identifier>'  
|  [1006](<Compiler_Error_1006.htm>) |  Invalid #DEFINE_CONSTANT value: '<identifier>'  
|  [1007](<Compiler_Error_1007.htm>) |  Missing array index: '<identifier>'  
|  [1008](<Compiler_Error_1008.htm>) |  Invalid integer argument or undefined variable: '<identifier>'  
|  [1009](<Compiler_Error_1009.htm>) |  Missing structure member: '<identifier>'  
Structure does not contain member: '<identifier>'  
|  [1010](<Compiler_Error_1010.htm>) |  Symbol Name contains illegal character: ';'  
|  [1011](<Compiler_Error_1011.htm>) |  Missing return value  
|  [1012](<Compiler_Error_1012.htm>) |  Unterminated string constant  
|  [1013](<Compiler_Error_1013.htm>) |  Source code does not evaluate to anything  
|  [1014](<Compiler_Error_1014.htm>) |  The compiler was expecting a parameter type variable and another declaration type or token was found.  
|  [1015](<Compiler_Error_1015.htm>) |  The compiler was expecting a parameter unit and another token or type was found.  
|  [1016](<Compiler_Error_1016.htm>) |  The compiler was expecting a parameter property and another token or type was found.  
|  [1017](<Compiler_Error_1017.htm>) |  **S yntax error: ****SIMPL# Classes and Structures are case-sensitive: ‘ <variable_name>’**  
Fatal Errors |  [1100](<Compiler_Error_1100.htm>) |  Statement outside of function scope  
|  [1101](<Compiler_Error_1101.htm>) |  Abort - Error count exceeded <max_errors>  
Expression Errors |  [1200](<Compiler_Error_1200.htm>) |  Invalid numeric expression: '<expression>'  
Invalid string expression  
Invalid expression: '<expression>'  
[1201](<Compiler_Error_1201.htm>) |  Invalid \\\x sequence  
Invalid \\\x sequence: '<expression>'  
Declaration Errors |  [1300](<Compiler_Error_1300.htm>) |  Array size missing  
Array size invalid  
[1301](<Compiler_Error_1301.htm>) |  Invalid array index  
[1302](<Compiler_Error_1302.htm>) |  Variable name, ‘<identifier>’, exceeds maximum length  
of <max> characters  
[1303](<Compiler_Error_1303.htm>) |  Declaration type not allowed within structure: '<identifier>'  
Structure cannot contain String Arrays or Structure  
variables: '<identifier>'  
Structure definitions not allowed within other structures  
Local Structure declarations are not allowed   
[1304](<Compiler_Error_1304.htm>) |  Local variables must be declared at top of function  
[1305](<Compiler_Error_1305.htm>) |  Local functions not supported  
[1306](<Compiler_Error_1306.htm>) |  Declaration type can only be used globally: '<identifier>'  
[1307](<Compiler_Error_1307.htm>) |  Variables must be declared before array declarations:  
'<identifier>'  
[1308](<Compiler_Error_1308.htm>) |  Global variable declaration cannot be declared in library  
file: '<identifier>'  
I/O Declaration cannot be declared in library file:  
'<identifier>'  
[1309](<Compiler_Error_1309.htm>) |  Compiler Directive must be set before all global variable  
declarations  
#DEFAULT_NONVOLATILE Compiler Directive  
already set  
#DEFAULT_VOLATILE Compiler Directive already set  
[1310](<Compiler_Error_1310.htm>) |  Compiler directive cannot be in function scope  
[1311](<Compiler_Error_1311.htm>) |  Undefined Wait Label: '<identifier>'  
Missing, invalid or already defined Wait label:  
'<identifier>'  
[1312](<Compiler_Error_1312.htm>) |  Array boundary exceeded maximum size of  
‘num_bytes’ bytes  
[1313](<Compiler_Error_1313.htm>) |  Minimum array size invalid  
[1314](<Compiler_Error_1314.htm>) |  Minimum array size is not allowed for this datatype:  
'<identifier>'  
Minimum array size for this datatype has already  
been declared: '<identifier>  
|  [1315](<Compiler_Error_1315.htm>) |  The receiving buffer size was not specified within the socket declaration. All socket declarations must contain a buffer size.  
[1316](<Compiler_Error_1316.htm>) |  An invalid Parameter Type was specified within a parameter declaration.  
[1317](<Compiler_Error_1317.htm>) |  A variable was found trying to be declared with the NONVOLATILE keyword.  
|  [1318](<Compiler_Error_1318.htm>) |  A parameter was being assigned a value that was either out of range or of the wrong type.  
|  [1319](<Compiler_Error_1319.htm>) |  A parameter was being assigned a value that was either out of range or of the wrong type.  
|  [1320](<Compiler_Error_1320.htm>) |  The property unit, unitString, cannot be combined with any other property unit (i.e., unitDecimal,unitCharacter, etc).  
|  [1321](<Compiler_Error_1321.htm>) |  The declaration keyword, Dynamic, can only be used when #DEFAULT_VOLATILE is specified for the program module.  
|  [1322](<Compiler_Error_1322.htm>) |  The declaration keyword, Dynamic, can only be used with string or array declarations. I/O declarations are not allowed to be declared as dynamic.  
|  [1323](<Compiler_Error_1323.htm>) |  In order to declare Strings and Arrays dynamically, the compiler directive, #ENABLE_DYNAMIC, must be specified beforehand within the module.  
|  [1324](<Compiler_Error_1324.htm>) |  propList cannot be used in conjunction with propBounds. propBounds cannot be used in conjunction with propList.  
|  [1325](<Compiler_Error_1325.htm>) |  Default values, if specified, must be specified before a propList declaration. If using propBounds, the Default Value must be defined beforehand. If a default value is specified, the propList must contain at least one element that contains this default value.  
|  [1326](<Compiler_Error_1326.htm>) |  The Default Value must be within the bounds specified in propBounds. The compiler will also enforce that the lower bound is less than the upper bound. All values specified must also be of the type indicated within propValidUnits.  
|  [1327](<Compiler_Error_1327.htm>) |  Variables that are declared as volatile are only allowed to be resized. Either the global compiler directive, #VOLATILE, or the declaration modifier, “VOLATILE”, may be used to declare a variable as volatile.  
|  [1328](<Compiler_Error_1328.htm>) |  Encoding only applies to strings. The declaration modifiers, ASCII, UTF16 and INHERIT can only be used with variables of type STRING.  
|  [1329](<Compiler_Error_1329.htm>) |  **Declaration error:  Class name exists in one or more namespaces. Fully-qualified name must be specified: ‘<class_name>’**  
Assignment  
Errors |  [1400](<Compiler_Error_1400.htm>) |  Illegal Assignment  
[1401](<Compiler_Error_1401.htm>) |  Variable cannot be used for assignment: '<identifier>'  
[1402](<Compiler_Error_1402.htm>) |  Variable can only be used for assignment: '<identifier>'  
Function  
Argument  
Errors |  [1500](<Compiler_Error_1500.htm>) |  Argument <arg_num> cannot be passed by reference  
[1501](<Compiler_Error_1501.htm>) |  Argument <arg_num> cannot be passed by value  
[1502](<Compiler_Error_1502.htm>) |  Function contains incomplete number of arguments  
Function call contains an unmatched number of  
arguments  
[1503](<Compiler_Error_1503.htm>) |  Input or Output signal expected: '<identifier>'  
[1504](<Compiler_Error_1504.htm>) |  Incomplete number of format string arguments  
Format string contains an unmatched number of  
arguments  
Argument <arg_num> is missing or invalid.  
Argument <arg_num> is missing or invalid.  
<decl_type> expected  
[1505](<Compiler_Error_1505.htm>) |  Format string contains invalid format specifier  
[1506](<Compiler_Error_1506.htm>) |  0, 1 or 2 constant expected for argument 1  
[1507](<Compiler_Error_1507.htm>) |  Argument <arg_num>: Missing or invalid array  
[1508](<Compiler_Error_1508.htm>) |  I/O variable cannot be passed to read file functions:  
'<identifier>'  
|  [1509](<Compiler_Error_1509.htm>) |  A valid class name was expected for a function argument and was not found.  
|  [1510](<Compiler_Error_1510.htm>) |  A valid class event handler was expected for a function argument and was not found.  
Construct  
Errors |  [1600](<Compiler_Error_1600.htm>) |  'Function Main' cannot contain function parameters  
'Function Main' cannot return a value  
[1601](<Compiler_Error_1601.htm>) |  Duplicate CASE Statement  
Constant expected: '<identifier>'  
[1602](<Compiler_Error_1602.htm>) |  Switch statement contains 'default' without 'case' labels  
[1603](<Compiler_Error_1603.htm>) |  #CATEGORY does not exist: '<categorgy_number>'  
Defaulting to Category Type, ""32"" (Miscellaneous).  
[1604](<Compiler_Error_1604.htm>) |  'EVENT' already has a body  
[1605](<Compiler_Error_1605.htm>) |  Function can only be contained within an event  
[1606](<Compiler_Error_1606.htm>) |  Statement must be contained within a loop statement  
[1607](<Compiler_Error_1607.htm>) |  GetLastModifiedArrayIndex may return an ambiguous  
signal index  
[1608](<Compiler_Error_1608.htm>) |  Missing library file name  
|  [1609](<Compiler_Error_1609.htm>) |  The compiler encountered this function call outside of Function Main  
|  [1610](<Compiler_Error_1610.htm>) |  The compiler encountered this function call within a Wait Statement.  
|  [1611](<Compiler_Error_1611.htm>) |  An invalid structure type was encountered within a construct.  
|  [1612](<Compiler_Error_1612.htm>) |  Custom category names can only be assigned to category “46”. A different category number was found.  
|  [1613](<Compiler_Error_1613.htm>) |  SocketGetSenderIPAddress can only be used within the SOCKETRECEIVE event. It cannot be used inside any other declared function or event type.  
|  [1614](<Compiler_Error_1614.htm>) |  SocketGetStatus can only be used within the SOCKETSTATUS event. It cannot be used inside any other declared function or event type.  
|  [1615](<Compiler_Error_1615.htm>) |  The functions, GetExcpetionMessage and GetExceptionCode can only be used within the CATCH portion of a TRY-CATCH statement block. It cannot be used inside any other type of statement block or event handler.  
|  [1616](<Compiler_Error_1616.htm>) |  When registering delegates, the callback function specified must be valid and exist within the SIMPL+ module. The delegate callback function’s signature must match the signature within the SIMPL# Library.  
File Errors |  [1700](<Compiler_Error_1700.htm>) |  End of file reached  
|  [1701](<Compiler_Error_1701.htm>) |  Error writing header file: '<file_name>'  
Error writing file: '<file_name>'  
Error writing library file  
Error writing output file  
Error creating compiler makefile: '<file_name>'  
Error opening compiler source makefile: '<file_name>'  
Error opening source file: '<file_name>'  
|  [1702](<Compiler_Error_1702.htm>) |  Error extracting library, '<file_name>', from archive:  
'<archive_file>'  
|  [1703](<Compiler_Error_1703.htm>) |  When including User or Crestron libraries, only the library name is needed within the functions, #USER_LIBRARY and #CRESTRON_LIBRARY. Passing in a fully qualified path is not allowed.  
|  [1704](<Compiler_Error_1704.htm>) |  Library names must be unique. They cannot have the same name as the SIMPL+ module.  
|  [1705](<Compiler_Error_1705.htm>) |  Fatal Error. SIMPL+ does not recognize a construct within the SIMPL# Library.  
|  [1706](<Compiler_Error_1706.htm>) |  A problem exists within a SIMPL# Library. This could be due to a signing issue or the SIMPL# Library being built incorrectly. The SIMPL# Library should be rebuilt again.  
|  [1707](<Compiler_Error_1707.htm>) |  Library error: Library path cannot be relative: <library name>. Absolute paths may be used.  
Compiler Warnings |  [1019](<Compiler_Warning_1019.htm>) |  Logic excluded as a result of #if_series3 directive  
[1800](<Compiler_Warning_1800.htm>) |  'Return' statement will only terminate current Wait  
statement's function scope   
[1801](<Compiler_Warning_1801.htm>) |  'TerminateEvent' statement will only terminate  
current Wait statement's function scope   
[1802](<Compiler_Warning_1802.htm>) |  #CATEGORY_NAME defined more than once. Using:  
#CATEGORY_NAME "<number>"   
[1803](<Compiler_Warning_1803.htm>) |  Possible data loss: LONG_INTEGER to INTEGER assignment

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Errors_%26_Warnings/Compiler_Errors_and_Warnings_Overview.htm*
