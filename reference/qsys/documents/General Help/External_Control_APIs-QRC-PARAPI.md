# Q-SYS PA Remote API (PARAPI)

> Source: https://help.qsys.com/Content/External_Control_APIs/QRC/PARAPI.htm

# Q-SYS PA Remote API (PARAPI)

The Q-SYS Public Address Remote API, or PARAPI, is a TCP/IP command protocol intended to allow third-party systems to programmatically issue and monitor pages using the PA features of Q-SYS. It is part of the [Q-SYS Remote Control Protocol (QRC)](QRC_Overview.htm).

The command and response syntax is based on JSON-RPC version 2.0 (see <http://jsonÂ­rpc.org/wiki/specification>). The `PA.PageSubmit` command allows the client to issue a page, either voice or message play. `PA.ZoneStatusConfigure` allows the client to monitor the activity of the PA Router output zones.

[Commands and Notifications](javascript:void(0))

With the `PA.PageSubmit` command, a client submits a page specification and gets a PageID âhandleâ back from Q-SYS that can be used to subsequently Start, Stop, or Cancel the page. The PageID also appears in notifications from Q-SYS on the progress of the page in the system.

`PA.ZoneStatusConfigure` supports starting and stopping `PA.ZoneStatus` notifications from Q-SYS. These notifications give updates on the activity of each PA Router output zone.

In addition to the notifications sent by Q-SYS, Q-SYS returns a JSON-RPC result or error for each command that includes a JSON-RPC id. The result from the `PA.PageSubmit` command, for example, contains a PageID.

If greater than 60 seconds elapses between commands sent to the PARAPI server, the socket connection is closed. The client can send the NoOp command periodically it there isn't enough other command activity to keep the connection alive.

**Note:** PageID is unique between connections and always returns CommandID with responses.

### Commands (to Q-SYS)

* `PA.PageSubmit` : Submit a page specification. Response contains a PageID.
* `PA.PageStart` : Start a page.
* `PA.PageStop` : End a voice page (when the announcer is finished talking).
* `PA.PageCancel` : Cancel a page.
* `PA.ZoneStatusConfigure` : Configure zone status change notifications.
* `PA.GetConfig` : Retrieve the configured Zones, Tags, and Priorities.

### Notifications (from Q-SYS)

* `PA.PageStatus` : Page status update. Returns an audit (recorded) filename.
* `PA.ZoneStatus` : Zone status change. Includes the PageID, message name, and the audit filename of the currently executing request.

### Remote Commands

* `PA.PageProceed` : Starts a remote page.
* `PA.SourceWatchdog` : Starts a watchdog on a remote system.

[JSON-RPC Error Codes](javascript:void(0))

The following PARAPI error codes can be returned as the code value in a JSONÂ­RPC error object.

Example: `{"id":"2235","jsonrpc":"2.0","error":{"message":"Message file does not exist","code":4}}`

| Code | Description |
| --- | --- |
| 1 | Bad Parameters â one or more of the parameters is bogus. |
| 2 | Bad PageID â the PageID refers to a Page Request which does not exist. |
| 3 | Bad Request â could not create requested Page Request. |
| 4 | Bad File â Message file doesn't exist. |

[Parameters](javascript:void(0))

[PA.PageSubmit](javascript:void(0))

| Parameter | Type | Value | Notes | Overrides Global Setting | Parameter Required | Parameter Applies to Mode | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Mode | string | "message" or "live" or "delay" or "auto" | Specifies the type of page. âliveâ, âdelayâ, and âautoâ are all voice pages. | - | Y | live | delay/auto | message |
| Description | string |  | Appended to the completion event generated for the page (events appear in the [Core Manager](../../Core_Manager/CoreManager_Overview.htm) Event Log). | - | N | Y | Y | Y |
| Zones | integer or string array |  | Array of integers and/or strings that represent zone numbers or literal zone name strings specified in Q-SYS Administrator. | - | Y (and/or ZoneTags) | Y | Y | Y |
| ZoneTags | string array |  | Array of zone tag strings. | - | Y (and/or Zones) | Y | Y | Y |
| Priority | integer | 1-Â­n | 1 is highest priority. | - | Y | Y | Y | Y |
| Preamble | url string | audio file path | The preamble to play preceding the voice page or message. | - | N | Y | Y | Y |
| Message | url string | audio file path | The message to play, located in the Messages directory. | - | Y, if Mode == message | N | N | Y |
| MessageDelete | boolean |  | The message file will be deleted on page completion. | - | N | N | N | Y |
| Station | integer | 1-Â­n | n is the number of PA Router Page Station inputs. | - | Y, if Mode != message | Y | Y | N |
| Start | boolean |  | Start the Page after Submitting it (otherwise, the client must issue a PA.PageStart). | - | N | Y | Y | Y |
| QueueTimeout | integer | seconds | Time before delayed page times out, 0 means infinite, Â­1 means no queuing (i.e. page will fail if zones are not ready). | Y | N | N | Y | Y |
| Archive | boolean |  | Archive the page on completion. | Y | N | Y | Y | Y |
| Split | boolean |  | Allow partial page. | Y | N | Y | Y | Y |
| RetryCount | integer | 0Â­-n | Number of retries when page is interrupted on one or more zones. | Y | N | N | Y | Y |
| MaxPageTime | integer | seconds | Time before a voice page times out. | Y | N | Y | Y | N |
| CancelDelay | integer | seconds | Time during which delayed pages and messages are held for possible cancellation. | Y | N | N | Y | Y |
| Originator | string |  | Optional string used for logging. Default value is "QRAPI". | - | - | - | - | - |
| SplitOnInterrupt | boolean |  | Once the paging command is being played, if one or more zones are interrupted by another higher priority command, then the zone that is not interrupted should continue playing. | Y | N | Y | Y | Y |

[PA.PageStart](javascript:void(0))

| Parameter | Type | Value | Notes |
| --- | --- | --- | --- |
| PageID | integer |  | Starts a page. |

[PA.PageStop](javascript:void(0))

| Parameter | Type | Value | Notes |
| --- | --- | --- | --- |
| PageID | integer |  | End a voice page (when the announcer is finished talking). |

[PA.PageCancel](javascript:void(0))

| Parameter | Type | Value | Notes |
| --- | --- | --- | --- |
| PageID | integer |  | Cancel a page. |

[PA.ZoneStatusConfigure](javascript:void(0))

| Parameter | Type | Value | Notes |
| --- | --- | --- | --- |
| Enabled | boolean |  | Configure zone status change notifications. |

[PA.PageProceed](javascript:void(0))

| Parameter | Type | Value | Notes |
| --- | --- | --- | --- |
| PageID | integer |  | Starts a remote page. |

[PA.SourceWatchdog](javascript:void(0))

**Note:** If a page is playing and the client that initiated the page gets disconnected, the PA.SourceWatchdog will force the page to end.

| Parameter | Type | Value | Notes |
| --- | --- | --- | --- |
| RemoteSystem  (name of the system) | string |  | Starts a watchdog on a remote system. |

[PA.PageStatus](javascript:void(0))

| State | SubState | Count | Message | | |
| --- | --- | --- | --- | --- | --- |
|  |  |  | Mode=live | Mode=delay | Mode=message |
| ready | queued | Â­ | Busy[1](#Zones) | Â­ | Message not ready[2](#Issued) |
|  | immediate | Â­ | Ready to Page | Ready to Record | Ready to play message |
| wait | preamble | Â­ | Playing Preamble | Â­ | Â­ |
|  | zones | Â­ | Please wait | Waiting to playback | Waiting to playback |
|  | system | Â­ | Â­ | Waiting to playback |  |
|  | cancel | Y | Â­ | Waiting to playback[3](#input.ca) | Waiting to playback[3](#input.ca) |
| input | live | Y | Paging[3](#input.ca) | Â­ | Â­ |
|  | record | Y | Â­ | Recording[3](#input.ca) | Â­ |
| output | output | Â­ | Â­ | Playing message[4](#Includes) | Playing message[4](#Includes) |
| done | success | Â­ | Page complete | Playback complete | Playback complete |
|  | cancel | Â­ | Page canceled | Playback canceled | Playback canceled |
|  | timeout | Â­ | Page timeout | Queue timeout, playback canceled | Queue timeout, playback canceled |
|  | interrupt | Â­ | Page interrupted | Playback interrupted | Playback interrupted |
|  | fail | Â­ | ? | ? | Message failed[2](#Issued) |

###### 1. Zones are busy.

###### 2. Issued if system hasn't moved file into buffer yet, or if message file doesn't exist. But, state will move from âMessage not readyâ to âReady to play messageâ if file comes into existence. If a Start is issued while file doesn't exist, status will move to done.fail: âMessage failedâ.

###### 3. input.cancel, input.live and input.record are issued once per second, with a Count parameter that counts down from CancelDelay or MaxPageTime to zero.

###### 4. Includes optional Preamble playback.

**Note:** After a Page is submitted with `PA.PageSubmit`, it moves to the ready.queued or ready.immediate state. When `PA.PageStart` is issued on that Page, it will move to the wait.x or input.x state. Mode = delay or message type Pages will then move to the output.output state. Finally, the Page will move to the done.x state.

[Examples](javascript:void(0))

[Live Page](javascript:void(0))

The client submits a live page request, receives a PageID as a result, and then issues a start on that page. When the input is ready, notifications with State=âinputâ and SubState=âliveâ are received once per second with a Count indicating how many seconds are left before MaxPageTime expires. When the client is finished, it issues a Stop and gets a final notification that the page was successful.

```lua
==> {"id":"8561","method":"PA.PageSubmit","jsonrpc":"2.0","params":{"Zones":[2],"Preamble":"Chime long ascending triple.wav","Description":"Remote Client XYZ","ZoneTags":["Terminal B Retail"], "MaxPageTime":45,"Mode":"live","Station":4,"Priority":3}}  
  
<== {"id":"8561","jsonrpc":"2.0","result":{"PageID":895}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"ready","Message":"Ready to page","SubState":"immediate","PageID":895}}  
  
==> {"id":"4549","method":"PA.PageStart","jsonrpc":"2.0","params":{"PageID":895}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"wait","Message":"Please wait","SubState":"zones","PageID":895}}  
  
<== {"id":"4549","jsonrpc":"2.0","result":"OK"}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"wait","Message":"Playing preamble","SubState":"preamble","PageID":895}}  
  
<==  
{"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"input","Message":"Paging","SubState":"live"," PageID":895}}  
  
<==  
{"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Paging","Count":45,"SubState":"live","Stat e":"input","PageID":895}}  
  
<==  
{"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Paging","Count":44,"SubState":"live","Stat e":"input","PageID":895}}  
  
<==  
{"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Paging","Count":43,"SubState":"live","Stat e":"input","PageID":895}}  
  
<==  
{"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Paging","Count":42,"SubState":"live","Stat e":"input","PageID":895}}  
  
==> {"id":"8047","method":"PA.PageStop","jsonrpc":"2.0","params":{"PageID":895}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"done","Message":"Page complete","SubState":"success","PageID":895}}  
  
<== {"id":"8047","jsonrpc":"2.0","result":"OK"}
```

[Message Play](javascript:void(0))

The client submits a message play request with Start set to true, receives a PageID as a result, and then receives notifications indicating the message is queued and then waiting for... Then, notifications with State=âinputâ and SubState=âcancelâ are received once per second with a Count indicating how many seconds are left before CancelDelay expires. When the Preamble starts playing, a output.output notification is received, and when the Message is finished playing, a done.success notification is received.

```lua
==> {"id":"8561","method":"PA.PageSubmit","jsonrpc":"2.0","params":{"Zones":[2],"Description":"Remote Client XYZ","QueueTimeout":30,"ZoneTags":["Terminal B Retail"],"Message":"ann2.wav","Preamble":"Chime long ascending triple.wav","Start":true,"Mode":"message","CancelDelay":5,"Priority":3}}  
  
<== {"id":"8561","jsonrpc":"2.0","result":{"PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"ready","Message":"Message not ready","SubState":"queued","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"wait","Message":"Waiting to playback","SubState":"cancel","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Waiting to playback", "Count":5,"SubState":"cancel","State":"wait","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Waiting to playback", "Count":4,"SubState":"cancel","State":"wait","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Waiting to playback", "Count":3,"SubState":"cancel","State":"wait","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Waiting to playback", "Count":2,"SubState":"cancel","State":"wait","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"Message":"Waiting to playback", "Count":1,"SubState":"cancel","State":"wait","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"wait","Message":"Waiting to playback","SubState":"system","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"output","Message":"Playing message","SubState":"output","PageID":7}}  
  
<== {"method":"PA.PageStatus","jsonrpc":"2.0","params":{"State":"done","Message":"Playback complete","SubState":"success","PageID":7}}
```

[Zone Status Configure](javascript:void(0))

The client sends a `PA.ZoneStatusConfigure` command with a JSON-RPC id and gets a response. Immediately, the status of each zone output of the PA Router is sent as a series of notifications (in this case, 8 zones). Subsequently, as pages are made, more status update notifications are sent. `PA.ZoneStatusConfigure` is then disabled to stop notifications.

```lua
==> {"id":"8185","jsonrpc":"2.0","method":"PA.ZoneStatusConfigure","params":{"Enabled":true}}  
  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":1,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":2,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":3,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":4,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":5,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":6,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":7,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:21Z", "Zone":8,"Active":false}}  
<== {"id":"8185","jsonrpc":"2.0","result":"OK"}  
  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"PriorityName":"Urgent","Time":"2012-05-14T16:57:24Z","Zone":1,"Priority":2,"Station":1,"Active":true}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"PriorityName":"Urgent","Time":"2012-05-14T16:57:24Z","Zone":5,"Priority":2,"Station":1,"Active":true}}  
  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:26Z", "Zone":1,"Active":false}}  
<== {"method":"PA.ZoneStatus","jsonrpc":"2.0","params":{"Time":"2012-05-14T16:57:26Z", "Zone":5,"Active":false}}  
  
==> {"id":"9204","jsonrpc":"2.0","method":"PA.ZoneStatusConfigure","params":{"Enabled":false}}  
<== {"id":"9204","jsonrpc":"2.0","result":"OK"}
```

[Get PA Configuration](javascript:void(0))

Retrieve the configured Zones, Tags, and Priorities.

#### Request

```lua
{  
    "method": "PA.GetConfig",  
    "params": {},  
    "id": "1"  
}
```

#### Response

```lua
{  
    "id": 1,  
    "jsonrpc": "2.0",  
    "result": {  
        "Priorities": [  
            {  
                "Archive": false,  
                "Color": "#FFFF7F80",  
                "Guid": "4e055259-34a4-45df-84c1-8e96faa9926f",  
                "Name": "Emergency",  
                "Retry": false,  
                "Split": false  
            },  
            {  
                "Archive": false,  
                "Color": "#FFFFB280",  
                "Guid": "39f9f05f-ad2f-4b83-92fb-5a2ce8ae11e7",  
                "Name": "Urgent",  
                "Retry": false,  
                "Split": false  
            },  
            {  
                "Archive": false,  
                "Color": "#FFFFE580",  
                "Guid": "5522845e-8536-4140-9c3e-7afc4d3d50d3",  
                "Name": "Important",  
                "Retry": false,  
                "Split": false  
            },  
            {  
                "Archive": false,  
                "Color": "#FFE6FF80",  
                "Guid": "9f405daa-a03a-45ad-8800-7a3f2fd29cd0",  
                "Name": "Normal",  
                "Retry": false,  
                "Split": false  
            },  
            {  
                "Archive": false,  
                "Color": "#FF80FF80",  
                "Guid": "59767f61-7e1e-47dd-b54c-1d6f874534e5",  
                "Name": "Background",  
                "Retry": false,  
                "Split": false  
            }  
        ],  
        "Tags": [  
            {  
                "Guid": "9aebb5f2-566a-4682-a068-85842f206e79",  
                "Name": "tag1"  
            },  
            {  
                "Guid": "1bb9fb07-513c-4419-bab7-e24ae36f4cf9",  
                "Name": "tag2"  
            },  
            {  
                "Guid": "6ea9a718-e177-4dbf-8834-569283c02c57",  
                "Name": "tag3"  
            },  
            {  
                "Guid": "939f7575-9d1e-4a88-86a4-47c43596d12c",  
                "Name": "tag4"  
            }  
        ],  
        "Zones": [  
            {  
                "Group": "Local",  
                "Index": "1",  
                "IsLocal": true,  
                "Name": "Zone 1",  
                "Tags": [  
                    {  
                        "Guid": "9aebb5f2-566a-4682-a068-85842f206e79",  
                        "Name": "tag1"  
                    },  
                    {  
                        "Guid": "6ea9a718-e177-4dbf-8834-569283c02c57",  
                        "Name": "tag3"  
                    }  
                ]  
            },  
            {  
                "Group": "Local",  
                "Index": "2",  
                "IsLocal": true,  
                "Name": "Zone 2",  
                "Tags": [  
                    {  
                        "Guid": "939f7575-9d1e-4a88-86a4-47c43596d12c",  
                        "Name": "tag4"  
                    },  
                    {  
                        "Guid": "6ea9a718-e177-4dbf-8834-569283c02c57",  
                        "Name": "tag3"  
                    }  
                ]  
            },  
            {  
                "Group": "Local",  
                "Index": "3",  
                "IsLocal": true,  
                "Name": "Zone 3",  
                "Tags": [  
                    {  
                        "Guid": "1bb9fb07-513c-4419-bab7-e24ae36f4cf9",  
                        "Name": "tag2"  
                    }  
                ]  
            }  
        ]  
    }  
}
```
