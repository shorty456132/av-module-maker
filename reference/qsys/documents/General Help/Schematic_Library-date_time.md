# Date/Time

> Source: https://help.qsys.com/Content/Schematic_Library/date_time.htm

# Date/Time

Use the Date/Time component to insert a date/time text box into your design. This is especially useful for adding the local date and time to a user control interface (UCI).

[Configuration Overview](javascript:void(0))

1. Drag the Date/Time component into your schematic and double-click it to open the control panel.
2. Copy the Output text box into your UCI design.
3. Press F5 to save your design to the Core and run it. (Or, press F6 to emulate your design.)

4. In the Date/Time component's control panel, select a Format. You can select from a list of common date/time formats, or select Custom to specify your own using date/time specifiers. See [Controls](#Controls).

The Core's date/time is now shown in your UCI using the selected format.

[Inputs and Outputs](javascript:void(0))

### Inputs and Outputs

Control components do not have traditional input and output pins. If a Control Pin is available for the component, an input or output will appear.

Control Pins represent the controls available in the component's Control Panel. Control Pins are used to link controls between Schematic Elements, and link to / from [Control Scripts](control_script_2.htm "Click to view the Control Script topic."). Control Pin signal pins are represented by a  square, and the wiring is represented by a thick blue / white line.

[Properties](javascript:void(0))

**Tip:** For additional properties that are not listed, refer to the [Properties Panel](../Q-Sys_Designer/properties_panel.htm) help topic for more information.

### Date/Time Properties

There are no configurable properties for this component.

[Controls](javascript:void(0))

#### Format

Select from a list of common date/time formats, or select Custom to specify your own date/time Format String.

#### Format String

Shows the date/time format of a selected Format string. Select Format > Custom (or modify a preformatted string) to specify your own date/time format. See [Date/Time Specifiers](#Date/Tim).

#### Output

Displays the output of the selected date/time format within a text box.

[Date/Time Specifiers](javascript:void(0))

**Note:** Date and time formats may vary between the Core and Emulation Mode due to differences in the operating systems.

[Date Specifiers](javascript:void(0))

| Specifier | Definition | Run Mode | Emulate Mode |
| --- | --- | --- | --- |
| %A | Full day of the week | Thursday | Thursday |
| %a | Abbreviated day of the week | Thu | Thu |
| %B | Full month name | December | December |
| %b | Abbreviated month name (same as %h) | Dec | Dec |
| %C | Two-digit century number | 20 | 20 |
| %c | Locale's preferred date and time stamp | Thu Dec 19 13:08:40 2024 | Thu Dec 19 13:08:40 2024 |
| %D | Equivalent to "%m/%d/%y" | 12/19/24 | 12/19/24 |
| %d | Two-digit day of the month with leading zeros | 19 | 19 |
| %e | Day of month with space preceding single digits | 19 | 19 |
| %F | Equivalent to "%Y-%m-%d" | 2024-12-19 | 2024-12-19 |
| %G | Four-digit version of %g | 2024 | 2024 |
| %g | Two-digit year (ISO-8601:1988). See %V. | 24 | 24 |
| %h | Abbreviated month name (same as %b) | Dec | Dec |
| %j | Three-digit numeric day of the year with leading zeros | 354 | 354 |
| %m | Two-digit month | 12 | 12 |
| %U | Week number of the year (starting with the first Sunday as the first week) | 50 | 50 |
| %u | Numeric representation of the day of the week (ISO-8601), with Monday as '1' | 4 | 4 |
| %V | Week number of the given year, starting with the first week of the year with at least four weekdays, with Monday being the start of the week (ISO-8601:1988) | 51 | 51 |
| %W | Numeric representation of the week of the year, starting with the first Monday as the first week | 51 | 51 |
| %w | Numeric representation of the day of the week, with Sunday as '0' | 4 | 4 |
| %x | Locale's preferred date representation without time | 12/19/24 | 12/19/24 |
| %Y | Four-digit year | 2024 | 2024 |
| %y | Two-digit year | 24 | 24 |

[Time Specifiers](javascript:void(0))

| Specifier | Definition | Run Mode | Emulate Mode |
| --- | --- | --- | --- |
| %H | Two-digit hour in 24-hour format | 13 | 13 |
| %I | Two-digit hour in 12-hour format | 01 | 01 |
| %k | Hour in 24-hour format with space preceding single digits | 13 | Emulate mode is not updating as expected.[1](#1.Doesnt_Update) |
| %l (lower-case 'L') | Hour in 12-hour format, with space preceding single digits. | 1 | 1[2](#2.ExtraSpace) |
| %M | Two-digit minute | 13 | 23 |
| %P | Lower-case 'am' or 'pm' | pm | Emulate mode is not updating as expected.[1](#1.Doesnt_Update) |
| %p | Upper-case 'AM' or 'PM' | PM | PM |
| %R | Equivalent to "%H:%M" | 13:14 | 13:23 |
| %r | Equivalent to "%I:%M:%S %p" | 01:14:32 PM | 01:23:06 PM |
| %S | Two-digit second | 49 | 28 |
| %s | Unix Epoch Time timestamp | 1734574513 | Emulate mode is not updating as expected.[1](#1.Doesnt_Update) |
| %T | Equivalent to "%H:%M:%S" | 13:15:30 | 13:24:55 |
| %X | Locale's preferred time representation without date | 13:15:45 | 13:25:10 |
| %Z | Time zone abbreviation | AEDT | AUS Eastern Daylight Time[3](#3.WindowsFormat) |
| %z | Time zone offset | +1100 | +1100 |

###### 1. Doesn't update in Emulate.

###### 2. There is an extra space before the single digit on the Core, but this issue does not occur in Emulate.

###### 3. There is a discrepancy in time zones due to the Windows format.

[Other Specifiers](javascript:void(0))

| Specifier | Definition |
| --- | --- |
| %n | Newline character ("\n") |
| %t | Tab character ("\t") |
| %% | Percentage character |
