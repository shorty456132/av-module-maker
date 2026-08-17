# HID Keyboard

> Source: https://help.qsys.com/Content/Schematic_Library/usb_keyboard.htm

# HID Keyboard

Use the HID Keyboard component to trigger keystrokes on a remote PC or Mac computer connected to a Q-SYS device that supports the HID Keyboard.

[Q-SYS Device Support](javascript:void(0))

HID Keyboard, HID Media, and HID Conferencing are inventory components included with these Q-SYS devices:

* [Core Nano](../Hardware/Processing/Core_Nano.htm)
* [Core 8 Flex](../Hardware/Processing/Core_8_Flex.htm)
* [Core 24f](../Hardware/Processing/Core_24f.htm)
* [Core 110f](../Hardware/Processing/Core_110f.htm) and [Core 110c](../Hardware/Processing/Core_110c.htm)
* [NV-21-HU Network Video Endpoint](../Hardware/Video/NV-21-HU.htm)
* [NV-32-H (Core Capable) Network Video Endpoint](../Hardware/Video/NV-32-H_Core_Capable.htm)
* [I/O-USB Bridge](../Hardware/IO_Expanders/IOUSB_Bridge.htm)
* [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm)
* [TSC-101-G3](../Hardware/Control_IO/TSC-101-G3.htm)

[Requirements](javascript:void(0))

* You need a USB A/B cable to connect a PC or Mac computer to the Q-SYS device.
* The HID Keyboard is designed to control a remote computer â connected to a Q-SYS device supporting the HID Keyboard â from another Q-LAN-connected device, such as a computer or touch screen controller. Do not use the component directly from the computer connected to the Q-SYS device, as unexpected behavior can occur.

[Configuration Overview](javascript:void(0))

1. Connect the USB A/B cable's rectangular 'A' connector to a USB port on a PC or Mac computer.
2. Connect the other end of the cable, the square 'B' connector, to the **USB B** port on the rear panel of the Q-SYS Core 110f processor.
3. On another PC connected to the Q-SYS network, drag the HID Keyboard component into your schematic from the Core 110f inventory tree.
4. Select the component. In Properties > HID Keyboard Properties, select a **Keyboard Layout** (PC or Mac).
5. Press F5 to save your design to the Core and run it.
6. Double-click the component to open the control panel. Use the keyboard to send keystrokes to the remote computer.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### HID Keyboard Properties

#### Keyboard Layout

Select a style for the HID keyboard: PC (default) or Mac.

**Note:** It is possible to control a Core-connected computer while using the opposite keyboard layout. However, some keys are interpreted differently. For example, if you are controlling a Mac computer while using the PC keyboard layout, pressing Print Screen, Scroll Lock, or Pause results in key presses for F13, F14, or F15, respectively.

[Controls](javascript:void(0))

The HID keyboard contains all the standard keys found on a PC or Mac keyboard. Num Lock, Caps Lock, and Scroll Lock LEDs indicate when these functions are enabled. The Connected LED indicates when the HID keyboard can communicate with the Core-connected computer.

### Key Combinations

To send a key combination command, select one or more special keys individually, and then press another key. A special key turns gray when it is active. Press the special key again to deselect it.

PC special keys are Ctrl, Alt, and Shift.

Mac special keys are Control, Option, Command (â), and Shift.

[Control Pins](javascript:void(0))

Only control pin categories are listed. The properties are the same for the individual pins within each category.

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Alpha Key | 0  1 | false  true | 0  1 | Input / Output |
| Arrow Key | 0  1 | false  true | 0  1 | Input / Output |
| Command Key | 0  1 | false  true | 0  1 | Input / Output |
| Cursor Key | 0  1 | false  true | 0  1 | Input / Output |
| Function Key | 0  1 | false  true | 0  1 | Input / Output |
| Keypad | 0  1 | false  true | 0  1 | Input / Output |
| LED | 0  1 | disabled  enabled | 0  1 | Output |
| Modifier Key | 0  1 | false  true | 0  1 | Input / Output |
| Number Key | 0  1 | false  true | 0  1 | Input / Output |
| Punct. Key | 0  1 | false  true | 0  1 | Input / Output |

[Scripting Example](javascript:void(0))

This example shows how you can use a scripting component (in this case, Text Controller) to send the key combination to lock the screen of a Core-connected Windows computer.

Three button controls are used. 'Home' (Windows key) and 'L' output control pins are wired to their corresponding input pins of the HID Keyboard component. A 'Lock\_Screen' button control, when pushed, locks the screen of the Core-connected computer.

### Lua Script

```lua
Controls.Lock_Screen.EventHandler = function( ctl )  
  if ctl.Boolean then  
    print( "Locking the screen..." )  
    Controls.Home.Value = true  
    Controls.L.Value = true  
  else  
    Controls.L.Value = false  
    Controls.Home.Value = false  
  end  
end
```

#### Debug Output

```lua
Locking the screen...
```
