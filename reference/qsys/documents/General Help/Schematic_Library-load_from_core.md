# Loading and Saving Designs

> Source: https://help.qsys.com/Content/Schematic_Library/load_from_core.htm

# Loading and Saving Designs

It's easy to load a running design from a Q-SYS Core processor, make changes, and save the modified design back to the Core. If you have created a brand new design and saved it locally on your PC, you can then save it to the Core to automatically start running it for the first time.

**Tip:** Click the Sign In button (located in the top-right corner of the Q-SYS Designer interface) to sign in to Q-SYS Reflect. You can then load and save designs remotely for Cores that are registered with a Q-SYS Reflect Plus subscription and are part of Organizations and Sites of which you are a member.

[Load from Core & Connect](javascript:void(0))

Click File > Load from Core & Connect (or press F8) to display a list of all discovered Q-SYS Core processors and their associated Systems (design files). Select a Core to load its design file. Once a design is loaded, you can then adjust controls in real time, or disconnect from the Core (F7) to make edits to the design.

**Tip:** Use the Path, Organization, and Site drop-down menus to filter by those parameters. You can also use the Search box to filter by a search term.

[Discovery Paths](javascript:void(0))

Cores can be discovered from three possible paths:

|  |  |
| --- | --- |
| LAN / Local | These are Cores that are on the same network as that of the PC running Q-SYS Designer Software. |
| Hard Link | These are Cores that have a configured Hard Link in Q-SYS Designer > File > [Preferences](preferences.htm). |
| Reflect | These are Cores that are registered with Q-SYS Reflect. To load from these Cores, they must be registered with a Q-SYS Reflect Organization that has a Q-SYS Reflect Plus subscription and you must be able to access the Site to which these Cores are registered.  To see Reflect-registered Cores, click the Sign In button located in the top-right corner of the Q-SYS Designer interface.  **Note:** If a Core is registered with Reflect and you are on the same local network as that Core, it appears in the list twice â once for each path type. For better performance, load from the local path. |

[System Status](javascript:void(0))

Discovered Cores are listed with a status icon:

|  |  |
| --- | --- |
| Available | The Core is online. Select it, and then click Load From Selected Core. |
| Contacting | Q-SYS Designer is attempting to contact the Core on the network. |
| Idle / Warning | This event indicates compromised operation of the affected source and reduced functionality, such as a network redundancy (LAN B) communication problem. |
| Error | There is a problem connecting to this Core. Hover over the icon to see the details of the issue, which could be one of the following:   * The Core is not currently running a design. * You do not have access permission to load from this Core. * The Core is offline from Q-SYS Reflect or is not running firmware version 9.0 or later. * Designer cannot connect to the Core on the local network. * This Core has later firmware than your version of Designer. |

[Managing a Core](javascript:void(0))

Click  to launch [Core Manager](../Core_Manager/CoreManager_Overview.htm) (for LAN or Hard Link connected Cores) or [Q-SYS Reflect](../Reflect/reflect_overview.htm) (for Reflect connected Cores) in a browser window.

[Save to Core & Run](javascript:void(0))

Click File > Save to Core & Run (or press F5) to upload your design to the Core specified in your design and automatically start running it.

**CAUTION:** When you save and run a design, the existing design on the Core is overwritten and restarted with the new changes and control settings. If your Core is connected to live audio output, any control setting changes have an immediate impact on the output.

[Saving New Designs](javascript:void(0))

New designs, by default, are saved to the Core with a design name of "untitled." If this is a new design, you should first save it to your PC with a descriptive file name using File > Save or File > Save As. The name you select for saving locally becomes the name used on the Core.

[Saving over the LAN or via Q-SYS Reflect](javascript:void(0))

Q-SYS Designer automatically selects the most suitable network path for uploading your design to the Core.

#### Local or Hard Link

If your PC is connected to the same network as the Core or has a configured Hard Link in Q-SYS Designer > File > [Preferences](preferences.htm), Designer uses the local or hard link connection for saving your design and upgrading Core firmware.

#### Q-SYS Reflect

If you are signed in to Q-SYS Reflect, Designer attempts to use the Reflect connection for remotely saving your design and upgrading Core firmware. To save to a Reflect-registered Core, the Core must be registered with a Q-SYS Reflect Plus subscription and part of the Organizations and Sites of which you are a member.

To sign in to Q-SYS Reflect, click the Sign In button located in the top-right corner of the Q-SYS Designer interface.

[Disconnecting from the Core](javascript:void(0))

After saving and running your design, you can press F7 (or go to File > Disconnect) to disconnect from the Core. The design continues to run on the Core, but you can then make changes to the design file on your PC.
