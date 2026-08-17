# Amp Output (DataPort Amplifiers)

> Source: https://help.qsys.com/Content/Schematic_Library/amplifier_dataport.htm

# Amp Output (DataPort Amplifiers)

This topic covers the Amp Output component for QSC DataPort amplifiers, including CX, DCA, and PowerLight models.

**Note:** DataPorts on multi-port amplifiers must be wired to DataPorts on the same I/O Frame or Core. You cannot wire some of the amplifier's DataPorts to a Core and others, on the same amplifier, to an I/O Frame. You cannot wire some of the amplifier's DataPorts to one I/O Frame and others, on the same amplifier, to another I/O Frame.

[Inputs and Outputs](javascript:void(0))

### Inputs

The inputs are digital audio connecting to loudspeaker components. Loudspeaker signal pins are represented by a left-pointing () triangle, and the wiring is represented by a thin orange line.

### Outputs

The outputs are digital audio connecting to loudspeaker components. Loudspeaker signal pins are represented by a left-pointing () triangle, and the wiring is represented by a thin orange line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Amp Output Dataport Properties

#### Model

The **Model** of the amplifier - The **Model** is selected when you add an amplifier to **Inventory**, when you place the amplifier component in the Schematic, it retains the **Model** information. In the **Properties** you can change the **Model** if you need to.

#### Mode *n-n*1

Choose if channels *n* and *n* are to be in the **Stereo** mode or the **Bridged** mode. This setting is to reflect the physical amplifier's setting.

1The DataPort amplifiers support Bridged, Parallel and Stereo modes. Q-SYS supports amplifier modes Bridged and Stereo only. Parallel mode supplies the same signal to two channels by connecting both channel inputs to a single source. In Q-SYS, Parallel mode is accomplished by sending the same signal to two channels on the DataPort card. One DataPort cable carries two channels, so effectively there is no difference if you connect the channel inputs at the amplifier or in Q-SYS.

[Controls](javascript:void(0))

### Amplifier Status

#### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

#### On / Standby

Button controls the amplifier from **Standby** to **Power On**.

#### Meter Select

Selects either **RMS** or **Peak** for the five meters in all channels.

### Channel *n* Status

#### Mute

**Mute** button mutes the associated channel of the amplifier. Linked to the **Mute** button on the associated band of a loudspeaker.

#### Atten. Pot. (dB)

Setting of the **Attenuation Potentiometer** on the front panel of the amplifier.

#### Temperature

**Temperature** reading of the channel in - Centigrade.

#### Bridge

The amplifier must be connected and the On state for the **Bridge** and **Parallel** LEDs to work properly.

Yellow LED indicating that channel is in the **Bridge Mode**.

When this LED and the **Parallel** LED are off, the amplifier is in **Stereo** Mode. When they're both on, the amplifier is in **Bridge-Parallel** mode.

#### DAC Limit

LED indicating that signal to the D to A Converter is larger than can be reproduced and a limiter has been engaged to prevent clipping. This is an indication that the gain structure is not correct.

#### Protect

LED indicating that the channel is in **Protect Mode**. Usually due to attempting to drive too low an impedance for too long.

#### Clip

Yellow LED indicating that the channel is clipping.

#### Parallel 1

The amplifier must be connected and the On state for the **Parallel** and **Bridge** LEDs to work properly.

Yellow LED indicating that channel is in the **Parallel** Mode.

When this LED and the **Bridge** LED are off, the amplifier is in **Stereo Mode**. When they're both on, the amplifier is in **Bridge-Parallel** mode.

1When an amplifier is in Bridge Mode, the Parallel LED on the amplifier is lit along with the Bridge Mode LED. This LED is reflecting what is seen on the amplifier. See the note in the Properties table for [Mode *n-n*](#Amplifier_mode).

### Channel *n* Meter

#### Input (dBFS)

Measures the analog input to the amplifier channel (output of the **DataPort** card after the signal has been converted to analog). This reading can be **RMS** or **Peak** depending on the **Meter Select** setting for the associated channel.

The meter in the [DataPort](io_card_dataport.htm) component displays the **Peak Digital** output before the D to A Converter.

#### Voltage (V)

Measures the voltage of the amplifier / loudspeaker circuit. This reading can be **RMS** or **Peak** depending on the **Meter Select** setting for the associated channel.

#### Current (A)

Measures the current of the amplifier / loudspeaker circuit. This reading can be **RMS** or **Peak** depending on the **Meter Select** setting for the associated channel.

#### Power (W)

Measures the power of the amplifier / loudspeaker circuit. This reading can be **RMS** or **Peak** depending on the **Meter Select** setting for the associated channel.

#### Headroom (dB)

Measures the amount of headroom left before reaching the amplifier's maximum capabilities.

### Channel *n* Monitor

#### Listen

Enables and disables the loudspeaker monitor.

This is a radio type button and is linked to all other **Listen** buttons in your design. When this is engaged, all other **Listen** buttons disengage.

You can only listen to one amplifier channel at a time. In the loudspeaker components, you have the option to listen to one, all, or any combination of bands.

You must have the Loudspeaker Monitor component in the Schematic and properly connected to make use of the monitoring capability.

**Note:** The Monitor buttons are not linked in **Emulate** mode. Your design must be in **Run** mode for the functionality described above to operate.

#### Gain (dB)

Controls the gain of the monitor. This control has effect only when the Listen button is engaged.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

### Amplifier

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Peak/RMS Select | 0  1 | Peak  RMS | 0  1 | Input / Output |
| Power On | 0  1 | Standby  On | 0  1 | Input / Output |
| Status | 0  1  2  3  4 | OK (green)  Compromised (orange)  Fault (red)  Unknown (red)  Updating (blue) | 0  0.250  0.500  0.750  1.00 | Output |

### Channel

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Attenuation Pot. | 0 to 25 and Infinity | 0 to 25, Infinity | 0  26 | Output |
| Bridge | 0  1 | false  true | 0  1 | Output |
| Clip | 0  1 | false  true | 0  1 | Output |
| Current | 0 to 70 | 0 A to 70 A | 0.000  1.000 | Output |
| DAC Output Limit | 0  1 | false  true | 0  1 | Output |
| Headroom | 0 to 70 | 0 dB to 70 dB | 0.000  1.000 | Output |
| Input Meter | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| Monitor Gain | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Monitor Listen | 0  1 | disable  enable | 0  1 | Input / Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| Parallel | 0  1 | false  true | 0  1 | Output |
| Power | 0 to 10000 | 0 W to 10,000 W | 0.000  1.000 | Output |
| Protect | 0  1 | false  true | 0  1 | Output |
| Temperature | *n* | *n* Â°C | 0.000  1.000 | Output |
| Voltage | 0 to 150 | V to 150 V | 0.000  1.000 | Output |
