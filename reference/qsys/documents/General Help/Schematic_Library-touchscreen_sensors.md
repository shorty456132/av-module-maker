# Sensors

> Source: https://help.qsys.com/Content/Schematic_Library/touchscreen_sensors.htm

# Sensors

The Sensors component displays read-only information from a TSC Series Gen 3 touch screen controller's Ambient Light Sensor, Proximity Sensor (TSC-70-G3 and TSC-101-G3 only including the PS-TSCG3 Touchscreen Page Station), and Near Field Communications (NFC) Sensor. You can also configure a brightness threshold value to trigger the display to become brighter as ambient lighting conditions change, as well as configure a proximity threshold value to trigger the display to wake.

[Sensors Overview](javascript:void(0))

**Note:** To see the location of these sensors on the hardware, refer to the individual [Q-SYS Products](../Hardware/Hardware_Overview.htm#TSC_Series_Gen_3) hardware topics.

### Ambient Light Sensor

All TSC Series Gen 3 touch screen controller models include an Ambient Light Sensor. This sensor is always enabled and produces a numeric value proportional to ambient light intensity. Greater light intensity (higher brightness) produces larger number values.

To view the numeric value of the sensor:

1. Drag the Sensors component into the schematic workspace.
2. Save and run the design to the Core.
3. Double-click the Sensors component to view the Brightness value of the sensor. Adjusting room lighting or placing an object over the sensor will change the reported Brightness value.

**Tip:** You can configure a threshold Brightness value to automatically trigger the display to increase its brightness level. To enable this feature, see the [Auto Bright](#Auto) property.

### Proximity Sensor

The TSC-70-G3 and TSC-101-G3 touch screen controller models include a Proximity Sensor. This sensor is always enabled and produces a numeric value proportional to detection of nearby objects. Detection of objects closer to the sensor produces larger numeric values. Sensitivity is greatest for objects within 0.5 meters of the front of the display. To view the numeric value of the sensor:

1. Drag the Sensors component into the schematic workspace.
2. Save and run the design to the Core.
3. Double-click the Sensors component to view the Proximity value of the sensor. Objects within the sensorâs range affect the numeric value displayed.

**Tip:** You can configure a threshold Proximity value to automatically wake the display. To enable this feature, see the [Auto Wake](#Auto3) property.

### NFC Sensor

All TSC Series Gen 3 touch screen controller models include a wireless Near Field Communications (NFC) initiator/reader that is compliant with ISO and IEC standards and also supports custom protocols. The sensor is always enabled and can scan for, detect, and read passive targets that are within range of the sensor.

TSC Series Gen 3 touch screen controllers support Type 2 tags (T2T) that are compliant with ISO/IEC 14443A, including MiFare Classic and MiFare Ultralight tags having NTAG21x series ICs. Supported tags are commercially available in a variety of form factors and storage capacities. Q-SYS Designer Software components can be configured to display tag attributes and identification (UID) as well as the data content type or record type from non-encrypted tags.

To view attributes for a given target:

1. Drag the Sensors component into the schematic workspace.
2. Save and run the design to the Core.
3. Double-click the Sensors component to open the control panel.
4. Place a compatible T2T tag over the touch screen controller's NFC antenna until the NFC attributes are populated â typically within 1 to 3 seconds.
5. Click the Clear button to purge the attribute data. (A subsequent read event also purges the current attribute data.)

For more detailed information see the [NFC Details](#NFC) topic.

[NFC Details](javascript:void(0))

All TSC Series Gen 3 touch screen controller models include a wireless Near Field Communications (NFC) initiator/reader that is compliant with ISO and IEC standards and also supports custom protocols. The sensor is always enabled and can scan for, detect, and read passive targets that are within range of the sensor.

### NFC Antenna Location

The NFC antenna is located on the left side of the touch panel when it is oriented in landscape mode. NFC tags are best detected when they are placed in this region.

**Tip:** More precise NFC antennae location information can be found in the user manual for [TSC Series Gen 3](https://www.qsys.com/resource-files/productresources/dn/touchscreen_controller_peripherals/q_dn_qsys_tscg3_usermanual_en.pdf) panels.

### How NFC Works

The NFC antenna is located on the left side of the touch panel when it is oriented in landscape mode. NFC tags are best detected when they are placed in this region.

When a NFC reader initiates a tag, the reader and the tag must follow a specific sequence to ensure proper operation. The reader and tag need to establish two things:

* That a specific tag is selected
* What sort of tag is selected

### The NFC Tag Initiation Sequence

While working with NFC, there is a proximity coupling device (PCD) and a proximity inductive coupling card (PICC). The PCD emits a radio frequency (RF) signal that provides energy to the PICC. However, if more than one PICC is available within the required distance, all the PICCs respond, resulting in a collision.

The initiation sequence ensures that the PCD selects only one PICC and communicates with it, preventing the collision from causing problems. When the PCD begins the initiation process by powering the PICC, it does so using the following steps:

1. The PCD sends a Request (REQA) command to the PICC. The REQA is specially constructed â it only has seven bits, it canât be confused with any other command. The PCD continues to send the REQA command until it receives at least one tag response. The intervals between these requests vary by vendor. The REQA command works only on PICCs that the PCD has not read before, those that are not "disabled". To read disabled tags, the PCD instead issues a Wakeup (WUPA) command.
2. The PICC responds with an Answer to Request (ATQA) block. This block contains information such as a Unique Identifier (UID) prefix. It also tells the PCD whether the tag provides anti-collision support. If not, the tag is proprietary â it doesnât provide standard NFC support. The UID prefix is not the complete identifier; it contains only part of the UID.
3. When the tags provide anti-collision support, the PCD sends a SELECT command that includes the UID prefix. Multiple tags can have the same prefix. If they do, the PCD detects this condition and sends another SELECT command with more prefix bits. As the PCD adds prefix bits, the number of responding tags becomes fewer until only one tag responds â the select tag.
4. The final step in the anti-collision process occurs when the PCD sends out a SELECT command that includes the complete UID for the PICC.
5. The PICC responds by sending a Select Acknowledgment (SAK) command to the PCD. The PICC activates at this point.
6. The PCD must know how to interact with the PICC at this point. When bit 6 of the SAK contains a 1, the activated PICC supports the Mifare protocol. Otherwise, the PCD can assume that the PICC provides standardized ISO 14443-4 support.
7. The PICC continues to process all commands until it receives a HALT command from the PCD. At this point, the PICC becomes disabled.

### NFC Forum Tag Types

Below are the complete set of NFC tag types. Of these, Q-SYS TSC G3 devices provide support for **Type 2** tags.

| **TAG Types** | **Type 1** | **Type 2** | **Type 3** | **Type 4** | **Type 5 (RFID)** |
| --- | --- | --- | --- | --- | --- |
| **Operation Specification** | ISO/IEC 14443A | ISO14443A | JIS X 6319-4 | ISO/IEC 14443A-4 A/B with ISO/IEC 7816 Security | ISO/IEC 15693\* |
| **Compatible Products** | Broadcom  Innovision  Topaz 512 | NXP MIFARE Ultralight  NXP MIFARE Ultralight C  NXP NTAG 21s (F)  NXP NTAG I2C | Sony FeliCa  Lite-S | NXP DESFire  NXP SmartMX-JCOP (MIFARE DESFire Implementation)  STMicroelectronics | NXP ICODE SLI (x)  Texas Instruments Tag-it HF-I EM423x  STMicroelectronics ST25TV |
| **Memory Size** | 454 Bytes | 48/128/144/504/888/1904 Bytes | 1, 4, 9 KBytes | 2/4/8 KBytes/ up to 144 Kbytes/ 106 Kbytes | 32/112/128/160/256 Bytes |
| **Unit Price** | Low | Low | High | Medium/High | Low/Medium |
| **Data Access** | Read/Write | Read/Write or Read-only | Read/Write or Read-only | Read/Write or Read-only, and self-modification of NDEF content | Read/Write |
| **Applications** | One-time provisioning  Read-only applications  Business cards  Pairing devices with Bluetooth  Reading a specific tag when more than one tag is present | Low-value transactions  Day transit passes  RFID event tickets  URL redirects | Transit tickets  E-money  Electronic ID  Membership cards  E-tickets  Health care devices  Home electronics | Payment and security | Library books, products, and packaging  Ticketing (such as ski passes)  Healthcare (medication packaging) |
| **Operating Frequency** | 13.56 MHz | 13.56 MHz | 13.56 MHz | 13.56 MHz | 13.56 MHz |

\* ISO/IEC 15693 specification was originally developed to enable a longer RF operational range that up to 1.5 meters. NFC Forum chose to support Active Communication mode that allows data transfer performance similar to the RFID technologies supported by NFC Forum but limits the reading distance at NFC devices.

You will likely want to write to these cards with a specific payload. This can be done using a mobile phone with an app like NFC Tools:

[NFC Tools](https://apps.apple.com/us/app/nfc-tools/id1252962749) - Apps on Apple App Store

[NFC Tool](https://play.google.com/store/apps/details?id=com.wakdev.wdnfc&hl=en_US&gl=US&pli=1) - Apps on Google Play

### NFC Data Exchange Format (NDEF)

NDEF messages provide a standardized method for a reader to communicate with an NFC device. The NDEF message contains multiple records. NDEF support is only available when working with standardized NFC tags. The NFC standard supports five tag types, all of which support the same NDEF message format.

**Note:** Proprietary tags typically do not provide this support.

Each record contains a header and a payload. The header contains useful information for the reader, such as the record ID, its length, and type. The type defines the sort of payload that the record contains. The payload is simply data.

[Properties](javascript:void(0))

These properties are specific to the Sensors component for the TSC Series Gen 3 touch screen controllers.

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

#### Auto Bright

Select 'Yes' to expose the Auto Bright control in the Sensors component control panel, which allows you to configure a threshold brightness value that, when reached, automatically triggers an increase in the display's brightness level. Enabling and setting this control is especially useful when the display is placed in a room with changing lighting conditions, such as a room with exterior windows, skylights, etc. Auto Bright is disabled by default.

**Note:** Room reflections, the type and location of artificial lighting, and even UCI brightness and background color selection can impact the ambient light detected by the sensor. You might need to experiment with [Auto Bright](#Auto2) control value to achieve the desired result.

#### Auto Wake

Select 'Yes' to expose the Auto Wake control in the Sensors component control panel, which allows you to configure a threshold proximity value that, when reached, automatically wakes the display.

**Note:** Moving objects in a room not related to touch screen controller use can be detected by the sensor. You might need to experiment with the [Auto Wake](#Auto4) control to achieve the desired result.

[Controls](javascript:void(0))

#### Brightness

The current brightness level detected by the Ambient Light Sensor, from 0 to 2000. The higher the value, the brighter the lighting conditions.

#### Proximity

The current proximity value for the detected objects in front of the Proximity Sensor, from 0 to 2000. The higher the value, the closer the detected objects are to the sensor.

#### Auto Bright

When the [Auto Bright](#Auto) property is enabled, set the threshold brightness at which to trigger the screen to increase in brightness automatically, from 0 to 2000 (default is 500).

#### Auto Wake

When the [Auto Wake](#Auto3) property is enabled, set the threshold proximity at which to trigger the display to wake, from 0 to 2000 (default is 500).

#### NFC UID

This is the detected read-only unique identifier provided by the tag manufacturer.

#### NFC ATQA

This is the detected read-only Answer to Request value.

#### NFC SAK

This is the detected read-only Select Acknowledge value.

#### NFC Type

This is the detected read-only NFC tag type.

#### NFC Payload

This is the detected payload data from the tag.

#### Clear

This clears all NFC data.

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| NFC | | | | |
| ATQA | (text) | | | Output |
| Clear | (trigger) | | | Input / Output |
| Payload | (text) | | | Output |
| SAK | (text) | | | Output |
| Type | (text) | | | Output |
| UID | (text) | | | Output |
| Sensor | | | | |
| Auto Bright | 0 to 2000 | 0 to 2000 | 0 to 1.00 | Input / Output |
| Auto Wake | 0 to 2000 | 0 to 2000 | 0 to 1.00 | Input / Output |
| Brightness | 0 to 2000 | 0 to 2000 | 0 to 1.00 | Output |
| Proximity | 0 to 2000 | 0 to 2000 | 0 to 1.00 | Output |
