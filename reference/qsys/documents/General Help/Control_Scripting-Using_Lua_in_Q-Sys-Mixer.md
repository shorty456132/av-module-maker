# Mixer

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Mixer.htm

# Mixer

Mixer objects allow access to Mixer components that have been named in the design. To create a mixer object, call Mixer.New( mixerName ). The mixer object uses a string specification to determine which inputs and outputs to apply changes to. The syntax supports either space or comma separated numbers, ranges of numbers or all (\*). It supports negation of selection with the '!' operator.

| Input/Output String Specification Examples | |
| --- | --- |
| Name | Description |
| \* | Everything |
| 1 2 3 | channels 1, 2, 3 |
| 1-6 | channels 1 through 6 |
| 1-6 9 | channels 1 through 6 and 9 |
| 1-3 5-9 | channels 1 through 3 and 5 through 9 |
| 1-8 !3 | channels 1 through 8 except 3 |
| \* !3-5 | everything but channels 3 through 5 |

| Mixer Methods | | |
| --- | --- | --- |
| Name | Arguments | Description |
| [SetCrossPointGain](#Mixer) | ( ins, outs, gain, <ramp> ) | Sets specified cross point gains with optional ramp time. |
| [SetCrossPointMute](#Mixer) | ( ins, outs, mute ) | Sets specified cross point mutes with boolean |
| [SetCrossPointSolo](#Mixer) | ( ins, outs, mute ) | Sets specified cross point solos with boolean |
| [SetCrossPointDelay](#Mixer) | ( ins, outs, delay, <ramp> ) | Sets specified cross point delay with optional ramp time |
| [SetInputGain](#Mixer) | ( ins, gain, <ramp> ) | Sets specified input gain with optional ramp time |
| [SetInputMute](#Mixer) | ( ins, mute ) | Sets specified input mutes |
| [SetInputSolo](#Mixer) | ( ins, solo ) | Sets specified input solos |
| [SetOutputGain](#Mixer) | ( outs, gain, <ramp> ) | Sets specified output gain with optional ramp time |
| [SetOutputMute](#Mixer) | ( outs, mute ) | Sets specified output mutes |
| [SetInputCueEnable](#Mixer) | ( ins, cues, enable ) | Sets specified input cues enables |
| [SetInputCueAfl](#Mixer) | ( ins, afls, enable ) | Sets specified input AFL enables |
| [SetCueGain](#Mixer) | ( cues, gain, <ramp> ) | Sets specified cue gains with optional ramp time |
| [SetCueMute](#Mixer) | ( cues, mute ) | Sets specified cue mutes |
| [GetMixerCrossPoints](#Mixer) | ( ins, outs) | Gets specified cross point values |

## Example

```lua
mixer = Mixer.New("my mixer")  
   
-- set all crosspoint gains to -100 over 5 seconds  
mixer:SetCrossPointGain("*", "*", -100, 5 )  
   
-- mute inputs 3 - 6  
mixer:SetInputMute("3-6", true )  
-- set all output gains except 5 to 0dB  
mixer:SetOutputGain("* !5", 0 )  
   
-- print all mixer crosspoints  
xpoints = mixer:GetMixerCrossPoints("3", "*" )  
for k,v in pairs( xpoints ) do  
print( v.Input, v.Output, v.Gain, v.Mute, v.Delay, v.Solo )  
end
```
