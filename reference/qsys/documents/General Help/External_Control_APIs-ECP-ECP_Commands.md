# ECP Commands

> Source: https://help.qsys.com/Content/External_Control_APIs/ECP/ECP_Commands.htm

# ECP Commands

This topic describes the protocol for controlling a Q-SYS Core processor in Run Mode using TCP/IP on port 1702. Before proceeding, read the [External Control Protocol (ECP)](ECP_Overview.htm) and [Named Controls](../../Schematic_Library/external_control.htm) topics to learn about using ECP.

**Note:** An External Control client must communicate with the Q-SYS Core at least once every 60 seconds, or the socket connection will be closed by the Core. This is a form of "keep-alive" to make sure that abandoned connections get reclaimed by the Core. Most client programs poll a Change Group at a much higher rate which serves as a keep-alive. If not, the client program can issue a "Status Get" command periodically, or a "Control Set Value" on an unused control if no return response is desired. If communication stops, the Core will send out a `response close` or `rc`, command and then drop the connection.

[Basic Data Types and Encoding](javascript:void(0))

### Data Types

Messages in the protocol are ASCII, composed of the following basic types of data.

| Data Type | Definition |
| --- | --- |
| Beginning of message | There is no beginning of message indicator in the protocol. White space is discarded after the previous null character and the first non-whitespace character is assumed to be the beginning the next message. |
| End of message (EOM) | All commands and responses end with the End of Message (EOM) character.  The EOM character is <LF> (0x0A).  The Core waits until the EOM is received before parsing and executing the command.  The Core will ignore a <CR> (0x0D) character if it precedes the EOM. (This allows the use of telnet for debugging because telnet generates <CR><LF> when you press the Enter key.)  The Core terminates all responses with <CR><LF>. (This makes the responses readable when using telnet for debugging, but it also means the client must ignore the <CR> character.)  If a command contains extra arguments before the EOM, a "bad\_command" error will be returned.  cg text extra  -> bad\_command "expected EOM"  If a string argument contains the <LF> character, it must be encoded as "\n" (the character back slash followed by the character n)  If a string argument contains the <CR> character, it must be encoded as "\r" (the character back slash followed by the character r)  cg text  -> cv "text" "" 0 0  css text "multi\r\nline" <-- in the GUI this will show up as 2 lines  -> cv "text" "multi\r\nline" 0 0 |
| unsigned integer | Whole number between 0 and 4294967294 inclusive |
| floating point number | 32 -bit floating point number |
| string | Sequence of ASCII characters.  Since arguments are separated by spaces, strings containing spaces must be enclosed in double quotation marks. If the string contains a quotation mark, the quotation mark must be escaped (preceded) with a back slash. If the string contains a back slash, the back slash must be escaped with another back slash. If the string contains the line feed character (0x0A) it must be encoded as back slash n. If the string contains the carriage return character (0x0D), it must be encoded as back slash r. |

### Arguments

The following arguments are used in commands. All arguments are separated by spaces. In order to reduce network traffic, it is suggested that you use short numbers and names for the arguments.

| Argument Name | Data Type | Definition |
| --- | --- | --- |
| Command string | string | This is the short string that begins each message. It indicates what action is to take place. None contain spaces and they do not need to be enclosed in quotation marks. Command strings are case sensitive. |
| Response string | string | This the short string that begins a response to a command message. |
| CONTROL\_ID | string | Identifies a control as defined as a Named Control in Q-SYS Designer. See [Named Controls](../../Schematic_Library/external_control.htm). |
| CONTROL\_VALUE | floating point number | Represents the numerical value of a control. The range of this number depends on the particular control. |
| CONTROL\_POSITION | floating point number | Between 0.00 and 1.0 inclusive. Indicates where the value lies within the range of the control. Subject to a mapping. |
| CONTROL\_STRING | string | Contains the textual representation of a control's state such as "-2.3 dB" or "3.45 kHz" |
| COUNT | unsigned integer | Indicates the count of elements that follow. |
| CHANGE\_GROUP\_ID | unsigned integer | Identifies a Change Group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. Also, a client cannot open two sockets to the Core, create a Change Group on one socket and poll it on the other. You can create up to four Change Groups, and poll the groups at separate rates. |
| DESIGN\_ID | string | A unique ID given to a design every time it is compiled or emulated. |
| DESIGN\_NAME | string | The name of the design currently running on the Core. |
| IS\_ACTIVE | unsigned integer | Is a 1 if this is the active Core of a redundant pair or the design is not redundant, 0 if it is not active |
| IS\_PRIMARY | unsigned integer | Is a 1 if this is the primary Core of a redundant pair, or the design is not redundant, 0 otherwise |
| NAME | string | The user name assigned to an external control system. The name is assigned on the [Users (Administrator)](../../Administrator/Users.htm) page. |
| PIN | string | Size is unlimited.  The personal identification number assigned to a User along with the NAME. The User must have privileges enabled for external control. The PIN is assigned on the [Users (Administrator)](../../Administrator/Users.htm) page. |
| RAMP\_TIME\_SEC | floating point number | Used as an argument in Snapshot Load for the ramp time in seconds. |
| SNAPSHOT\_BANK | string | Identifies a bank of [Snapshots](../../Schematic_Library/snapshot_bank.htm). This is the name given to the bank when it was created in Q-SYS Designer. |
| SNAPSHOT\_NUMBER | unsigned integer | Identifies a snapshot within a snapshot bank. The range is 1 to the number of snapshots in the bank, inclusive. |
| POLL\_PERIOD\_MS | unsigned integer | Used as an argument in Change Group Schedule for the poll period in milliseconds. |

