# Q-SYS Communications Library

> Source: https://help.qsys.com/Content/External_Control_APIs/Communications_Library.htm

# Q-SYS Communications Library

As an alternative to connecting and controlling a Core directly via a TCP/IP connection, you can use the same communications library used by Q-SYS Designer. This library presents connection, status, control and monitoring of a Core at a higher level than direct TCP/IP socket communications, and thus is easier to use.

**Note:** An External Control client must communicate with the Q-SYS Core at least once every 60 seconds, or the socket connection will be closed by the Core. This is a form of "keep-alive" to make sure that abandoned connections get reclaimed by the Core. Most client programs poll a Change Group at a much higher rate which serves as a keep-alive. If not, the client program can issue a "Status Get" command periodically, or a "Control Set Value" on an unused control if no return response is desired.

[Connect to Q-SYS](javascript:void(0))

The Q-SYS Communications Library uses a library assembly in Microsoft .NET framework. The library, named QSysControl.dll, can be found in the Q-SYS Designer install directory. (typically "\program files\qscaudio\qsys\qsyscontrol.dll") The Q-SYS Communications Library supports multi-threading, creating one thread for each client the host application creates.

### General

#### Vector Type Controls

A vector type control has multiple strings, values and positions at a time, for example, a meter bar. A meter displays peak and RMS values. The `GetControl` Method returns `ControlResponse` (for non-vector controls) and `ControlVectorResponse` for vector type controls. You cannot set the values of a vector type control.

#### Metadata Type Controls

Metadata means "data about data". In Q-SYS, some controls have metadata attached that describe aspects of the control. These aspects can include the range of the control, its color, whether it is disabled or invisible or its value is indeterminate, or a list of legal values for the control.

As an example, take the Crossover component. The Slope, Type and Bessel Normalization controls all have metadata that describe the choices available in the drop-down list. The Bessel Normalization control also has metadata to make it invisible when the filter type is not Bessel-Thomson. When a Link button is pressed, all of the controls on the high frequency side of the crossover point are disabled using metadata.

#### Numbers and Strings

* Unsigned integers are 32-bit numbers.
* Floats are IEEE single precision floating numbers (32-bit)
* Strings

[AsciiClient](javascript:void(0))

The AsciiClient class provides simple methods for connecting, monitoring and controlling a Q-SYS system over a network.

In order to connect and control a Q-SYS system, an AsciiClient needs to be created using the host name or IP Address and port number (1702) of the Q-SYS Core. If the system has a redundant Core, you must use its host name or IP Address.

Excluding the initial Constructor, all methods are asynchronous - they do not block waiting for a network response. Any responses or errors are registered through Events.

### AsciiClient Constructor(String, Int32)

#### **Purpose:**Initializes a new instance of the AsciiClient class and connects to the specified port on the specified host.

#### **Syntax:**public AsciiClient(

#### string *hostname*,

#### int *port*

#### )

#### **Parameter:** hostname

#### **Type:** System.String

#### **Definition:** The DNS name or IP Address of the remote host to which you intend to connect.

#### port

#### **Type:** System.Int32

#### **Definition:** The port number of the remote host to which you intend to connect.

#### **Exceptions:** ArgumentNullException : hostname is a null reference

#### ArgumentOutOfRangeException : port is not between MinPort and MaxPort

#### SocketException : An error occurred when accessing the socket.

[AsciiClient Events](javascript:void(0))

