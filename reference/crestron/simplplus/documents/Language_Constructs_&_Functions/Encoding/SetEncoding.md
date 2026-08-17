# SetEncoding

Name:

SetEncoding

Syntax:

SetEncoding(STRING myString, ENCODING_TYPE encoding);

Description:

Sets the encoding of a string. Encoding can only be one the following types:

ENCODING_ASCII – Encoding of the string is set to ASCII.

ENCODING_UTF16 – Encoding of the string is set to [UTF16](<UTF16_Unicode_Encoding.htm>).

ENCODING_INHERIT – Encoding of the string is set to the inherited encoding of the module. The encoding directive is used to set the encoding.

Parameters:

myString is a string declared in the program. This can either be a global string or a local string.

Encoding can either be ENCODING_ASCII, ENCODING_UTF16 or ENCODING_INHERIT.

Return Value:

None.

Example:

In this example, the string encoding is set on a string.

Function SetEncodingFunction()

{

STRING myString[10];

// Set encoding to ASCII

setencoding(myString, ENCODING_ASCII);

// Set encoding to UTF16

setencoding(myString, ENCODING_UTF16);

// Set encoding to default encoding inherited using the encoding directive.

setencoding(myString, ENCODING_INHERIT);

}

Version:

X Generation: Not Supported

2-Series: Not Supported

3-Series: Supported

4-Series: Supported

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/SetEncoding.htm*
