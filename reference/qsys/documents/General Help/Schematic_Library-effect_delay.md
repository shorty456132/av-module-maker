# Delay Effect

> Source: https://help.qsys.com/Content/Schematic_Library/effect_delay.htm

# Delay Effect

The Delay Effect component allows you to create the sound of a repeating, decaying echo.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **I/O Configuration**Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Delay Effect component is set to a **Mono In / Mono Out**, which provides one input. Additionally, you can set the Properties to allow for **Mono In / Stereo Out**, which gives you one input, or you can set it to **Stereo In /Stereo** Out which will give you two inputs.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Delay Effect component is set to a **Mono In / Mono Out**, which provides one output. Additionally, you can set the Properties to allow for **Mono In / Stereo Out**, which gives you two outputs (Left and Right), or you can set it to **Stereo In /Stereo Out** which will also give you two outputs (Left and Right).

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Delay Effect Properties

#### I/O Configuration

Sets the input to output configuration. When you select one of the stereo options, many of the controls are presented in Left and Right parameters. In addition, you are able to link some of the left/right parameters and the left/right tempos.

#### Max Delay (seconds)

Sets the upper limit for the Delay Time parameter.

[Setting the Delay](javascript:void(0))

* Adjust the Tempo, the Delay time changes within limits.
* Adjust the Delay, the Tempo changes within limits.
* Adjust the Note value, the Delay or Tempo changes depending on which was set last.
* The Note value does not change unless you change it.

### Start by setting the Tempo

1. Set the Tempo   
   If you know the beats per minute, you can enter that in the Tempo field. The Delay is set to the proper value for that Tempo and whatever the Note value is. Or, when the music starts, you can tap the tempo using the Tempo Tap button.
2. Adjust the Note value.   
   As you adjust the Note value, the Delay time changes to the appropriate delay for the set Tempo and the set Note value.

The table below shows the Delay times for 30, 60 and 120 BPM for each Note value. In addition, the table shows the Delay range available for each Note value when the Tempo value is at its minimum (30 BPM) and its maximum (60 BPM).

The shortest delay possible when adjusting the Note and Tempo values is 31.2 ms with the Note at 1/32 and the Tempo at 30 BPM. However, the minimum Delay you can have is 0.333 ms, and the maximum is 60 s, which means you can continue to adjust the Delay in both directions when the Tempo and Note values have reached their limits.

### Start by Setting Delay

1. Set the Delay  
   Enter the Delay time in either milliseconds, or seconds.(For example, *6m* for 6 milliseconds, and *6s* for 6 seconds.)
2. Adjust the Note value.   
   As you adjust the Note value, the Tempo changes to the appropriate Tempo for the set Delay and the set Note value. The Delay does not change.

|  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | 60 BPM | | |  | 30 BPM |  | 120 BPM |  | Delay Range @ 30 - 240 BPM | |
| Note | | Delay | Beat |  | Delay |  | Delay |  | Min | Max |
| (1/4) | | 1 s | 1 |  | 2 s |  | 500 |  | 250 ms | 2.00 s |
| (1/8) | | 500 ms | .5 |  | 1 s |  | 250 |  | 125 ms | 1.00 s |
| (1/16) | | 250 ms | 0.25 |  | 500 ms |  | 125 |  | 62.5 ms | 500 ms |
| (1/32) | | 125 ms | 0.125 |  | 250 ms |  | 62.5 |  | 31.2 ms | 250 ms |
| (1/2T) | | 1.33 s | 1.33 |  | 2.67 s |  | 667 |  | 333 ms | 2.67 s |
| (1/4T) | | 667 ms | 0.67 |  | 1.33 s |  | 333 |  | 167 ms | 1.33 s |
| (1/8T) | | 333 ms | 0.33 |  | 667 ms |  | 375 |  | 83.3 ms | 667 ms |
| (1/2.) | | 3 s | 3 |  | 6 s |  | 1.5 s |  | 750 ms | 6 s |
| (1/4.) | | 1.5 s | 1.5 |  | 3 s |  | 750 |  | 375 ms | 3 s |
| (1/8.) | | 750 ms | 0.75 |  | 1.5 s |  | 167 |  | 188 ms | 1.5 s |

