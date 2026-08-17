# ToUTF16

Name:

ToUTF16

Syntax:

STRING ToUTF16 (STRING myString); 

Description:

Converts the encoding of the string to [UTF16](<UTF16_Unicode_Encoding.htm>).

Parameters:

myString is a string declared in the program. This can either be a global string or a local string.

Return Value:

A reference to myString after conversion.

Example:

In this example, the string encoding is converted to UTF16.

Function ConvertEncodingToUTF16()

{

ASCII STRING ascString[10];

INTEGER encoding;

TOUTF16(ascString);

encoding = getencoding(ascString);

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
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/ToUTF16.htm*
