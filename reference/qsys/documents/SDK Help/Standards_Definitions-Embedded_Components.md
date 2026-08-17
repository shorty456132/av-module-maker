# Embedded Components

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Standards_Definitions/Embedded_Components.htm

# Embedded Components

Most Audio components and some Control components can be embedded in a Plugin via the [GetComponents(props)](Reserved_Functions.htm#GetCompo) reserved function. You can interact with these components via their controls and audio pins. Other types of pins are not supported, such as Control, USB, Mediacast, or Dataport pins.

**Note:**  Inventory components cannot be embedded in a plugin.

**Tip:** Go to [Storing Secrets in Plugins](../Code_Examples/Storing_Secrets_in_Plugins.htm) to see an example of storing Strings in an Embedded Component.

## Accessing Controls of an Embedded Component

### Finding Control Names

The best tool to obtain the correct control names for any component is the "Component Controls" pane in Q-SYS Designer Software (QDS).

To show this pane, select Tools > View Component Controls Info. You then select any component in your design.

### Accessing Embedded Components during Runtime

The name you assign to the component will be added to the global table for access of that component during the runtime. For example, if you defined a crossfader with the name of Xfade, you would use `Xfade["crossfade.to.B"].Boolean = true` to execute a crossfade.

If you create components using a loop, you can access them via the global table. For example:

```lua
 -- Part of GetComponents(props)  
 for x = 1, (props["Output Count"].Value) do  
  table.insert(  
    components,  
    {  
      Name = "XFader" .. x,  
      Type = "crossfader",  
      Properties = {  
        ["multi_channel_type"] = multiTypeIndex,  
        ["multi_channel_count"] = props["Count"].Value  
      }  
    }  
  )  
 end  
  
  
-- Part of runtime  
local XFaders = {}  
for i = 1, Properties["Output Count"].Value do  
  table.insert(XFaders, _G["XFader" .. i])  
end
```

**Tip:** Remember that Properties are configured in Design Time and are read-only during Runtime.

## Supported Components

### Audio Components

[Audio Players](javascript:void(0))

[Audio Player (audio\_file\_player)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/audio_file_player.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Track Count | n\_channels | integer | 2 | 1 to 128 | This affects the number of Audio Player Tracks counted against a design |
| Player Name | player\_name | string | no default value |  | This is for aesthetics in designer and not required in this case |
| Playlist Capable | b\_playlist | boolean | false |  |  |

[Bin Loop (binloop)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/binloop.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Output Count | n\_channels | integer | 1 | 0 to 128 | This affects the number of Audio Player Tracks counted against a design. |

[Loop Player (loop\_player)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/loop_player.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Time Source | io\_config | integer | 0 | 0 - GPS  1 - LTC  2 - None  3 - GPS External  4 - PTP |  |
| Frame Rate(fps) | frame\_rate | float | 29.97002997003 | 29.97002997003  30  25  24 | Only used when Time Source is set to LTC |
| Output Count | n\_channels | integer | 8 | 1 to 128 | This affects the number of Audio Player Tracks counted against a design |
| Buffer Adjustment | buffer\_adjustment | float | 1 | 0.1 to 1 |  |
| User UTC | utc\_offset\_rw | boolean | false |  | Only used when Time Source is set to PTP |

[Audio Recorder (audio\_file\_recorder2)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/audio_file_recorder2.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Track Count | n\_channels | integer | 2 | 1 to 4 | This affects the number of Audio Recorder Channels counted against a design |

[Cinema](javascript:void(0))

[Active Matrix Surround Decoder (active\_matrix\_surround\_decoder)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/active_matrix_surround_decoder.htm)

This component has no properties.

[MDA Player (mda\_player)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/mda_player.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| File Source | file\_source | integer | 1 | 0 - Local  1 - HTTP |  |
| Output Count | n\_channels | integer | 8 | 1 to 128 |  |

[Cinema Pink Noise Generator (pink\_cinema)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/pink_cinema.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Crossfader (crossfader)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/crossfader.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Crossover (crossover)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/crossover.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Max Slope | max\_slope | integer | 48 | 12, 24, 36, 48, 60, 72, 84, 96 | Measured in dB / Octave |
| Band Count | n\_bands | integer | 3 | 2 - 6 | Changing this property will change audio pin and control names.  2 - High, Low  3 - High, Mid, Low  4 - High, Mid-High, Mid, Low  5 - High, Mid-High, Mid, Low, Sub  6 - High, Mid-High, Mid, Low-Mid, Low, Sub |
| Highpass Low Band | highpass\_low\_band | boolean | false |  |  |
| Lowpass High Band | lowpass\_high\_band | boolean | false |  |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Delay (delay)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/delay.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Tap Count | n\_taps | integer | 1 | 1 - 512 |  |
| Max Delay (Seconds) | max\_delay | float | 0.5 | 0.001 - 60 |  |
| Delay Type | delay\_type | integer | 0 | 0 - Standard  1 - Fractional  2 - Crossfaded |  |
| Tap Gain | linear\_tap\_gain | integer | 0 | 0 - Standard  1 - Linear  2 - X-Fade -3dB  3 - X-Fade -6dB |  |
| Distance Controls | distance\_ctrls | boolean | false |  |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Dynamics](javascript:void(0))

[Automatic Gain Control (leveler)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/leveler.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Side Chain Input | b\_has\_sidechain | boolean | false |  |  |
| Detector Time | detector\_time | float | 0.005 | 0 - Use Control  0.005 - 5ms  0.01 - 10ms  0.02 - 20ms  0.05 - 50ms |  |
| Bypass Gain Meter | bypass\_mode | integer | 0 | 0 - Active  1 - Inactive |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Compressor (compressor)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/compressor.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Side Chain Input | b\_has\_sidechain | boolean | false |  |  |
| Detector Time | detector\_time | float | 0.005 | 0 - Use Control  0.005 - 5ms  0.01 - 10ms  0.02 - 20ms  0.05 - 50ms |  |
| Bypass Gain Meter | bypass\_mode | integer | 0 | 0 - Active  1 - Inactive |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Continuous Ambient Compensator (ambient\_compensator\_continuous\_2)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/ambient_compensator_continuous_2.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Audio Bandwidth | subsample\_factor | integer | 8 | 1 - 20kHz  2 - 10kHz  4 - 5kHz  8 - 2.5kHz  16 - 1.25kHz |  |
| Microphone Filter | microphone\_filter | boolean | true |  |  |
| Relative Venue Size | relative\_venue\_size | integer | 4 | 1 - 10 |  |
| Detector Time Constant | detector\_time | integer | 1 | 0 - Use Control  1 - 1s  10 - 10s  60 - 60s |  |

[Expander (expander)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/expander.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Side Chain Input | b\_has\_sidechain | boolean | false |  |  |
| Detector Time | detector\_time | float | 0.005 | 0 - Use Control  0.005 - 5ms  0.01 - 10ms  0.02 - 20ms  0.05 - 50ms |  |
| Bypass Gain Meter | bypass\_mode | integer | 0 | 0 - Active  1 - Inactive |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Gate (gate)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/gate.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Side Chain Input | b\_has\_sidechain | boolean | false |  |  |
| Detector Time | detector\_time | float | 0.005 | 0 - Use Control  0.005 - 5ms  0.01 - 10ms  0.02 - 20ms  0.05 - 50ms |  |
| Bypass Gain Meter | bypass\_mode | integer | 0 | 0 - Active  1 - Inactive |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Gated Ambient Compensator (ambient\_compensator\_gated\_2)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/ambient_compensator_gated_2.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Microphone Filter | microphone\_filter | boolean | true |  |  |

[Peak Limiter (limiter\_peak)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/limiter_peak.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Side Chain Input | b\_has\_sidechain | boolean | false |  |  |
| Detector Time | detector\_time | float | 0.005 | 0 - Use Control  0.005 - 5ms  0.01 - 10ms  0.02 - 20ms  0.05 - 50ms |  |
| Bypass Gain Meter | bypass\_mode | integer | 0 | 0 - Active  1 - Inactive |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Priority Ducker (priority\_ducker)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/priority_ducker.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Channels | n\_channels | integer | 8 | 1 - 512 |  |
| Detector Time | detector\_time | float | 0.005 | 0 - Use Control  0.005 - 5ms  0.01 - 10ms  0.02 - 20ms  0.05 - 50ms |  |
| Bypass Gain Meter | bypass\_mode | integer | 0 | 0 - Active  1 - Inactive |  |

[Effects](javascript:void(0))

[Auto-Pan Effect (effect\_autopan)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/effect_autopan.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| I/O Configuration | io\_config | integer | 0 | 0 - Mono In/Stereo Out  1 - Stereo In/Stereo Out |  |

[Chorus Effect (effect\_chorus)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/effect_chorus.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| I/O Configuration | io\_config | integer | 0 | 0 - Mono In/Mono Out  1 - Mono In/Stereo Out  2 - Stereo In/Stereo Out |  |
| Max Delay (Seconds) | max\_delay | 0.1 | .001 - 1 |  |  |

[Delay Effect (effect\_delay)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/effect_delay.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| I/O Configuration | io\_config | integer | 0 | 0 - Mono In/Mono Out  1 - Mono In/Stereo Out  2 - Stereo In/Stereo Out |  |
| Max Delay (Seconds) | max\_delay | 1 | .001 - 60 |  |  |

[Flanger Effect (effect\_flange)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/effect_flange.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| I/O Configuration | io\_config | integer | 0 | 0 - Mono In/Mono Out  1 - Mono In/Stereo Out  2 - Stereo In/Stereo Out |  |
| Max Delay (Seconds) | max\_delay | 0.1 | .001 - 1 |  |  |

[Pitch Shifter Effect (effect\_pitch)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/effect_pitch.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| I/O Configuration | io\_config | integer | 0 | 0 - Mono In/Mono Out  1 - Mono In/Stereo Out  2 - Stereo In/Stereo Out |  |
| Max Delay (ms) | max\_delay | 1 | 1 - 100 |  |  |

[Reverb Effect (effect\_reverb)](javascript:void(0))

[Component Help](https://help.qsys.com/q-sys_9.9/#Schematic_Library/effect_reverb.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| I/O Configuration | io\_config | integer | 0 | 0 - Mono In/Stereo Out  1 - Stereo In/Stereo Out |  |
| Reverb Type | reverb\_type | integer | 0 | 0 - Lush  1 - Dense |  |

[Tremolo Effect (effect\_tremolo)](javascript:void(0))

[Component Help](https://help.qsys.com/q-sys_9.9/#Schematic_Library/effect_tremolo.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| I/O Configuration | io\_config | integer | 0 | 0 - Mono In/Mono Out  1 - Mono In/Stereo Out  2 - Stereo In/Stereo Out |  |

[Equalizers and Filters](javascript:void(0))

[All-Pass Filter (filter\_allpass)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_allpass.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Filter Order | filter\_order | integer | 2 | 1 - First order  2 - Second Order |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Band-Pass Filter (filter\_bandpass)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_bandpass.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Band-Stop Filter (filter\_bandstop)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_bandstop.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Dual-Shelf Equalizer (equalizer\_shelving\_dual)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/equalizer_shelving_dual.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Filter Slope | filter\_slope | integer | 12 | 6 - 6dB/Octave  12 - 12dB/Octave |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[FIR Custom Filter (filter\_fir)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_FIR.htm)

**Note:** Coefficients can't be loaded in from a file while embedded but they can be loaded in via the JSON String control. See the above Component Help file for more information and an example.

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Coefficient Count | n\_taps | integer | 384 | 4 - 16384 | Ensure that the Coefficient Count equals the number of coefficients (FIR taps) in your FIR coefficients configuration |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[FIR High-Pass Filter (filter\_highpass\_fir)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_highpass_fir.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Transition Bandwidth | bandwidth | float | 1 | 1 - 1 Octave  0.5 - 1/2 Octave  0.25 - 1/4 Octave | Custom is not supported as an embedded component |
| Stopband Attenuation | attenuation | integer | 100 | 40, 60, 80, 100 | Custom is not supported as an embedded component |
| Phase Response | phase\_type | integer | 1 | 0 - Minimum Phase  1 - Linear Phase |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[FIR Low-Pass Filter (filter\_lowpass\_fir)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_lowpass_fir.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Transition Bandwidth | bandwidth | float | 1 | 1 - 1 Octave  0.5 - 1/2 Octave  0.25 - 1/4 Octave | Custom is not supported as an embedded component |
| Stopband Attenuation | attenuation | integer | 100 | 40, 60, 80, 100 | Custom is not supported as an embedded component |
| Phase Response | phase\_type | integer | 1 | 0 - Minimum Phase  1 - Linear Phase |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Flattop Graphic Equalizer (equalizer\_graphic\_flattop)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/equalizer_graphic_flattop.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Band Count | n\_bands | integer | 11 | 6, 11, 16, 31, 61 |  |
| Transition Bandwidth | transition\_bandwidth | float | 0.0833333333333333 | 0.0833333333333333, 0.166666666666667, 0.333333333333333, 0.5, 1 | Measured in fraction of an Octave  Example: 0.0833333333333333 = 1/12 Octave |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Flattop Parametric Equalizer (equalizer\_parametric\_flattop)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/equalizer_parametric_flattop.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Band Count | n\_bands | integer | 4 | 1 - 32 |  |
| Minimum Transition Bandwidth | minimum\_transition\_bandwidth | float | 0.0833333333333333 | 0.0833333333333333, 0.166666666666667, 0.333333333333333, 0.5, 1 | Measured in fraction of an Octave  Example: 0.0833333333333333 = 1/12 Octave |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Graphic Equalizer (equalizer\_graphic)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/equalizer_graphic.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Band Count | n\_bands | integer | 11 | 6, 11, 16, 31, 61 |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[High-Pass Filter (filter\_highpass)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_highpass.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Max Slope | max\_slope | integer | 24 | 12, 24, 36, 48, 60, 72, 84, 96 | Measured in dB / Octave |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[High-Shelf Equalizer (equalizer\_shelving\_high)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/equalizer_shelving_high.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Filter Slope | filter\_slope | integer | 12 | 6 - 6dB/Octave  12 - 12dB/Octave |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[IIR Custom Filter (filter\_IIR)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_IIR.htm)

**Note:** Coefficients can't be loaded in from a file while embedded but they can be loaded in via the JSON String control. See the above Component Help file for more information and an example.

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Section Count | n\_sections | integer | 1 | 1 - 256 | The quantity defined here should match the number of coefficients passed in |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Low-Pass Filter (filter\_lowpass)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_lowpass.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Max Slope | max\_slope | integer | 24 | 12, 24, 36, 48, 60, 72, 84, 96 | Measured in dB / Octave |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Low-Shelf Equalizer (equalizer\_shelving\_low)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/equalizer_shelving_low.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Filter Slope | filter\_slope | integer | 12 | 6 - 6dB/Octave  12 - 12dB/Octave |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Notch Feedback Controller (feedback\_canceler\_notch)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/feedback_canceler_notch.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Max Filter Count | max\_filter\_count | integer | 32 | 8 - 32 |  |

[Notch Filter (filter\_notch)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_notch.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Parametric Equalizer(equalizer\_parametric)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/equalizer_parametric.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Band Count | n\_bands | integer | 4 | 1 - 32 |  |
| Bandwidth or Q-Factor | bandwidth\_q\_factor | integer | 0 | 0 - Bandwidth  1 - Q-Factor  2 - Both |  |
| High Precision | high\_precision | boolean | false |  |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Weighting Filter (filter\_weighting)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/filter_weighting.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Weighting | type | integer | 1 | 1 - ANSI S1.42 A  2 - ANSI S1.42 C |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |
| Enabled | response\_panel\_enabled | boolean | true |  |  |
| Size | response\_panel\_size | integer | 1 | 1 - Small  2 - Medium  3 - Large | Only used when Enable is set to true |

[Gain (gain)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/gain.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Max Gain (dB) | max\_gain | integer | 20 | -100 - 20 |  |
| Min Gain (dB) | min\_gain | integer | -100 | -100 - 20 |  |
| Enable Ramp Controls | enable\_stepper | boolean | false |  |  |
| Mode | step\_mode | integer | 0 | 0 - Continuous  1 - Discrete | Only Used when Enable Ramp Controls is set to true |
| Number of Steps | num\_steps | integer | 8 | 3 - 100 | Only Used when Enable Ramp Controls is set to true and Mode is set to Discrete |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Gain Ramp (ramp)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/ramp.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Meters](javascript:void(0))

[Level Meter (meter2)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/meter2.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Meter Type | meter\_type | integer | 1 | 1 - True Peak/RMS  2 - Peak Program  3 - True Peak/RMS - dB-Linear |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[LKFS Meter (BETA) (meter\_LKFS)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/meter_LKFS.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Input Type | n\_channels | integer | 1 | 1 - Mono  2 - Stereo  3 - LCR  5 - 5.1 Surround  7 - 7.1 Surround |  |

[SPL/Leq meter (meter\_SPL)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/meter_SPL.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Meter Type | meter\_type | integer | 1 | 1 - SPL  2 - Leq |  |
| Frequency Weighting | type | integer | 2 | 1 - Linear  2 - ANSI S1.42 A  3 - ANSI S1.42 C |  |
| Level Range | level\_offset | integer | 20 | 0 - 0-100dB  10 - 10-110dB  20 - 20-120dB  40 - 40-140dB |  |

[Mixers](javascript:void(0))

[Delay Matrix Mixer (delay\_matrix)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/delay_matrix.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Input Count | n\_inputs | integer | 8 | 1 - 512 |  |
| Output Count | n\_outputs | integer | 8 | 1 - 512 |  |
| Max Delay (Seconds) | max\_delay | float | 0.5 | 0.001 - 60 |  |
| Delay type | delay\_type | integer | 0 | 0 - Standard  1 - Fractional  2 - Crossfaded |  |
| Gain Type | linear\_gain | integer | 0 | 0 - Standard  1 - Linear  2 - X-Fade -3dB  3 - X-Fade -6dB |  |
| Label Controls | label\_controls | boolean | false |  |  |
| Input Gain | input\_gain | boolean | false |  |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Gain-Sharing Automatic Mic Mixer (auto\_mixer)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/auto_mixer.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Channels | n\_channels | integer | 8 | 2 - 512 |  |
| Outputs | output\_choice | integer | 3 | 1 - Mix Only  2 - Channel Only  3 - Mix and Channel |  |
| Side-Cain Filter | sidechain\_filter | boolean | false |  |  |
| Detector Time | detector\_time | float | 0.005 | 0 - Use Control  0.005 - 5ms  0.01 - 10ms  0.02 - 20ms  0.05 - 50ms |  |

[Gating Automatic Mic Mixers](javascript:void(0))

[Gating Automatic Mic Mixer (Legacy) (auto\_mixer\_gated)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/auto_mixer_gated.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Channels | n\_channels | integer | 8 | 2 - 512 |  |
| Outputs | output\_choice | integer | 3 | 1 - Mix Only  2 - Channel Only  3 - Mix and Channel |  |
| Side-Cain Filter | sidechain\_filter | boolean | false |  |  |
| Show Advanced Controls | show\_advanced\_controls | boolean | false |  |  |

[Gating Automatic Mic Mixer (auto\_mixer\_gating\_adaptive)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/auto_mixer_gating_adaptive.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Channels | n\_channels | integer | 8 | 2 - 512 |  |
| Outputs | output\_choice | integer | 3 | 1 - Mix Only  2 - Channel Only  3 - Mix and Channel |  |
| Side-Cain Filter | sidechain\_filter | boolean | false |  |  |
| Show Advanced Controls | show\_advanced\_controls | boolean | false |  |  |

[Matrix Mixer (mixer)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/mixer.htm)

**Note:** Max size of the Mixer is 512x512 channels. See the Component Help for more details and limitations.

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Mono | n\_inputs | integer | 8 | 1 - 512\* | Number of total input channels between mono and stereo must be equal or less than 512 |
| Stereo | n\_stereo\_inputs | integer | 0 | 1 - 256\* | Number of total input channels between mono and stereo must be equal or less than 512 |
| Mono | n\_outputs | integer | 8 | 1 - 512\* | Number of total output channels between mono and stereo must be equal or less than 512 |
| Stereo | n\_stereo\_outputs | integer | 0 | 1 - 256\* | Number of total output channels between mono and stereo must be equal or less than 512 |
| Input Bank Size | input\_bank\_strategy | integer | 1 | 0 - Not Banked  1 - Automatic  2 - 1 Channel  3 - 16 Channel  4 - 32 Channel  5 - Custom |  |
|  | input\_bank\_custom | integer | 32 | 1 - 512 | Only used when Input bank Size is set to Custom |
| Output Bank Size | output\_bank\_strategy | integer | 1 | 0 - Not Banked  1 - Automatic  2 - 1 Channel  3 - 16 Channel  4 - 32 Channel  5 - Custom |  |
|  | output\_bank\_custom | integer | 32 | 1 - 512 | Only used when Output bank Size is set to Custom |
| Cue Bus Count | n\_cues | integer | 0 | 0 - 511\* | Each Cue counts as an output for counting against the max 512 output channels |
| VCA Groups | n\_vca\_groups | integer | 0 | 0 - 16 |  |
| 2-D Matrix Panner | matrix\_panner | boolean | false |  | Available only when there are no stereo inputs or outputs |
| Panner Normalization | spatializer\_normalization | integer | 0 | 0 - Constant Voltage  1 - Constant Power | Only used when 2-D Matrix Panner is set to true |
| Pan Controls | pan\_strategy | integer | 1 | 0 - No Pan Controls  1 - Pan Per Input  2 - Pan Per Crosspoint | Only can be used when at least one of the Input or Output channels is Stereo |
| Label Controls | label\_controls | boolean | true |  |  |
| Crosspoint Mute Controls | crosspoint\_mute | boolean | false |  | Only used when 2-D Matrix Panner is set to false |
| Crosspoint Solo Controls | crosspoint\_solo | boolean | false |  | Only used when 2-D Matrix Panner is set to false |
| Crosspoint Gain Type | crosspoint\_gain\_type | integer | 0 | 0 - Standard  1 - X-Fade -3dB  2 - X-Fade -6dB |  |

[Room Combiner (room\_combiner)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/room_combiner.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Rooms | n\_rooms | integer | 8 | 2 - 256 |  |
| Walls | n\_walls | integer | 8 | 1 - 256 |  |
| Channels | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo |  |
| BGM Inputs | n\_bgm | integer | 0 | 0 - 32 |  |

[Router (router\_with\_output)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/router_with_output.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Input Count | n\_inputs | integer | 8 | 1 - 1024 |  |
| Output Count | n\_outputs | integer | 8 | 1 - 1024 |  |
| Selection Controls | select\_strategy | integer | 2 | 0 - Knobs  1 - Combo Boxes  2 - Crosspoint Buttons |  |
| Selection Mode | output\_select | integer | 0 | 0 - Source  1 - Destination |  |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Signal Presence (signal\_presence)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/signal_presence.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[System Mute (system\_mute)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/system_mute.htm)

This component has no properties.

[Test and Measurement](javascript:void(0))

[IO Monitor (io\_monitor)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/io_monitor.htm)

This component has no properties.

[Pink Noise Generator (pink)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/pink.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Responsalyzer (responsalyzer)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/responsalyzer.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| RTA Bandwidth | n\_bands | integer | 121 | 11 - 1 Octave  31 - 1/3 Octave  61 - 1/6 Octave  121 - 1/12 Octave  241 - 1/24 Octave |  |
| FFT Size | n\_bins | integer | 16384 | 512, 1024, 2048, 4096, 8196, 16384, 32768, 65536 |  |
| Time Constant Controls | time\_constant\_controls\_name | boolean | false |  |  |

[RTA - Band-Pass (rta\_bandpass)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/rta_bandpass.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Bandwidth | n\_bands | integer | 31 | 11 - 1 Octave  31 - 1/3 Octave  61 - 1/6 Octave  121 - 1/12 Octave  241 - 1/24 Octave |  |

[Sine Generator (sine)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/sine.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[White Noise Generator (white)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/white.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | multi\_channel\_type | integer | 1 | 1 - Mono  2 - Stereo  3 - Multi-channel |  |
| Count | multi\_channel\_count | integer | 8 | 2 - 256 | Only used when Type is set to Multi-channel |

[Timecode](javascript:void(0))

[SMPTE LTC Generator (linear\_timecode\_encoder)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/linear_timecode_encoder.htm)

This component has no properties.

[SMPTE LTC Reader (linear\_timecode\_decoder)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/linear_timecode_decoder.htm)

This component has no properties.

### Control Components

[Astronomical Clock (sun)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/sun.htm)

This component has no properties.

[Blinking LED (blinker)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/blinker.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Assign component to | io\_assignment | integer | 0 | 0 - Core  1 - I/O Frame | I/O Frame is not supported as an Embedded Component |

[Color Picker (color\_picker)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/color_picker.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Color Picker Size | color\_picker\_size | integer | 256 | 160 - 512 | This is for aesthetics in designer and not required in this case |

[Contact List (contact\_list)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/contact_list.htm)

This component has no properties.

[Custom Controls (custom\_controls)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/custom_controls.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | type\_<1-10> | integer | 0 | 0 - None  1 - Level fader w/taper (dB )  2 - Level knob (dB)  3 - Frequency knob (Hz)  4 - Time Knob (seconds)  5 - Generic float knob  6 - Generic Integer knob  7 - Mute button  8 - Toggle button  9 - Trigger button  10 - Percent knob  11 - Position knob  12 - Pan knob  13 - Text edit  14 - Text display  15 - LED  16 - Meter  17 - Momentary button  18 - Distance knob (meters)  19 - Status Display  20 - Hexadecimal knob  21 - Time knob | For more information about each type see below |
| Count | count\_<1-10> | integer | 1 | 1-256 |  |
| Customize range | range\_custom\_<1-10> | boolean | false |  | See Table Below for Types that support Custom ranges |
| Minimum | range\_minimum\_<1-10> | integer | See Table Below | See Table Below | Only used when Customize range is set to true |
| Maximum | range\_maximum\_<1-10> | integer | See Table Below | See Table Below | Only used when Customize range is set to true |

| Type | Control Name | Default Range | Supports Custom Range | Custom Range | Notes |
| --- | --- | --- | --- | --- | --- |
| Level fader w/taper (dB ) | fader.1 | -100 - 20 | No |  |  |
| Level knob (dB) | level.1 | -100 - 20 | Yes | -100 - 100 |  |
| Frequency knob (Hz) | frequency.1 | 10 - 20000 | Yes | 0.1 - 20000 |  |
| Time Knob (seconds) | time.1 | 0 - 1 | Yes | 0 - 86400 | Can't use at same time as Time knob |
| Generic float knob | float.1 | 0 - 1 | Yes | -1000000000 - 1000000000 |  |
| Generic Integer knob | integer | 0 - 1 | Yes | -16777216 - 16777216 |  |
| Mute button | mute.1 |  | No |  |  |
| Toggle button | toggle.1 |  | No |  |  |
| Trigger button | trigger.1 |  | No |  |  |
| Percent knob | percent.1 | 0 - 100 | No |  |  |
| Position knob | position.1 | 0 - 1 | No |  |  |
| Pan knob | pan.1 | L100 - R100  -1 - 1 | No |  | Center Value is shown as C with a Value of 0 |
| Text edit | text.1 |  | No |  |  |
| Text display | text.display.1 |  | No |  |  |
| LED | led.1 |  | No |  |  |
| Meter | meter.1 | -120 - 20 | No |  |  |
| Momentary button | momentary.1 |  | No |  |  |
| Distance knob (meters) | distance.1 | 0 - 100 | Yes | 0 - 999 |  |
| Status Display | status.1 |  | No |  |  |
| Hexadecimal knob | hexadecimal.1 | 0 - 8  0x0 - 0xFF | Yes | 0 - 24  0x0 - 0xFFFFFF | Any bits below the minimum results in a high bit. for example a range of 3-8 results in 0x3 - 0xFF |
| Time knob | time.1 | 0 - 1 | Yes | 0 - 86399 | Can't use at same time as Time knob (seconds) |

[Date/Time (date\_time)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/date_time.htm)

This component has no properties.

[E-mailer (email)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/email.htm)

This component has no properties.

[Event Log (event\_log)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/event_log.htm)

This component has no properties.

[Event Logger (event\_logger)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/event_logger.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Arg Count | Args | integer | 1 | 0 - 16 |  |

[Flip-Flop (flip\_flop)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/flip_flop.htm)

This component has no properties.

[GPS Info (gps\_info)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/gps_info.htm)

This component has no properties.

[LFO (control\_lfo)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/control_lfo.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Type | lfo\_type | integer | 0 | 0 - Generic (Percentage)  1 - Level Modulator  2 - Frequency Modulator |  |

[PIN Pad (pinpad\_2)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/pinpad.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| PIN Count | n\_pins | integer | 1 | 0 - 16 |  |

[Press and Hold (press\_n\_hold)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/press_n_hold.htm)

This component has no properties.

[Selector (selector)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/selector.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Selection Count | num\_sel | integer | 4 | 2 - 64 |  |

[UCI Layer Controller (uci\_layer\_controller)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/uci_layer_controller.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| UCI | uci | string |  |  |  |
| Page | page | string |  |  |  |
| Is Shared | is\_shared | boolean | false |  |  |

[UCI Style Controller (uci\_style\_controller)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/uci_style_controller.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| UCI | uci | string |  |  |  |

[Value Stepper (stepper)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/stepper.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| Control Type | control\_type | integer | 2 | 0 - Gain  1 - percentage  3 - Integer |  |
| Mode | gain\_mode | integer | 0 | 0 - Continuous  1 - Discrete | Only used when Control Type is set to Gain |
| Number of Steps | num\_steps | integer | 8 | 3 - 100 | Only used when Control Type is set to Gain and Mode is set to Discrete, or when Control Type is set to Integer |
| Max Gain (dB) | max\_gain | integer | 20 | -100 - 20 | Only used when Control Type is set to Gain |
| Min Gain (dB) | min\_gain | integer | -100 | -100 - 20 | Only used when Control Type is set to Gain |

### Monitor Components

[Ping (ping)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/ping.htm)

This component has no properties.

[SNMP Query (snmp\_query)](javascript:void(0))

[Component Help](https://help.qsys.com/#Schematic_Library/snmp_query.htm)

Properties:

| QDS Name | Lua Name | Type | Default Value | Supported Range or values | Notes |
| --- | --- | --- | --- | --- | --- |
| OID Count | snmp\_num\_oid | integer | 1 | 1 - 16 |  |
| Version | snmp\_version | integer | 0 | 0 - v2c  1 - v3 |  |
