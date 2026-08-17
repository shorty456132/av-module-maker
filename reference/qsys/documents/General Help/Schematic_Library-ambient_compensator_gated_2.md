# Gated Ambient Compensator Component

> Source: https://help.qsys.com/Content/Schematic_Library/ambient_compensator_gated_2.htm

# Gated Ambient Compensator Component

The purpose of the **Gated Ambient Compensator** is to control the gain of a **Program**, for example, announcements, in a situation where the ambient noise varies.

The ambient noise is measured, and as it increases, the applied gain to the announcements increases at a set **Ratio**, so that when the announcement is made it is loud enough to overcome the ambient noise. When the announcement level exceeds the **Threshold Level**, the **Ambient Detector** becomes inactive so that the announcement is not measured along with the ambient noise. When the announcement level falls below the **Threshold Level**, the **Ambient Detector** again becomes active.

When the ambient noise is low, and an announcement is made, depending on the input level of the announcement, and the gain settings in the **Compensator**, attenuation may be applied to the announcement so that it is not too loud.

[Properties](javascript:void(0))

### Gated Ambient Compensator Properties

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Microphone Filter

Determines if the Mic Filter is active and available in the Control Panel.

[Controls](javascript:void(0))

### General

#### In Gain (dB)

Adjusts the microphone input level.

#### Detector (dB)

Displays the ambient level, including any program material present.

#### Response Panel

Graphically displays the operation of the Continuous Ambient Compensator.

The X axis represents the recovered ambient signal RMS level.

The Y axis represents the dB gain that is applied to the program material.

#### Bypass

When engaged, the Continuous Ambient Compensator is bypassed.

#### Gain (dB)

Displays the gain applied to the program material.

#### Out Gain (dB)

Adjusts the Program output level.

### Mic Filter

**Note:** Depending on the Type of filter you select, some of the controls listed below may not be available.

#### Bypass

When engaged, the Mic Filter is bypassed, the ambient noise is not filtered except by the Audio Bandwidth setting in the Properties.

#### Type

Selects the type of filter to use. You can select one of the following:

* Low-Pass
* High-Pass
* Band-Pass
* Band-Stop
* Parametric
* Low-Shelf
* High-Shelf

#### Bandwidth (Octave)

Sets the width of the frequency band to be filtered. Available only with the Band-Pass, Band-Stop, and Parametric filters.

#### Frequency (Hz)

Sets the frequency of the filter. For filters that have a bandwidth setting, this is the center frequency of the bandwidth.

The upper limit for this control is either 1.25 kHz, 2.5 kHz, or 5.0 kHz depending on the Audio Bandwidth Property.

#### Gain (dB)

Sets the gain for the Parametric, High-Shelf, and Low-Shelf filters.

### Detector

#### Program Threshold (dB)

Sets the threshold, of the **Program** input, above which the **Ambient Detector** is not active. When the program level falls below this setting, the **Ambient Detector** becomes active

#### Sense Delay (seconds or milliseconds)

Sets a delay in the time it takes the **Ambient Detector** to go from inactive to **Active**. This is to compensate for momentary pauses in the **Program** input.

#### Sensing

LED indicating if the **Ambient Detector** is active or not.

### Gain Calculation

#### Ambient Threshold (dB)

The crossing point of the ambient level and the **Minimum Gain**. At this point, as the ambient level rises, the gain applied to the **Program** moves from the **Minimum Gain** towards the **Maximum Gain**. The point at which the ambient level is high enough to have an impact on the **Program** gain.

#### Ratio ( *n*:1)

The ratio between the **Minimum Gain** and the **Maximum Gain** as measured from the **Ambient Threshold Level**.
The closer the **Ratio** is to 2, the lower the ambient level needs to be for the **Maximum Gain** to be used when the **Program** input passes the **Program Threshold**.

For example: If the **Ambient Threshold** is -30 dB,
**Minimum Gain** is -10 dB, **Maximum Gain** is 10 dB, and the **Ratio** is 2.0, when the ambient level reaches -20 dB, **Maximum Gain** is applied when the **Program Threshold** is reached.

Same example except the **Ratio** is 0.5. When the ambient level reaches 10 dB the **Maximum Gain** is applied when the **Program Threshold** is reached.

#### Minimum Gain (dB)

The minimum amount of gain you want to apply to the **Program** output when the ambient noise is at it's lowest point. Usually a negative amount, or attenuation - shown in red on the **Gain** meter. Gain is added to the **Program** input level up to this setting. If the **Minimum Gain** is -15 dB, and the **Program** input level is 5 dB, the **Program Output** is -10 dB

5 + (-15) = -10

#### Maximum Gain (dB)

The maximum amount of gain you want to apply to the **Program** output when the ambient noise is at it's highest point. Gain is added to the **Program** input level up to this setting. If the **Maximum Gain** is set to 10 dB, and the **Program** input level is 5 dB, the Program Output is 15 dB.

### Time Constants

#### Attack Time (seconds)

Sets the time it takes for the output amplitude to rise to 63% of the specified **Ratio** of the input amplitude once the **Ambient Threshold Level** is exceeded.

#### Release Time (seconds)

Sets the time it takes for the output to fall to 63% of the level set by the **Minimum Gain** control after the **Ambient Detector** level drops below the **Ambient Threshold Level**.

[Control Pins](javascript:void(0))

The available **Control Pins** depend on settings in **Properties**.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Ambient Detector Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Ambient Sense Delay Time | 0.00 to 10 | 0 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Ambient Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Applied Gain | 0 to 20 | 0 dB to 20 dB | 0.000 to 1.00 | Output |
| Attack Time | 1 to 10 | 1 s to 10 s | 0.000 to 1.00 | Input / Output |
| Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Input Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Maximum Program Gain | 0 to 20 | 0 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Microphone Filter Bandwidth | .010 to 3.00 | .010 to 3.00 | 0.000 to 1.00 | Input / Output |
| Microphone Filter Bypass | 0  1 | active  bypass | 0  1 | Input / Output |
| Microphone Filter Frequency | 10 to 5000 | 10 Hz to 5 kHz | 0.000 to 1.00 | Input / Output |
| Microphone Filter Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Microphone Filter Type | 1.00  2.00  3.00  4.00  5.00  6.00  7.00 | Low-Pass  High-Pass  Band-Pass  Band-stop  Parametric  Low-Shelf  High-Shelf | 0  .167  .333  .500  .667  .833  1.00 | Input / Output |
| Minimum Program Gain | -20 to 0 | -20 dB to 0 dB | 0.000 to 1.00 | Input /Output |
| Output Gain | -20 to 20 | -20 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Program Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Ratio | 0.500 to 2.00 | .500 to 2.0 | 0.000 to 1.00 | Input / Output |
| Release Time | 1 to 10 | 1 s to 10 s | 0.000 to 1.00 | Input / Output |
| Sensing | 0  1 | false  true | 0  1 | Output |
