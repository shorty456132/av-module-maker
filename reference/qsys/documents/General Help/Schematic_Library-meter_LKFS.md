# LKFS Meter [BETA]

> Source: https://help.qsys.com/Content/Schematic_Library/meter_LKFS.htm

# LKFS Meter [BETA]

The LKFS Meter [BETA] provides the ability to measure sound loudness using the LKFS (Loudness, K-weighted, relative to full scale) standard. It is typically used to measure the loudness of broadcast program material, which could be music or speech.

**Note:** This is a BETA component. Though it is functional, it is not feature complete and is subject to change.

[Configuration Overview](javascript:void(0))

### Set properties

In your schematic, select the component to configure the Input Type, which determines the number of input and output pins. See [Properties](#Properti).

### Connect inputs and outputs

* **Input**: Connect the left side pins to the sound source, such as an audio player or some other audio output.
* **Output**: Connect the right side pins to the [Responsalyzer](responsalyzer.htm) component if you want to measure the frequency of the input signal. The output pins send frequency-weighted filter audio output.

### Run your design and configure controls

1. Press F5 to save your design to the Core and run it.
2. Double-click the LKFS Meter component to open its control panel.
3. Observe the Loudness (LKFS) meter as the input signal is processed, and configure component controls as desired. See [Controls](#Controls).

[Inputs and Outputs](javascript:void(0))

**Note:** The number of signal pins is variable and set in the component's **Input Type** Property.

### Input Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the LKFS Meter [BETA] component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; you can choose **LCR**, which will give you Left, Right, and Center weighted inputs and outputs; **5.1 Surround** give you Left, Right, and Center weighted inputs and outputs along with Left and Right Surrounds; **7.1 Surround** will offer Left, Right, and Center weighted inputs and outputs along with Left and Right Surrounds, and weighted Center Right and Center Left.

### Output Pins

#### Channels

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the LKFS Meter [BETA] component is set to a **Mono** channel, which provides one input and one output. Additionally, you can set the Properties to allow for **Stereo**, which gives you two inputs and outputs; you can choose **LCR**, which will give you Left, Right, and Center weighted inputs and outputs; **5.1 Surround** give you Left, Right, and Center weighted inputs and outputs along with Left and Right Surrounds; **7.1 Surround** will offer Left, Right, and Center weighted inputs and outputs along with Left and Right Surrounds, and weighted Center Right and Center Left.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### LKFS Meter [BETA] Properties

#### Input Type

Select the type (number of channels) of incoming audio to measure. You can choose from any of the following:

* Mono
* Stereo
* LCR
* 5.1 Surround
* 7.1 Surround

[Controls](javascript:void(0))

#### Loudness (LKFS)

Displays the measured LKFS level. The meter range is -39dB to -9dB.

#### Max Hold Time

Sets the time interval (seconds) to reset the maximum level.

#### Infinite Max Hold

When enabled, Max Hold Time is ignored. The maximum level is held until manually reset.

#### Reset Max

Click to reset the maximum level.

#### Max Loudness (LKFS)

Keeps track of the maximum LKFS loudness level over time.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Infinite Maximum Hold | 0  1 | false  true | 0  1 | Input / Output |
| Loudness (LKFS) | -120 to 20 | -120dB to 20dB | 0.00 to 1.00 | Output |
| Maximum Hold Time | 1 to 100 | 1.00s to 100s | 0.00 to 1.00 | Input / Output |
| Maximum Loudness (LKFS) | -120 to 20 | -120dB to 20dB | 0.00 to 1.00 | Output |
| Reset Maximum Loudness | 0  1 | false  true | 0  1 | Input / Output |
