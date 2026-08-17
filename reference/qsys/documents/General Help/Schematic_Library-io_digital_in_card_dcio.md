# Digital In â DCIO/DCIO-H

> Source: https://help.qsys.com/Content/Schematic_Library/io_digital_in_card_dcio.htm

# Digital In â DCIO/DCIO-H

The Digital Input on the DCIO supports 16 channels of AES3 audio and, with the DCIO-H, 8 channels of AES3 audio and 8 channels of HDMI audio.

The HDMI input extracts audio from incoming HDMI stream and passes the video stream directly to output HDMI port for connection to a downstream video device. Up to 8 channels of PCM audio are supported. Additionally, Dolby Digital Plusâ¢ and DTS-HDÂ® decoders are automatically applied if those bitstreams are detected.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

[Controls](javascript:void(0))

### HDMI (DCIO-H only)

#### HDMI Enable

Click to enable or disable HDMI functionality. When this is activated, the AES channels 9 through 16 are disabled and become HDMI channels.

**Note:** The HDMI Enable and AES 9-16 Enable are radio-type buttons. Both cannot be in the same position at the same time.

#### Audio Format

The format of the detected audio input.

#### Sample rate

The sample rate of the detected audio input.

#### Upmix

Select whether to upmix HDMI stereo audio content to synthesize a center channel, as well as side and rear surround channels. Options include None (default), 5.1, and 7.1:

|  | Upmix Control Selection | | |
| --- | --- | --- | --- |
| Format of Input Audio | None | 5.1 | 7.1 |
| Stereo[1](#LFE) | Stereo | 7.0 | 7.0 |
| Lt/Rt (Surround-encoded stereo)[1](#LFE) | 5.0 / 7.0 | 5.0 / 7.0 | 5.0 / 7.0 |
| 5.1 | 5.1 | 5.1 | 7.1 |
| 7.1 | 7.1 | 7.1 | 7.1 |

###### 1. LFE not supported.

#### LEDs

An LED is illuminated when there is a signal available on that channel: L (left), R (right), C (center), LFE (low frequency extension), Ls (left surround), Rs (right surround), Lb (left back), Rb (right back).

### AES (DCIO-H only)

#### AES 9-16 Enable

Click to enable or disable AES functionality for channels 9 through 16. When this is activated, the HDMI functionality is disabled.

**Note:** The HDMI Enable and AES 9-16 Enable are radio-type buttons. Both cannot be in the same position at the same time.

### Input (for DCIO-H) / AES (for DCIO)

#### Peak Input Level (dBFS)

Graphic display of the peak input level to the AES3 and / or the HDMI Input, measured in dBFS.

### Digital

#### Invert

Inverts the input signal.

#### Mute

Mutes the input signal.

#### Gain

Sets the gain of the input signal, from -100 to 20dB (default is 0).

### Status

Component status is conveyed with the Status LED and Status box, which uses both color and text to indicate the current condition:

* **OK**: The device is functioning normally.
* **Initializing**: The device is in the process of a firmware, patch, or configuration update, or the design is starting.
* **Compromised**: The device is functioning, but a non-fatal problem exists. Refer to the Status box for details.
* **Missing**: The device cannot be discovered.
* **Fault**: The device is malfunctioning or is not properly configured. Refer to the Status box for details.
* **Unknown**: This status appears during a Core reboot (for example, during a firmware update), or when a design is being uploaded to the Core and before it has started running.
* **Not Present**: If applicable to the device, this status appears when the device is not connected to the network and its Is Required component property is set to 'No'. This status also appears if the device component's Dynamically Paired property is set to 'Yes', pairing has not been assigned in Core Manager, and the device component's Is Required property is set to 'Yes'. See [Dynamic Pairing](../Core_Manager/System_Management/Dynamic_Pairing.htm).

[Control Pins](javascript:void(0))

| Pin Name | Value | String | Position | Pins Available |
| --- | --- | --- | --- | --- |
| Channel (1 through 16) | | | | |
| Gain | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Input / Output |
| Invert | 0  1 | normal  invert | 0  1 | Input / Output |
| Level (Peak Input Level (dBFS)) | -100 to 20 | -100 dB to 20 dB | 0.000 to 1.00 | Output |
| Mute | 0  1 | unmute  mute | 0  1 | Input / Output |
| AES Input 9-16 Enable | 0  1 | disable  enable | 0  1.00 | Input / Output |
| Channel Status C | 0  1 | false  true | 0  1.00 | Output |
| Channel Status L | 0  1 | false  true | 0  1.00 | Output |
| Channel Status Lb | 0  1 | false  true | 0  1.00 | Output |
| Channel Status LFE | 0  1 | false  true | 0  1.00 | Output |
| Channel Status Ls | 0  1 | false  true | 0  1.00 | Output |
| Channel Status R | 0  1 | false  true | 0  1.00 | Output |
| Channel Status Rb | 0  1 | false  true | 0  1.00 | Output |
| Channel Status Rs | 0  1 | false  true | 0  1.00 | Output |
| HDMI Audio Format | 0  1 | false  true | 0  1.00 | Output |
| HDMI Index | 0  1 | false  true | 0  1.00 | Output |
| HDMI Audio Samplerate | N / A | text-kHz | N / A | Output |
| HDMI Audio Upmix | - | None  5.1  7.1 | - | Input / Output |
| HDMI Input Enable | 0  1 | disable  enable | 0  1.00 | Input / Output |
| Status | N / A | Text | N / A | Output |
