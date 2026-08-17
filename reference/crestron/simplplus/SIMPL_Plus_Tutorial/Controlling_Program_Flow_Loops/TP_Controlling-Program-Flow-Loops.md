# Controlling Program Flow: Loops

[Controlling Program Flow: Branching](<../Controlling_Program_Flow_Branching/TP_Controlling-Program-Flow-Branching.htm>) discussed constructs for controlling the flow of a program by making decisions and branching. Sometimes a program should execute the same code a number of times. This is called looping. SIMPL+ provides three looping constructs: the `for` loop, the `while` loop, and the `do‑until` loop.

## for Loops

The `for` loop is useful to cause a section of code to execute a specific number of times. For example, consider clearing each element of a 15‑element string array (set it to an empty string). Use a for loop set to run 15 times and clear one element each time through the loop.

Control the number of loops a `for` loop executes through the use of an index variable, which must be an integer variable previously declared in the variable declaration section of the program. Specify the starting and ending values for the index variable, and an optional step value (how much the variable increments by each time through the loop). Inside the loop, the executing code can reference this index.

The syntax of the `for` loop is as follows.

for (<variable> = <start> to <end> step <stepValue>)   
{  
// code in here executes each time through the loop} 

To see an example of the `for` loop use the situation alluded to above. That is, a need to clear each string element in a string array. A program to accomplish this might look like the following.

DIGITAL_INPUT clearArray; // a trigger signal  
INTEGER i; // the index variable  
STRING stringArray[50][14]; // a 15-element array  


PUSH clearArray // event function  
{  
for (i = 0 to 14)  
{stringArray[i] = ""; // set the ith element  
// to an empty string   
print("cleared element %d\n",i); // debug message} // this ends the for  
// loop} // this ends the push  
// function

In this example, the loop index `i` is set to run from `0 to 14`, which represents the first and last elements in `stringArray` respectively. Also notice that the step keyword is omitted. This keyword is optional and if it is not used, the loop index increments by 1 each time through the loop. To clear only the even‑numbered array elements, the following could have used.

for (i = 0 to 14 step 2)  
{ . . . }

The step value can also be negative, allowing the loop index to be reduced by some value each time though the loop.

The `for` loop flexibility can be enhanced further by using expressions instead of constant values for the start, end, and step values. For example, there might be a need to add up the value of each byte in a string in order to calculate the value of a `checksum` character. Since the length of the string can change as the program runs, the number of iterations through the loop is unknown. The following code uses the built‑in function, `len`, to determine the length of the string and only run through the for loop the necessary number of times. System functions are described in detail in [Using System Functions](<../Using_System_Functions/TP_Using-System-Functions.htm>).

checksum = 0; // initialize the chucksum variable

/* iterate through the string and add up the bytes.   
Note that the { } braces are not needed here  
because the contents of the for-loop is only  
a single line of code */for (i = 1 to len(someString))  
checksum = checksum + byte(someString,i);

/* now add the checksum byte on to the string  
using the chr function. Note that in this  
example we only use the low-order byte from  
the checksum variable */someString = someString + chr(checksum);

## while and do‑until Loops

The `for` loop discussed in an earlier section is useful for iterating through code a specific number of times. However, sometimes the exact number of times a loop should repeat is unknown. Instead, it may be necessary to check to see if a condition is true after each loop to decide whether or not the loop should execute again.

There are two looping constructs in SIMPL+ which allows execution of a loop only for as long as a certain condition is true. These are the `while` and `do‑until` loops. The `while` loop has the following syntax.

while (expression)  
{  
<statements>} 

When the `while` statement is executed, the expression contained in parentheses is evaluated. If this expression evaluates to True, then the statements inside the braces are executed. When the closed brace is reached, the program returns to the `while` statement and reevaluates the expression. At this point the process is repeated. It should become clear that the code inside the braces is executed over and over again as long as the `while` expression remains True.

The nature of the `while` loop means that it is the responsibility of the programmer to ensure that the loop is exited at some point. Unlike the `for` loop discussed previously, this loop does not run for a set number of times and then finishes. Consider the example after this paragraph.

x = 5;  
while (x < 10)  
{  
y = y + x;  
print("Help me out of this loop!\n");}

NOTE: Endless loops cause the SIMPL+ module (in which they occur) to rerun the same code forever. However, due to the multi‑tasking nature of the operating system, an endless loop in one module does not cause the rest of the SIMPL program (including other SIMPL+ modules) to stop running. This is discussed in more detail in [Understanding Processing Order](<../Understanding_Processing_Order/TP_Understanding-Processing-Order.htm>). 

This example shows an endless loop. That is, a loop that runs forever and never exits. The problem is that the value of the `while` expression never changes once the loop is entered. Thus the expression can never evaluate to `False`. Include code inside the loop that affects the `while` expression (in this case the variable `x` must be modified in some way) and allows the loop to exit at some point.

The `do‑until` looping construct is similar to the `while` loop. The difference lies in where the looping expression is evaluated and how this evaluation affects the loop. To see the difference, examine the form of a `do‑until` loop.

do  
{  
<statements>} until (expression)

From the syntax, it is obvious that the looping expression for a `do‑until` appears after the looping code. This expression appears before the code in a `while` loop. This discrepancy affects the way the loop is initially entered. As was shown above, a `while` loop first evaluates the expression to see if it is `True`. If it is, then the loop runs through one time and then the expression is evaluated again.

The `do‑until` loop differs from this in that it always executes at least one time. When the `do` keyword is reached, the code that follows (enclosed in braces) is executed before the value of the `until` expression is evaluated. After the initial pass through this code, the value of this expression determines whether or not the code should be executed again. Here lies the other difference between the `while` and `do‑until`. The `while` loop executes as long as the expression remains `True`. A `do‑until` loop executes until an expression becomes `True`.

When deciding which type of loop should be used, first understand that using any of the three types of loops discussed here can solve many problems. However, one particular loop is usually better suited for a given application than the others. As a general rule of thumb, when the number of iterations the code should execute is known, a `for` loop is preferred. A `while` or a `do‑until` loop is ideal to execute a section of code continuously based on the value of some expression.

Once a `while` or a `do‑until` loop is determined suitable for a particular application, the question becomes which one of the two should be used? Once again realize that either one can usually accomplish the goal, but one type of loop may require less coding or be more readable in some cases. The basic question to ask is whether or not the loop needs to run through at least one time. If so, a `do‑until` is the best choice. If instead, the value of an expression should be checked, then use the `while` loop.

## Exiting from Loops Early

All three loops discussed above have built‑in ways to exit. The `for` loop exits when the index variable reaches the stated maximum. The `while` loop exits when the expression becomes `False`. The `do‑until` loop exits when the expression becomes `True`.

Sometimes programming tasks do not always fall neatly into place regarding loops and it may be desirable (or necessary) to exit a loop prematurely. Consider the following example.

INTEGER x,y;

for (x = 3 to z)  
{  
y = y + x*3 ‑ z*z;  
if (y = 0)break;}

Notice that in most (if not all) cases, the need for the break statement could be avoided by the use of a different type of loop. In the example above, this could be accomplished by using a `do‑until` loop. Consider the following.

x = 3;

do  
{  
y = y + x*3 ‑ z*z;  
x = x + 1;} until ((y = 0) || (x = z)) 

Either technique would be considered acceptable.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Controlling_Program_Flow_Loops/TP_Controlling-Program-Flow-Loops.htm*
