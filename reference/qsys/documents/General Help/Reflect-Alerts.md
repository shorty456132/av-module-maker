# Alerts & Notifications

> Source: https://help.qsys.com/Content/Reflect/Alerts.htm

# Alerts & Notifications

The Alerts table provides a list of events that indicate compromised operation (Warning) or a more serious issue (Fault) â for example, a missing device â across all Organizations and Domains of which you are a member. Additionally, you can configure email notifications to alert you in real time (or at a specified time) whenever a new Alert is generated.

## What Generates an Alert?

An Alert is generated if a System goes offline, or whenever an Inventory item's state changes to Compromised, Fault, or Missing. These events trigger an Alert:

* A System went offline and cannot be monitored with Q-SYS Reflect.
* A device is Compromised.
* A device is in an error or Fault condition â for example, lost connection, missing, etc.
* Unable to export a Page Archive - for example, if the Media directory is full.
* The System design is being stopped because of a device name change.
* The System Mute is muted.

## Viewing Alerts

Alerts are listed by order of newest first. When more than one alert has been generated for a source, only the most recent alert is shown in the table, while older alerts for that source are viewable in the [Alert History](#Alert).

The Status column shows the current status of the source, while the Message column shows the severity level and description of the logged alert. Alerts are assigned an Error or Warning severity level, while the current status can be one of all four conditions.

**Tip:** Use the side-by-side comparison of the Status and Message columns to determine what faults may need the most and least attention. For example, a device that once generated an Error alert that is now in OK status may indicate only a temporary issue that is now resolved.

| Icon | Definition | Status Column | Message Column |
| --- | --- | --- | --- |
| OK | Indicates that the source is currently in a healthy condition. | X |  |
| Warning | Indicates compromised operation of the affected source and reduced functionality, such as a network redundancy (LAN B) communication problem. | X | X |
| Error | Indicates a more serious issue (Fault) with the affected source, such as a connection failure, clock sync fault, or missing device. | X | X |
| Not Available | Indicates that the current source status cannot be obtained, such as when a device is offline or you no longer have permission to see that device. | X |  |

[Alert History](javascript:void(0))

If there are multiple faults for a given source, only the most recent alert for that source is shown in the Alerts table. The  icon indicates that alerts for a source have been grouped, and the number of grouped alerts is indicated. Click the  icon to see all the of the source's alerts in its Alert History.

[Filtering Alerts](javascript:void(0))

You can filter Alerts by:

* Severity: Normal, Warning, Error, or Fault.
* Organization: Restrict the list to show only Alerts from specific Organizations.
* Domain: Restrict the list to show only Alerts from specific Domains.
* System: Restrict the list to show only Alerts from specific Systems.
* Source: Restrict the list to show only Alerts from specific devices or components.
* Start date ~ End date: Restrict the list to show only events whose Date & Time stamp is within a target range.
* Search Messages: Restrict the list to show only events with a Message containing a specified text string.

**Tip:** When selecting filter parameters, the quantity for each parameter is indicated. This can help you quickly determine, for example, the number of Error alerts, the number of alerts associated with a particular device, and so on.

[Hiding/Showing Columns](javascript:void(0))

Click the Columns button to select what columns to show or hide. You can toggle all columns except for Status, Message, and Actions.

**Tip:** To change the order in which columns appear, click and drag a column name within the Columns menu.

## Setting Email Notifications

Email notifications are disabled by default. When enabled, a notification email is sent to the user's email address whenever an alert is added to the Alerts table. To configure email notifications:

1. Click Notification Settings.
2. Toggle on the Enable Email notifications option.
3. Specify the alert Severities for which you want to receive an email alert â Error, Warning, Normal, Fault.
4. Specify how often to receive alert notification emails:
   * Real time, but not more often than every *nn* number of Seconds, Minutes, or Hours.
   * Once per hour, on the hour (if a new Alert was generated during that period).
   * Once per day at a specified time (if a new Alert was generated during that period).
5. Select the Time Zone to use for determining when to generate email notifications. This would typically be your local PC time zone.

**Note:** When you enable email notifications, you are only enabling notifications for your Q-SYS Reflect account.

## Webhook Notifications

Webhook notifications are another channel to notify you that a new alert has been created.

Webhook notifications are disabled by default. When enabled for **Teams**, **Slack**, or **Generic Webhook**, a notification is sent whenever an alert is added to the Alerts table. To configure Webhook notifications:

1. Click Notification Settings.
2. Toggle on the Enable Webhook Notifications option for either, or any combination of **Teams**, **Slack**, or **Generic Webhook**.
3. Specify the alert Severities for which you want to receive an alert â Error, Warning, Normal, Fault.
4. Specify the **Teams**, **Slack**, or **Generic Webhook** Notifications URL.
   * **Teams Webhook URL**: Visit [Create in Incoming Webhook for Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook?tabs=dotnet) to acquire unique URL.
   * **Slack Webhook URL**: Visit [Create in Incoming Webhook for Slack](https://api.slack.com/messaging/webhooks) to acquire unique URL.
   * **Generic Webhook URL**: Any custom URL can be used to send the HTTP POST request with a raw JSON. HTTPS protocol is mandatory.

**Note:** When you enable notifications, you are only enabling notifications for your Q-SYS Reflect account.

[HTTP Request Details](javascript:void(0))

#### HTTP Method

`POST`

#### HTTP Paylod

In setting up Teams and Slack Webhook Notifications, custom formatting is parsed by the messengers.

Generic Webhook raw JSON may look like:

```lua
{  
  "user": { "id": 12345 },  
  "alert": {   
    "id": 1839884,  
    "created": "2023-04-20T11:20:09.000Z",  
    "severity": "error",  
    "type": "item",  
    "siteId": 20704,  
    "siteName": "KBP 2E",  
    "organizationName": "QA_Default_Org",  
    "systemName": "kbp1-webqa-1100-49-file",  
    "coreId": 27220,  
    "itemId": 3718845,  
    "systemEventId": 121521851,  
    "systemId": 22120,  
    "source": "Tsc80-5",  
    "message": "Tsc80-5 is Missing",  
    "status": {  
      "code": 4,  
      "message": "Missing",  
      "details": ""  
    },  
    "isLicenseExpired": false  
  }  
}
```

#### HTTP Headers

```lua
Accept: */*  
Content-Type: application/json  
User-Agent: QSC-Webhooks/1.0  
X-QSC-Hook-UUID: 0e0ed467-d97a-4e4c-93f8-e574a0ac008c  
X-QSC-Attempt: 1
```

#### Retries

First attempt immediately, second - in a minute, third - in 10 minutes.

#### Requirements for Generic Webhook Servers

All 2xx responses are considered as Success, everything else is considered as a Failure. In case of a failure, the request will be retried.

The clientâs server should respond as fast as possible, any request which takes longer than 30 seconds will be considered as failed. That would start the retry mechanism and could lead to the situation when the same notification is handled twice.

Each notification has a unique UUID in HTTP headers `X-QSC-Hook-UUID`.

## Suppressing Alert Notifications

To create an alert email notification suppression:

1. Click the  icon for an alert.
2. Specify the suppression criteria, including an optional Description. By default, the criteria is filled out based on the selected alert. However, you can adjust the suppression parameters for Severity, Organization, Domain, System, Source, and matching Message.
3. Click Create. The  icon indicates that email notifications for that alert are now suppressed.

**Tip:** You can easily edit or delete an alert suppression from the Alerts & Notifications page > Notification Settings button > Suppressed Notifications section.

## Clearing Alerts

To clear Alerts, including alerts with Alert History:

1. Select the boxes for one or more alerts in the table.
2. Click Clear Selected Alerts.

**CAUTION:** This action cannot be undone.
