# Hardware Compatibility: by Product Revisions

> Source: https://help.qsys.com/Content/Q-SYS_Compatibility/Hardware_Compatibility_Product.htm

# Hardware Compatibility: by Product Revisions

This page outlines the minimum versions, both mainline and Long-Term Support (LTS), that are compatible with these hardware product revisions. For an overview of hardware compatibility by Q-SYS Designer Software (QDS) version, see [Hardware Compatibility: by QDS Version](Hardware_Compatibility_QDS_Version.htm).

| Product | Description of Change | First Shipped S/N or Approximate Ship Date | Minimum Required QDS Mainline Version | Minimum Required QDS LTS Version[1](#If) |
| --- | --- | --- | --- | --- |
| TSC-50-G3 | Updated LCD display[2](#TSC-50-G) | Estimated March 2026 | v10.1.0 |  |
| TSC-70-G3  TSC-101-G3 | Updated NIC hardware sensor | Estimated late October 2025 | v10.0.2 |  |
| I/O USB Bridge | Intel LAN controller replaced due to EOL[3](#I/O) | S/N: 24TW2530000001 to 24TW2530000010, 24TW2548000001 or higher | v10.0.0 | v9.13.1 |
| Core 110f v2 | Peripheral mode support | N/A | v9.8 |  |
| Core 110f v2 | Removal of GPIO from Core 110f due to NXP shortage | v2 does not have any GPIO inputs | v9.6 | v9.4.3 |
| Core 8 Flex | Core 8 Flex i226 LAN controller rev support[4](#The) | Shipped after June 2024  S/N: 21TW2419400001 or higher,  21MX2420300117 or higher | v9.12 |  |
| Core 8 Flex | Peripheral mode support | N/A | v9.7 |  |
| Core 8 Flex | Core 8 Flex change from NXP to Renesas, S049 | Shipped after March 2023 | v9.7 |  |
| Core Nano | Core Nano i226 LAN controller rev support[4](#The) | Shipped after June 2024  S/N: 21TW2419400001 or higher,  21MX2420300117 or higher | v9.12 |  |
| Core Nano | Peripheral mode support | N/A | v9.7 |  |
| CX-Q (All) | Support new Ethernet PHY used on Processor board | S/N: 25CN2342500304 or 21MX2338100099 | v9.7 | v9.4.4 |
| CX-Q 2K4 | ADC and DAC changes | S/N: 25CN2321500101 or 21MX2240100025 | v9.4 | v9.4.3 |
| CX-Q 4K4 | ADC and DAC changes | S/N: 25CN2316500139 or 21MX2240100010 | v9.4 | v9.4.3 |
| CX-Q 4K8 | ADC and DAC changes | S/N: 25CN2323500068 or 21MX2307100129 | v9.4 | v9.4.3 |
| CX-Q 8K4 | ADC and DAC changes | S/N: 25CN2323500001 or 21MX2240100023 | v9.4 | v9.4.3 |
| CX-Q 8K8 | ADC and DAC changes | S/N: 25CN2316500114 or 21MX2307100214 | v9.4 | v9.4.3 |
| DCIO | DCIO hardware revision support | S/N: 12US2402134267 | v9.10 |  |
| DCIO-H | DCIO hardware revision support | S/N: 12US2350133864 | v9.10 |  |
| SPA-Q | Stand alone mode support | N/A | v9.8.1 |  |
| TSC-101-G3 | LAN controller change to i210 in May 2023 | S/N: 14TW2312G00299 | v9.7 | v9.4.5 |
| TSC-50-G3 | LAN controller change to i210 in May 2023 | S/N: 14TW2312C00228 | v9.7 | v9.4.5 |
| TSC-70-G3 | LAN controller change to i210 in May 2023 | S/N: 14TW2312F00118 | v9.7 | v9.4.5 |
| TSC-G2 | TSC-G2 models | Shipped after August 1, 2021 | v9.1.2 | v9.4.3 |
| TSC-G3 | AV Bridging support | N/A | v9.7 |  |

###### 1. If value is empty, the product is not designed to work in any 9.4.x LTS branch.

###### 2. TSC-50-G3 units with the new LCD cannot be downgraded below v10.1.

###### 3. I/O USB Bridges shipped after July 2025 cannot be downgraded below v10.0.

###### 4. The legacy motherboard's LAN port is black while the new motherboard's LAN port is blue. Once upgraded to v9.12 or higher, Core 8 Flex and Core Nano units with the i226-LM LAN controller cannot be downgraded below v9.12.
