# Audio

> Source: https://help.qsys.com/Content/RoomSuite/Audio.htm

# Audio

Use the Audio section to fine-tune how the room sounds during calls and presentations through Optimization and Settings.

* Optimization â Runs Room System Optimization (RSO) to automatically measure the room and apply recommended settings (levels, EQ, AEC, etc.) for supported Q SYS microphones and loudspeakers.
* Settings â Allows you to manually adjust audio channels and processing if you need to fine tune the system beyond what Optimization provides, are using a third party or Dante ceiling microphone, or simply prefer full manual control.

**Tip:** A common workflow is to run RSO first to establish a solid baseline, and then make small, targeted adjustments in Settings to match the specific needs of your room.

## Optimization

### Room System Optimization (RSO)

Room System Optimization (RSO) is an automated, audio tuning engine built into Room Manager for the RoomSuite Modular System, which simplifies audio calibration through a guided, one-button optimization, and allowing manual tuning for final adjustments.

When you RSO, the system performs a sequence of actions designed to measure and optimize the roomâs acoustic environment.

You can use RSO in two ways: during setup, to quickly establish a repeatable baseline for a new room without relying on external tuning tools, and as a health check, to periodically verify that the room continues to meet performance standards and to troubleshoot audio issues caused by environmental changes or hardware shifts.

### Preparing for Room System Optimization

Before running RSO, ensure all AV endpoints installed, discovered, active and viewable in the Devices view. At minimum, the system should include one NM-T1 microphone and one NL-series loudspeaker. Additionally, be sure the room is quiet enough for RSO to take accurate measurements.

**Note:** RSO is supported only when using the NM-T1 microphone. RSO is not supported when using Dante microphones; audio tuning must be performed manually using the controls available in Audio > Settings. Additionally, you may choose to disconnect the Dante microphone from the system, run RSO, then reconnect the Dante microphone, and manually adjust the settings.

**Note:** During the RSO process, the system plays a series of loud test signals, including spoken word audio, through the room speakers. Volume levels will fluctuate throughout the test and may become loud at certain points. Ensure the room is unoccupied where possible and advise nearby users before starting optimization.

#### Running Room System Optimization (RSO)

1. **Open RoomSuite Modular System.**

   * In a browser, connect to the IP address of the RMP-100 processor.
   * If access control is enabled, log in with an account that has permission to modify audio settings.
2. **Confirm Devices**.

   * Verify that the Devices main content pane shows your active peripherals.
   * If the system indicates missing or unpaired devices, resolve those issues before continuing.

   **Note:** RSO cannot run while Dante microphones are connected to the system.
3. **Go to Optimization Page**.

   * Audio > Optimization.
4. **Start Optimization**.

   * Click Run Optimization.
   * RoomSuite Modular System begins the RSO process.

   **Note:** During optimization, the system will play loud test tones and noise through the speakers, which may be startling. The microphones capture these sounds to measure room acoustics. A spoken word-audio track also plays during the process to explain what is happening throughout the optimization.
5. Wait for completion and review results.

   The results include a downloadable summary along with pass / fail status for each test. Use the status messages and detail descriptions to determine whether any follow-up action is needed. For example, adjusting microphone placement, changing the room layout, or rerunning RSO after an issue has been resolved.
6. To make additional manual adjustments to the audio, go to Audio > Settings.

### Room System Optimization Results

After Room System Optimization is completed, the results help you understand how well the room and audio system are performing and whether any follow up action is needed.

Reports are divided into high level sections that summarize key aspects of the room and system, with an expandable Details panel available for additional information.

* Room Noise - Shows whether background noise levels in the room fall within recommended limits for conferencing.
* Room Reverb - Indicates how reflective the room is and whether sound decays at an acceptable rate.
* System Performance - Summarizes how well the audio system is operating, including signal levels, frequency response, and Acoustic Echo Cancellation (AEC)

Information in the Details viewâavailable as an expand / hide panelâcan be exported to a file. Depending on the section, the Details view may include:

* Pass / fail results for individual checks.
* Measured values compared to recommended targets, with green, yellow, or red indicators showing how the measured result falls within or outside the target range.
* Descriptions that explain why a result passed or failed.

You can also run RSO periodically as a room health check to verify that performance remains consistent over time. Re-running Optimization from Audioâ¯>â¯Optimization allows you to measure the room again and compare the results to previous runs, helping you identify gradual degradation or unexpected changesâsuch as a failed speaker, increased background noise from HVAC systems, or a microphone that has been moved out of position.

## Settings

The Settings page provides a channel strip style mixer interface for all key audio paths in the room.

### Snapshots

#### Save: User

Saves the current audio settings and all visible channels to the User snapshot.

#### Load

Optimized - Loads the RSO settings. Use this to restore the latest RSO tuned configuration.

User - Loads your previously saved custom settings.

Default - Loads factory default audio settings for the room.

#### Channels

#### Inputs

The following input channel strips are always present: Soundcard, Speakerphone, and HDMI. Additional input channels appear based on which audio sources are connected or enabled.

#### Outputs

Output channels depend on what audio destinations exist in the system, including:

