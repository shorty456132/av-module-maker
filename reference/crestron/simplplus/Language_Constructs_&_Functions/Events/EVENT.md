# EVENT

Name:

EVENT

Syntax:

EVENT

{

[Local Variable Definitions]

<statements>

}

Description:

Executes the defined <statements> anytime one of the inputs to the SIMPL+ symbol changes. It is similar to having a CHANGE statement listed for every input, and each change is set up to execute a common block of code.

(see also [StackedEvents](<Stacked_Events.htm>) and [THREADSAFE](<THREADSAFE.htm>))

Example:

ANALOG_INPUT level1, level2, level3;

STRING_INPUT extra$[2][20];

STRING_OUTPUT OUT$;

EVENT

{

OUT$=extra$[0]+extra$[1]+CHR(level1)+CHR(level2)+CHR(level3);

}

In this example, when the ANALOG_INPUTs level1, level2, level3, or level4 have any change or the STRING_INPUT array extra$ has changed, the STRING_OUTPUT OUT$ will be recomputed and reissued.

Version:

X Generation:

SIMPL v1.20.01 and later

2-Series

SIMPL v2.01.05 and later [Same as X Generation v1.20.01], however Local variables are allowed within EVENT statements.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Events/EVENT.htm*
