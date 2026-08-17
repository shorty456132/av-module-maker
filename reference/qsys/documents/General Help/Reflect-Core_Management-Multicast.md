# Network > Multicast

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Multicast.htm

# Network > Multicast

Configure the IP address ranges used for multicast address assignment for the Q-SYS cameras, video endpoints, and AES67 transmitters in your design. Each device type is configured separately and supports both automatic and manual range assignment. You can also set the Time-to-Live (TTL) value for multicast camera and video endpoint streams.

**Note:** When you update the ranges for a system with existing streams, the currently assigned stream IP addresses are preserved to avoid disruption. New streams will use the revised range values.

## Auto Mode

To reduce the chance of multicast address overlap, 'Auto' mode seeds addresses in the following ranges using a combination of the device type and MAC address of the Core's primary LAN interface. For each Core, the third octet of the range receives the seeded value.

**Tip:** 'Auto' mode is suitable most installations. For very large systems that are planned to exceed the Maximum Multicast Streams Per Core value in the table, use 'Manual' mode and specify a custom address range.

| Device Type | Multicast Address Range | Maximum Multicast Streams Per Core | Notes |
| --- | --- | --- | --- |
| Cameras | 233.253.0.0 - 233.253.255.255 | 128 | Applies to PTZ camera multicast streams in your design. |
| Video Endpoints | 233.252.0.0 - 233.252.255.255 | 256 | Applies to NV Series multicast AV streams in your design. |
| AES67 Transmitters | 233.254.0.0 - 233.254.255.255 | 256 | Applies to both AES67 Transmitter component streams and System Link Transmitter component audio pin connections. |

## Manual Mode

This mode allows you to customize the multicast range for each device type. The range must:

* Be between 224.0.0.0 and 239.255.255.255
* Be valid, Class D multicast addresses
* Not conflict with those registered with the IANA, any Q-SYS network services, or multicast address ranges for other Q-SYS device types (Cameras, Video Endpoints, AES67).

**Note:** Transmitting AES67 audio to a Brooklyn II-based Dante device requires address assignment within the 239.69.xxx.xxx range.

## Multicast Time-to-Live (TTL)

For multicast Q-SYS Camera streams and Q-SYS Shiftâ¢ AV streams between Video Endpoints, network administrators can adjust the TTL value to set the maximum number of hops multicast traffic is allowed to traverse the network between origin and destination. This can be useful in cases where network traffic is heavy and it is necessary to prevent excessive hop counts. The TTL value is placed in the IP header of each packet. Once a packet has reached the TTL value, it is dropped. The default TTL value is 10, and can be set between 1 and 10.

**Note:** The TTL value is only applicable to Q-SYS Camera and Q-SYS Shift AV streams. It is not applicable to multicast audio from the AES67 Transmitter or audio from the System Link Transmitter, as the TTL value for those streams is hard-coded to 64.