* In-room loudspeakers (soundbar, ceiling, or pendant).
* Dante output paths to feed AEC reference input on connected ceiling array microphones.
* Primary mix output to feed loudspeakers, external devices, and AEC reference paths.

As hardware is added, removed, or reconfigured, the Outputs tab automatically updates to reflect the available audio paths; however, the Dante Out and Mix are always displayed.

### Channel Strips

#### Channel Name and Status

The channel name describes the input-source or the output-destination, while the status text shows device presence and connectivity.

#### Processing Buttons

Each processing button opens a detailed view for fine-tuning how the audio signal is processed.

#### HPF

High Pass Filter; removes low-frequency content form an audio signal below a selected cutoff frequency.

Controls:

* Frequency - Sets the cutoff frequency for example, 80â¯Hz. Audio below this point is attenuated.
* Bypass - Temporarily disables the HPF without losing your settings.

#### PEQ

Parametric EQ; allows precise adjustment of specific frequency ranges to shape the tonal quality of the audio.

Controls:

* Frequency - The center frequency being adjusted.
* Gain - Boosts or cuts the selected frequency range.
* Bandwidth (Q) - Controls how wide or narrow the affected range is.
* Type - Filter shape. For example, parametric, high shelf, or low shelf.
* Bypass (per band or global) - Disables EQ without clearing settings.

#### AEC

Acoustic Echo Cancellation; prevents far end participants from hearing their own voices echoed back from the room speakers.

Controls:

* AEC On / Off (Bypass) - Enables or disables echo cancellation processing.
* Echo Return Loss Enhancement (ERLE) / Reference Levels - Indicates how effectively echo is being removed.
* Noise Reduction - Reduces background noise picked up by microphones.
* Residual Echo Suppression - Further suppresses remaining echo artifacts after cancellation.

#### GATE

Noise gate; reduces or mutes signals that fall below a specified level.

Controls:

* Threshold - The level below which audio will be reduced or muted.
* Depth - How much the signal is reduced when the gate is closed.
* Status - Indicates whether the gate is currently open or closed.
* Bypass - Turns the gate off without removing settings.

#### COMP

Compressor; reduces the dynamic range of a signal by lowering the level of louder sounds, making overall audio more consistent.

Controls:

* Threshold - Level above which compression starts.
* Ratio - Determines how strongly loud sounds are reduced.
* Depth / Makeup Gain - Controls how much compression is applied and how the signal is balanced afterward.
* Status - Indicates Active or Inactive. When Active, the input signal has exceeded the threshold, and compression is currently being applied. When Inactive, the input signal is below the threshold, so no compression is being applied, and the signal is passing through unchanged.
* Output level - Final level after compression.
* Bypass - Disables compression without losing settings.

**Tip:** A typical workflow is to start with Optimization, then use HPF, PEQ, GATE, and COMP sparingly to address specific room or microphone behaviors rather than making large corrective changes.

#### Trim Fader and Meter

A vertical meter displays the signal level for the channel, while a Trim fader next to the meter allows you to adjust the input or output gain in dB. A numeric readout at the bottom of the strip (for example, â53.2â¯dB or 0â¯dB) shows the current trim setting.

#### Mute

The mute button at the bottom of each strip toggles the channel on or off; when muted, audio from that channel is not heard or routed further through the system.

#### Config Button - Dante In Channel

Opens the Dante In - Connection Config window which allows you to route the Dante ceiling microphone to the systemâs Dante In channel, configure its connection, and confirm that the audio and control are configured correctly.

#### Config Button - NM-T1 Channel (Beam Wizard)

Opens the Table Mic â Beams Config window which allows you to view real time level meters for each microphone beam, enable or disable individual beams to match the room layout and seating positions, and adjust per beam gain to balance pickup across participants.

## Auto-Mixer for NM-T1 Tabletop Beaming Microphone

The NM-T1 Auto-Mixer is a built-in gating mixer that automatically keeps your room quiet and intelligible by opening only the microphone beams with active talkers while keeping idle beams closed. Each NM-T1 provides four independent beams, and when AutoMix is ON, the system intelligently prioritizes real speech and limits the number of open beams, so background noise doesnât flood the mix and far end participants hear a clear, focused signal. When AutoMix is OFF, the AutoMixer is bypassed, and you can manually adjust per beam gain for advanced or nonstandard setups.

**Note:** If a Dante ceiling microphone is connected, the NM-T1 auto-mixer does not operate.

#### Using Auto-Mixer

1. **Open the NM-T1 input channel.**

   From Audio > Settings > Inputs, locate your NM-T1 input channel.
2. **Check you basic mic level first.**

   Confirm that the NM-T1 level is set reasonably :

   * Watch the NM-T1 meter while someone speaks from a normal position.
   * Adjust the Trim fader so speech lands safely below clipping.
3. **Toggle Auto-Mixer ON (recommended).**

   For most rooms, youâll want the Auto Mixer on, so it can automatically manage who is âon micâ at any moment.