| Events | | |
| --- | --- | --- |
| Event | Syntax | Purpose |
| ChangeGroupAck | () | Response to `AsciiClient.PollChangeGroup` - appears at the end of a response, or alone if nothing has changed in the group since the last polling. |
| CommunicationError | string errorMessage | A communication error defined in the returned string. |
| ControlMetaDataResponse | [ControlValue](#ControlValue) value, [ControlMetaData](#ControlMetaData) metadata | Occurs when metadata changes on a control in a Change Group. |
| ControlMetaDataVectorResponse | [ControlValueVector](#ControlValueVector) value, ControlMetaData metadata | Occurs when metadata changes on a control in a Change Group. |
| ControlResponse | ControlValue value | The value of a control. |
| ControlVectorResponse | ControlValueVector value | The array of values of a control. |
| EngineStatusResponse | [EngineStatus](#EngineStatus) status | The status of the Core. |
| InvalidChangeGroup | unsigned int ChangeGroupId | The changeGroupID sent to Q-SYS is incorrect. |
| InvalidCommand | string command |  |
| InvalidControlId | string ControlId |  |

[AsciiClient Methods](javascript:void(0))

| Methods Quick Reference | | |
| --- | --- | --- |
| Method | Syntax | Purpose |
| [AddControlToChangeGroup](#AddControlToChangeGroup) | unsigned int changeGroupID, string controlID | Add a control to a ChangeGroup. |
| [ClearChangeGroup](#ClearChangeGroup) | unsigned int changeGroupID | Remove all of the controls from a change group. |
| [ControlTrigger](#ControlTrigger) | string controlID | Trigger a control |
| [CreateChangeGroup](#CreateChangeGroup) | unsigned int changeGroupID | Creates the specified ChangeGroup. Maximum of four Change Groups. |
| [DestroyChangeGroup](#DestroyChangeGroup) | unsigned int changeGroupID | Destroy a ChangeGroup. |
| [GetControl](#GetControl) | string controlID | Get the value, position and string descriptions of a control's state. |
| [GetControlMetadata](#GetControlMetaData) | string controlID | Gets any metadata attached to a control |
| [GetEngineStatus](#GetEngineStatus) | () | Gets the status of the Core. |
| [InvalidateChangeGroup](#InvalidateChangeGroup) | unsigned int changeGroupID | Marks all the controls in a Change Group as if they had changed. |
| Login | string name, string pin | Initiates a login to a Q-SYS Core for an external control system. |
| [PollChangeGroup](#PollChangeGroup) | unsigned int changeGroupID | Checks the specified ChangeGroup for changes. |
| [RemoveControlToChangeGroup](#RemoveControlToChangeGroup) | unsigned int changeGroupID, string controlID | Remove a control from a change group. |
| [ScheduleChangeGroup](#ScheduleChangeGroup) | string controlID, unsigned int | The interval, in milliseconds, for a change group to be polled. |
| [SetControlPosition](#SetControlPosition) | string controlID float controlPosition | Set a control's state from a position. This is converted to a value using the controls range and its mapping. |
| [SetControlString](#SetControlString) | string controlID , string controlString | Sets the specified control to the specified control string value. |
| [SetControlValue](#SetControlValue) | string controlID , float controlValue | Sets the specified control to the specified single precision value. |
| [SnapshotLoad](#SnapshotLoad) | string snapshotID, unsigned int snapshotNumber, float secondsToRamp | Loads a saved snapshot. |
| [SnapshotSave](#SnapshotSave) | string snapshotID, unsigned int snapshotNumber | Saves a snapshot. |

### AsciiClient.AddControlToChangeGroup (Uint32, String)

#### **Purpose:**Add a control to a change group.

#### **Syntax:**public void AddControlToChangeGroup (

#### unsigned int changeGroupID,

#### string controlID

#### )

#### **Parameter:** changeGroupID

#### **Type:** System.Uint32

#### **Definition:** Identifies a change group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. Also, a client cannot open two sockets to the Core, create a change group on one socket and poll it on the other.

#### controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### **Response:**none

#### InvalidChangeGroup

#### InvalidControlId

### AsciiClient.ClearChangeGroup (Uint32)

#### **Purpose:**Remove all of the controls from a change group.

#### **Syntax:**public void ClearChangeGroup (

#### unsigned int changeGroupID

#### )

#### **Parameter:** changeGroupID

#### **Type:** System.Uint32

#### **Definition:** Identifies a change group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. Also, a client cannot open two sockets to the Core, create a change group on one socket and poll it on the other.

#### **Response:**none

#### InvalidChangeGroup

### AsciiClient.ControlTrigger (String)

#### **Purpose:**To trigger a control.

#### **Syntax:**public void ControlTrigger (

#### string controlID

#### )

#### **Parameter:** controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### **Response:**none

#### InvalidControlId

### AsciiClient.CreateChangeGroup (Uint32)

#### **Purpose:**Creates the specified ChangeGroup. You can create up to four change groups, on a single external client, that can be polled at separate intervals. The `InvalidChangeGroup` response is returned if you attempt to create more than four. This command is "silently" ignored if you attempt to create a change group with a `changeGroupID` that is already in use.

#### **Syntax:**public void CreateChangeGroup (

#### unsigned int changeGroupID

#### )

#### **Parameter:** changeGroupID

#### **Type:** System.Uint32

#### **Definition:** Identifies a change group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. Also, a client cannot open two sockets to the Core, create a change group on one socket and poll it on the other.

#### **Response:**none

#### InvalidChangeGroup

### AsciiClient.DestroyChangeGroup (Uint32)

#### **Purpose:**Destroy a change group.

#### **Syntax:**public void DestroyChangeGroup (

#### unsigned int changeGroupID

#### )

#### **Parameter:** changeGroupID

#### **Type:** System.Uint32

#### **Definition:** Identifies a change group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. Also, a client cannot open two sockets to the Core, create a change group on one socket and poll it on the other.

#### **Response:**none

#### InvalidChangeGroup

### AsciiClient.GetControl (String)

#### **Purpose:**Get the value, position and string descriptions of a control's state.

#### **Syntax:**public void GetControl (

#### string controlID

#### )

#### **Parameter:** controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### **Response:**ControlResponse (for non-vector controls)

#### ControlVectorResponse (for vector controls)

#### InvalidControlId

### AsciiClient.GetControlMetaData (String)

#### **Purpose:**Returns any metadata attached to a control.

#### **Syntax:**public void ControlTrigger (

#### string controlID

#### )

#### **Parameter:** controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### **Response:**ControlMetaDataResponse

#### ControlMetaDataVectorResponse

#### InvalidControlId

### AsciiClient.GetEngineStatus ()

#### **Purpose:**Requests the status of the Core.

#### **Syntax:**public void GetEngineStatus (

#### )

#### **Parameter:** none

#### 

#### **Response:**EngineStatusResponse

### AsciiClient.InvalidateChangeGroup (Uint32)

#### **Purpose:**To mark all the controls in the Change Group as if they had changed. At the next Change Group Poll, the state of all the group's controls is returned.

#### **Syntax:**public void InvalidateChangeGroup 9

#### unsigned int changeGroupID

#### )

#### **Parameter:** changeGroupID

#### **Type:** System.Uint32

#### **Definition:** Identifies a change group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. A client cannot open two sockets to the Core, create a change group on one socket and poll it on the other.

#### **Response:**none

### AsciiClient.Login (Uint32)

#### **Purpose:**Initiates a login to a Q-SYS Core for an external control system. The User Name and PIN must be a valid user, with permission to access the Core using external control. If an attempt is made to access a Q-SYS Core, that requires a login for an external control system, without a user name and PIN, a `LoginRequired` response is sent.

#### **Syntax:**public void login (

#### string name

#### unsigned int pin

#### )

#### **Parameter:** name

#### **Type:** System.String

#### **Definition:** Identifies an external control system to a Q-SYS design running on a Q-SYS Core. The name is set up in the Q-SYS Designer Administrator, on the User tab.

#### pin

#### **Type:** System.String

#### **Definition:** Verifies that the supplied `name` is a valid user in the Q-SYS design running on a Q-SYS Core. The PIN is set up in the Q-SYS Designer Administrator, on the User tab.

#### **Response:**LoginSuccess

#### LoginFailed

#### LoginRequired

### AsciiClient.PollChangeGroup (Uint32)

#### **Purpose:**Checks the specified ChangeGroup for changes.

#### **Syntax:**public void PollChangeGroup (

#### unsigned int changeGroupID

#### )

#### **Parameter:** changeGroupID

#### **Type:** System.Uint32

#### **Definition:** Identifies a change group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. Also, a client cannot open two sockets to the Core, create a change group on one socket and poll it on the other.

#### **Response:**0-n ControlResponse events

#### ChangeGroupAck

#### InvalidChangeGroup

### AsciiClient.RemoveControlToChangeGroup (Uint32, String)

#### **Purpose:**Remove a control from a change group.

#### **Syntax:**public void RemoveControlToChangeGroup (

#### unsigned int changeGroupID,

#### string controlID

#### )

#### **Parameter:** changeGroupID

#### **Type:** System.Uint32

#### **Definition:** Identifies a change group. This identifier is scoped to the connection that created it so it is not a problem if two clients each create groups with the same identifier. Also, a client cannot open two sockets to the Core, create a change group on one socket and poll it on the other.

#### controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### **Response:**none

#### InvalidChangeGroup

#### InvalidControlId

### AsciiClient.ScheduleChangeGroup (String, Uint32)

#### **Purpose:**Schedule a Change Group to be polled at the specified interval. `pollPeriodMS` is the interval in milliseconds. Minimum for `pollPeriodMS` is 30 ms, any amount less than this is changed to 30 ms. To turn off the scheduling of a group, enter 0 (zero) for `pollPeriodMS`. To change the schedule, issue this command with a new `pollPeriodMS`.

#### **Syntax:**public void ScheduleChangeGroup (

#### string controlID

#### unsigned int pollPeriodMS

#### )

#### **Parameter:** controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### pollPeriodMS

#### **Type:** System.Uint32

#### **Definition:** The interval, in milliseconds, for a change group to be polled.

#### **Response:**none

#### InvalidControlId

### AsciiClient.SetControlPosition (String, Float)

#### **Purpose:**Set a control's state from a position. This is converted to a value using the controls range and its mapping.

#### **Syntax:**public void SetControlPosition (

#### string controlID,

#### float controlPosition

#### )

#### **Parameter:** controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### controlPosition

#### **Type:** Float

#### **Definition:** A floating point number between 0.0 and 1.0 inclusive. Indicates where the value lies within the range of the control. Subject to a mapping.

#### **Response:**ControlResponse

#### InvalidControlId

### AsciiClient.SetControlString (String, String)

#### **Purpose:**Sets the specified control to the specified control string value.

#### **Syntax:**public void SetControlString (

#### string controlID,

#### string controlString

#### )

#### **Parameter:** controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### controlString

#### **Type:** System.String

#### **Definition:** Contains the textual representation of a control's state such as "-2.3dB" or "3.45 kHz"

#### **Response:**ControlResponse

#### InvalidControlId

### AsciiClient.SetControlValue (String, Float)

#### **Purpose:**Sets the specified control to the specified single precision value

#### **Syntax:**public void SetControlValue (

#### string controlID,

#### float controlValue

#### )

#### **Parameter:** controlID

#### **Type:** System.String

#### **Definition:** Identifies a control; defined in Q-SYS Designer.

#### controlValue

#### **Type:** float

#### **Definition:** A floating point number representing the numerical value of a control. The range of this number depends on the particular control.

#### **Response:**ControlResponse

#### InvalidControlId

### AsciiClient.SnapshotLoad (String, Uint32, Float)

#### **Purpose:**Loads a saved snapshot.

#### **Syntax:**public void SnapshotLoad (

#### string SNAPSHOT\_BANK,

#### unsigned int snapshotNumber,

#### float secondsToRamp

#### )

#### **Parameter:** SNAPSHOT\_BANK

#### **Type:** System.String

#### **Definition:** Identifies a bank of snapshots. This is the name given to the bank when it was created in Q-SYS Designer.

#### snapshotNumber

#### **Type:** System.Uint32

#### **Definition:** Identifies a snapshot within a snapshot bank. The range is 1 to the number of snapshots in the bank, inclusive.

#### secondsToRamp

#### **Type:** float

#### **Definition:** A floating point number indicating the load ramp time in seconds.

#### **Response:**none

### AsciiClient.SnapshotSave (String, Uint32)

#### **Purpose:**Saves a snapshot.

#### **Syntax:**public void SnapshotSave (

#### string SNAPSHOT\_BANK,

#### unsigned int snapshotNumber,

#### )

#### **Parameter:** SNAPSHOT\_BANK

#### **Type:** System.String

#### **Definition:** Identifies a bank of snapshots. This is the name given to the bank when it was created in Q-SYS Designer.

#### snapshotNumber

#### **Type:** System.Uint32

#### **Definition:** Identifies a snapshot within a snapshot bank. The range is 1 to the number of snapshots in the bank, inclusive.

#### **Response:**none

[QSC.QSys.ControlValue](javascript:void(0))

| Properties | | |
| --- | --- | --- |
| System.String | ID | The identifier of the control |
| System.String | String | The string representation of the value of a control |
| float | Position | The position representation of the value of a control (0.0 -> 1.0) |
| float | Value | The value representation of the value of a control |

[QSC.QSys.ControlValueVector](javascript:void(0))

| Properties | | |
| --- | --- | --- |
| System.String | ID | The identifier of the control |
| System.String[] | Strings | The string representations of the value of a control |
| float[] | Positions | The position representations of the value of a control (0.0 -> 1.0) |
| float[] | Values | The value representations of the value of a control |

[QSC.QSys.EngineStatus](javascript:void(0))

| Properties | | |
| --- | --- | --- |
| System.String | DesignName | The name of the design currently running on the Core. |
| System.String | ComplieGuid | The compile ID of the design currently running on the Core. |
| Boolean | IsActive | True if core is currently active and passing audio |
| Boolean | IsPrimary | True if core is the primary (or only core) in the design |

[QSC.QSys.ControlMetaData](javascript:void(0))

| Members | |
| --- | --- |
| Range | Description |
| !IsIndeterminate | Description |
| Choices | Description |
| Color | Description |
| !IsHidden | Description |
| !IsDisabled | Description |
| Legend | Description |
