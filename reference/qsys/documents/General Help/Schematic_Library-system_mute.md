# System Mute Component

> Source: https://help.qsys.com/Content/Schematic_Library/system_mute.htm

# System Mute Component

The System Mute component allows you to mute the system outputs at the Core. This used as a panic button for operators, and for bringing up new designs, where the individual gain settings have not been tested, in order to avoid extreme outputs. When you are in the Run mode, then switch to Design mode, whatever state the System Mute is in when you go to Design mode is remembered, in the design, when you deploy the design and go back to Run mode.

To deploy a design in a quiet mode:

**Note:** This procedure can be performed starting with Q-SYS Designer in Run Mode, or from a different design than the one running on the Core.

1. If Q-SYS Designer is in Run Mode press F7 (or File > Disconnect).
2. Press F6 (File > Emulate) to start the Emulate Mode.
3. Set the System Mute button to the active or muted state.
4. Make any desired changes/adjustments in the design.
5. Press F7 (File > Disconnect) to exit Emulate Mode.
6. Press F5 (File >Save to Core and Run). The system is muted.
7. Click the System Mute button to unmute the system.

**Note:** If the currently running design is "System Muted" , and you deploy a design that also "System Muted", the system remains muted after deployment. If the currently running design is "System Muted", and you deploy a design that is NOT "System Muted" the system will NOT be muted after deployment. The state of the System Mute button is stored in the design.

When you change the System Mute button from muted to unmuted, the gain ramps from -20 dB to 0 dB over a period of 3 seconds.

Since the System Mute controls the outputs at the Core, if there is a signal connected directly to an amplifier, such as the emergency audio on a [DAB-801](../Hardware/Accessories/017_DataPort_Amplifier_Backup_Panel.htm), or if there is an issue with an output card that is causing noise, using the System Mute will have no effect on those situations.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component has no input pins.

### Output Pins

This component has no output pins.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### System Mute Properties

This component has no configurable properties.

[Controls](javascript:void(0))

#### Mute

Mutes and un-mutes all system outputs at the Core.

#### Gain

Text display of the gain. When the system is muted, there is -100 dB applied to the core's outputs. When the system is then unmuted, the gain jumps from -100 dB to -20 dB, then ramps from -20 dB to 0 dB in three seconds.

#### System Mute / Unmute

The System Mute/Unmute is available only in **Emulate** or **Run** modes. Mutes and un-mutes all system outputs at the Core. This control is at the upper right-hand corner of the System Information bar, below the main menu.

[Control Pins](javascript:void(0))

The available **Control Pins** are:

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.000 | Output |
| Mute | 0  1 | unmuted  muted | 0  1 | Input / Output |
