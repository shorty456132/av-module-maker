# Introduction 

SIMPL+ is a language extension that enhances SIMPL by using a procedural "C-like" language to code elements of the program that were difficult, or impossible, with SIMPL alone. This help system provides specific information about the SIMPL+ language syntax, and can be used as a reference manual.

For a tutorial on SIMPL+ programming, consult the Crestron SIMPL+ Software Programming Guide (Doc. 5789A). The latest version of the guide can be obtained from the Product Manuals area of the Crestron website ([www.crestron.com](<http://www.crestron.com>)). You can also click [here](<../SIMPL_Plus_Tutorial/What_is_SIMPL_Plus_.htm>) to open the programming guide from this help file.

A SIMPL+ program is a module that directly interacts with the control system. To interact with the control system, a module must contain a few essential elements. The first element is a starting point. A starting point is needed for two reasons. First, it serves as a convenient place to initialize any global variables that are declared within the module. Second, any functionality that the module needs to perform on it’s own (instead of being triggered though an event), can be instantiated here. Another element is event processing. In order for a SIMPL+ module and a control system to interact, they must be able to send and receive signals to and from one another. Input and output (I/O) signals are declared within the module and are then tied directly to the control system. Input signals are sent from the control system and are received within the SIMPL+ module. Output signals are sent from the SIMPL+ module to the control system. Events are functions that are triggered through input signals from the control system. I/O signals can be either digital, analog or serial and are declared within the SIMPL+ module. Events tell the SIMPL+ module that something has changed within the control system and allows the module to perform any action accordingly.

NOTE: In some cases the version of the SIMPL+ Cross Compiler Include file can cause unexpected return values. If you experience this phenomenon check the Cross Compiler Include file version by opening Help | About SIMPL+ . . . in the SIMPL+ Editor.

hv.3.03.03; 23.5.18

---
*Source: https://help.crestron.com/simpl_plus/Content/General_Information/Index.htm*
