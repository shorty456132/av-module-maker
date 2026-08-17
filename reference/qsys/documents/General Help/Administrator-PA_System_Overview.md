# Q-SYS PA System Overview

> Source: https://help.qsys.com/Content/Administrator/PA_System_Overview.htm

# Q-SYS PA System Overview

The Q-SYS Public Address System is a set of elements that work together within a Q-SYS system to implement sophisticated paging and messaging. Some of the PA System features are shared, or interact with other general Q-SYS audio and control features, while others are specific to public address. The features are generic enough to yield flexibility, but specific enough to make system design and installation easy.

There are very few limitations. Any number of Priority Levels can be created. Every input to the PA Router can be simultaneously recorded if circumstances dictate. Each PA Zone output is independent, and can simultaneously issue different content consisting of a live page, delayed page, or a pre-recorded message. Currently, up to 128 page station inputs and 256 zone outputs are supported in a single system.

[Administrator](javascript:void(0))

The Q-SYS Administrator allows you to set up and maintain various Q-SYS resources for the PA System including:

* [PA Global Settings](PA_Global_Settings.htm)
* [Page Station Settings](Page_Stations.htm)
* [PA Zones](PA_Zones.htm)
* [PA Commands](Commands.htm)
* [Command Schedule](Command_Schedule.htm)
* [Users](Users.htm)

**Note:** Manage audio files for the PA system in the Q-SYS Core Manager > Audio Files page.

PA System security is established in a combination of the items listed above. Refer to the individual topics for details. You access the Administrator either through Q-SYS Designer, or as a stand-alone application.

[Hardware](javascript:void(0))

* PS-TSCG3 (does not have physical command buttons. Instead, it features a touchscreen interface that pairs with the TSC-70-G3 touchscreen)

* **PS-TSCG3-G**: desktop model with replaceable gooseneck microphone and an embedded push-to-talk button
* **PS-TSCG3-H**: wall-mount model with replaceable handheld microphone and an integrated push-to-talk button

The Q-SYS Page Station is a networked page station intended to connect to a Q-SYS system via Q-LAN. All audio deliveries to and from the Page Station use the Q-LAN network. In addition to audio and data deliveries via Q-LAN, the Page Station is designed to receive its power from the Q-LAN network via IEEE 802.3af compliant power sourcing equipment. This technology is better known as PoE (Power over Ethernet).

It also has one USB-C port designed to connect the TSC-70-G3 to the Page Station.

[Q-SYS Designer Elements](javascript:void(0))

In order for the Public Address functionality to be available in a design, you must have a Page Station; either the Page Station component, or the Virtual Page Station, and a PA Router in the design. Refer to the Q-SYS Designer online help for details on each of these.

**Note:** If you have a Core 1000, the Core must have at least 2 GB of RAM installed to compile a design containing a PA Router.

### Page Station Hardware Component

This is the representation, in Q-SYS Designer, of a physical Page Station connected to your Q-SYS System. You must add one Page Station component to the design's Inventory for each physical Page Station connected to the Q-LAN network. Once you have the Page Station components in your design, you must configure them in Q-SYS Designer. Configuration includes Name, Location, Model, Network Redundancy, Inputs and Outputs including GPIO, and others.

The control panel for the Page Station component includes Page Station Status, Analog and Digital Audio controls, Control I/O controls, and Network information, the outputs are Microphone audio and Station Control, both of which connect to the PA Router.

The input to the physical Page Station is typically a microphone (can be the Aux Mic/Line input).

### Virtual Page Station

The Virtual Page Station is designed to be used on a touchscreen, and provides individual Zone selections, Group Zone selections, and Snapshot Zone Selections. The Virtual Page Station can be automated by a script, or External Control. The Virtual Page Station component in Q-SYS Designer does not have an audio output pin, and does not have any parameters that relate to hardware. The Virtual Page Station's audio comes from an audio source connected directly to the PA Router.

### PA Router

The PA Router is the hub of the Q-SYS PA System. You must add one, and only one, PA Router to your design from the Schematic Library. If there is a Page Station in your design, and no PA Router, or if there is more than one PA Router, the design will not compile. The PA Router can accommodate up to 128 Page Stations, and 256 Zones.

[PA System Work Flow in the Administrator](javascript:void(0))

This work flow is not a complete procedure for establishing a PA System in Q-SYS. It is meant to describe the dependencies of one tab to another and show the simplest order based on the dependencies. The workflow assumes a Q-SYS design with the proper components for a paging system is in place and running on the Q-SYS Core. You can change any of the parameters at any time, but doing that may require changes in other components that were set previously.

1. Establish the **Global Settings**. The **Priority Mode** and **Priority Levels** have an impact on **Page Stations**, **Commands**, and **Users**.
2. In the **PA Zones** tab, create **Tags** and assign them to the PA Zones. (This step is not required.) The PA Zones are assigned to **Commands**. Using Tags simplifies assigning the PA Zones.
3. In the Q-SYS Core Manager > Audio Files page, you upload audio files for use in **Message Commands** and for preambles in **Page Commands**.
4. In the **Commands** tab, you can create **Tags** to group your Commands for easy assignment to **Users** and **Page Stations**. Optionally, Commands are used in the **Command Schedule** tab.
5. In the **Users** tab, you can create **Tags** to group the Users for easy assignment to **Page Stations**.
6. In the **Page Stations** tab, you make use of all the things you established in the preceding steps.
7. The **Command Schedule** tab allows you to schedule various Commands you created. It is not required.
