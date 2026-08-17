# Access Management

> Source: https://help.qsys.com/Content/RoomSuite/AccessManagement.htm

# Access Management

The Access Management section of RoomSuite Modular System controls who can sign in to the local RoomSuite Manager web interface running on the RoomSuite processor, RMP-100. From here, you can enable or disable local access control and manage the processorâs single local administrative user account.

When Access Control is disabled, the RoomSuite Manager interface is open to anyone who can reach the processorâs IP address. This allows unrestricted access to system configuration and operational settings. For this reason, enabling Access Control is strongly recommended for production environments, or any deployment where network reachable devices must be protected from unauthorized changes.

The Access Management > Users page is where you configure and maintain this local administrator account. Before Access Control is enabled, the page displays a banner indicating that no user accounts exist and provides the Enable Access Control button. Once enabled, this page lists the administrator account and provides tools for updating its password.

#### Enabling Access Control

When no user account exists, the Users page displays a banner stating that Access Control is not enabled and shows an Enable Access Control button.

1. Open Access Management > Users.
2. Click Enable Access Control.

   The Enable Access Control dialog opens.
3. In the dialolg, enter the following:

   * Username - A name for the administrative user.
   * Password - The password for this user.
   * Confirm Password - Re-enter the password to confirm.
4. Ensure the password meets the minimum requirement shown in the dialog (at least 8 characters).
5. Click Create.

After completion, RoomSuite Modular System will require this username and password for all future sign-ins. The Users page will display the administrator account along with password management controls.

**Note:** Be sure to remember your Username and Password. If you forget, a factory reset will be required to regain access to Q-SYS RoomSuite Modular System, which will result in the loss of all processor settings and system designs.

#### Changing the Administrator Password

1. Sign in to RoomSuite manager software with the existing administrator credentials.
2. Navigate to Access Management > Users.
3. Use the Edit / Change Password control next to the administrator account.
4. Enter and confirm the new password then click Save.

The new password takes effect immediately for all newly opened sessions.

#### Disabling Access Control

**Note:** Disabling Access Control removes password protection from RoomSuite Modular System. Only disable it temporarily for troubleshooting in secure environments.

1. Go to Access Management > Users.

2. Click Disable Access Control.

3. Confirm.

You can re-enable Access Control at any time by following the steps in [Enabling Access Control](#Enabling)
