# Dynamic Pairing

> Source: https://help.qsys.com/Content/Core_Manager/System_Management/Dynamic_Pairing.htm

# Dynamic Pairing

Use the Dynamic Pairing page to pair a logical Q-SYS hardware component in your design with a matching hardware device on the network, either by the device's network name (hostname) or by the switch port to which the device is connected. This allows for easy swapping of Q-SYS hardware without having to update your design and redeploy it to the Q-SYS Core processor, preventing audio and control downtime.

**Note:** Dynamic pairing configuration is only available if the design running on the Q-SYS Core contains one or more devices whose Dynamically Paired property is set to 'Yes'. Not all hardware supports Dynamic Pairing.

## Requirements

* To configure Dynamic Pairing, one or more hardware components in your design must have the Dynamically Paired property set to 'Yes'.
  (If the hardware does not support Dynamic Pairing, this property does not exist.)
* The paired hardware device must be the same type of hardware and configuration as the logical hardware component in your design. For example, if you configure a logical I/O Frame component with four Line Out cards, you can only connect an I/O Frame with four Line Out cards to pair with the logical component.
* If a device is configured for device redundancy, it cannot be dynamically paired; however, devices using network redundancy are supported for dynamic pairing.
* After swapping devices, it can take approximately 10 seconds for the Q-SYS Core to recognize the swap.
* To use the Switch Port pairing method, the network switch must support the Link Layer Discovery Protocol (LLDP). Check with your local IT person if you have questions about LLDP and port labeling.

  **Note:** Daisy-chained QIO Series peripherals connected to a single switch port do not support the Switch Port pairing method.

## Pairing Methods

You can pair a logical Q-SYS hardware component in your design to a matching hardware device in one of two ways:

[Network Name](javascript:void(0))

The logical hardware component in your design is paired to a hardware component on the network with a hostname that matches the Network Name selected on the Dynamic Pairing page.

**Tip:** Select this method when you primarily care about the exact device name rather than where it connects to the network. For example, if you knew that your Q-SYS installation would eventually expand to need an additional Page Station, you could build the Page Station into your design now and use a Network Name dynamic pairing to integrate the Page Station in the future - without having to redeploy your design.

[Switch Port](javascript:void(0))

The logical hardware component in your design is paired to the hardware component on the network that is connected to the Switch Port selected on the Dynamic Pairing page. (The Switch Port is commonly the port's MAC address, but your switch may use different labeling.) Once you have selected a Switch Port for pairing, Q-SYS will always look for matching hardware plugged into that specific switch port to pair with the logical component in your design.

**Tip:** Select this method when you primarily care about where the device is being plugged in. For example, if you have multiple I/O-22 devices â each on a rolling cart serving a different purpose â any of them could be plugged into the LAN port in a conference room and Q-SYS will treat them the same, without having to redeploy your design.

**Note:** Daisy-chained QIO Series peripherals connected to a single switch port do not support the Switch Port pairing method.

## Configuring Dynamic Pairing

1. In your design:
   * Select a hardware component and set the Dynamically Paired property to 'Yes'.
   * Set the Is Required property to 'No' to avoid a Fault error (and instead report as 'Not Present') if the hardware device is not connected to the network.
2. Save and run your design on the Core.
3. In Q-SYS Core Manager, select Dynamic Pairing. All devices configured for Dynamic Pairing are listed.
4. Click Edit.
5. For the device you want to pair, select the pairing Method. See [Pairing Methods](#Pairing).
6. Select the Pairing:
   * For the Network Name method, select from a list of discovered hardware devices matching the logical hardware component type in your design.
   * For the Switch Port method, select from a list of switch ports that have connected hardware devices matching the logical hardware component type in your design.
7. Click Save.
