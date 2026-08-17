# Design Backup and Restore (Beta)

> Source: https://help.qsys.com/Content/Reflect/System_Management/Design_Backup.htm

# Design Backup and Restore (Beta)

To provide peace of mind in situations when reverting a Q-SYS Core processor to a previous state is necessary, any Q-SYS Core processor registered with Reflect backs up its running design to Reflect. With a Q-SYS Reflect Plus subscription, a backup can then be exported and re-deployed, or restored and re-deployed to a Core when needed.

**Note:** This is a BETA feature. Though it is functional, it is not feature complete.

## Automatic Backups

A Q-SYS Core processor registered with Reflect backs up its design to Reflect whenever the design is deployed (i.e., saved and run) to the Core. Control settings changes while the design is running â for example, from a User Control Interface (UCI) â are appended to the backup every 10 minutes.

**Note:** A maximum of five backups â each with any updated control settings changes â are retained in Reflect, with the oldest backups removed to make room for new backups.

### Viewing Automatic Backup Information

The Design Backup page lists up to five saved automatic backups, listed by design name.

* The Date Updated field shows the date and time that any captured control settings changes were appended to the backup at the last 10 minute interval.

* Click a backup's drop-down arrow to reveal the backup's details, including Core Name, Firmware Version, Backup Size (in MB), and Date Created.

### Exporting Automatic Backups

A Q-SYS Reflect Plus subscription is required to export an automatic backup. To export a design backup, click on the Options (ellipsis) icon to the right of the **Date Created** field, then click Export. The design is saved to the Downloads folder on your PC.

**Note:** At this time, exported designs do not include any captured control settings changes appended to the backup while the design was running on the Core.

### Restoring Automatic Backups

A Q-SYS Reflect Plus subscription is required to restore an automatic backup. To restore a design backup:

1. Open **Design Backup** page or be on it
2. Find **Automatic Backups** card with already created backup
3. Click on **Options (ellipsis)** icon in the end of the backup item
4. Find **Restore** item in the opened options list
5. Click on **Restore** item to start restoration process
6. Click on **Restore** button in the opened window to confirm restore operation
   * If needed, click on **Cancel** button to stop operation and close the window
7. Restore operation has started
   * The **Restore** button will be disabled during backup. The system will go into Idle mode and come back after restore is completed.
   * '*The restore procedure cannot be started because another one is in progress*' will show if restore procedure has been started but you are trying to start another one.
   * '*Restore failed. Unexpected error*' will show if restore procedure failed with unknown reason.

## Manual Backups

A Q-SYS Core processor registered with Reflect allows you to manually back up its design to Reflect. This option essentially makes a copy of the latest Automatic Backup but retains until the maximum backup allotment is reached. At which point, older backups will have to be deleted manually. To create a Manual Backup, choose the option that says **Create Backup**.

**Note:** A maximum of three backups are retained in Reflect. If the allotted three are already in use, you will be unable to create a new manual backup until you have deleted an older backup.

### Viewing Manual Backup Information

The Design Backup page lists up to three manually saved backups, listed by design name.

* The Date Created field shows the date and time that any captured control settings changes were saved.

* Click a backup's drop-down arrow to reveal the backup's details, including Core Name, Firmware Version, Backup Size (in MB), and Date Created.

### Exporting Manual Backups

A Q-SYS Reflect Plus subscription is required to export a manual backup. To export a design backup, click on the Options (ellipsis) icon to the right of the **Date Created** field, then click Export. The design is saved to the Downloads folder on your PC.

### Restoring Manual Backups

A Q-SYS Reflect Plus subscription is required to restore a manual backup. To restore a design backup:

1. Open **Design Backup** page or be on it
2. Find **Manual Backups** card with already created backup
3. Click on **Options (ellipsis)** icon in the end of the backup item
4. Find **Restore** item in the opened options list
5. Click on **Restore** item to start restoration process
6. Click on **Restore** button in the opened window to confirm restore operation
   * If needed, click on **Cancel** button to stop operation and close the window
7. Restore operation has started
   * The **Restore** button will be disabled during backup. The system will go into Idle mode and come back after restore is completed.
   * '*The restore procedure cannot be started because another one is in progress*' will show if restore procedure has been started but you are trying to start another one.
   * '*Restore failed. Unexpected error*' will show if restore procedure failed with unknown reason.

### Edit Comment Manual Backups

A Q-SYS Reflect Plus subscription is required to edit comments of a manual backup. To edit comments of a design backup, click on the Options (ellipsis) icon to the right of the **Date Created** field, then click Edit Comment. You will be prompted to enter additional or edit existing comments in the comment field.

### Delete Manual Backups

A Q-SYS Reflect Plus subscription is required to delete a manual backup. To delete a design backup, click on the Options (ellipsis) icon to the right of the **Date Created** field, then click Delete. You will be prompted to confirm your desire to delete the backup.