[Command Quick Reference](javascript:void(0))

| Command Title | Command String | Syntax | Response |
| --- | --- | --- | --- |
| [Change Group Add](#cmd_change_group_add) | cga | cga CHANGE\_GROUP\_ID CONTROL\_ID | none  bad\_change\_group\_handle  bad\_id |
| [Change Group Clear](#cmd_change_group_clear) | cgclr | cgclr CHANGE\_GROUP\_ID | none  bad\_change\_group\_handle |
| [Change Group Create](#cmd_change_group_create) | cgc | cgc CHANGE\_GROUP\_ID | none  bad\_change\_group\_handle |
| [Change Group Destroy](#cmd_change_group_destroy) | cgd | cgd CHANGE\_GROUP\_ID | none  bad\_change\_group\_handle |
| [Change Group Invalidate](#cmd_change_group_invalidate) | cgi | cgi CHANGE\_GROUP\_ID | none  The next Change Group Poll, returns all the controls, including their: values, positions, and so on. |
| [Change Group Poll](#cmd_change_group_poll) | cgp | cgp CHANGE\_GROUP\_ID | cv  cmvv  cgpa  bad\_change\_group\_handle |
| [Change Group Poll No ACK](#Cmd_Change_Group_Poll_No_ACK) | cgpna | cgpna CHANGE\_GROUP\_ID | cv  cmvv  bad\_change\_group\_handle |
| [Change Group Remove](#cmd_change_group_remove) | cgr | cgr CHANGE\_GROUP\_ID CONTROL\_ID | none  bad\_change\_group\_handle  bad\_id  After a control has been removed from a Change Group, it may still be returned from the next polling. |
| [Change Group Schedule](#cmd_change_group_schedule) | cgs | cgs CHANGE\_GROUP\_ID POLL\_PERIOD\_MS | none  bad\_change\_group\_handle  Based on the schedule, a `cgp` response will be sent. |
| [Change Group Schedule No ACK](#cmd_Change_Group_Schedule%C2%A0No_ACK) | cgsna | cgsna CHANGE\_GROUP\_ID POLL\_PERIOD\_MS | none  bad\_change\_group\_handle |
| [Control Get](#cmd_control_get) | cg | cg CONTROL\_ID | cv  cvv  bad\_id |
| [Control Get Metadata](#cmd_control_get_metadata) | cgm | cgm CONTROL\_ID | cmv  cmvv  bad\_id  zero or more |
| [Control Set Position](#cmd_control_set_position) | csp | csp CONTROL\_ID CONTROL\_POSITION | cv  bad\_id |
| [Control Set Position Ramp](#cmd_Control_Set_Position_Ramp) | cspr | cspr CONTROL\_ID CONTROL\_POSITION RAMP\_TIME | `nothing` or `bad_id` |
| [Control Set Position Vector](#cmd_control_set_position_vector) | cspv | cspv CONTROL\_ID NUM\_POSITIONS CONTROL\_POS1 CONTROL\_POS2 CONTROL\_POS3â¦CONTROL\_POSx | `nothing` or `bad_id` |
| [Control Set Position Vector Ramp](#cmd_Control_Set_Position_Vector_Ramp) | cspvr | cspv CONTROL\_ID NUM\_POSITIONS CONTROL\_POSITION1 CONTROL\_POS2.. CONTROL\_POSx RAMP\_TIME | `nothing` or `bad_id` |
| [Control Set String](#cmd_control_set_string) | css | css CONTROL\_ID CONTROL\_STRING | cv  bad\_id |
| [Control Set String Vector](#cmd_control_set_string_vector) | cssv | cssv CONTROL\_ID NUM\_STRINGS CONTROL\_STRING1 CONTROL\_STRING2 CONTROL\_STRING3â¦CONTROL\_STRINGx | `nothing` or `bad_id` |
| [Control Set Value](#cmd_control_set_value) | csv | csv CONTROL\_ID CONTROL\_VALUE | `cv` or `bad_id` |
| [Control Set Value Ramp](#cmd_Control_Set_Value_Ramp) | csvr | csvr CONTROL\_ID CONTROL\_VALUE RAMP\_TIME | `nothing` or `bad_id` |
| [Control Set Value Vector](#cmd_control_set_value_vector) | csvv | csvv CONTROL\_ID NUM\_VALUES CONTROL\_VALUE1 CONTROL\_VALUE2.. CONTROL\_VALUEx | `nothing` or `bad_id` |
| [Control Set Value Vector Ramp](#cmd_Control_Set_Value_Vector_Ramp) | csvvr | csvvr CONTROL\_ID CONTROL\_VALUE1 CONTROL\_VALUE2 CONTROL\_VALUE3â¦CONTROL\_VALUExRAMP\_TIME | `nothing` or `bad_id` |
| [Control Trigger](#Control_Trigger) | ct | ct CONTROL\_ID | `nothing` or `bad_id` |
| [Login](#cmd_login) | login | login NAME PIN | `login_succes`  `login_failed`  An attempt to access a Core that requires an external control system to login, receives a `login_required` response. |
| [Snapshot Load](#cmd_snapshot_load) | ssl | ssl SNAPSHOT\_BANK SNAPSHOT\_NUMBER FLOATING\_POINT\_NUMBER | none |
| [Snapshot Save](#cmd_snapshot_save) | sss | sss SNAPSHOT\_BANK SNAPSHOT\_NUMBER | none |
| [Status Get](#cmd_status_get) | sg | sg | sr |

[Response Quick Reference](javascript:void(0))

| Response Title | Response String | Syntax | Response To |
| --- | --- | --- | --- |
| [Change Group Poll Ack](#rsp_change_group_poll_ack) | cgpa | cgpa | cgp |
| [Control Metadata Value](#rsp_control_get_metadata) | cmv | cmv CONTROL\_ID metadata\_aspec CONTROL\_STRING CONTROL\_VALUE CONTROL\_POSITION | cgm |
| [Control Metadata Vector Value](#rsp_control_get_metadata_vector) | cmvv | cmvv CONTROL\_ID metadata\_aspec COUNT CONTROL\_STRING ... COUNT CONTROL\_VALUE ... COUNT CONTROL\_POSITION ... | cgm |
| [Control Read Only](#rsp_control_read_only) | core\_read\_only | cro <CONTROL\_ID> | csp  css  csv |
| [Control Value](#rsp_control_get) | cv | cv CONTROL\_ID CONTROL\_STRING CONTROL\_VALUE CONTROL\_POSITION | cgp  cg  csp  css |
| [Control Vector Value](#rsp_control_get_vector) | cvv | cvv CONTROL\_ID COUNT CONTROL\_STRING ... COUNT CONTROL\_VALUE ... COUNT CONTROL\_POSITION ... | cg |
| [Core Not Active](#resp_Core_Not_Active) | core\_not\_active | core\_not\_active | csp  css  csv  ssl  sss  ct |
| [Invalid Change Group Handle](#rsp_invalid_change_group_handle) | bad\_change\_group\_handle | bad\_change\_group\_handle CHANGE\_GROUP\_ID | cga  cgclr  cgc  cgd  cgp  cgr  cgs |
| [Invalid Command](#rsp_invalid_command) | bad\_command | bad\_command STRING | Any command |
| [Invalid Control Id](#rsp_invalid_control_id) | bad\_id | bad\_id CONTROL\_ID | cga  cgr  cg  cgm  csp  css  ct |
| Login Failed | login\_failed | login\_failed | login |
| Login Required | login\_required | login\_required | Attempt to access a Core that requires a login. |
| Login Success | login\_success | login\_success | login |
| [Status Response](#rsp_status_response) | sr | sr DESIGN\_NAME DESIGN\_ID IS\_PRIMARY IS\_ACTIVE | sg |
| [Too Many Change Groups](#too_many_change_groups) | too\_many\_change\_groups | too\_many\_change\_groups | cgc |

[Change Groups](javascript:void(0))

Refer to the [External Control Protocol (ECP)](ECP_Overview.htm) > Change Groups section.

[Commands](javascript:void(0))

### Change Group Add

#### **Purpose:**Add a control to a Change Group.

#### **Syntax:**cga CHANGE\_GROUP\_ID CONTROL\_ID

#### **Example:**cga 2 slope

#### **Response:**none

#### [bad\_change\_group\_handle](#bad_change_group_handle)

#### [bad\_id](#bad_id)

### Change Group Clear

#### **Purpose:**Remove all of the controls from a Change Group.

#### **Syntax:**cgclr CHANGE\_GROUP\_ID

#### **Example:**cgclr 2

#### **Response:**none

#### [bad\_change\_group\_handle](#bad_change_group_handle)

### Change Group Create

#### **Purpose:**Create a Change Group. You can create up to four Change Groups on a single external client. The `CHANGE_GROUP_ID` is a 32-bit unsigned integer, however, it is recommended that you use smaller numbers to reduce network traffic. The `bad_change_group_handle` response is returned if you attempt to create more than four. This command is "silently" ignored if you attempt to create a Change Group with a `CHANGE_GROUP_ID` that is already in use. For more information on Change Groups refer to [Change Groups](ECP_Overview.htm#Change_Groups) in the External Control Overview.

#### **Syntax:**cgc CHANGE\_GROUP\_ID

#### **Example:**cgc 2

#### **Response:**none

#### [bad\_change\_group\_handle](#bad_change_group_handle)

### Change Group Destroy

#### **Purpose:**Destroy a Change Group.

#### **Syntax:**cgd CHANGE\_GROUP\_ID

#### **Example:**cgd 2

#### **Response:**none

#### [bad\_change\_group\_handle](#bad_change_group_handle)

### Change Group Invalidate

#### **Purpose:**To mark all the controls in the Change Group as if they had changed. At the next Change Group Poll, the state of all the group's controls is returned.

#### **Syntax:**cgi CHANGE\_GROUP\_ID

#### **Example:**cgi 1

#### **Response:**none

### Change Group Poll

#### **Purpose:**To poll a Change Group. This returns the state of all controls that have been added to the Change Group and/or that have changed since the last time the group was polled. The `cgpa` response is sent at the end of the response, or by itself if nothing in the Change Group has changed.

#### **Syntax:**cgp CHANGE\_GROUP\_ID

#### **Example:**cgp 2

#### **Response:**[cv](#cv)

#### [cmvv](#cmvv)

#### [cgpa](#cgpa)

#### [bad\_change\_group\_handle](#bad_change_group_handle)

#### **Example:**cv "slope" "12dB/Oct" 12 0.142857cmvv "slope" 2 4 "12 dB/Oct" "24 dB/Oct" "36 dB/Oct" "48 dB/Oct" 0 0 cgpa

#### cv "gain1" "0dB" 0 0.833333 cgpa

### Change Group Poll No ACK

#### **Purpose:**To poll a Change Group without an acknowledgement response. This returns the state of all controls that have been added to the Change Group and/or that have changed since the last time the group was polled. A `cgpa` response is *not* sent.

#### **Syntax:**cgpna CHANGE\_GROUP\_ID

#### **Example:**cgpna 2

#### **Response:**[cv](#cv)

#### [cmvv](#cmvv)

#### [bad\_change\_group\_handle](#bad_change_group_handle)

#### **Example:**cv "slope" "12dB/Oct" 12 0.142857cmvv "slope" 2 4 "12 dB/Oct" "24 dB/Oct" "36 dB/Oct" "48 dB/Oct" 0 0

#### cv "gain1" "0dB" 0 0.833333

### Change Group Remove

#### **Purpose:**Remove a control from a Change Group.

#### **Syntax:**cgr CHANGE\_GROUP\_ID CONTROL\_ID

#### **Example:**cgr 2 slope

#### **Response:**none

#### [bad\_change\_group\_handle](#bad_change_group_handle)

#### [bad\_id](#bad_id)

#### After a control has been removed from a Change Group, it may still be returned from the next `cgp`.

### Change Group Schedule

#### **Purpose:**Schedule a Change Group to be automatically polled periodically. The `POLL_PERIOD_MS` argument is an unsigned integer for the poll period in milliseconds. Minimum for `POLL_PERIOD_MS` is 30 ms, any amount less than this is changed to 30 ms. To turn off the scheduling of a group, enter 0 (zero) for `POLL_PERIOD_MS`. To change the schedule, issue this command with a new `POLL_PERIOD_MS`.

#### **Syntax:**cgs CHANGE\_GROUP\_ID POLL\_PERIOD\_MS

#### **Example:**cgs 2 100

#### **Response:**none

#### [bad\_change\_group\_handle](#bad_change_group_handle)

#### Periodically, the response from `cgp will be sent`.

### Change Group Schedule No ACK

#### **Purpose:**Schedule a Change Group to be automatically polled periodically without an acknowledgement response. The `POLL_PERIOD_MS` argument is an unsigned integer for the poll period in milliseconds. Minimum for `POLL_PERIOD_MS` is 30 ms, any amount less than this is changed to 30 ms. To turn off the scheduling of a group, enter 0 (zero) for `POLL_PERIOD_MS`. To change the schedule, issue this command with a new `POLL_PERIOD_MS`.

#### **Syntax:**cgsna CHANGE\_GROUP\_ID POLL\_PERIOD\_MS

#### **Example:**cgsna 2 100

#### **Response:**none

#### [bad\_change\_group\_handle](#bad_change_group_handle)

#### Instead of periodically issuing a `cgp`, a `cgpna` is issued, so there is no `cgpa sent`.

### Control Get

#### **Purpose:**For non-vector controls, get the string description, value, and position of a control's state. For vector controls, get the count of string elements, string array, count of value elements, value array, count of position elements, and position array.

#### **Syntax:**cg CONTROL\_ID

#### **Example:**cg gain1

#### **Response:**[cv](#cv)

#### [cvv](#cvv)

#### [bad\_id](#bad_id)

#### **Example:** cv "gain1" "-100dB" -100 0

#### cvv "meter1" 4 "-100dB" "-100dB" "-100dB" "-100dB" 4 -100 -100 -100 -100 4 0 0 0 0

#### Vector Control

A Vector Control has multiple strings, values and positions at a time, for example, a meter bar. A meter displays RMS, Max RMS, Peak, and Max Peak values. The Control Get command (`cg`) returns Control Vector Value response (`cvv`) when the control is a vector type control. You cannot set the values of a Vector Control.

#### **Example:**cvv "meter1" 4 "-100dB" "-100dB" "-100dB" "-100dB" 4 -100 -100 -100 -100 4 0 0 0 0

**Note:** For a Meter component, the strings, values, and positions are RMS, Max RMS, Peak, and Max Peak, in that order.

### Control Get Metadata

#### **Purpose:**Get all metadata attached to a control. This command does not give you the current state of a control, just the state of the metadata. Use the Control Get command to get the current state of the control. For more information about metadata see [Metadata Controls](#Metadata_Controls).

#### **Syntax:**cgm CONTROL\_ID

#### **Example:**cgm slope

#### **Response:**[cmv](#cmv)

#### [cmvv](#cmvv)

#### [bad\_id](#bad_id)

#### **Example:**cmv "load1" 6 "false" 0 0

#### cmvv "slope" 2 4 "12 dB/Oct" "24 dB/Oct" "36 dB/Oct" "48 dB/Oct" 0 0

### Control Set Position

#### **Purpose:**Set a control's state from a position. This is converted to a value using the controls range and its mapping.

#### **Syntax:**csp CONTROL\_ID CONTROL\_POSITION

#### **Example:**csp gain1 1

#### **Response:**[cv](#cv)

#### [bad\_id](#bad_id)

#### **Example:**cv "gain1" "20.0dB" 20 1

### Control Set Position Ramp

#### **Purpose:**Set a control's position from a number, with ramp time

#### **Syntax:**cspr CONTROL\_ID CONTROL\_POSITION RAMP\_TIME

#### **Example:**cspr id4 0.7 5

#### **Response:**nothing

#### [bad\_id](#bad_id)

**Note:** `cspr` does not return a "`cv`" response of the final value. To check the value after a ramp has completed use the "`cg`" command.

### Control Set Position Vector

#### **Purpose:**Sets a control position vector.

#### **Syntax:**cspv CONTROL\_ID NUM\_POSITIONS CONTROL\_POS1 CONTROL\_POS2 CONTROL\_POS3â¦CONTROL\_POSx

#### **Example:**cspv id4 3 0.2 0.5 0

#### **Response:**nothing

#### [bad\_id](#bad_id)

### Control Set Position Vector Ramp

#### **Purpose:**Sets a control value vector with ramp time.

#### **Syntax:**csvvr CONTROL\_ID CONTROL\_VALUE1 CONTROL\_VALUE2 CONTROL\_VALUE3â¦CONTROL\_VALUExRAMP\_TIME

#### **Example:** csvvr id4 3 2.1 3.2 5.3 10

### Control Set String

#### **Purpose:**Set a control's state from a text string.

#### **Syntax:**css CONTROL\_ID CONTROL\_STRING

#### **Example:**css id4 5.0db

#### **Response:**[cv](#cv)

#### [bad\_id](#bad_id)

#### **Example:**cv "id4" "5.00dB" 5 0.75

### Control Set String Vector

#### **Purpose:**Sets a control string vector.

#### **Syntax:**cssv CONTROL\_ID NUM\_STRINGS CONTROL\_STRING1 CONTROL\_STRING2 CONTROL\_STRING3â¦CONTROL\_STRINGx

#### **Example:**cssv textbox14"one" "two" "dog" "cat"

#### **Response:**nothing

#### [bad\_id](#bad_id)

### Control Set Value

#### **Purpose:**Set a control's state from a number.

#### **Syntax:**csv CONTROL\_ID CONTROL\_VALUE

#### **Example:**csv id4 6.2

#### **Response:**[cv](#cv)

#### [bad\_id](#bad_id)

#### **Example:**cv "id4" "6.20dB" 6.2 0.77

### Control Set Value Ramp

#### **Purpose:**Set a control's value from a number, with ramp time

#### **Syntax:**csvr CONTROL\_ID CONTROL\_VALUE RAMP\_TIME

#### **Example:**csvr id4 6.2 5

#### **Response:**nothing

#### [bad\_id](#bad_id)

**Note:** `csvr` does not return a `cv` response of the final value. To check the value after a ramp has completed the `cg` command should be used.

### Control Set Value Vector

#### **Purpose:**Sets a control value vector.

#### **Syntax:**csvv CONTROL\_ID NUM\_VALUES CONTROL\_VALUE1 CONTROL\_VALUE2 CONTROL\_VALUE3â¦CONTROL\_VALUEx

#### **Example:**csvv id4 4 7.0 2 3.2 5.3

#### **Response:**nothing

#### [bad\_id](#bad_id)

### Control Set Value Vector Ramp

#### **Purpose:**Sets a control value vector with ramp time.

#### **Syntax:**csvvr CONTROL\_ID CONTROL\_VALUE1 CONTROL\_VALUE2 CONTROL\_VALUE3â¦CONTROL\_VALUExRAMP\_TIME

#### **Example:**csvvr id4 3 2.1 3.2 5.3 10

#### **Response:**nothing

#### [bad\_id](#bad_id)

### Control Trigger

#### **Purpose:**To trigger a trigger-type control such as the "Play" button in the Audio Player.

#### **Syntax:**ct CONTROL\_ID

#### **Example:**ct play

#### **Response:**none

#### [bad\_id](#bad_id)

### Login

#### **Purpose:**Login to a Core that requires a login for external control. The `NAME` and `PIN` arguments must be for a valid User, with the appropriate permissions, existing in the Q-SYS System. If an attempt is made to login, without a `NAME` and `PIN`, to a system requiring login, a `login_required` response is sent. If a `login_failed` response is sent, the socket is automatically closed.

#### **Syntax:**login NAME PIN

#### **Example:**login Joe 1234

#### **Response:**login\_success

#### login\_failed

### Snapshot Load

#### **Purpose:**Load a snapshot. The `RAMP_TIME_LOAD` argument is a floating point number for the load ramp time in seconds.

#### **Syntax:**ssl SNAPSHOT\_BANK SNAPSHOT\_NUMBER FLOATING\_POINT\_NUMBER

#### **Example:**ssl snapshot1 2 5

#### **Response:**none

**Tip:** The floating point number here specifies the ramp time in seconds for loading a snapshot, which means how quickly or slowly the snapshot settings should be applied. The example `ssl snapshot1 2 5` uses `5` as the floating point number, indicating that the snapshot should be loaded with a ramp time of 5 seconds. If you wanted a more gradual change, you could use a larger number, or for a quicker change, a smaller number, including decimals for more precision, like `2.5` seconds.

### Snapshot Save

#### **Purpose:**Save a snapshot.

#### **Syntax:**sss SNAPSHOT\_BANK SNAPSHOT\_NUMBER

#### **Example:**sss snapshot1 3

#### **Response:**none

### Status Get

#### **Purpose:**Request the status of the Core.

#### **Syntax:**sg

#### **Example:**sg

#### **Response:**[sr](#sr)

#### **Example:**sr "MyDesign" "yq81K7SOhcDT" 1 1

[Responses](javascript:void(0))

### Change Group Poll ACK

#### **Purpose:**Acknowledges the Change Group was polled successfully. The `cgpa` response is sent at the end of a response, and by itself if nothing in the Change Group has changed.

#### **Response to:** `cgp`

#### **Syntax:**cgpa

#### **Example:**cv "pos1" ".586" 0.586406 0.586406cmv "pos1" 3 "" 0 0cmv "pos1" 6 "false" 0 0cmv "pos1" 4 "false" 0 0cmv "pos1" 5 "false" 0 0cv "gain1" "-100dB" -100 0cgpa

### Control Metadata Value

#### **Purpose:**Some controls have metadata attached to them. Metadata can be: a list of choices, if the control is invisible, disabled, and so on (see table below). Each metadata aspect has three facets: string, value and position. In the first example below, the aspect value 6 has a string of "false", a value of 0, and a position of 0. The second example is the same control in a disabled state, and now shows an aspect value 6 with a string of "true", value of 1, and position of 1.

#### The metadata responses do not give the actual state of the control, but the state of the attached metadata. For an explanation of metadata controls refer to [Control Get Metadata](#cmd_control_get_metadata).

#### **Response to:** `cgm` or `cgp`

#### **Syntax:**cmv CONTROL\_ID metadata\_aspect CONTROL\_STRING CONTROL\_VALUE CONTROL\_POSITION

#### The metadata aspect value is an unsigned integer with one of the following values:

| Value | Name | Description |
| --- | --- | --- |
| 0 | metadata\_aspect\_none | Should never appear. |
| 1 | metadata\_aspect\_range | Minimum and maximum value as in a 2-element floating-decimal vector control |
| 2 | metadata\_aspect\_choices | An array of strings |
| 3 | metadata\_aspect\_color | A string describing the color of the control. Used when a Custom control is in a not-normal state, for example, grayed out. |
| 4 | metadata\_aspect\_indeterminant | Boolean control, position > 0.5 indicates the control represents an unknown value, or represents multiple different values simultaneously. |
| 5 | metadata\_aspect\_invisible | Boolean control, position > 0.5 means the control is invisible and should not be displayed because it is irrelevant in the current context. For example, a bandwidth control on a high-shelf equalizer. |
| 6 | metadata\_aspect\_disabled | Boolean control, position > 0.5 means grayed / disabled. |
| 7 | metadata\_aspect\_legend | String control, specifies the legend drawn on buttons |

#### **Example:**cmv "pos1" 3 "" 0 0cmv "pos1" 6 "false" 0 0cmv "pos1" 4 "false" 0 0cmv "pos1" 5 "false" 0 0

#### cmv "pos1" 3 "" 0 0cmv "pos1" 6 "true" 1 1cmv "pos1" 4 "false" 0 0cmv "pos1" 5 " false" 0 0

#### Metadata Controls

Metadata means "data about data". In Q-SYS, some controls have metadata attached that describe aspects of the control. These aspects can include the range of the control, its color, whether it is disabled or invisible or its value is indeterminate, or a list of legal values for the control.

As an example, consider the Crossover component. The Slope, Type and Bessel Normalization controls all have metadata that describe the choices available in the drop-down list. The Bessel Normalization control also has metadata to make it invisible when the filter type is not Bessel-Thomson. When a Link button is pressed, all of the controls on the high frequency side of the crossover point are disabled through the use of metadata.

When you ask a control for its metadata with cgm (Control Get Metadata), you get a response for each aspect of metadata attached to that control, if any. The response is either cmv (Control Metadata Value) or cmvv (Control Metadata Value Vector). These responses look very similar to the responses you get when asking for a control's state with cg (Control Get), this is because the metadata is very much like a control itself in that is has a value, a position and a string. The only difference between the cv (Control Value) response and the cmv (Control Metadata Value) response is that cmv has the extra unsigned integer second argument that identifies which aspect of metadata is being described. Similarly the only difference between cvv (Control Value Vector) and cmvv (Control Metadata Value Vector) is the same additional argument.

#### **Example:**Control Value responses from the `cg` command: cv "slope" "48dB/Oct" 48 1

#### **Example:**Control Metadata Value Vector response from the `cgm` command: cmvv "slope" 2 4 "12 dB/Oct" "24 dB/Oct" "36 dB/Oct" "48 dB/Oct" 0 0

| Control Metadata Value Vector Response Breakdown | |
| --- | --- |
| Response | Description |
| slope | The CONTROL\_ID |
| 2 | The `metadata_aspect_choices` |
| 4 | The COUNT of the "strings" following  "12 dB/Oct" "24 dB/Oct" "36 dB/Oct" "48 dB/Oct" |
| 0 | The COUNT of the "values" following (in this case, none) |
| 0 | The COUNT of the "positions" following (in this case, none) |

#### **Example:**Control Value response from the `cg` command: cv "ssload" "" 0 0

#### **Example:**Control Metadata Value response from the `cgm` command: cmv "ssload" 6 "false" 0 0

| Control Metadata Value Response Breakdown | |
| --- | --- |
| Response | Description |
| ssload | The CONTROL\_ID |
| 6 | The `metadata_aspect_disabled` |
| false | The string describing the state of the control. |
| 0 | The "value" of the control |
| 0 | The "position" of the control |

### Control Metadata Vector Value

#### **Purpose:**Returns metadata information from a vector control. Sent in response to `cgm` or `cgp`. See [Control Get Metadata](#rsp_control_get_metadata) for details.

#### **Response to:** `cgm` or `cgp`

#### **Syntax:**cmvv CONTROL\_ID metadata\_aspec COUNT CONTROL\_STRING ... COUNT CONTROL\_VALUE ... COUNT CONTROL\_POSITION ...

#### **Example:**cmvv "Slope" 2 4 "12 dB/Oct" "24 dB/Oct" "36 dB/Oct" "48 dB/Oct" 0 0

### Control Read Only

#### **Purpose:**Returned when a Control Set command (`csp`, `css`, `csv`) is performed on a read-only control.

#### **Response to:** `csp`, `css`, or `csv`

#### **Syntax:**control\_read\_only CONTROL\_ID

### Control Value

#### **Purpose:**Contains the control's ID and the three facets of the control's state: string, value and position.

#### **Response to:** `css`, `csv`, `csp`, `cg`, and `cgp`.

#### **Syntax:**cv CONTROL\_ID CONTROL\_STRING CONTROL\_VALUE CONTROL\_POSITION

#### **Example:**cv "gain1" "-100dB" -100 0

### Control Vector Value

#### **Purpose:**Contains the three facets of a vector control's state.

#### **Response to:** `cg`

#### **Syntax:**cvv CONTROL\_ID COUNT CONTROL\_STRING ... COUNT CONTROL\_VALUE ... COUNT CONTROL\_POSITION ...

#### **Example:**cvv "meter1" 2 "-100dB" "-100dB" 2 -100 -100 2 0 0

**Note:** For a Meter component, the strings, values, and positions are current reading and Max reading. The readings change from RMS to Peak depending on the Peak/RMS switch on the meter.

### Core Not Active

#### **Purpose:**Returned when a Control Set command (`csp`, `css`, `csv`), Snapshot Load command (`ssl`, `sss`), or Control Trigger (`ct`) is performed on the standby Core of a redundant pair.

#### **Response to:** `csp`, `css`, `csv`, `ssl``sss`, `ct`

#### **Syntax:**`core_not_active`

### Invalid Change Group Handle

#### **Purpose:**To indicate an invalid `CHANGE_GROUP_ID`.

#### **Response to:** Any command with a `CHANGE_GROUP_ID` argument that is not recognized.

#### **Syntax:**bad\_change\_group\_handle CHANGE\_GROUP\_ID

### Invalid Command

#### **Purpose:**To indicate an invalid command.

#### **Response to:** Any command that is not recognized.

**Note:** The "CG" command in the example below is not recognized because the commands are all lower case, and case sensitive.

#### **Syntax:**bad\_command "string"

#### **Example:**bad\_command "CG"

### Invalid Control Id

#### **Purpose:**Indicates that a `CONTROL_ID` argument is not recognized.

#### **Response to:** Any command with a `CONTROL_ID` argument that is not recognized.

**Note:** The "load3" command in the example below is not valid because it does not exist.

#### **Syntax:**bad\_id CONTROL\_ID

#### **Example:**bad\_id "load3"

### Status Response

#### **Purpose:**Gives the status of the Core

#### **Response to:** [sg](#sg)

#### The arguments in order are:

| Argument | Data Type | Description |
| --- | --- | --- |
| DESIGN\_NAME | string | The name with which the currently running design file was saved. |
| DESIGN\_ID | string | A unique string generated every time a Design is deployed to a Core, or pair of Cores, or when the Design is emulated. |
| IS\_PRIMARY | unsigned integer | Is a 1 if this is the primary Core of a redundant pair, or the design is not redundant, 0 otherwise |
| IS\_ACTIVE | unsigned integer | Is a 1 if this is the active Core of a redundant pair or the design is not redundant, 0 if it is not active |

#### **Syntax:**sr DESIGN\_NAME DESIGN\_ID IS\_PRIMARY IS\_ACTIVE

#### **Example:**sr "MyDesign" "NIEC2bxnVZ6a" 1 1

### Too Many Change Groups

#### **Purpose:**Returned when Change Group Create (`cgc`) is called and four change groups have already been created on the connection, or the total count of 512 change groups system wide would be exceeded with this command.

#### **Response to:** `cgc`

#### **Syntax:**too\_many\_change\_groups
