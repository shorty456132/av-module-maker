# Page Stations (Administrator)

> Source: https://help.qsys.com/Content/Administrator/Page_Stations.htm

# Page Stations (Administrator)

Page Stations can be either physical hardware, or virtual. This topic describes configuring either type using the Administrator. You must have at least one Page Station (virtual or physical hardware proxy) and a PA Router in your design to access these settings.

When you access the Page Stations tab in the Administrator, a list of the Page Stations, both proxies and virtual, and grouped by model, displays. Double clicking any of the Page Stations in the list opens the Page Station Settings dialog box with the controls listed in the table below. Depending on the Priority Mode setting (PA Global Settings), different controls are available as indicated below.

**Note:** The PS-TSCG3 identifies as a Virtual Page Station on Input *n* within Administrator.

[Virtual Page Station Controls](javascript:void(0))

### Settings

On the Page Station Settings dialog box, click the Settings tab. The following parameters are available on all Page Station models.

#### Name

Read only field. The **Name** field matches the device name given to the **Page Station proxy** in the Q-SYS design. This must match the network name with which the physical device is to be configured.

The **Virtual Page Station** name can only be changed by changing the **Station Control** wiring from one **PA Router** input pin to another. The name is "**VPS on Input** *n*".

#### Override Command Priority Level

This selection is available only when the **Priority Mode** in the **PA Global Settings** is set to **Command Priority**.

Selecting Yes for this control causes the Priority of the Page Station to be used instead of the Priority of the Command used in a paging event.

**Note:**  The Page Station Priority is used regardless of what the actual priority of the **Command** is. If a Page Station with the lowest priority has **Override Command Priority Level** set to **Yes**, and invokes a Command with the highest priority, the page is sent out as the lowest priority.

#### Priority Level

This selection is available in **Station/User Priority Mode**, and in **Command Priority Mode** when the station has **Override Command Priority Level** set to **Yes**.

Sets the Priority Level for the Page Station. This priority is used to determine the priority of concurrent paging events based on any override settings.

#### Revert Selected Command

After a Command Button is pressed, and the Command is either completed, canceled, interrupted or not executed, the Page Station can do one of three things with or without a specified timeout period: select Command Button A, clear the selected button, or leave the last Command Button you press selected.

This section gives you three parameters to set up the action: **after timeout**, **after execute**, and **revert to**. Below are the possible scenarios.

* Both **after timeout** and **after executing** are **No**. You cannot make a selection in **revert to**.
  + A Command button is pressed and the page is not executed
    - The currently selected Command Button remains selected.
  + A Command button is pressed and the page is executed
    - The currently selected command remains selected.

* **After timeout** is set to one of the selections and **after execute** is set to No, **revert to** can be either Command Button A or no command.
  + A Command Button is pressed, but the page is not executed
    - after the timeout expires. the action specified in **revert to** takes place.
  + A Command Button is pressed, and the page is executed
    - The currently selected Command Button remains selected and the timeout timer is restarted.

* **After timeout** is set to No, **after execute** is set to Yes, and **revert to** is set to either Command Button A or no command.
  + A Command Button is pressed, and the page is not executed
    - The currently selected Command Button remains selected.
  + A Command Button is pressed, and the page is executed
    - The action specified in **revert to** takes place immediately.

* **After timeout** is set to one of the selections and **after execute** is set to Yes, **revert to** can be any Command Button or no command.
  + A Command Button is pressed, and the page is not executed
    - The action specified in **revert to** takes place after the timeout.
  + A Command Button is pressed, and the page is executed
    - The action specified in **revert to** takes place immediately.

#### Maximum Page Duration

Sets the time limit of a page. Page Commands only.

### Command Buttons

On the Page Station Settings dialog box, click the Command Buttons tab. The following parameters are available on all Page Station models.

#### Button A Command through Button *x* Command

Depending on the Page Station model (16-, 8-, or 4-button), there can be up to 16 buttons to which you can assign **Commands**. When a Command is assigned to a button, the user simply presses the button associated with the desired Command, and that Command is executed.

You can select a **Command** from the drop-down list associated with the desired button. The list is populated by the Commands created on the Commands tab of the Administrator.

### OK / Cancel

Click **OK** to accept the changes and exit the dialog box, **Cancel** to exit without accepting the changes.

**Note:** In order to save any changes made while in the Administrator, you must click the **Update** button, available at the bottom left of the interface, after making a change.

[Physical Page Station Controls](javascript:void(0))

The PS-TSCG3 models, available in both gooseneck and handheld versions, feature the [TSC-70-G3](../Hardware/Control_IO/TSC-70-G3.htm) touchscreen, with the only physical button being an embedded push-to-talk button, while all other on-screen buttons are configured via the UCI.
