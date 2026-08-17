# #STRING_INPUT_JOIN

Name:

#STRING_INPUT_JOIN

Syntax:

#STRING_INPUT_JOIN<constant>

Description:

Changes the join number starting with the next STRING_INPUT or BUFFER_INPUT definition to the join number specified by <constant>.

Example:

STRING_INPUT SIG1[20], SIG2[20], SIG3[20], SIG4[20];

BUFFER_INPUT B1$[20]

In this example, SIG1 references Join #1, SIG2 references Join #2, SIG3 references Join #3, SIG4 references Join #4, and B1$ references Join#5.

STRING_INPUT SIG1[20], SIG2[20];

#STRING_INPUT_JOIN 20

STRING_INPUT SIG3[20], SIG4[20];

BUFFER_INPUT B1$[20]

SIG1 and SIG2 still reference Join #1 and Join #2, but SIG3 has been changed to reference Join #20, SIG4 references Join #21, and B1$ references Join#22.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Interfacing_to_the_CEN-OEM_via_a_SIMPL_Plus_Program/_STRING_INPUT_JOIN.htm*