4. **Listen to multiple talkers.**

   Have two or more people speak from typical seating positions. With Auto Mix ON, you should hear:

   * The active talker clearly.
   * Other mics / positions step back in level when they are not speaking, reducing room noise and echo. If the overall level feels too loud or too soft, adjust the Trim fader rather than turning Auto Mix off.
5. **Decide if you ever need Auto-Mix OFF.**

   Most rooms should leave Auto Mix ON all the time. You might temporarily turn it OFF (enable bypass) if:

   * You are doing troubleshooting and want to hear the raw mic behavior.
   * You have a special use case where all beams must act like a single, always open microphone.
6. **Save your preferred state.**

   Save your settings using Audio > Settings > Snapshots.

   * Use Load â Optimized if you want to revert to the system tuned default after optimization.
   * Use Save â User to store your own preferred Auto Mix state and levels.

## Beam Wizard for the NM-T1 Tabletop Beamforming Microphone

The Beam Wizard gives you a simple, visual way to tell the NM-T1 where to âlistenâ in the room. Instead of adjusting individual beam IDs or gains, the Beam Wizard presents the microphone and its four beams as an in-room graphic that you can align to real talker locations. From there, you can turn specific beams on or off and orient them toward the actual seating zones, while the system handles the detailed beam parameters behind the scenes. Proper beam alignment improves speech clarity and supports optimal downstream processing, including echo cancellation and Auto-Mixer performance. After applying beam coverage, you can make small PEQ refinements if needed, and if the room layout changes later, simply rerun the Beam Wizardâwhether during initial installation, after a seating or table layout change, following a mic reposition or noticeable pickup issue, or as part of periodic room checks.

#### Using Beam Wizard

1. **Open Beam Wizard.**

   From Audio > Settings, open the NM-T1 microphone section and select Beam Wizard. A simple room graphic appears, showing the NM-T1 and its four microphone beams.
2. **Position microphones.**

   Place and rotate microphones so that the beams directly face where people in the room will be standing or sitting.
3. **Configure microphones.**

   Use the mute buttons on each microphone to toggle the unconfigured state on or off. If the beams face each other or are aimed in undesirable directions, use the mute button to toggle off.
4. **Confirm the Configuration is complete**.

   Selecting Close confirms the configuration is complete, selecting Back allows you to go back to revise the configuration, or you may proceed to Room System Optimization.

## Configuring a Dante Ceiling Microphone

When a Dante ceiling microphone is part of the room, RoomSuite Modular System provides a Dante In â Connection Config window to help you route Dante audio into the system. Because Room System Optimization (RSO) is only supported for the NM-T1 tabletop microphone, the Dante ceiling microphone requires manual configuration using the tools in Audio > Settings.

**Note:** When a Dante ceiling microphone is connected, Room System Optimization (RSO) is automatically disabled, because RSO supports the NM-T1 tabletop microphone only. In this configuration, the Dante microphone and any NM-T1 microphones must be tuned manually using the tools available in Audio > Settings.

If you want to run RSO for the NM-T1 microphones, temporarily disconnect the Dante microphone, run RSO, and then reconnect the Dante microphone. After reconnecting, the Dante input will require manual adjustment, while the NM-T1 will use the optimized settings provided by RSO.

#### Pairing a Dante Ceiling Microphone

1. From the RoomSuite Modular System, select the Devices page.
2. Connect the Dante microphone to RMP-100 Ports 2-8 or QIO-VEN4 Ports 1-4 on the RMS A/V LAN.

   * RoomSuite Modular System automatically discovers the Dante microphone. A labeled icon representing the Dante microphone will be visible on the Devices page.

#### Using the Dante In-Connection Config

Before configuring Dante audio, keep the following in mind:

* Use the microphone manufacturerâs software for any advanced microphone configuration beyond basic routing.
* To access Dante Controller or the microphoneâs own software tools, your computer must be connected to the RMP‑100 A/V LAN. These tools are not accessible from the RMP‑100 AUX A or AUX B networks.
* Dante Controller is required to route the RMP‑100 transmit channel into the microphoneâs AEC Reference input (when supported by the microphone).
* The audio route from the microphone to the RMP‑100 (the input / receive channel) cannot be changed in Dante Controller. You must configure this receive path using the RoomSuite Manager software. Dante Controller is only used for the return path back to the microphone.

1. **Open the Dante In - Connection Config window.**

   * From Audio > Settings > Inputs, locate the Dante In channel and click Config.
2. **Configure Audio Routing.**

   * From Device select the Dante ceiling microphone detected on the network.
   * From Channel (mono mix), choose the Dante audio channel the microphone transmitts.
   * Check the status of the indicator to confirm the device is present.
3. **Configure Control Settings.**

   RoomSuite attempts to automatically establish a control connection with the Dante microphone. If additional information is needed for discovery or control, complete the fields below:

   * **Mic Model** - Select the microphone model.
   * **Control IP** - Confirm the microphone's control IP. If this is not determined by RoomSuite Modular System automatically, enter it manually. You can find the microphone's IP address by clicking on the microphone's icon in the Devices page.
   * **Username / Password** - If the microphone requires authentication for control features, enter its credentials here. If not required, leave the fields blank. Use the presence indicator to confirm that the control connection has been successfully established.
