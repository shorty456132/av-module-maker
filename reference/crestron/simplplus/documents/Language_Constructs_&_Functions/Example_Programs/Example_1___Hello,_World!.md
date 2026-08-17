# Example 1: Hello, World!

// A digital input from the SIMPL program DIGITAL_INPUT TRIG;

// Upon the digital signal TRIG going high or low, the Hello,

// World! message is printed.

CHANGE TRIG

{

PRINT("Hello, World!\n");

}

// Main is only called once when the system starts up or is reset.

FUNCTION MAIN()

{

PRINT("Main Starts!\n");

}

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Example_Programs/Example_1___Hello%2C_World%21.htm*
