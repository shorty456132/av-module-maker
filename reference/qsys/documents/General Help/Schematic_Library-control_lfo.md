# LFO (Low Frequency Oscillator) Component

> Source: https://help.qsys.com/Content/Schematic_Library/control_lfo.htm

# LFO (Low Frequency Oscillator) Component

The LFO produces control outputs that you can use to control other components based on the various outputs of the LFO. For example, you can have the RMS Level of a Sine generator component varying at a set rate over a set range with a specific waveform.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### LFO Properties

#### Type

To choose the desired type of oscillator.

The **Generic** output varies the control to which it is connected anywhere from 0 to 100% of the controlled Control's range or within a specified window of the entire range. Good for a variety of controls.

The **Level Modulator** output varies the control to which it is connected based on dB level. You can vary the level for a specified window (Depth) of 0 dB to 20 dB, starting at a specified level (Input) anywhere from -100 dB to 20 dB. Good for dB level controls.

The **Frequency Modulator** output varies the control to which it is connected based on frequency. You can vary the frequency for a 2-Octave window (Depth) starting at a specified frequency anywhere from 10 Hz to 20 kHz. Good for frequency controls.

[Controls](javascript:void(0))

### Setup

#### Waveform

To choose the form of the output.

PWM allows you to change the Duty Cycle from 0 to 100%.

The Pulse Train provides a spike pulse at an interval specified by the period adjustment.

#### Period (seconds)

Sets the period time of the waveform. This is the speed at which the controls are varied.

The period is the reciprocal of the frequency. A Period 100 ms (0.100 s) = 10 Hz, a Period of 60 s = .016 Hz

#### Duty Cycle (percent)

**Note:** Duty Cycle available with PWM Waveform only.

Sets the percentage of the period where the pulse is positive, or high.

The ratio between the pulse duration and the period of a rectangular waveform expressed as a percentage.

### Run

#### Free-Run

Allows the oscillator to run continually.

#### One-Shot / Sync

Supplies one period of output.

### Oscillator Output - Generic (Percentage)

The Generic (percentage) oscillator output controls behave in the same way as a position control. For example, 50% is midpoint of the range of the control to which it is connected. The Minimum and Maximum controls form a window between them in which the connected control is modulated. For example, if you set the Minimum at 10% and the Maximum at 30%, the connected control is modulated 20% of its range between 10% and 30%. You could change the Minimum and Maximum to 20% and 40%, and the control would still be modulated 20% of its range, but at a different position.

The fact that this is a percentage control, makes it adaptable to most controls regardless of their range.

#### Minimum (percent)

Sets the Minimum output percentage. This is the starting point of the range (or window) over which the connected control is modulated.

If the Minimum is set above the Maximum, it acts as the Maximum.

#### Maximum (percent)

Sets the Maximum output percentage. This is the ending point of the range (or window) over which the connected control is modulated.

If the Maximum is set below the Minimum, it acts as the Minimum.

#### Output (percent)

A display and text readout of the output as it is varied between the starting (Minimum) and ending points of the variation range.

### Oscillator Output - Level Modulator

The Level Modulator is intended primarily to be used with level type controls with ranges of -100 dB to 20 dB. The range of modulation is limited to 20 dB.

#### Input (dBFS)

Sets the Input level for the modulator. This is the starting point of the range (or window) over which the connected control is modulated.

#### Depth (dB)

Sets the range (or window) over which the connected control is modulated. This control is limited to a 0 dB to 20 dB range.

#### Output (dB)

A display and text readout of the output as it is modulated between the starting point (Input) over the range of modulation set by the Depth control.

### Oscillator Output - Frequency Modulator

The Frequency Modulator is intended primarily to be used with frequency type controls with ranges of 10 Hz to 20 kHz. The range of modulation is limited to 2 octaves.

#### Input (Hz)

Sets the Input frequency for the modulator. This is the starting point of the range (or window) over which the connected control is modulated.

#### Depth Octave

Sets the range (or window) over which the connected control is modulated. This control is limited to a 0 dB to 20 dB range.

#### Output (Hz)

A display and text readout of the output as it is modulated between the starting point (Input) over the range of modulated set by the Depth Octave control.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Depth [2](#Level_Modulator) | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Depth Octaves [3](#Frequency_Modulator) | 0.000 to 2.00 | 0.000 to 2.00 | 0.000 to 1.00 | Input / Output |
| Duty Cycle [1](#Generic_(Percentage))[2](#Level_Modulator)[3](#Frequency_Modulator) | 0.0 to 100 |  | 0.000 to 1.00 | Input / Output |
| Enable (Free Run) [1](#Generic_(Percentage))[2](#Level_Modulator)[3](#Frequency_Modulator) | 0  1 | false  true | 0  1 | Input / Output |
| Input Frequency [3](#Frequency_Modulator) | 10.0 to 20,000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Input / Output |
| Input Level [2](#Level_Modulator) | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Input / Output |
| Minimum [1](#Generic_(Percentage)) | 0.0 to 100 | â | 0.000 to 1.00 | Input / Output |
| Maximum [1](#Generic_(Percentage)) | 0.0 to 100 | â | 0.000 to 1.00 | Input / Output |
| Output [1](#Generic_(Percentage)) | 0.0 to 100 | â | 0.000 to 1.00 | Output |
| Output Level [2](#Level_Modulator) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Output Frequency [3](#Frequency_Modulator) | 10.0 to 20,000 | 10 Hz to 20 kHz | 0.000 to 1.00 | Output |
| Period [1](#Generic_(Percentage))[2](#Level_Modulator)[3](#Frequency_Modulator) | 0.100 to 60 | 100 ms to 60 s | 0.000 to 1.00 | Input / Output |
| Trigger (1-Shot/Sync) [1](#Generic_(Percentage))[2](#Level_Modulator)[3](#Frequency_Modulator) | Trigger Button | | | Input / Output |
| Waveform [1](#Generic_(Percentage))[2](#Level_Modulator)[3](#Frequency_Modulator) | 0.00  1.00  2.00  3.00  4.00  5.00  6.00  7.00 | Off  Square  PWM  Sine  Triangle  Rising Sawtooth  Falling Sawtooth  Pulse Train | 0  0.143  0.286  0.429  0.517  0.714  0.857  1.00 | Input / Output |
|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1. Available with the Generic (Percentage) LFO Type.2. Available with the Level Modulator LFO Type.3. Available with the Frequency Modulator LFO Type. | | | | |
