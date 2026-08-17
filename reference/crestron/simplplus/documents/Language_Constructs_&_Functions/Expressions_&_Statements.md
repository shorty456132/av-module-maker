# Expressions & Statements

An expression consists of operators and operands.

i.e.

5 * 6

or

(VAL1 + 5) / 30

or

(26 + BYTE(THESTRING$,1)) MOD Z = 25

Statements consist of function calls, expressions, assignments, or other instructions. There are two types of statements, Simple and Complex.

A simple statement ends with a semicolon (;). Examples of simple statements are:

X = Z/10; // Simple assignment statement using

// operators.

PRINT("Hello, World!\n"); // Simple statement using a function

// call.

CHECKSUM = ATOI(Z$) + 5; // Simple assignment statement using

// a function call and operators.

A complex statement is a collection of simple statements that start with '{' and end with '}'. An example would be:

{ // Start of a complex statement

X = Z/10; // Simple assignment statement

// using operators.

PRINT("Hello, World!\n"); // Simple statement using a

// function call.

CHECKSUM = ATOI(Z$) + 5; // Simple assignment statement

// using a function call and

// operators.

} // End of a Complex statement

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Expressions_%26_Statements.htm*
