# Status/Control (DDI-11)

> Source: https://help.qsys.com/Content/Schematic_Library/dataport_line_out_adapter.htm

# Status/Control (DDI-11)

The DDI-11 (DataPort Line Out Adapter) component enables you to convert the output of one connector on a DataPort card installed in the Core, or an I/O Frame to two standard analog line out connections for use with a non-DataPort amplifier. The component in Q-SYS Designer represents a physical [adapter cable available from QSC](http://yhst-93643794936312.stores.yahoo.net/sg00051500.html) along with the installation instructions.

**Note:** Use the installation instructions under **Alternate Uses** in the DDI-11 Installation Guide.

This topic covers the use and configuration of the component in Q-SYS Designer.

When the DDI-11 is used, there is no control or telemetry available through the two associated DataPort card channels - they behave the same as a Line Out card. You must have the DDI-11 component in your design and wired to a DataPort component, and the DDI-11 adapter connected to the DataPort card for this feature to operate. If either is installed, and the other missing, the output is muted.

[Inputs and Outputs](javascript:void(0)) 

### Input Pins

Amplifier signal pins are represented by a left-pointing () triangle, and the wiring is represented by a thin orange line. This component only has one input pin available.

### Output Pins

This component has no output pins available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

There is one set of the following controls for each channel.

#### Meter (dBu)

Measures the output level.

#### Mute

Mutes the output.

#### Invert

Inverts the output.

#### Gain (dB)

Sets the gain of the output.

[Control Pins](javascript:void(0))

There is one set of the following control pins for each channel.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Meter | -100 to 20 | -100 dB to 20 dB | 0.000  1.000 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
