# Rnd

Name:

Rnd

Syntax:

INTEGER Rnd();

Description:

Generate a random number. See also: [Seed](<SEED.htm>) and [Random](<RANDOM.htm>).

Parameters:

None.

Return Value:

An INTEGER from 0 to 65535.

Example:

INTEGER NUM;

FUNCTION MAIN()

{

NUM = RND();

PRINT("The random number is: %u\n", NUM);

}

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Random_Number_Functions/RND.htm*
