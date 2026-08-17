# Priority Ducker

> Source: https://help.qsys.com/Content/Schematic_Library/priority_ducker.htm

# Priority Ducker

The Priority Ducker is used to attenuate one or more channels of audio input when the audio input of a "priority" channel reaches a specified **Threshold**. The audio on the Priority channel is then mixed to the outputs in place of, or louder than, the attenuated audio (refer to the diagram below). Using the controls provided in the Control Panel, you can control:

* The amount of gain applied to the main channels
* How long the main channels are held at the gain level
* How fast the reduced gain is applied to the main channels, and how fast the initial gain is re-applied, providing smooth transitions
* The gain of the **Priority** channel.

The Priority Ducker can have from 1 to 512 audio inputs and 1 **Priority** channel. You can choose a pre-set **Detector Time**, or you can choose the manual control. The **Priority** channel is the last input on the left side of the Priority Ducker Component.

A typical application would be for emergency announcements; when an emergency announcement begins, all of the other channels are reduced in gain and only the emergency announcement is heard.

[Priority Ducker Block Diagram](javascript:void(0))

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Channels**Property.

### Input Pins

#### Input

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Priority Ducker component is set to a **8**channels, which provides eight inputs. Additionally, you can choose between 1 and 512 inputs.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line.

By default, the Priority Ducker component is set to a **8**channels, which provides eight outputs. Additionally, you can choose between 1 and 512 outputs.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Priority Ducker Properties

#### Channels

Sets the number of available channels for the Priority Ducker. You can choose between 1 and 512.

#### Detector Time

Selects a preset Detector Time, or enables the Detector Time control in the Control Panel.

#### Bypass Gain Meter

When set to **Active**, the **Applied Gain** meter is active regardless of the state of the **Bypass** button. This means you can adjust the Priority Ducker in **Bypass** mode.

When set to **Inactive**, the **Applied Gain** meter is inactive to indicate that the component is in **Bypass** mode.

[Controls](javascript:void(0))

### Detector / Response

#### In Gain (dB)

Controls the input **Gain** of the **Priority** channel. This control has no effect on the main channel inputs to the Priority Ducker.

#### Response Panel (dB)

**Response** graph:

The x-axis represents the RMS Level Detector level.

The y-axis represents the gain of the main inputs.

#### Detector (dB)

The **Detector** meter monitors the RMS Level Detector level.

#### Bypass

The **Bypass** button bypasses the In and Out Gain controls.

### Gain Calculation

#### Threshold Level (dBFS)

The **Threshold Level** is the RMS level of the **Priority** channel at which the Priority Ducker activates.

#### Depth (dB)

The **Depth** sets the amount of attenuation applied to the main input channels when the Priority Ducker is activated. The Priority channel is mixed with the main outputs, so the **Depth** setting controls how much of the main channels are heard in the output. Setting the **Depth** to 60 dB of attenuation essentially mutes the main channels.

#### Priority Gain (dB)

The **Priority Gain** controls the output gain of the priority channel. Adjust this gain to the level you wish the priority channel to be heard when mixed to the outputs with the attenuated audio.

### Time Constants

#### Attack Time (ms)

The **Attack Time** is the time it takes the main channel output to fall to 63% of the **Depth** level when the Priority Ducker is activated.  
Use this control to provide a smooth transition from the main channel audio to the Priority channel audio.

#### Hold Time (ms)

The **Hold Time** determines how long the main channel stays at **Depth** once the **Detector** level drops below the **Threshold**.  
This is to prevent the main channel from opening and closing due to momentary pauses in the Priority channel input.

#### Release Time (ms)

The **Release Time** is the time it takes the main channel output to return to 63% of its normal level when the Priority Ducker is deactivated and the **Hold Time** expires.  
Use this control to provide a smooth transition from the **Priority** channel audio back to the main channel audio.

#### Detector Time (ms)

The **Detector Time** control is available when you have selected **Use Control** for Detector Time in the Properties.

The Detector Time determines the rate of change of the **Detector** level in response to changes in the Priority input signal.  
This adjustment is to prevent changes (spikes, low frequency signals) in the priority input from causing unwanted, momentary output.

### Gain

#### Applied Gain (LED)

The **Applied Gain** LED lights when the RMS level of the **Priority** channel exceeds the **Threshold Level**, that is, when the Priority Ducker is activated.

#### Applied Gain

The **Gain** meter represents the amount of gain applied to the main channels.

#### Out Gain

Control the Gain of the overall output of the Priority Ducker, both Priority and main channels.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Active | 0  1 | false  true | 0  1 | Output |
| Applied Gain | 00 to -40 | 0 dB to -40 dB | 0.000 to 1.00 | Output |
| Attack Time | 0.0005 to 10.0 | 5.00 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Bypass | 0  1 | Active Bypass | 0  1 | Input / Output |
| Depth | 0 to 100 | 0 dB to 100 dB | 0.000 to 1.00 | Input / Output |
| Detector Level | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Detector Time | 0.0001 to 0.1 | .100 ms to 100 ms | 0.000 to 1.00 | Input / Output |
| Hold Time | 0.001 to 30 | 1.00 ms to 30 s | 0.000 to 1.00 | Input / Output |
| Input Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Output Gain | -20.0 to 20.0 | -20.0 dB to 20.0 dB | 0.000 to 1.00 | Input / Output |
| Priority Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Release Time | 0.010 to 10 | 10.0 ms to 10 s | 0.000 to 1.00 | Input / Output |
| Threshold Level | -60 to 20 | -60 dB to 20 dB | 0.000 to 1.00 | Input / Output |
