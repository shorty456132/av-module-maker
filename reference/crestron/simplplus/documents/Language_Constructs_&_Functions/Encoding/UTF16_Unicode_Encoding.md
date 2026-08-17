# UTF16 Unicode Encoding

Systems may either be ASCII compliant or use Unicode.

Unicode allows for characters that are greater than 8 bits, which means that character sets other than the standard US character sets may be used. Typically this would be for talking to a touch screen using other character sets (Chinese, Japanese, etc.)

In Unicode terminology, it is commonplace to express a character in terms of a “Codepoint”. This allows someone to reference a particular character without worrying about the underlying encoding mechanism. A codepoint is specified as U+{4 digits} or U+{6 digits}.

In the 2 series, strings are encoded as a series of bytes, and so there is no concept of encoding for Unicode. 

In the 3 series, strings are encoded as a series of words. Therefore a string expressed in SIMPL as “\x25\x26\x27” is actually stored as 3 words; 0x0025, 0x0026, and 0x0027. Since the system deals with bytes at the lowest level, Crestron has decided to encode as in a format known as “Little Endian” – which is the Low byte of a word followed by the High byte of a word. The actual storage on a byte level is 0x26 0x00 0x26 0x00 0x27 0x00.

NOTE: A word is another name for a 16b value, much like a byte is a name for an 8b value.

In the 3 Series, Crestron has chosen to use UTF-16LE as our particular encoding method for Unicode. LE stands for Little Endian to reflect the above storage concept.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Encoding/UTF16_Unicode_Encoding.htm*
