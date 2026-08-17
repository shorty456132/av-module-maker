# Access Management > Roles

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Roles.htm

# Access Management > Roles

View current user role assignment on the Q-SYS Core processor and create custom user roles. After creating a user role, you can assign it to one or more users from the [Access Management > Users](Users.htm) page.

## Viewing Roles and Permissions

For each built-in role and custom role, the number of users assigned to that role is indicated. Click a role name to view assigned permissions for each page in Q-SYS Core Manager and Q-SYS Reflect > Systems.

* Full Access: The user can see the page within the Core Manager or Q-SYS Reflect navigation tree, view the page and its settings, and modify all settings.
* View: The user can see the page within the Core Manager or Q-SYS Reflect navigation tree and view the page and its settings. The user cannot modify any settings.
* Hidden: The user cannot see the page within the Core Manager or Q-SYS Reflect navigation tree.

**Note:** The Status page can never be hidden.

## Adding a Custom Role

The built-in user roles â Administrator, Technician, and Viewer â provide preset permissions assignment for typical access needs. However, it's easy to create a new role with custom page navigation in Core Manager and Q-SYS Reflect.

**Note:** Users with a custom role cannot load a design from the Q-SYS Core processor, regardless of the role permissions.

1. Click .
2. Specify a Role Name.
3. For each page name, select a permission level: Full Access, View, or Hidden.

   **Tip:** If your custom role will use most of one permission level, click one of the permission Presets. For example, clicking the View preset assigns all pages as View. You can then tweak individual page permissions.
4. Click Save.
5. Go to the Users page to assign the new custom role to a user. To learn how, see the [Access Management > Users](Users.htm) topic.

## Editing a Custom Role

You can easily modify the permissions of an existing custom role, even if that role is currently assigned to one or more users.

1. From the Custom Roles list, select a role.
2. Click Edit.
3. Modify the Permissions table for the role.
4. Click Save.

## Deleting a Custom Role

You can only delete a custom role if that role is not assigned to any users. If the role that you want to delete is assigned to one or more users, go to the Users page to assign those users another role.

1. From the Custom Roles list, select a role with 0 users.
2. Click .
