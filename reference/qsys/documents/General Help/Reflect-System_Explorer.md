# System Explorer

> Source: https://help.qsys.com/Content/Reflect/System_Explorer.htm

# System Explorer

System Explorer provides a detailed, system-centric view that allows you to navigate organizations, domains, and systems seamlessly. It helps you monitor overall system health, review logs, and drill down into individual systems for diagnostics and reliability insights.

## Interface Overview

System Explorer is divided into two panels:

* Left Pane â Navigation (Organizations, Equipment, and Spaces).
* Right Pane â Contextual details based on the selection in the left pane.

### Left Pane â Navigation

[Organization](javascript:void(0))

Select the active organization.

Create new domains under the selected organization.

Register new systems under the domain

[Equipment](javascript:void(0))

Navigate between Organization, Domain, and System.

Organization View â Overview of all systems and domains within an organization.

Domain View â Summary of all systems in a selected domain.

System View â Detailed insights for an individual system.

[Spaces](javascript:void(0))

* Displays organization-defined spaces (as configured in Space Manager).
* Allows navigation to a space details page showing system health summary, error log graph, and log list.
* Includes a hyperlink to open the full space details in Space Manager.

**Note:** This section only groups systems by spaceâit does not allow editing or creation of spaces.

### Right Pane â Contextual Views

The right pane updates based on your selection in the left pane.

[Organization View](javascript:void(0))

* **Overview** â Name, icon, and metadata.
* **Counts** â Number of domains and number of systems.
* **Error Log Graph** â 24-hour time-based graph showing counts of faults and warnings across all systems.

  + Tooltip shows alert count and timestamp.
* **Log List** â Expandable, scrollable list of logs (Severity, Message, Timestamp, System Name).
* **System State Summary Bar** â Color-coded graph aggregating all system statuses in the organization with counts and labels.

[Domain View](javascript:void(0))

* **Overview** â Domain name, icon, and metadata.
* **System Counts** â Total number of systems and count per status.
* **Error Log Graph** â 24-hour time-based graph showing faults and warnings.
* **Log List** â Expandable, paginated list with Severity, Message, Timestamp, and System Name.
* **System State Summary Bar** â Aggregated status view across all systems in the domain.

[System View](javascript:void(0))

* **System Details** â Logo, name, and static label âSystem.â
* **Status Section** â Current system status (always displayed), last update timestamp, and location (as defined in the system design file).

  + If the system is linked to a space, the associated building is shown.
  + If unlinked, the field remains blank.
* **System Notes** â Free-form notes visible to all Reflect users in the organization.
* **System Reliability Graph** â Displays system reliability data with a link to the System Reliability module (Reflect Plus required).
* **Error Log Graph & List** â 24-hour graph of faults and warnings with expandable log list (Severity, Message, Timestamp, System Name).
* **Inventory** â Overview of system inventory details (e.g., components, resources, configuration).

[Space View](javascript:void(0))

* Displays system health summary for all systems in the space.
* Includes an error log graph and expandable log list.
* Provides a link to view full details in Space Manager.

## Notes

* **Logs** â Always limited to the last 24 hours and include only faults and warnings.
* **Unassigned Systems** â Systems not linked to spaces still appear under their domain in the Equipment section.
* **Deleted Domains/Systems** â Instantly removed from System Explorer once deleted in Reflect.
* **Reflect Plus Requirement** â Accessing the System Reliability module via the reliability graph requires a Reflect Plus subscription.
