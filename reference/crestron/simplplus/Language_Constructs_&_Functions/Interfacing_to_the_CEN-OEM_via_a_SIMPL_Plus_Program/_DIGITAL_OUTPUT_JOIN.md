# #DIGITAL_OUTPUT_JOIN

Name:

#DIGITAL_OUTPUT_JOIN

Syntax:

#DIGITAL_OUTPUT_JOIN<constant>

Description:

Changes the join number starting with the next DIGITAL_OUTPUT definition to the join number specified by <constant>.

Example:

DIGITAL_OUTPUT SIG1, SIG2, SIG3, SIG4;

In this example, SIG1 references Join #1, SIG2 references Join #2, SIG3 references Join #3, and SIG4 references Join #4.

DIGITAL_OUTPUT SIG1, SIG2;

#DIGITAL_OUTPUT_JOIN 20

DIGITAL_OUTPUT SIG3, SIG4;

SIG1 and SIG2 still reference Join #1 and Join #2, but SIG3 has been changed to reference Join #20, and SIG4 references Join #21.

Version:

CEN-OEM ONLY: SIMPL v1.50.06 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Interfacing_to_the_CEN-OEM_via_a_SIMPL_Plus_Program/_DIGITAL_OUTPUT_JOIN.htm*
