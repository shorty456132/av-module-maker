# Operators, Expressions, and Statements

This sections deals with the core programming elements in SIMPL+.

## Operators

Operators take one or two operands and combine them in some way to produce a result. In SIMPL+ operators can be binary (takes two arguments) or unary (takes a single argument). For example, the + operator is binary (e.g., x + y), while the ‑ operator can be binary or unary (e.g., x ‑ y, or ‑x are valid). Most operators in SIMPL+ are binary. Notice that operands do not have to be simple constants or variables. Instead they can be complex expressions that result in an integer.

SIMPL+ operators can be classified into three categories: arithmetic, bitwise, and relational. The sections below describe each category briefly. For a complete list of operators and their function, consult the latest revision of the SIMPL+ Language Reference Guide.

### Arithmetic Operators

Arithmetic operators are used to perform basic mathematical functions on one or two variables. In all but one case, these operations make sense only for integer types (includes analog inputs and outputs). For example, to add two integers, `x` and `y`, together, use the addition operator `+`, as follows.

x + y 

As mentioned in the previous paragraph, use these operators with integers in all but one case. The exception is the `+` operator when used with string variables. In this case the operator performs a concatenation instead of addition, which is very handy for generating complex strings from smaller parts. This is discussed in more detail later.

### Bitwise Operators

Arithmetic operators deal with integers as a whole. Bitwise operators treat the individual binary bits of a number independently. For example, the unary operator `NOT` simply negates each bit in number, while the `&` operator performs a binary “and” operation to each bit in the arguments (bit0 and-ed with bit0, bit1 with bit1, etc.).

### Relational Operators

Relational operators are used in expressions when it is necessary to relate (compare, equate, etc.) two values in some way (the exception to this is the unary operator `NOT`). When a comparison is done using a relational operator, the result is an integer, which represents `True` or `False`. In SIMPL+, `True` results equal `1` and `False` results equal `0`. In general, any non-zero value is considered by SIMPL+ to be `True`, while `False` is always `0`.

Typically, relational operators are used to help control the program flow. That is, test certain conditions and the result determines what happens next. This is discussed in more detail in [Controlling Program Flow: Branching](<../Controlling_Program_Flow_Branching/TP_Controlling-Program-Flow-Branching.htm>).

## Expressions

As reading through the later parts of this guide, as well as the latest revision of the SIMPL+ Language Reference Guide, the term expression is mentioned in many places. For example, in describing the syntax of the `if‑else` construct, it may be described as the following:

if (expression1)  
{  
// code to execute}  
else if (expression2)  
{  
// code the execute} 

In the above example, `expression1` and `expression2` can be any valid SIMPL+ expression. This section describes what is and what is not an expression.

An expression in SIMPL+ is anything that consists of operators and operands. Operators were discussed previously in this section, and operands are simply the things on which operators act. For example, refer to the following simple expression.

x + 5 

In this expression the operator is the addition operator (`+`), and the operands are `x` and `5`. Expressions can contain constants, variables, and function calls in addition to operators. One expression may be made up of many smaller expressions. The following are all valid SIMPL+ expressions.

max(x,15)  
y * x << z  
a = 3  
(26 + byte(aString,i) mod z = 25 

Expressions can range from the very simple to the very complex. Also note that the last two expressions contained an equal sign. It is very important to recognize that this operator can have two different meanings based upon where it is used. In the first example above, the equal sign can serve as an assignment operator (assign the value `3` to the variable `a`) or as an equivalency comparison operator (does the variable `a` equal `3`?). However, an expression cannot contain an assignment (it would then become a statement, discussed in Operators, Expressions, and Statements), so it is indeed recognized as a comparison operation. In the second case, the equal sign also serves as a equivalency comparison operator. Here there is no ambiguity since a value cannot be assigned into an expression (as opposed to a variable).

Expressions always evaluate to either an integer or a string. Refer to the following example.

x + 5 // this evaluates to an integer  
chr(i) + myString // evaluates to a string  
a = 3 // evaluates to 1 if true, 0 if false  
b < c // evaluates to 1 if true, 0 if false 

The last two expressions are comparisons. Comparison operations always result in a `true` or `false` value. In SIMPL+, `true` expressions result in a value of `1` and `false` expressions result in a value of `0`. Understanding this concept is key to performing decision making in SIMPL+. In reality, any expression that evaluates to a non‑zero value is considered `true`. This concept is discussed in [Controlling Program Flow: Branching](<../Controlling_Program_Flow_Branching/TP_Controlling-Program-Flow-Branching.htm>) and [Controlling Program Flow: Loops](<../Controlling_Program_Flow_Loops/TP_Controlling-Program-Flow-Loops.htm>).

## Statements

Statements in SIMPL+ consist of function calls, expressions, assignments, or other instructions. Statements can be of two types: simple or complex. Simple statements end in a semicolon (**;**). Examples of simple statements are as follows:

x = MyInt / 10; // An assignment  
print("hello, world!\n"); // A function call  
checksum = atoi(MyString) + 5; /* Assignment using function calls and operators */ 

A complex statement is a collection of simple statements surrounded with curly braces (`{}`). An example of a complex statement would be as follows:

{ // start of a complex statement  
x = MyInt / 10;  
print("hello, world!\n");  
checksum = atoi(MyString) + 5;} // end of a complex statement

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Operators%2C_Expressions_and_Statements/TP_Operators%2C%20Expressions%2C%20and%20Statements.htm*
