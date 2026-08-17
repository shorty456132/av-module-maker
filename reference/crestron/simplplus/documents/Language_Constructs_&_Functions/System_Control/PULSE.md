# Pulse

Name:

Pulse

Syntax:

Pulse(TIME, DIGITAL_OUTPUT OUT);

Description:

Pulses the output high then low for the specified length of time (in hundredths of a second). When the pulse starts, a task switch is performed so other logic can be processed. Pulse is always high, then low. If the output is already high, the high is ignored, but the low will be sent at the appropriate time.

Parameters:

TIME is the number of hundredths of a second to pulse. For example, 500 specifies a 5-second delay.

OUT is a DIGITAL_OUTPUT that is to be pulsed.

Return Value:

None.

NOTE: (X-Gen only) Elements of a DIGITAL_OUTPUT array cannot be used within the Pulse function

Example:

// A pulse of 525 hundredths of a second or 5.25 seconds

#define_constant MY_PULSE_TIME 525

DIGITAL_OUTPUT OutputToPulse;

PULSE(MY_PULSE_TIME, OutputToPulse);

This will execute immediately and output a pulse of 5.25 seconds to the digital output OutputToPulse.

Version:

X Generation: SIMPL v1.20.01 and later

2-Series: SIMPL v2.01.05 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Control/PULSE.htm*
