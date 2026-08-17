# Datatype Conversions

Source |  Destination |  Action  
---|---|---  
INTEGER |  LONG_INTEGER |  Lower 2 bytes of destination = source. Upper 2 bytes cleared.  
INTEGER |  SIGNED_INTEGER |  The 2 bytes of source moved to destination. 2 byte number now treated as signed.  
INTEGER |  SIGNED_LONG_INTEGER |  Lower 2 bytes of destination = source. Upper 2 bytes cleared.  
LONG_INTEGER |  INTEGER |  Lower 2 bytes of source moved to destination, treated as unsigned.  
LONG_INTEGER |  SIGNED_INTEGER |  Lower 2 bytes of source moved to destination, treated as signed.  
LONG_INTEGER |  SIGNED_LONG_INTEGER |  The 4 bytes of destination = source, now treated as signed.  
SIGNED_LONG_INTEGER |  INTEGER |  Lower 2 bytes of source moved to destination.  
SIGNED_LONG_INTEGER |  SIGNED_INTEGER |  Lower 2 bytes of source moved to destination.  
SIGNED_LONG_INTEGER |  LONG_INTEGER |  The 4 bytes of destination = source, now treated as unsigned.  
SIGNED_INTEGER |  INTEGER |  Lower 2 bytes of source moved to destination, 2 byte number now treated as unsigned.  
SIGNED_INTEGER |  LONG_INTEGER |  2 byte source is sign extended to 4 bytes  
SIGNED_INTEGER |  SIGNED_LONG_INTEGER |  2 byte source is sign extended to 4 bytes

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Data_Conversion_Functions/Datatype_Conversions.htm*
