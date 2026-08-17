# System Reliability

> Source: https://help.qsys.com/Content/Reflect/System_Reliability.htm

# System Reliability

The System Reliability module in Q-SYS Reflect helps you monitor and analyze system performance trends over time. It is designed to pinpoint systems with recurring issues, prioritize support and preventive maintenance, and build confidence in overall operational stability.

## Interface Overview

System Reliability provides two key views:

1. **System Reliability View** â Explore performance and issue trends for individual systems.
2. **Reliability Report View** â Compare systems across your organization to identify the most and least reliable.

## System Reliability View

The System Reliability View displays detailed performance data for selected systems. It is divided into multiple sections for filtering and exploration:

### Organization

* Displays the currently selected organization.
* If you have access to multiple organizations, you can toggle between them.

### Filters

Filters allow you to refine which systems and issue types are displayed.

[Issue Type](javascript:void(0))

* **Only Faults** - When On, only systems with a Fault status are displayed.
* When disabled, the following statuses may be selected:

  + **OK** - Normal operation
  + **Fault** - Critical issues
  + **Warning** - Minor issues or risks
  + **Initializing** - Starting up
  + **Offline** - Not connected or powered on
  + **Idle** - Inactive

[Systems](javascript:void(0))

* **All** â Shows all systems in the organization.
* **Assigned Systems** â Only systems assigned to a space in Space Manager.
* **Unassigned Systems** â Systems without an associated space.

[Spaces](javascript:void(0))

* **Only Spaces with Systems** â Shows only spaces that contain at least one system.
* **Search** â Type a space name to quickly locate it.
* **Listed Spaces** â Displays available spaces based on filters or search.

### Center Display Options

* **Date Range** â Select a date range to display reliability data.
* **Time Range** â Choose a specific time window within the selected date range.
* **Sort By** â Sort systems based on:

  + **System Name** (ascending/descending)
  + **Fault Duration** (ascending/descending)
* **Search** â Search for systems by their assigned names

## Reliability Report View

The Reliability Report View provides a high-level overview of reliability across the entire organization. It is especially useful for identifying which systems require attention or investment.

### Key Features

* **Organization-Level Report** â Displays the most and least reliable systems to help prioritize maintenance and improve uptime.
* **Date Range** â Select the period of analysis.
* **Sort By** â Order systems by fault duration or reliability scores.
* **Export CSV** â Download a CSV of the report for external analysis or record keeping.

### Systems

Lists all systems in the organization, ranked based on reliability metrics.

* Time / Percentage spent in
* Toggle between time spent or percentage spent in each system state.
* Available statuses include:

  + Fault
  + Warning
  + Offline
  + Idle
  + OK
  + Initializing

### Bucketing Strategy for Historical Data

To make historical reliability easier to interpret, the module uses a bucketing strategy to summarize system states over time.

* **Time Buckets** â When viewing data (e.g., past 24 hours, 7 days), system states are grouped into time intervals.
* **Impact-Based Display** â Each bucket highlights the most impactful state during that period, based on severity and duration.
* **Severity Ranking** â A fallback severity hierarchy ensures that the most critical state is shown when multiple statuses occur.
* **Drill-Down** â Users can click into a bucket for a more detailed view of events during that time.

This approach allows you to quickly assess long-term reliability trends while still being able to drill into specifics when needed.
