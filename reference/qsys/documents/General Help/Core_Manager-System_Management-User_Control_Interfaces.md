# User Control Interfaces

> Source: https://help.qsys.com/Content/Core_Manager/System_Management/User_Control_Interfaces.htm

# User Control Interfaces

View UCIs directly from Core Manager, as well as manage access to the UCIs contained in the design running on the Q-SYS Core processor.

**CAUTION:** By default, there is open access to the UCIs in the design running on the Core. To secure access to UCIs, create user PINs.

## Viewing a UCI

To view a UCI directly from Core Manager:

1. From the left pane, select a UCI in your design. If your design contains many UCIs, click the  button to filter by panel type or use the Search box.
2. Click the UCI View tab. If the UCI is protected with a PIN, enter the PIN to log in. (Administrator users can open pin-protected UCIs without entering a PIN.)

**Tip:** Click Open UCI in New Window if you prefer to open the UCI outside of the Core Manager window. Or, right-click and select to open the UCI in a new tab.

## Creating User PINs

The first step to establishing UCI access control is to create user and PIN credentials. These credentials are used exclusively for UCI access. You can create up to 100 PINs.

1. From the top-right corner, click Edit PINs.
2. Click + New PIN.
3. Enter credentials for the new user:
   * Name: A descriptive name for the UCI user. For example, this could describe an individual, group, or location.
   * PIN: A code containing a maximum of eight numbers the user must enter to gain access to the UCI.
4. Click +New PIN for each additional PIN you require. When finished, click Save.

## Configuring UCI Access

Once you have created user PINs for UCI access, you can then associate those users with specific UCIs.

1. From the left pane, select a UCI in your design. If your design contains many UCIs, click the  button to filter by panel type or use the Search box.
2. Click the PIN Protection tab.
3. Click Edit.
4. Use the check boxes to select the users to grant access to the UCI.
5. Click Save. In the list of UCIs, the  icon indicates access control is now enabled for the UCI.

## UCI Links

Q-SYS 9.9 introduces a UCI Links tab that allows you to create http(s) link(s) to the UCI view and use it to embed the UCI to other apps, and/or hardware.

1. From the left pane, select a UCI in your design. If your design contains many UCIs, click the  button to filter by panel type or use the Search box.
2. From the UCI Links tab, select **Create Link**.
3. Enter the name of the Link you would like to use and click **Create**.
4. You will then be prompted to **Copy Link + Token**, **Copy Link**, or **Copy Token**. Choose the one that best fits your situation.
5. Use the Link or Token to embed the UCI into other applications or hardware (i.e., you can use the link in a web browser window).

**Note:** Once you copy the link or token, they will no longer be visible after you close the window. Be sure to save it in a safe place for future reference.

## Revoking UCI Links

When the UCI Link or Token is no longer needed, you can revoke it.

1. From the left pane, select a UCI in your design. If your design contains many UCIs, click the  button to filter by panel type or use the Search box.
2. From the UCI Links tab, select the desired **UCI Link Name** you wish to delete.
3. One it is selected, click **Revoke**.

**Note:** Once you revoke the UCI Link or Token, it will cease to function wherever it is embedded.

## UCI Variables

In Q-SYS Core Manager, the UCI Variables tab is used to manage and configure variables associated with UCIs.

### View UCI Variables

1. From the left pane, select a UCI in your design. If your design contains many UCIs, click the  button to filter by panel type or use the Search box.
2. By default, the UCI Variables tab is compacted for a streamlined view. To reveal its content, simply click to expand it.

### Search or Sort UCI Variables

1. From the left pane, select a UCI in your design. If your design contains many UCIs, click the  button to filter by panel type or use the Search box.
2. By default, the UCI Variables tab is compacted for a streamlined view. To reveal its content, simply click to expand it.
3. If you have a longer list of UCI Variables, you can search by the following:
   * Search Field: Type the name of the UCI Variable into the Search field and click on the  magnifying glass.
   * Sorting: At the bottom of the UCI Variables tab, click on the dropdown menu for **Sort by**. You can arrange the variables either by **Alphabetically (Ascending)** or **Alphabetically (Descending)**.

### Edit UCI Variables

1. From the left pane, select a UCI in your design. If your design contains many UCIs, click the  button to filter by panel type or use the Search box.
2. By default, the UCI Variables tab is compacted for a streamlined view. To reveal its content, simply click to expand it.
3. After finding the UCI Variable you need, you can choose to **Show Component** and edit the **Room Name**, **Room Support**, and **Background Color**.
   * As you make changes, Core Manager will automatically save them.
   * In the event that an error is encountered during the saving process, a distinct red "X"  accompanied by the notification **Save failed** will be displayed. Hovering over this symbol will provide you with an informative error message, allowing for quick and informed resolution.
