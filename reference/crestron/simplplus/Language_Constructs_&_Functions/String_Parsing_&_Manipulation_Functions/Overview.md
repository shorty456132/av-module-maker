# String Parsing and Manipulation Functions Overview

String parsing and manipulation functions are used where the contents of string variables need to be examined or modified.

Function |  Description  
---|---  
[ClearBuffer](<CLEARBUFFER.htm>) |  Deletes the contents of the specified buffer.  
[CompareStrings](<CompareStrings.htm>) |  Performs a case-sensitive comparison of two strings.  
[CompareStringsNoCase](<CompareStringsNoCase.htm>) |  Performs a case-insensitive comparison of two strings.  
[Find](<FIND.htm>) |  Finds the position in SOURCE_STRING where MATCH_STRING first occurs. Search is case sensitive.  
[FindNoCase](<FindNoCase.htm>) |  Finds the position in SOURCE_STRING where MATCH_STRING first occurs. The search is case insensitive.  
[Gather](<GATHER.htm>) |  Concatenates the data from SOURCESTRING and issues it on the return string when the specified delimiter has been reached.  
[GatherAsync](<GatherAsync.htm>) |  Concatenates the data from the BUFFER INPUT string into the destination string parameter until specific sequence of characters is received  
[GatherAsyncByLength](<GatherAsyncByLength.htm>) |  Concatenates the data from the BUFFER INPUT string until the number of bytes specified in NumCharsToMatch is received,  
[GatherByLength](<GatherByLength.htm>) |  Concatenates the data from SourceString and issues it on the return string when the specified number of bytes have been reached.  
[GatherByLengthWithDest](<GatherByLengthWithDest.htm>) |  Concatenates the data from the BUFFER INPUT string into the destination string parameter till the specified number of characters has been reached.  
[GetEncoding](<../Encoding/GETENCODING.htm>) |  Returns the encoding of a string. The following constants are declared to help comparison: ENCODING_ASCII – Returned when the encoding of the string is set to ASCII ENCODING_UTF16 – Returned when the encoding of the string is set to UTF16 Any other return value should be treated as an error.  
[Left](<LEFT.htm>) |  Takes the leftmost NUM characters of SOURCE and returns them in an output string.  
[Len](<LEN.htm>) |  Returns the actual length of the string, not the declared maximum length.  
[Lower](<LOWER.htm>) |  Takes a source string and converts characters with the values A-Z (uppercase) to a-z (lowercase).  
[Mid](<MID.htm>) |  Returns a string NUM characters long from SOURCE, starting at position START.  
[RearmGatherAsync](<RearmGatherAsync.htm>) |  Resets the Gather trigger to the criteria used in the previous match  
[Remove](<REMOVE.htm>) |  Begins searching a string <source> for the <delimiter> at the specified position, then removes all characters from the beginning of the string <source> up to and including the delimiter.  
[RemoveByLength](<RemoveByLength.htm>) |  Removes all characters from the beginning of the SOURCESTRING up to the NumBytes specified and returns a string containing the number of bytes removed  
[RemoveGatherAsync](<RemoveGatherAsync.htm>) |  Removes the specified the BUFFER INPUT serial data from the gather operation.  
[ResizeString](<ResizeString.htm>) |  Changes the allocated size of the string to NewSize bytes.  
[ReverseFind](<REVERSEFIND.htm>) |  Finds the position in SOURCE_STRING where MATCH_STRING last occurs. Case sensitive.  
[ReverseFindNoCase](<ReverseFindNoCase.htm>) |  Finds the position in SOURCE_STRING where MATCH_STRING last occurs. Case insensitive.  
[Right](<RIGHT.htm>) |  Takes the rightmost NUM characters of SOURCE and returns them in an output string.  
[SetEncoding](<../Encoding/SetEncoding.htm>) |  Converts the encoding of a [UTF16](<../Encoding/UTF16_Unicode_Encoding.htm>) string to ASCII.  
[SetString](<SETSTRING.htm>) |  Overwrites the bytes in DESTINATION with the bytes in SOURCE starting at POSITION in the DESTINATION string.  
[ToASCII](<../Encoding/ToASCII.htm>) |  Converts the encoding of a [UTF16](<../Encoding/UTF16_Unicode_Encoding.htm>) string to ASCII.  
[ToUTF16](<../Encoding/ToUTF16.htm>) |  Converts the encoding of the string to [UTF16](<../Encoding/UTF16_Unicode_Encoding.htm>).  
[Upper](<UPPER.htm>) |  Takes a source string and converts characters with the values a-z (lowercase) to A-Z (uppercase).

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Parsing_%26_Manipulation_Functions/Overview.htm*
