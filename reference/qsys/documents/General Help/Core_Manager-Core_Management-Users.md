# Access Management > Users

> Source: https://help.qsys.com/Content/Core_Manager/Core_Management/Users.htm

# Access Management > Users

Enable Access Control and manage local users on the Q-SYS Core, including assigning user [Access Management > Roles](Roles.htm).

## Enabling Access Control

**CAUTION:** By default, the Q-SYS Core is unprotected. For security purposes, QSC recommends that you enable Access Control, create users, and assign permissions to restrict access to the Core.

By default, Q-SYS Cores ship with Access Control disabled. To enable Access Control and create an Administrator account:

1. Click Enable Access Control.
2. Enter a Username and Password. Usernames must not contain spaces. Passwords must be at least 8 characters in length.
3. Click Create.

You must now sign in with those credentials whenever viewing or modifying your Core configuration in Q-SYS Core Manager.

**CAUTION:** Do not lose your Administrator account credentials.

## Adding Users

When you enabled Access Control, you created an account with Administrator privileges to the Q-SYS Core. However, you can create additional user accounts and assign permission levels as you require.

**Tip:** Before adding a new user, you may want to create a custom user role first. Refer to the [Access Management > Roles](Roles.htm) topic to learn how.

1. Click + New User.
2. Type a Username. Usernames must not contain spaces.
3. Select a User Role. These three roles are standard, but any custom [Access Management > Roles](Roles.htm) you have created are also assignable:

* Administrators can view and modify all Core settings and features, deploy design files, and update Core firmware. They can also launch pin-protected User Control Interfaces (UCIs) without entering a PIN.
* Technicians have the same access as Administrators, but without the ability to manage Core users. They can view Core users, but cannot enable or disable Access Control or create, edit, or remove users.
* Viewers can view all settings and launch PIN-protected UCIs (with the appropriate PIN). They cannot edit any settings, preview audio files from the Files page, or download system information from the Utilities page.

**Note:** Administrators and Technicians can also enable user access for the External Control Protocol and File Management Protocol. These permissions are set in Q-SYS Administrator using separate user PINs specifically for these purposes.

4. Enter a Password for the account. Passwords must be at least 8 characters in length.
5. Click Create.

## Managing Users

Only users with the Administrator role can manage existing users. From the Actions column:

* Click Edit to change a user's name and role.
* Click Change Password to update a user's password. Passwords must be at least 8 characters in length.
* Click Delete to remove the user from the Q-SYS Core.

**Note:** Administrators can also update their own username and password. Click your username in the top-right corner, and then select Manage Account.

## Disabling Access Control

Disabling Access Control deletes all security settings, including the Administrator account, and returns the Q-SYS Core to non-protected mode.

**CAUTION:** When you disable Access Control, all user accounts are deleted, and a sign-in is no longer required to gain access to Q-SYS Core Manager. This is not recommended for security reasons.

1. Click Disable Access Control.
2. Click Disable to confirm.
