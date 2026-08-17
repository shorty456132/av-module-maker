# Comments

It is beneficial to comment code to make it more readable and for documentation. Comments do not exist in any form after code generation and are not required.

SIMPL+ has two styles of comments, single line and block comments. Single line comments start with the characters //. The rest of the line (until a carriage return) is considered a comment. If they occur within a quoted string, such as in PRINT, they are NOT treated as comment characters, but rather as two backslash (Hex 2F) characters.

Examples:

PRINT("Hello, World!\n"); // This stuff is a comment.

PRINT("hello, // world!\n"); // This stuff is a comment,

// but the string actually

// printed is hello, // world.

The second form of comment characters are the block comments. /* starts a block comment and */ ends a block comment. This is useful for commenting out large sections of code or writing large sections of documentation. Note that nested comments are not supported. Also, if /* or */ appear inside of a quoted string such as in an PRINT statement, they are not considered comments but part of the string.

Examples:

/*

This

is

all

a comment!

*/

PUSH Trig

{

// code that does something.

}

---
*Source: https://help.crestron.com/simpl_plus/Content/General_Information/Comments.htm*
