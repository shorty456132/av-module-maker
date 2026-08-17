# RTA - Band-Pass

> Source: https://help.qsys.com/Content/Schematic_Library/rta_bandpass.htm

# RTA - Band-Pass

The RTA (Real Time Analyzer) - Band-Pass component allows you to measure the magnitude of a signal over the audio frequency range. The RTA - Band-Pass is typically used for tuning your system. For example, you can place microphones around your venue, feed them into the RTA - Band-Pass, and adjust the EQ for the individual areas to get the best/same tuning for each area.

[Inputs and Outputs](javascript:void(0))

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the RTA- Band-Pass component only has one input pin available.

### Output Pins

This component does not have any output pins available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### RTA - Band-Pass Properties

#### Bandwidth

Selects the bandwidth for the band-pass filters in the RTA - Band-Pass.

One octave provides 10 filters for the audio spectrum giving a wide bandwidth for each filter and a smoother response. A bandwidth of 1/24 octave provides 124 filters giving a narrow bandwidth for each filter, and a more granular response - more distinct highs and lows. You can choose from the following:

* 1 Octave
* 1/3 Octave
* 1/6 Octave
* 1/12 Octave
* 1/24 Octave

[Controls](javascript:void(0))

### Response Graph

#### Response Panel

Graphical display of the RTA - Band-Pass response.

### Configure

#### RMS Response Time constant (ms / seconds)

Sets the RMS Level Detector time constant for both attack and decay.

This controls how quickly the RTA - Band-Pass A respond to changes in the input levels.

#### Max Hold Time (seconds)

Sets how long the maximum magnitude displays are held before refreshing.

#### Infinite Hold (button)

Holds the display, until the button is disengaged.

During the period the Infinite Hold button is on, the RTA - Band-Pass updates the display with any magnitudes that are higher than the initial response, but does not change if the magnitude is lower.

#### Clear Response

Clears the Response Panel display.

[Control Pins](javascript:void(0))

**Note:** These outputs represent array values displayed in the RTA graph that may be used in scripting.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Clear | trigger | | | Input / Output |
| Frequencies | see note | | | Output |
| Infinite Max Hold | 0  1 | false  true | 0  1 | Input / Output |
| Max Hold Time | 0.100 to 10 | 100 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Max RMS Levels | see note | | | Output |
| RMS Levels | see note | | | Output |
| RMS Response Time | 0.010 to 1.00 | 10 ms to 1 s | 0.000 to 1.00 | Input / Output |
