# Operators Overview

SIMPL+ operators perform functions between two or more variables. SIMPL+ operators consist of Arithmetic, Bitwise, Rational and String Operators.

Refer to [Arithmetic Operators](<Arithmetic_Operators.htm>), [Bitwise Operators](<Bitwise_Operators.htm>), [Relational Operators](<Relational_Operators.htm>), [String Operators](<../Language_Constructs_&_Functions/String_Formatting_&_Printing_Functions/String_Operators.htm>).

Arithmetic Operators

OPERATOR |  NAME |  EXAMPLE |  EXPLANATION  
---|---|---|---  
- |  Negation |  -X |  Negate the value of X (2's Complement of X).  
* |  Multiplication |  X *Y |  Multiply X by Y (signed arithmetic).  
/ |  Unsigned Division |  X / Y |  Divide X by Y, truncates result (unsigned arithmetic).  
S/ |  Signed Division |  X S/ Y |  Divide X by Y, truncates result (signed arithmetic).  
MOD |  Signed Modulo |  X MOD Y |  Remainder after dividing X by Y (signed arithmetic).  
UMOD |  Unsigned Modulo |  X UMOD Y |  Remainder after dividing X by Y (unsigned arithmetic). Only 2-Series Systems.  
% |  Signed Modulo Alias |  X % Y |  Translates to Signed Modulo  
+ |  Addition |  X + Y |  Add the value of Y to X.  
- |  Subtraction |  X - Y |  Subtract the value of Y from X.  
  
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

Relational Operators

OPERATOR |  NAME |  EXAMPLE |  EXPLANATION  
---|---|---|---  
= |  Comparison |  X = Y |  True if X is equal to Y, False otherwise.  
= |  Assignment |  X = Y |  Assigns the contents in Y to X. The assignment operator cannot be used within expressions.  
! |  Complement |  ! X |  If X = 0, X changes to 1. If X is different from 0, evaluates to 0.  
<> |  Not Equal To |  X <> Y |  X is not equal to Y.  
< |  Unsigned Less Than |  X < Y |  X is less than Y (unsigned).  
> |  Unsigned Greater |  X > Y |  X is greater than Y (unsigned).  
<= |  Unsigned Less Than or Equal |  X <= Y |  X is less or equal to Y (unsigned).  
>= |  Unsigned Greater Than or Equal |  X >= Y |  X is greater or equal to Y (unsigned).  
S< |  Signed Less Than |  X S< Y |  X is less than Y (signed).  
S> |  Signed Greater Than |  X S> Y |  X is greater than Y (signed).  
S<= |  Signed Less Than or Equal |  X S<= Y |  X is less or equal to Y (signed).  
S>= |  Signed Greater Than or Equal |  X S>= Y |  X is greater or equal to Y (signed).  
&& |  Logical AND |  X && Y |  True if X and Y are both non-zero. False otherwise.  
|| |  Logical OR |  X || Y |  True if either X or Y is non-zero. False otherwise.  
  
All of the above operators, with the exception of the negation (-), NOT, and complement (!) operators, are called binary operators. Binary operators take two values, perform an operation, and return a third value as a result. For example, 5 + 6 would return the value of 11. The arguments for a given operator are called its operands. In the above example, the + sign is the operator and 5 and 6 are the operands.

The negation, NOT, and complement operators are called unary operators, which means it takes a single number and performs an operation. In this case, the negation operator performs a negate, or 2's complement. A 2's complement takes a 16-bit number, bitwise inverts it, and adds 1. The operand in a negation is the value being negated. Operands do not have to be simple numbers. They may also be variables or the results of a function call. For example, in the expression -X, the - sign is the operator and the variable X is the operand.

Note that the '=' is used as both comparison and assignment. The behavior depends on the type of statements that are being written.

String Operators

OPERATOR |  NAME |  EXAMPLE |  EXPLANATION  
---|---|---|---  
= |  Assignment |  A$ = B$ |  Assigns the contents in B$ to A$. NOTE: Not allowed in expressions because it would be confused with Comparison.  
= |  Comparison |  A$ = B$ |  A$ equal B$  
<> |  Not Equal To |  A$ <> B$ |  A$ is not equal to B$  
< |  Less Than |  A$ < B$ |  A$ is less than B$  
> |  Greater Than |  A$ > B$ |  A$ is greater than B$  
  
For less than and greater than operations, the string is evaluated in ASCII order. For example, the comparison "ABC" > "ABD" would be false. The system looks character by character; the first two characters are identical in both strings, and when it evaluated the characters C (ASCII 67) vs. D (ASCII 68), the result is false.

---
*Source: https://help.crestron.com/simpl_plus/Content/Operators/Overview.htm*
