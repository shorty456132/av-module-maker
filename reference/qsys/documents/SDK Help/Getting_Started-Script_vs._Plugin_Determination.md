# Script vs. Plugin Determination

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Getting_Started/Script_vs._Plugin_Determination.htm

# Scripts vs. Plugins

Short answer: they're similar but not the same. Read on to understand what makes plugins different from scripts.

## What is a plugin?

In the Q-SYS Core OS Platform, a plugin is essentially a custom component. Analogous to an app on your smart phone, the purpose of a plugin is to help extend or augment the inherent functionality offered by the Core OS Platform. Plugins are written using the lightweight, embeddable programming language of Lua (resulting in a file that has the .qplug extension), and then compiled into the C++ of the application layer of the Core OS Platform.

While many users can capture their needs by using one of our various scripting components, plugins offer several benefits over a simple script. First, version control and code collaboration between developers is much easier with plugins, which can save a lot of time and effort. Furthermore, plugins can offer more robust features: user interface and user experience control, scalability of controls, access to user configurable properties, internal wiring, and even reporting data into Core Manager or Enterprise Manager. Lastly, plugins can be a great way to make integration with various manufacturers easier.

## When should I use a plugin?

* **You consistently specify or install the same device**: Investing some time in the fabrication phase will not only make your tool set more modular and extendable, youâll reduce time spent on site during commissioning.
* **You want to standardize control practices**: Converting a script into a plugin offers a streamlined work flow with version control and standardization. This can ease the commissioning burden for systems. For more information about QSC's developer tools for version control, see [Plugin Compiler](../Development_Tools/Plugin_Compiler.htm).
* **You need a more robust user experience**: Plugins offer nuance with configurable properties and dynamic interfaces. This can ease the burden of system maintenance.
* **You want to provide consistent branding**: As the conferencing industry moves towards simpler, all-in-one solutions, plugins can offer an agile and consistent control implementation that maintains a centralized platform without sacrificing integration with third-party manufacturers.
* **Some other plugin benefits**:

  + You can download plugins from the Q-SYS Asset Manager and see update badges within Q-SYS Designer Software if a plugin has a newer version available.
  + QSC authored plugins can report their status directly to Core Manager and Enterprise Manager, allowing for robust remote monitoring of the system.
  + Multiple programmers can contribute work on plugins using source control tools. For more information on version control, visit [Atlassian's Git tutorials](https://www.atlassian.com/git/tutorials/what-is-version-control).

## What about User Components?

Letâs say you donât quite have time for a plugin, but you do want combine multiple components into a reusable interface. You can use the Core OS Platform mechanism of User Components to do this. While it might seem like a shortcut when compared to a plugin, itâs more accurate to think of them as different solutions to different problems.

For example, if you want to standardize an audio processing chain for your commissioning engineers, simply wiring together existing components and dragging some controls out for ease of use would be well suited to a User Component, since it can act more like a template or jumping off point for the engineer to customize for the system. Controlling third party devices â which require scripting â benefit more from a plugin, since users can manipulate and interact with the plugin without fundamentally changing the function of it.

**Tip:** Consideration of the end user or IT specialist that will eventually be maintaining the system can help determine the appropriate components for the best user experience.
