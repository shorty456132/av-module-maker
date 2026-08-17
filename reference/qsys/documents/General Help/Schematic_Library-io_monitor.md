# IO Monitor Component

> Source: https://help.qsys.com/Content/Schematic_Library/io_monitor.htm

# IO Monitor

The IO Monitor allows you to monitor the audio of any supported analog audio input or output or any network RX (Q-LAN, System Link, AES67, Software Dante, Media Stream, and WAN Stream) from a single location in your design or UCI.

* The I/O represented by the component you want to monitor must have a supported I/O type. For example, Flex Input on a Core 8 Flex, a Mic/Line Input on a QIO-ML2x2, or a Q-LAN RX in the Core.
* The component you want to monitor must be in the design. In addition, the output component you want to monitor from must be wired in the design.

[Inputs and Outputs](javascript:void(0))

### Input Pins

This component does not have any input pins available.

### Output Pins

#### Output

Audio signal pins are represented by a () circle, and traditional wiring is represented by a thin black line. You can use Signal Names on audio signal pins.

By default, the IO Monitor component only has one output pin available.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

#### Location

When you add a component to the Inventory, you can leave it in the "Default Location" or create a new location in the Properties of the component.

In the IO Monitor, the Location control is a drop-down list displaying all the Locations created in the design.

Select the Location of the equipment you want to monitor.

#### Device

After selecting the Location, all of the devices in the selected Location and associated with an output or input are listed in this drop-down list.

Select the device with the audio you want to monitor.

#### Channel

After selecting the Device, this list narrows the selection to the inputs and outputs available on the selected device. Select the Channel you want to monitor.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel | N / A | Name of the Channel associated with the device | N / A | Input / Output |
| Device | N / A | Name of the Device | N / A | Input / Output |
| Location | N / A | Location Name | N / A | Input / Output |
