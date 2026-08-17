# Emulate Mode

> Source: https://help.qsys.com/Content/Q-SYS_Designer/003_Emulate_Mode.htm

# Emulate Mode

There are three modes of operation available in Q-SYS Designer: **Run**, **Design**, and **Emulate**.

* The **Run** mode is a full operation mode occurring on the Core. All components of the design are operational, controls can be adjusted, audio is passed.
* The**Design** mode is for designing your system. You can add and delete components, wire components one to another, arrange items in the Schematic or UCI, and so on. None of these operations can be accomplished in the **Run** or **Emulate** modes.
* The **Emulate** mode allows you to enter a run-type mode without being connected to a Core (or network).

**Note:** Even if you are connected to a network and have a Core available, using the Emulate mode does not connect Q-SYS Designer to the Core.

**Emulate** mode is used during the design phase of your system to:

* preset the controls of Schematic Elements to their **Run** mode positions. (If you make control settings in the **Emulate** mode and save them, either on your PC, or on the Core using **Save to Core & Run**, they become part of the design.)
* test control logic such as User Control Interfaces (UCI), control scripts, and so on.

[Emulating a Design](javascript:void(0))

To enter the **Emulate** mode, open a design in Q-SYS Designer and press the **F6** button, or select **File** > **Emulate** from the main menu.

In Emulate mode the Schematic Library, and Component Properties are not available. The Inventory, Schematic Pages, User Control Interfaces, Snapshots, and Named Controls accordion bars are available you can not add or delete items from those areas. In addition you cannot move any components in the Schematic.

Open any of the component's control panels to make adjustments to controls, test external controls, UCIs, and so on.

### Limitations

Since the design is open in Q-SYS Designer on your PC, and not connected to a Core, there is no DSP taking place - the DSP takes place on the Core. As a result, there is functionality that does not work in the **Emulate** mode.

#### General

During Emulation, there is no audio or information from physical hardware, being passed through the design. In general, the following items do not work in the **Emulate** mode. Some of these items may be populated with default information or values in the **Emulate** mode.

* **Meters** and text fields indicating level or gain.
* **Status** fields indicating audio flow, hardware status, temperature, clock information (Clock Offset), hardware control position (Atten. Pot. on amplifiers), basically, anything to do with the condition of physical hardware.
* LEDs indicating signal, or status from hardware.
* Response Graphs on the **Crossover**, **Responsalyzer**, **RTA - Band-Pass** components, **Dynamic** components, **Equalizers**, and **Filters**
* In **Control Scripts**, anything that requires audio signal or other information that is not available in **Emulate** mode, does not work.
* **Script**, **plugin**, or **command button** connected to a serial port on a Core or Q-SYS peripheral.

#### Specific Instances

There are some components that are unique in their operation in the **Emulate** mode.

* **Audio Player**
  + You can click the **Play**, **Stop**, **Pause** and **Loop** buttons, but they don't affect the state of their associated LEDs. The **Loop** button itself changes state, but not its LED.
  + You cannot load a file.
* **Crossfader**
  + You can click the **Xfade to** buttons but the **Gain** and **Position** fields do not change.
* **Gain Ramp**
  + You can click the **Ramp To** buttons, but the **Gain** reading does not change.
  + You can change the **Time** controls, but the **Rate dB/s** information does not change.
* **Listen** buttons in **Amplifier** and **Loudspeaker** components
  + In **Run** mode all the **Listen** buttons in the design are linked. When you click a **Listen** button in an **Amplifier** or **Loudspeaker** component, if another button is on it is turned off. In **Emulate** mode, the buttons are not linked.

[Errors](javascript:void(0))

Following are a few examples of errors that may occur when you attempt to **Emulate** a design.

You can have multiple Q-SYS designs open on a PC at one time, but you can only **Emulate** one design at a time. If you attempt to Emulate more than one design, Q-SYS displays the following error message.

If you attempt to Emulate a design that has invalid connections in the design, Q-SYS Designer displays an error message similar to the following.

The message shown above indicates that the design has a multi-port DataPort amplifier connected to either a Core and one or more I/O Frames, or two or more I/O Frames.
