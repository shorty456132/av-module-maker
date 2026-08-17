# FIR Custom Filter

> Source: https://help.qsys.com/Content/Schematic_Library/filter_FIR.htm

# FIR Custom Filter

Q-SYS provides the capability of loading your filter design results into the FIR (Finite Impulse Response) Custom Filter, giving you explicit control over the phase and magnitude response of the Custom FIR filter.

You set the size of the FIR filter, in the component properties, by specifying the number of coefficients. If the FIR Filter component has more coefficients defined than what is contained in the loaded file, Q-SYS assigns zeros to missing coefficients. If there are more coefficients in the file than defined in the design, Q-SYS discards the extra coefficients.

[Coefficient File](javascript:void(0))

You can load a custom FIR coefficients file at runtime. Typically, a FIR filter is designed using filter design software that computes the coefficients. After you design the filter, you export the coefficients to a .csv (comma separated value) or .wav file. This file is then loaded at runtime by clicking Load Coefficients - see [Controls](#Controls). The file containing the coefficients is a row of values, separated by commas, representing time from left to right.

**Note:** Ensure that the Coefficient Count equals the number of coefficients (FIR taps) in your FIR coefficients file. See [Properties](#Properties).

**Note:** A change of the coefficient count property is not immediately reflected in the componentâs open control panel. Before loading a new coefficient set file, close the control panel and re-open it for the coefficient count change to go into effect.

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Type** Property.

### Input Pins

#### Input

Audio signal pins are represented by a circle, and traditional wiring is represented by a thin black line.

By default, the FIR Custom Filter component is set to a **Mono** channel, which provides one input. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 inputs.

### Output Pins

#### Output

Audio signal pins are represented by a  circle, and traditional wiring is represented by a thin black line.

By default, the FIR Custom Filter component is set to a **Mono** channel, which provides one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two outputs; or you can choose **Multi-Channel**, which will allow you to choose between 2 and 256 outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### FIR Custom Filter Properties

#### Coefficient Count

Determines the number of coefficients for the FIR filter. The quantity defined here must match the number of coefficients contained in the .wav or .csv file loaded at runtime. You can choose between 4 and 16,384.

**Note:** A change of the coefficient count property is not immediately reflected in the componentâs open control panel. Before loading a new coefficient set file, close the control panel and re-open it for the coefficient count change to go into effect.

### Channels

#### Type

Sets the type of Channel input and output. You can choose from **Mono**, **Stereo**, or **Multi-channel**. When Multi-channel Type is selected, you can select from 2 to 256 channels.

#### Count

Only available when **Multi-channel** is selected, you can select from 2 to 256 channels.

### Response Panel

#### Enabled

If enabled, you will have access to the [Response Graph](#ResponseGraph) in Controls.

#### Size

You can choose to view the [Response Graph](#ResponseGraph) in **Small**, **Medium**, or **Large** scale within the Controls.

[Controls](javascript:void(0))

### Response

#### Response Graph

The scales for the Response Graph vary depending on the measurement method you select.

The vertical line of the crosshair cursor provides a readout of its position on the X axis scale.

The vertical movement of the horizontal crosshair follows the magnitude or amplitude of the signal.

#### Magnitude

Measures the magnitude of the input signal over the audio frequency range. Represented by the blue line.

#### Magnitude / Phase

Same as the Magnitude selection but with the addition of a phase line.

#### Impulse

Measures amplitude (Y axis) vs. time in milliseconds (X axis) of the impulse response.

#### Load Coefficients

Opens a standard Windows "Open" dialog box where you can navigate to, and open either a .csv or .wav file containing the coefficients defining the filter.

**Note:** A change of the coefficient count property is not immediately reflected in the componentâs open control panel. Before loading a new coefficient set file, close the control panel and re-open it for the coefficient count change to go into effect.

### Master

#### Bypass

Bypasses all phase and magnitude response of the Custom FIR filter.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Master: Bypass | 0  1 | no  bypassed | 0  1 | Input / Output |
| JSON1 | (text) | | | Input / Output |

[JSON1 Example](javascript:void(0))

Expected JSON is a JSON array of floats for the filter values.

#### Schematic Example

#### Script Example

```lua
require("json")  
taps_json = json.encode( { 0.019103115507295647, 0.08978343604891695,  
                           0.1932546034443056,   0.27616188977139156,  
                           0.27616188977139156,  0.1932546034443056,  
                           0.08978343604891695,  0.019103115507295647 } )  
print( taps_json )  
Controls["taps"].String = taps_json
```

#### Debug Output

```lua

2023-03-08T17:22:24.226	Starting Script
2023-03-08T17:22:24.227	[0.019103115507296,0.089783436048917,0.19325460344431,0.27616188977139,0.27616188977139,0.19325460344431,0.089783436048917,0.019103115507296]
```
