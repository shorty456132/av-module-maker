# Reflect Users and Roles

> Source: https://help.qsys.com/Content/Reflect/Reflect_Sites/Users_Roles.htm

# Reflect Users and Roles

The ability to manage and view Organizations and Domains in Q-SYS Reflect is governed by Q-SYS Reflect user roles. Q-SYS Reflect users are separate from Core [Access Management > Users](../Core_Management/Users.htm) established in Q-SYS Core Manager.

**Note:** When you register a Q-SYS Core with Q-SYS Reflect, the access level you choose during registration (Administrator, Technician, Viewer) becomes the highest permitted access level allowed to that Core, regardless of the Q-SYS Reflect user role.

## Organization Users

## Domain Users

An Organization Owner automatically becomes a Domain Manager of all Domains within the Organization. When you invite a new member to join a Domain, you can choose from two roles:

* Domain Managers can access and edit all Domain features, including inviting and managing new Members. Domain Managers have Administrator access to all Systems in the Domain. Domain Managers can register new Q-SYS Cores with the Domain.
* Domain Members can view Domain membership but cannot manage Core registration, Domain Managers, or Members. They can access Q-SYS Cores within the Domain, subject to an access level that you assign to that Member:

+ Administrators can view and modify all Core settings and features, deploy design files, and update Core firmware. They can also launch pin-protected User Control Interfaces (UCIs) without entering a PIN.
+ Technicians have the same access as Administrators, but without the ability to manage Core users. They can view Core users, but cannot enable or disable Access Control or create, edit, or remove users.
+ Viewers can view all settings and launch PIN-protected UCIs (with the appropriate PIN). They cannot edit any settings, preview audio files from the Files page, or download system information from the Utilities page.

**Note:** Administrators and Technicians can also enable user access for the External Control Protocol and File Management Protocol. These permissions are set in Q-SYS Administrator using separate user PINs specifically for these purposes.
