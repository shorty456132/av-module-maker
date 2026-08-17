# What is SIMPL+?

SIMPL+® is a language extension to SIMPL. It does not replace SIMPL, but instead it enhances it. With SIMPL+ it is now possible to use a procedural “C-like” language to code elements of the program that were difficult, or impossible with SIMPL alone.

A SIMPL+ program is a module that directly interacts with the control system. In order to interact with the control system, a module must contain a few essential elements. The first element is a starting point. A starting point is needed for two reasons. 

  * First, it serves as a convenient place to initialize any global variables that are declared within the module. 

  * Second, any functionality that the module needs to perform on its own (instead of being triggered through an event), can be instantiated here. 




Another element is event processing. In order for a SIMPL+ module and a control system to interact, they must be able to send and receive signals to and from one anothe. Input and output (I/O) signals are declared within the module are then tied directly to the control system. Input signals are sent from the control system and are received within the SIMPL+ module. Output signals are sent from the SIMPL+ module to the control system. Events are functions that are triggered through input signals from the control system. I/O signals can be either digital, analog or serial and are declared within the SIMPL+ module. Events tell the SIMPL+ module that something has changed within the control system and allows the module to perform any action accordingly.

.

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/What_is_SIMPL_Plus_.htm*
