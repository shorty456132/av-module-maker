# Seed

Name:

Seed

Syntax:

Seed(INTEGER SeedValue);

Description:

Provides a seed or origin for the random number generator so that the numbers returned by RND and RANDOM are pseudo-random numbers. SEED is not required for generating random numbers as the random number generator will be seed with a default value. This default value is issued at control system restart, not program restart. That is, if you don't used the SEED call, you will not get the same value if you restart the program. For any particular value of SEED, the random number generator will generate a predictable series of numbers. Note that specifying the seed value is global to all SIMPL+ programs running inside a control system. The sequence begins again whenever SEED is called.

Parameters:

None.

Return Value:

None.

Example:

INTEGER NUM;

FUNCTION MAIN()

{

SEED(25);

NUM = RANDOM(25, 80);

PRINT("The random number between 25 and 80 is: %u\n", NUM);

}

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Random_Number_Functions/SEED.htm*
