# Peripheral Manager

> Source: https://help.qsys.com/Content/Peripheral_Manager/PeripheralManager_Overview.htm

# Peripheral Manager

Q-SYS Peripheral Manager contains a set of tools for managing Q-SYS peripherals, including I/O devices, network video endpoints, amplifiers, touch screen controllers, and page stations. Beginning with Q-SYS version 9.0, Peripheral Manager replaces many of the configuration and management functions formerly found in [Configurator](../Hardware/0017_Configurator.htm).

**Note:** Q-SYS PTZ cameras are still managed directly within [Configurator](../Hardware/0017_Configurator.htm). Q-SYS Core processors are managed with [Core Manager](../Core_Manager/CoreManager_Overview.htm).

## Accessing Q-SYS Peripheral Manager

Peripheral Manager is accessible from Q-SYS Configurator (within Q-SYS Designer Software) or from a browser.

[From Q-SYS Configurator](javascript:void(0))

1. Open Q-SYS Designer Software.
2. Go to Tools > Show Configurator.
3. In the left pane, select a peripheral from the list of discovered devices.
4. In the right pane, click the link for Peripheral Manager.

[From a Browser](javascript:void(0))

If you already know the peripheral's IP address, use a browser to navigate to Peripheral Manager using that address. If you do not know the IP address, you can obtain it from the peripheral's front panel (if present). Press the Next button until you see the IP address. If the peripheral does not have a front panel, open Peripheral Manager from Q-SYS Configurator.

## Q-SYS Peripheral Manager Pages

#### [Status](Status.htm)

View basic information about the Q-SYS peripheral, including its device name and firmware version.

#### [Network Settings](Network_Settings.htm)

View and configure how the Q-SYS Core connects to the network.

#### [Security](Security.htm)

Enable and configure security policies.

#### [802.1X](8021X.htm)

Enable or disable 802.1X for each LAN interface to comply with network security requirements.

#### [Certificates](Certificates.htm)

Install device certificates on the Q-SYS peripheral to meet organization security requirements and allow web browsers to trust connections to the peripheral.

#### [Utilities](Utilities.htm)

Download the Q-SYS log archive (if requested by Q-SYS Support), change the operation mode (NV-32-H Core Capable and I/O-510i only), and reboot peripheral.

#### [Device Password](Device_Password.htm)

Set, change, or clear the peripheral admin password.
