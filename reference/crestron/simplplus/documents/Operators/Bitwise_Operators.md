# Bitwise Operators

Bitwise Operators

OPERATOR |  NAME |  EXAMPLE |  EXPLANATION  
---|---|---|---  
<< |  Shift Left |  X << Y |  Shift X to the left by Y bits; 0 is Shifted in.  
>> |  Shift Right |  X >> Y |  Shift X to the right by Y bits; 0 is Shifted in.  
{{ |  Rotate Left |  X {{ Y |  Rotate X to the left by Y bits; full 16 bits used. Same as RotateLeft().  
}} |  Rotate Right |  X }} Y |  Rotate X to the right by Y bits; full 16 bits used. Same as RotateRight().  
NOT |  1's Complement |  NOT(X) |  Change 0 bits to 1, 1 bits to 0.  
& |  Bitwise AND |  X & Y |  AND the bits of X with the bits of Y.  
| |  Bitwise OR |  X | Y |  OR the bits of X with the bits of Y.  
^ |  Bitwise XOR |  X ^ Y |  XOR the bits of X with the bits of Y.  
  
NOTE: For the Shift and Rotate operators, only the lower 5-bits of Y are used, giving values of Y ranging from 0 to 31. For example, if Y=600, the lower 5-bits equate to 24. Rotating a 16-bit number through 16 positions gives the original number back. Therefore, for rotating 24, the result is equivalent to rotating through 8. Shifting greater than 16 will always give a 0 as a result.

---
*Source: https://help.crestron.com/simpl_plus/Content/Operators/Bitwise_Operators.htm*
