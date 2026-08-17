# Controlling Program Flow: Branching

In any substantial program, making decisions must control the program. SIMPL+ provides two constructs for branching the program based on the value of expressions: `if‑else` and the `switch‑case` statement.

## if‑else

`if‑else` is the most commonly used branching construct. In its most basic form, it is structured as follows.

if (expression1)  
{  
// do something here} 

Where `expression1` represents any valid SIMPL+ expression, including variables, function calls, and operators. If this expression evaluates to `True`, then the code inside the braces is executed. If this expression evaluates to `False`, the code inside the braces is skipped.

What is the definition of `True` and `False` in SIMPL+? As was discussed in [Working with Data (Variables)](<../Working_With_Data/TP_Working-with-Data-\(Variables\).htm>), expressions, which evaluate to a non‑zero result, are considered `True`, and expressions that evaluate to `0` are considered `False`. For example, refer to the expressions in the table that follows.

Expressions Expression | Evaluates to  
---|---  
a = 3 | true if a=3, false otherwise  
b*4 ‑ a/3 | true as long as the result is non-zero  
1 | always true  
0 | always false  
  
One limitation with the `if` construct, as shown above, is that the code inside the `if` is run whenever `expression1` evaluates as `True`, but any code after the closing braces runs regardless. It is often useful to execute one set of code when a condition is `True` and then another set of code if that same condition is `False`. For this application, use the `if‑else` construct, which looks like the following.

if (expression1)  
{  
// do something if expression1 is true}  
else  
{  
// do something else if expression1 is false} 

NOTE: Programming to anticipate user errors and handle them appropriately is called error‑trapping. It is a recommended programming practice.

It should be clear that the code following the `if` runs whenever `expression1` evaluates to `True` and the code following the `else` executes whenever `expression1` evaluates to `False`. Obviously, there can never be a case where both sections of code execute together.

The following example is designed to control a CD changer. Before telling the CD player to go to a particular disc number, it checks to see that the analog value, which represents the disc number, does not exceed the maximum value.

#DEFINE_CONSTANT NUMDISCS 100

ANALOG_INPUT disc_number;  
STRING_OUTPUT CD_command, message;

CHANGE disc_number  
{  
if (disc_number <= NUMDISCS)  
{CD_command = "DISC " + itoa(disc_number) + "\r";  
message = "Changing to disc " + itoa(disc_number) + "\n";}  
else  
{message = "Illegal disc number\n";}}

There is one last variation on the `if‑else` statement. In the example above, the decision to be made is binary. That is, do one thing if this is true, otherwise do something else. In some cases decisions are not that straight forward. For example, to check the current day of the week, execute one set of code if it is Saturday, another set of code if it is Sunday, and yet some other code if it is any other day of the week. One way to accomplish this is by using a series of `if‑else` statements. For this example, the code might look like the following.

today = GetDayOfWeekNum(); // gets the current day of the week

if (today = 0) // is today Sunday?  
{  
// code to run on Sundays}  
else if (today = 5) // is today Friday?  
{  
// code to run on Friday}  
else if (today = 6) // is today Saturday?  
{  
// code to run on Saturdays} else // only gets here if the first three  
{ // conditions are false  
// code to run on all other days} 

NOTE: There can be as many if‑else statements in a single construct as necessary. However, sometimes tasks like these are better handled with the switch‑ case construct, discussed in the next section.

Finally, note that `if` statements can be nested inside other if statements.

## switch-case

In the last section, it was shown that the `if‑else` construct can be used for making complex decisions. Also it was used for making a choice between mutually exclusive conditions (conditions that cannot coexist), the syntax can become cumbersome. For this particular case SIMPL+ offers the switch‑case construct.

Think of `switch‑case` as a compact way of writing an `if‑else` construct. The basic form of the `switch‑case` is shown after this paragraph.

switch (expression)  
{  
case (expression1):  
{  
// code here executes if  
// expression = expression1}  
case (expression2):  
{  
// code here executes if  
// expression = expression2}  
default:  
{  
// code here executes if none  
// of the above cases are true}}

NOTE: The use of the default keyword allows specific code to execute if none of the other cases are true. This is identical to the final else statement in the `if‑else` construct mentioned in Controlling Program Flow: Branching.

Examine an example using the `switch‑case` construct. Perhaps there is a variable that should hold the number of days in the current month. The following example uses `switch‑case` to set the value of this variable.

switch (getMonthNum())  
{  
case (2): //February  
{if (leapYear) // this variable was set elsewhere  
numdays = 29;else  
numdays = 28;}  
case (4): // April  
numdays = 30;  
case (6): // June  
numdays = 30;  
case (9): // September  
numdays = 30;  
case (11): // November  
numdays = 30;  
default: // Any other month  
numdays = 31;  
} 

Notice that curly braces did not enclose many of the statements in the previous example. For most SIMPL+ constructs, the braces are only needed when more than one statement is to be grouped together. If the program has only a single statement following the case keyword, then the braces are optional.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Controlling_Program_Flow_Branching/TP_Controlling-Program-Flow-Branching.htm*
