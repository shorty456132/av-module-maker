# Relational Operators

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

---
*Source: https://help.crestron.com/simpl_plus/Content/Operators/Relational_Operators.htm*
