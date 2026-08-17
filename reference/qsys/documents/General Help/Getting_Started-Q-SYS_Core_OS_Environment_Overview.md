# Q-SYS Core OS Environment Overview

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Getting_Started/Q-SYS_Core_OS_Environment_Overview.htm

# Q-SYS Core OS Environment Overview

To understand whatâs happening under the hood of the Q-SYS Core OS Platform, you first need to understand what comprises it.

## Applications

The Q-SYS Core OS Platform is a Linux-based application that runs on a Q-SYS Core processor. The Core OS Platform has two major sub applications: the Audio engine and the Runtime engine. The Audio engine manages the DSP processing, and the Runtime engine handles all the control changes and syncing between the Core OS Platform and the Q-SYS Core processor itself. In addition, any Lua scripting within the Core OS Platform is handled by the Runtime engine. Q-SYS Designer Software (QDS) is a Windows application that is the front-end DSP and programming tool for the Core OS Platform. You can also use QDS to emulate the Runtime engine of the Core OS Platform on your local machine.

If youâre familiar with using Q-SYS for its audio DSP capabilities, then you know the Audio Engine processes 3000 audio frames per second (fps) when sampling audio. Similarly, the Runtime engine processes changes in controls within the application at 30 fps. When you manipulate a control (press a button, fiddle a knob, etc.), the data of those changes are added to the next control frame, which, when processed, updates the control feedback back to the Core processor. Itâs important to keep this in mind when setting or exposing control values: the Runtime engine transfers control values to DSP coefficients every 33 ms so setting a control value faster than 30 times per second will not have any effect.

**Tip:** While these two engines run simultaneously and independently, all Lua scripts within the Core OS Platform (e.g., plugins, Block Controller, etc.) run on a single thread, meaning they all share the same resource. If one of your scripts is hitting the max number of executions allowed by the Runtime engine, itâs utilizing the entirety of the resource and prevents other scripts within the design from running.

## Lua in Q-SYS

Lua is a lightweight language that was created with the intention of it being embedded in or integrated with software written in C (and some other languages). As a benefit for all programmers, itâs also an extremely forgiving language and its simplicity makes it easy to learn.

The Core OS Platform uses Lua 5.3 and most of the standard libraries. Furthermore, there are specific Q-SYS extensions added to the Lua environment in the Core OS Platform to offer functionality that is common for installs. These are documented in [Q-SYS Help](https://q-syshelp.qsc.com/#Control_Scripting/Using_Lua_in_Q-Sys/01_Using_Lua_in_Q-Sys_Overview.htm). For basic scripting within Q-SYS Designer Software, Lua can be generated within a scripting component, either within an embedded IDE or using block-based visual programming and is managed by the Runtime engine. For plugins, once youâve generated the full file, you can add it to the QSC file directory within âMy Documents', which will then read on disk.

Now that we understand the mechanism of plugins within Q-SYS, we can break down plugins into smaller chunks. The two primary aspects of plugins are the Design Time (pre-compile) and the Runtime (the functional code while the Design is running). Once a plugin component is pulled into the schematic, its graphics and properties (Design Time) are processed by Q-SYS Designer Software's Design Time engine and any graphical or property changes require a redeploy to the Core. Any control values will be managed by the Runtime engine, just like any other Lua script.

For more information on the capabilities of plugins, see [Scripts vs. Plugins](Script_vs._Plugin_Determination.htm).