[Controls](javascript:void(0))

#### High-Pass Frequency (L/R)

Frequencies below this setting are attenuated. You can use this to simulate distance. As distance increases, high and lower range frequencies drop off.

#### Low-Pass Frequency (L/R)

Frequencies above this setting are attenuated. You can use this to simulate distance. As distance increases, high and lower range frequencies drop off.

#### Delay (L/R)

Sets the time the wet signal is delayed from the dry signal. The Delay time can be set directly, by adjusting the Tempo, and by changing the Note value. If you change the Delay time, the Tempo changes, but not the Note value.

The Max Delay of 60 seconds is set in the Properties.

**Note:** Entering anything from 0.001Âµs to 0.005Âµs gets interpreted as 1.00 through 5.00 milliseconds. Entering anything greater than 0.005 gets interpreted as the milliseconds as entered (example 0.006 gets interpreted as .006 ms). The basic idea is that the value that you enter is larger than the max value and Q-SYS Designer assumes you want the value to be divided by 1000. If you need to input less than 6ms, you must manually type in ("5us", "4us", etc.). You will then see it convert to .005 ms, .004ms, etc.

#### Tempo (L/R)

Sets the beats per minute (BPM) time interval.
The BPM is based on one quarter note per beat. If you change the Tempo, the Delay changes.

#### Tempo Tap (L/R)

Allows you to set the tempo by tapping with a mouse pointer.

#### Note (L/R)

Sets the time the wet signal is delayed from the dry signal. When you change the Note value, the Tempo changes if you set the Delay first, and the Delay changes if you set the Tempo first. The Note value is not changed by changing the Delay or Tempo.

#### Regeneration (L/R)

Sets the amount of signal sent back into the delay.

#### Link (Stereo only)

Links the following parameters:

* Left & Right Regeneration
* Left & Right High-Pass Filter
* Left & Right Low-Pass Filter

#### Tempo Link (Stereo only)

Only on the Stereo (Out or In / Out) Delay. Links the Left and Right Tempo.

#### Dry/Wet Mix

Changes the balance between the dry input signal and wet delayed signal.

#### Master Bypass

Bypasses the controls of the Delay Effect Component.

[Control Pins](javascript:void(0))

The table below gives you the values you can enter, via the control pin inputs, to set the control to the desired position. In addition, you can use the output for controlling other components. All the data is taken using a Custom Controls Component connected to the output side of the Control Pins.

**Value**
- Taken from a Generic Float knob with a custom range equal to the range of the control or greater.

**String**
- Taken from a Text Display control.

**Position**
- Taken from a Position knob.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Delay (L/R) | .333 - 1.00 | .333ms to 1.00s | 0 - 1.00 | Input / Output |
| Dry/Wet Mix | 0 - 100 | â | 0 - 1.00 | Input / Output |
| High-Pass Frequency (L/R) | 20 - 20000 | 20.0Hz to 20.0kHz | 0 - 1.00 | Input / Output |
| Link | 0  1.00 | off  on | 0  1.00 | Input / Output |
| Low-Pass Frequency (L/R) | 20 - 20000 | 20.0Hz to 20.0kHz | 0 - 1.00 | Input / Output |
| Master Bypass | 0  1.00 | no  bypassed | 0  1.00 | Input / Output |
| Note (L/R) | 1.00  2.00  3.00  4.00  5.00  6.00  7.00  8.00  9.00  10.00 | 1/4  1/8  1/16  1/32  1/2T  1/4T  1/8T  1/2.  1/4.  1/8. | 0  .111  .222  .333  .444  .556  .667  .778  .889  1.00 | Input / Output |
| Regeneration (L/R) | 0 - 100 | â | 0 - 1.00 | Input / Output |
| Tempo (L/R) | 30.0 - 240 | 30.0bpm to 240bpm | 0 - 1.00 | Input / Output |
| Tempo Link | 0  1.00 | off  on | 0  1.00 | Input / Output |
| Tempo Tap (L/R) | 0  1.00 | false  true | 0  1.00 | Input / Output |
