# Writing Your First SIMPL+ Program: "Hello World"

The best way to become acquainted with SIMPL+ is to write a simple program right off the bat. Although programs can be written in SIMPL+, it is important to understand that all control system I/O must be defined directly in SIMPL. This SIMPL program can be thought of as a shell in which the SIMPL+ modules are contained. This shell consists of hardware definitions at the very least, but in most cases also consists of raw SIMPL code. SIMPL+ program(s) appear as logic symbols in the overall SIMPL program.

Based on the fact that SIMPL+ programs can exist only inside this wrapper, it is necessary to create a skeleton SIMPL program before testing the program. This is covered in [Making It Work](<Making_it_Work.htm>) section. For now, concentrate on writing the SIMPL+ code only.

Start creating a new SIMPL+ program while running SIMPL. Select **File > New > New SIMPL+ Module**. The SIMPL+ programming environment appears. Instead of a blank window, a skeleton program filled with commented code shows up. This commented out code makes it easy to remember the language syntax and structure. Simply locate the necessary lines, uncomment them, and add the appropriate code. To uncomment a line of code, either remove the // that appears at the start of the line or remove the multi-line comment indicators /*…*/

SIMPL+ programs communicate with the SIMPL wrapper program via inputs and outputs. These inputs and outputs correspond to signals in the world of SIMPL and can be digital, analog, or serial signals (if these terms are unfamiliar, they are covered in more detail in [Input/Output Types](<../The_Structure_of_a_SIMPL_Plus_Program/TP_Structure-of-a-SIMPLPlus-Program.htm#Inputs,>)). For this first program, only a single digital input is defined. Find the line of code that says // DIGITAL_INPUT. Uncomment it and edit it so it looks like the following:

DIGITAL_INPUT speak;

This line defines the variable speak as the first digital input to the SIMPL+ program. Notice that most lines in SIMPL+ end in a semi-colon (;). To be precise, all statements end with a semi-colon. The definition of a statement in SIMPL+ can be found in the latest revision of the SIMPL+ Language Reference Guide..

Find the line of code that says // #PRINT_TO_TRACE and uncomment it so it looks like the following:

#PRINT_TO_TRACE

When a digital input goes from low to high, a push event is generated. To define a push event function for that signal, program this function to yield the desired actions. From the skeleton program, find the commented line of code that says PUSH input.. Uncomment the function block by removing the surrounding comment characters and edit it to read the following:

PUSH speak

{

Print("Hello World!\n");

}

This function causes the string Hello World! plus a carriage return and line feed to be sent out the control system computer port whenever the signal speak goes high. Notice the curly-braces ({}) surrounding the print statement above. In SIMPL+ these braces are used to group multiple statements into a compound statement. In the case of a function definition, always surround the contents of the function with these braces.

The next step is to add another event function, one that responds when a signal goes from high to low. This event is called a release event. From the skeleton program, find the line of code that says RELEASE input. Uncomment and edit it to read the following:

RELEASE speak

{

Print("Crestron people make the difference\n");

}

Finally, define what happens when the control system first boots up. This is accomplished using Function Main. Upon system startup, the program code defined in this function executes. Unless there are looping constructs (discussed in [Controlling Program Flow: Loops](<../Controlling_Program_Flow_Loops/TP_Controlling-Program-Flow-Loops.htm>)) defined in this function, this code executes only one time for the life of the control system (or until it is rebooted). From the skeleton program, find the section of the program that says Function Main. Edit it to read the following.

Function Main()

{

Print("I am born!\n");

}

This causes the text I am born! to be sent out to the computer port only upon startup.

To save the file, from the menu, select **File > Save**. Assign the name, My **first SIMPL+**. To compile the file, select **Build > Save and Compile**. This command saves the code module, compiles it, and tells SIMPL how to present it to the SIMPL programmer. SIMPL+ version 2.0 requires that all SIMPL+ modules reside in the User SIMPL+ directory (this can be checked in SIMPL by selecting **Options > Preferences...** and clicking on the **Directories** tab). In SIMPL+ 3.0 and later, SIMPL+ modules can also reside in the corresponding SIMPL Project Directory, where the SIMPL program also resides.

Each time the program is saved, an update log appears at the bottom of the screen. This log shows the results of the save, compile, and update process that just occurred. Review and become familiar with it. The window should display something similar to this code:

Compiling c:\Crestron\simpl\usrsplus\my first simpl+.usp...

Total Error(s): 0

Total Warning(s): 0

SIMPL+ file saved successfully

No errors found: SIMPL Windows Symbol Definition updated

This first SIMPL+ program is complete. The next section explains how to incorporate this program into the required SIMPL wrapper, and how to run and test it.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Quick_Start/Writing_Your_First_SIMPL_Plus_Program.htm*
