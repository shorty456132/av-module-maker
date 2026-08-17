# ToASCII()

Name:

ToASCII

Syntax:

STRING ToASCII(STRING myString); 

Description:

Converts the encoding of a [UTF16](<UTF16_Unicode_Encoding.htm>) string to ASCII.

Parameters:

myString is a string declared in the program. This can either be a global string or a local string.

Return Value:

A reference to myString after conversion.

Example:

In this example, the string encoding is converted to ASCII.

Function ConvertEncodingToASCII()

{

UTF16 STRING utf16String[10];

INTEGER encoding;

TOASCII(utf16String);

encoding = getencoding(utf16String);

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
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/ToASCII.htm*
