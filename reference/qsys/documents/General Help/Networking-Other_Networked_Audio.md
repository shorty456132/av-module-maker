# Other Networked Audio

> Source: https://help.qsys.com/Content/Networking/Other_Networked_Audio.htm

# Other Networked Audio

Read this topic to understand using Q-LAN with other networked audio protocols and applications.

[AES67](javascript:void(0))

If your Q-SYS network contains AES67 devices, observe these limitations:

* 3rd-party AES67 devices may not be able to support layer 3 multicast routed networks (for example, PIM-SM routed in the ASIC). This can cause issues for Q-SYS deployments in layer 3 multicast routed networks.
* Some 3rd-party AES67 devices require designation as the PTPv2 clock master. This can prevent other devices, such as Q-SYS devices, from working properly in layer 3 multicast routed networks.

[Audio Video Bridging (AVB)](javascript:void(0))

Q-LAN and AVB cannot co-exist on a single VLAN on a switch or across shared uplinks under any circumstances (in separate VLANs or not). Bandwidth reservation schemes required by AVB specifically request dynamic switch configurations that are contradictory and harmful to the PTP clock and RTP audio packet priority requirements of Q-LAN.

When using AVB (such as the [CAN32 â AVB Audio Video Bridge Card](../Hardware/IO_Expanders/CAN32.htm)) with an AVB-compliant switch, do not enable the IEEE 802.1AS / 802.1Qat / 802.1Qav features on the switch. These features effectively override normal QoS functionality on the switch.

[SIP Softphone Interface](javascript:void(0))

Use Q-SYS Softphone to connect to a digital phone system (IP-PBX, such as Cisco CUCM and FreeSwitch), as well as place ad-hoc IP-to-IP calls and connect to non-registered SIP-compatible equipment. Softphone supports out-of-band DTMF RTP Events (RFC2833), STUN, SIP trunking, Caller ID, Redial, Auto-Answer, and Do Not Disturb.

### Protocols and Ports

Softphone uses SIP/TLS for VoIP telephony control on UDP port 5060 and RTP/SRTP on ports 16384-32768 for audio transport. You can change the inbound (listening) SIP port in Q-SYS Core Manager and Q-SYS Reflect. (Outbound calls always use port 5060.)

### Configuration

* Use the Q-SYS Core Manager or Q-SYS Reflect > Softphones page to configure settings for all Softphones in your design (including the inbound SIP port and LAN interface for SIP traffic), as well as individual Softphone properties. Refer to the Core Manager > [Telephony > Softphones](../Core_Manager/System_Management/Softphones.htm) topic for guidance, including information about SIP trunk support.
* Use the Q-SYS Core Manager or Q-SYS Reflect > Network Settings page to enable DNS if the Core must resolve a SIP proxy address, such as when the Core must communicate with a cloud-based SIP server. (In that case, any public DNS address should be sufficient.) If the Core only needs to communicate with an in-network SIP proxy server, enabling DNS is not required. Refer to the Core Manager > [Network > Basic](../Core_Manager/Core_Management/Network_Settings.htm) topic for information on enabling DNS.

### Control

Add individual Softphones to your design from the Q-SYS Designer Inventory > Streaming I/O category. To learn about Softphone and its components and properties, see the [Status/Control (Softphone)](../Schematic_Library/Softphone.htm) topic.

[Analog Telephone Interface (POTS)](javascript:void(0))

Q-SYS supports connections to analog phone systems, either with Q-SYS hardware that includes POTS interfaces or with Softphone.

### Q-SYS Hardware

The following Q-SYS hardware can connect to analog phone systems. If you are connecting to a digital system, you can use an FXO gateway (Analog Telephone Adapter or ATA) that has an analog POTS connection and a network connection.

* The Q-SYS [Core 110f](../Hardware/Processing/Core_110f.htm) and [Core 110c](../Hardware/Processing/Core_110c.htm) include a single RJ-11 interface.
* The [CTEL4 â Analog Telephony Card](../Hardware/IO_Expanders/CTEL4.htm) provides four RJ-11 interfaces.

### Q-SYS Softphone

Use an FXO gateway to interface to a POTS system. Avoid multi-port models featuring an FXS port.

[Other Voice and Video Over IP Applications](javascript:void(0))

VoIP and video / VC systems are designed to tolerate network latencies between 50-150 milliseconds, while Q-LAN requires maximum network latencies measured in microseconds. As a result, Q-LAN PTP and audio must always be placed in a higher priority queue than voice, video, or video conferencing applications.
