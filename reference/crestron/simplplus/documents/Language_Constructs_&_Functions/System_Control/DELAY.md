# Delay

Name:

Delay

Syntax:

Delay(INTEGER TIME);

Description:

Forces a task switch and starts a timer for the hundredths of a second specified by TIME. The system continues with the statements after a delay when the delay time has expired.

See also: [Wait](<../Wait_Events/WAIT.htm>).

Parameters:

TIME is the number of hundredths of a second to delay. For example, 500 specifies a 5-second delay.

Return Value:

None.

Example:

// A delay of 525 hundredths of a second or 5.25 seconds

#define_constant MY_DELAY 525

DELAY(MY_DELAY);

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Control/DELAY.htm*
