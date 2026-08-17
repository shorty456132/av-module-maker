# Random

Name:

Random

Syntax:

INTEGER Random(INTEGER LowerBound, INTEGER UpperBound);

Description:

Generate a random number. See also: [Seed](<SEED.htm>) and [Rnd](<RND.htm>).

Parameters:

LowerBound is an INTEGER specifying the lower end of the range.

UpperBound is an INTEGER specifying the upper end of the range.

Both LowerBound and UpperBound are treated as unsigned values.

Return Value:

Returns an unsigned number from LowerBound to UpperBound. Both LowerBound and UpperBound are legal values.

Example:

INTEGER NUM;

FUNCTION MAIN()

{

NUM = RANDOM(25, 80);

PRINT("The random number between 25 and 80 is: %u\n", NUM);

}

An example output from this would be:

The random number between 25 and 80 is: 42

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Random_Number_Functions/RANDOM.htm*
