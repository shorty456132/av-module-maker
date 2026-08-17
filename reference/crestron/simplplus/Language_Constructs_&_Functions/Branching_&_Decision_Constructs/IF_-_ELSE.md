# IF - ELSE

Name:

IF - ELSE

Syntax:

IF ( <expression>)

[{]

<statements>

[}]

[ELSE]

[{]

<statements>

[}]]

Since <statements> can be an IF construct, you can string out a series of IF-ELSE-IF statements of the form:

IF (<expression>)

[{]

<statements>

[}]

[ELSE] IF (<expression>)

[{]

<statements>

[}]]

NOTE: A final ELSE may be used to express default handling if none of the previous conditions were met.

IF (<expression>)

[{]

<statements>

[}]

[ELSE] IF (<expression>)

[{]

<statements>

[}]

[ELSE]

[{]

<statements>

[}]

Description:

Executes a piece of code only if its associated <expression> evaluates to true. Many expressions can be tested if the IF-ELSE-IF construct is used. Note that only one <statements> block in an IF-ELSE or IF-ELSE-IF construct is executed. In any section of the construct, if <statements> is only a single statement, then the { and } characters may be omitted.

Example:

STRING_INPUT IN$[100];

STRING Y$[100];

INTEGER X;

IF (IN$ = "STRING1")

{

X=5;

Y$ = IN$;

}

ELSE

{

X=6;

Y$ = "";

}

In this example, if IN$ is equal to STRING1, then the first two statements are executed. If IN$ is a different value, then the second groups of statements are evaluated. A more complex IF-ELSE-IF construct appears as:

IF (IN$ = "STRING1")

{

X=5;

Y$ = IN$;

}

ELSE IF (IN$="STRING2")

{

X=6;

Y$ = "";

}

ELSE

{

X = 7;

Y$ = "ZZZ";

}

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Branching_%26_Decision_Constructs/IF_-_ELSE.htm*
