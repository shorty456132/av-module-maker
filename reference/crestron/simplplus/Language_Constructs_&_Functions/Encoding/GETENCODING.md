# GetEncoding

Name:

GetEncoding

Syntax:

GetEncoding(STRING myString);

Description:

Returns the encoding of a string. The following constants are declared to help comparison:

ENCODING_ASCII – Returned when the encoding of the string is set to ASCII.

ENCODING_UTF16 – Returned when the encoding of the string is set to [UTF16](<UTF16_Unicode_Encoding.htm>).

Any other return value should be treated as an error.

Parameters:

myString is a string declared in the program. This can either be a global string or a local string.

Return Value:

An INTEGER containing the encoding of the string. The value of the return value can either be ASCII or UTF16.

Example:

In this example, the string encoding is retrieved from a string an appropriate string is printed on the console.

Function GetEncodingFunction()

{

INTEGER encoding;

STRING myString[10];

encoding = getencoding(myString);

if (encoding = ENCODING_ASCII)

print ("ASCII\r\n");

else if (encoding = ENCODING_UTF16)

print ("UTF16\r\n");

else

print ("Error getting encoding\r\n");

}

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: Supported

4-Series: Supported

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/GETENCODING.htm*
