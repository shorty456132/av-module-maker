# Control Aspects / Metadata

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Control_Aspects_Metadata.htm

# Control Aspects / Metadata

## Control Aspects

Controls use aspects to store attribute data related to the state of the control. Each control contains multiple aspects of data, however, it is not required to utilize every possible aspects. In general, as a feature of Q-SYS, many native controls simultaneously update multiple interrelated aspects to describe their state (e.g., a Mute button in the âonâ state will have a `.Boolean` attribute of True, a `.Value` attribute of 1, a `.String` attribute of âMutedâ, and a `.Position` attribute of 1). However, as a caveat, it is not required that every aspect be related or change simultaneously in an interdependent fashion, e.g., on a Status control it is possible to update the `.String` without causing an interrelated update of the `.Value`.

| Name | Type | Comment |
| --- | --- | --- |
| .Value | Float | Floating point value - no limit range. |
| .Values | Table of Float | Table of floating point values. Only available when a Control Script is connected to controls that create tables of values such as the 2D panner, RTA - Band-Pass, Responsalyzer, or another Control Script. |
| .Position | Float | Floating point between 0.0 and 1.0 of the ratio of the current control Value to the total range of the control (requires a range to be set on the control). |
| .Positions | Table of Float | Table of floating point positions. The same rules as .Values applies. |
| .String | String | Alphanumeric string |
| .Strings | Table of Strings | Table of strings. The same rules as .Values applies. |
| .Boolean | Boolean | True or False |
| .Index | Integer | Index of control â Only applicable when control is part of an array of controls. |
| .EventHandler |  | An internal mechanism (for a particular control) within a script that will call an indicated function in response to that controlâs change of attribute data. (e.g., a change of state.)  **Note:** State changes due to internal manipulation within the script will not be recognized as an event and will be disregarded by that EventHandler. |
| .RampTime | Integer | Amount of time the control will take to transition between values. Default is 0s.  **Note:** This aspect exists within the script calling for the change, not on the control itself. |

## Control Metadata

Metadata aspects manipulate the visual presentation of a control. Metadata aspects can specify the color, whether itâs disabled or invisible, or even the list of valid values for a control. Manipulation of Metadata aspects are available for controls originating from a Custom Control component, a scripting component (Block Controller / Text Controller), the UCI Toolbox, or a Plugin. Additionally, Metadata aspects are used in native components that utilize Combo Boxes/List Boxes.

| Name | Type | Comment |
| --- | --- | --- |
| .IsInvisible | Boolean | false = control visible, true = control hidden |
| .IsDisabled | Boolean | false = control enabled, true = control disabled |
| .IsIndeterminate | Boolean | false = no indeterminate styling is applied  true = indeterminate styling is applied  Native components will utilize .IsIndeterminate in the following cases:   * The control is inside a Q-SYS peripheral with which the core does not have communications. * The control is inside a Channel Group where multiple channels are selected, and the given control has a different value in each selected channel. |
| .Color | String | Colorâ¯metadataâ¯is in the form of a string. Q-SYS uses the built in .NET string->color converter which allows for strings in the form "#RGB", "#RRGGBB",â¯"#AARRGGBB" (for transparency support), [CSS Color Names](https://www.w3schools.com/colors/colors_names.asp), and HSV values using the format "!HHSSVV".  [Example](javascript:void(0)) This example shows a red button with varying transparency values (steps of approximately 10%):  ```lua Controls.Control_1.Color = "#00FF0000" Controls.Control_1.Color = "#19FF0000" Controls.Control_1.Color = "#32FF0000" Controls.Control_1.Color = "#4bFF0000" Controls.Control_1.Color = "#64FF0000" Controls.Control_1.Color = "#7dFF0000" Controls.Control_1.Color = "#96FF0000" Controls.Control_1.Color = "#AFFF0000" Controls.Control_1.Color = "#cbFF0000" Controls.Control_1.Color = "#e1FF0000" Controls.Control_1.Color = "#FAFF0000" ``` |
| .Choices | String Array ( table ) | Array of strings to be presented as the choices for Combo Box and List Box Controls |
| .Legend | String | Text legend displayed on button |
| .CssClass | String | String which represents the name of the CSS class you want to apply to the UCIâ¯element. By assigning a CSS class, you can control its appearance, such as colors, fonts, sizes, and other visual properties based on the styles defined in your CSSâ¯file. |
