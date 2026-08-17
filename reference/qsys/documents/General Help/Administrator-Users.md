# Users (Administrator)

> Source: https://help.qsys.com/Content/Administrator/Users.htm

# Users (Administrator)

Create users in Q-SYS Administrator to control access for External Control and File Management (the ability to manage audio files from an external connection). In addition, Administrator users can be assigned PA system paging capabilities, including the ability to override Page Station settings and invoke selected commands.

**Note:** Q-SYS Administrator users are not the same as Q-SYS Core users (created in Q-SYS Core Manager), which are used to control access to Q-SYS system features, including Administrator. For more information, see [Administrator Access Control](Accessing_Administrator.htm#Administ).

[Guest User](javascript:void(0))

A User named "Guest" is in the User list by default. This User cannot be renamed or deleted and has no PIN. The Guest User determines if permission to use certain features are given to all Users globally, or to Users on an individual basis. When the Guest User is given permission to use one of the features, all Users have permission to use that feature without a PIN. If the Guest User is denied permission to use one of these features you can specify which Users have permission when editing the User's properties.

To edit the Guest User:

1. Select the **Users** tab in the Administrator.
2. Double-click the **Guest** User. The Edit User dialog box displays.
3. Configure Access Permissions. These permissions are used for all users.

[Adding Users](javascript:void(0))

**Note:** Set up the Guest user before adding users.

1. Click **+**.
2. Configure the user name, Access Permissions, and Paging settings. See [User Settings](#User).
3. Add and assign Tags as desired. See [Assigning Tags to Users](#Assigning_Tags_to_Users).

**Tip:** To modify permissions for multiple users at once, select multiple users from the list, and then double-click a user name.

[Assigning Tags to Users](javascript:void(0))

You may wish to establish a group of Users who all perform the same or similar functions. To form a group of Users:

1. Edit the Guest User's properties as required.
2. Create the Users you are going to add to the group. Each User must have a unique Name and PIN.
3. Select the Users you want in the group.
4. Create a [Tag](Tags.htm) to identify the group. When you create the Tag, and have the Users selected, the Tag is applied to all the selected Users.
5. With the Users still selected, double-click one of the Users.
6. Update the user permissions, which are then applied to all selected users.
7. When you edit the properties for a Page Station, you can assign the entire group of Users permission to use that item simply by selecting the Tag you assigned to them.

To add another User to the group, select the User, and click the check box next to the group Tag in the Tags list.

**Note:** The assigned Tags are listed alphabetically from left to right next to the Users.

### Filter the Users by Tags

You can filter the list of Users based on the Tags you assign.

1. Click the filter icon in the top left corner (next to the plus sign). A list of Tags displays.
2. Click the check box of the Tag or Tags you wish to filter by. Only the Users assigned the selected Tags display.
3. Click the filter icon again and deselect any or all of the Tags to remove or modify the filter.

[User Settings](javascript:void(0))

#### Name

The user name of the person or group. You can use characters A-Z a-z 0-9 - . \_

#### Pin

Personal Identification Number for use when logging on to a Page Station, or User Control Interface.

### Access Permissions

#### External Control Protocol

Determines if the User can connect to the Core via External Control.

#### File Management Protocol

Determines if the User can manage Audio Files via an external connection.

For more information about the File Management Protocol, contact [Support](../Support.htm).

### Paging

#### Override Page Station Settings

Determines if the User Priority settings takes the place of the Page Station Priority settings.

* If you select Yes, the User's Priority is used to determine the Priority of the page, even if the User's Priority is lower than that of the Page Station.
* If you select No, the Page Station's Priority is used to determine the Priority of the page.

#### Override Command Priority Level

This selection is available only in Command Priority Mode and when the User's Override Station Settings is set to Yes.

Determines if the User Priority takes the place of the Command's Priority.

* If you select Yes, the User's Priority is used to determine the Priority of the page. This is true even if the User's Priority is lower than that of the Command.
* If you select No, the Command's Priority is used to determine the Priority of the page.

#### Priority

Priority Levels are used to determine priority of concurrent paging events. An event with a higher priority will interrupt an event with a lower priority level if there are any common destination **Zones**.

All of the Priorities created on the PA Global Settings tab are available to select for a User.

The Priority of a User is used when:

1. The Priority Mode is Command, and the
2. Override Page Station Settings is set to Yes, and the
3. Override Command Priority Level is set to Yes.

OR

1. The Priority Mode is Station/User, and the
2. Override Page Station Settings is set to Yes.

In either one of these cases, the User's Priority is used to determine the Priority of the page regardless of the Command or Page Station Priority.

#### Limit Available Commands

If you select No, the user can Use any of the Commands that have been created.

If you select Yes, you can then select the Commands that the User is allowed to use.

#### Available Commands

Select the Commands you want the User to be able to use by clicking the check box next to the individual Commands or by clicking the check box next to the Tag containing the Commands you want the User to use.
