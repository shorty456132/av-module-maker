# Program Structure

When a new SIMPL+ program is created, a template is provided that lists the order in which constructs and statements should be defined. Sections can be uncommented and expanded out to implement the desired code.

A SIMPL+ program layout would consist of, in order:

1\. [Compiler Directives](<Compiler_Directives/Overview.htm>)

2\. Input/Output definitions From/To a SIMPL Program

3\. Global declarations for the module, including STRING, [INTEGER](<Declarations/INTEGER.htm>), [Arrays](<Array_Operations/Arrays.htm>), [Structures](<Declarations/STRUCTURES.htm>), etc.

4\. [FUNCTION](<Functions_Overview.htm>) declarations

5\. PUSH/RELEASE/CHANGE statements

6\. FUNCTION MAIN

NOTE: All of these are not mandatory and may be left out as needed.

NOTE: In SIMPL+ Version 3.00, local variables are allowed.

Forward references are not allowed in a SIMPL+ program. This means you cannot CALL a function before it has been defined. This is the reason FUNCTION declarations are placed before other code. If function A calls function B, then function B should be located first in the source file.

FUNCTION MAIN is a special case function. It is not required, but any code present between the { and } is executed at startup. This is typically used for initialization purposes. For example:

FUNCTION MAIN()

{

MyVar=0;

For(I=1 to 10)

B[I] = I;

}

Sometimes FUNCTION MAIN() contains an endless loop with a DELAY statement that executes periodically while the program runs.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Program_Structure.htm*
