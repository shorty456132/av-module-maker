# GPIO Behavior During Boot-up and Redeploy

> Source: https://help.qsys.com/Content/Application_Integration/GPIO_Application/gpio_bootup_redeploy_behavior.htm

# GPIO Behavior During Boot-up and Redeploy

During startup or configuration changes, Q SYS GPIO devices may briefly toggle their output states. Once initialization is complete, all outputs return to their defined states in the design.Q-SYS device GPIO output states are undefined during boot-up and design redeploy. In the following table, "While On" and "While Off" indicate the button setting as defined in the running design file. During a reboot or redeploy, the setting may toggle depending on the GPIO type before returning to the defined setting after the design starts running. **Bold** text indicates a temporary GPIO setting during boot-up and redeploy.

[Core 510i](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Toggles to On |
| Open Collector | Toggles to Off | Stays Off |
| Raw | Stays On | Toggles to On |

[I/O Frame](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Toggles to Off | Stays Off |
| Open Collector | Stays On | Toggles to On |
| Raw | Stays On | Toggles to On |

[CX-Q, CXD-Q, DPA-Q Series](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Toggles to On |

[SPA-Qf Series](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Stays Off |

[I/O-22](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Toggles to On |

[Page Station](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Toggles to On |

[GPIO Out Core 24f, I/O-Core 24f](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Stays Off |
| Open Collector | Stays On | Stays Off |
| Raw | Stays On | Stays Off |

[GPIO Out Core 8 Flex, I/O-8 Flex](javascript:void(0))

**Note:** The Core 8 Flex and I/O-8 Flex GPIO output position persists during boot-up and redeploy.

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Stays Off |
| Open Collector | Stays On | Stays Off |
| Raw | Stays On | Stays Off |

[GPIO Out Core 110f, I/O-Core 110f, Core 110c](javascript:void(0))

**Note:** The Core 110f GPIO output setting persists during boot-up and redeploy.

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Stays Off |
| Open Collector | Stays On | Stays Off |
| Raw | Stays On | Stays Off |

[GPIO Out (NV-32-H)](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Toggles to Off | Stays Off |
| Open Collector | Stays On | Toggles to On |
| Raw | Toggles to Off | Stays Off |

[GPIO Out QIO-GP8x8, QIO-FLEX4A](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Digital Output | Stays On | Toggles to On |
| Open Collector | Toggles to Off | Stays Off |
| Raw | Stays On | Toggles to On |

[QIO-LVR4](javascript:void(0))

| GPIO Type | While On | While Off |
| --- | --- | --- |
| Relay Output | Stays On | Stays Off |
