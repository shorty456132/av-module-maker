# Presets

> Source: https://help.qsys.com/Content/Reflect/Reflect_Sites/Presets.htm

# Presets

Use the Presets feature to assign settings to multiple Systems (Q-SYS Core processors) at the same time. This is useful in cases where many Systems require the same configuration â for example, network settings for Q-SYS Core processors residing on the same network. Applying settings simultaneously to multiple Systems saves time and reduces the chance of configuration errors.

## Supported Preset Settings

The Presets feature supports configuration and System synchronization of these settings:

* [Network > Basic](../Core_Management/Network_Settings.htm) â LAN configuration (except LAN A Mode), static routing, DNS, and proxy configuration
* [Network > Date & Time](../Core_Management/Date_Time.htm) â Time zone and NTP server synchronization
* [Network > Services](../Core_Management/Network_Services.htm)
* [Network > SNMP](../Core_Management/SNMP.htm)
* [Files](../Core_Management/Audio_Files.htm) â Files, folders, and playlists
* [Access Management > Users](../Core_Management/Users.htm) (Access Control) â Administrator role creation

  **CAUTION:** Including Access Control in a preset will overwrite Access Management settings on the Cores that are linked to it.

## How do Presets work?

Easy! In Q-SYS Reflect, just create the settings you want for each supported category, save the Preset, and then apply it to one or more Systems. Q-SYS Reflect then syncs those settings with each Q-SYS Core processor. In the case of files (for example, audio files), those are uploaded to the Reflect cloud and then pushed to the local storage of the Core during synchronization.

**Tip:** Only one Preset can be applied to a System at a time.

## Creating and Linking Presets

[Create a Preset](javascript:void(0))

1. From the Q-SYS Reflect > Domains page, click a Domain name.
2. From the left menu, click Presets.
3. Click the + Create Preset button.
4. Give the Preset a name, and then click Create.
5. From the list of Presets, click the name of the Preset you just created.
6. From the left pane, select a category to configure, and then click Edit.
7. For each sub-category to include in your Preset, select the Included in Preset box.
8. When you are finished with a category, click Save. Configure other categories as needed.

[Link a Preset](javascript:void(0))

When you are ready to apply a Preset to one or more Systems:

1. From the Presets page, click the System Links button.
2. From the list of Systems, select a Preset to push for each System. If a System already has a Preset selected, you must first deselect the existing Preset.
3. Click Save. Synchronization begins. When complete, a "System Links Updated" message appears. The Preset is now applied to the Q-SYS Core processor.

**Note:** If the Preset sync fails, see [Resync a Preset](#Resync).

[Resync a Preset](javascript:void(0))

To safeguard against losing connectivity to a Q-SYS Core processor due to improper Preset settings, Q-SYS Reflect backs up the current settings for each Preset category and then checks for proper connectivity to the Core before applying new settings. If this connectivity check fails, the Preset settings are reverted.

If a Preset synchronization fails:

1. Verify that the Preset settings are valid for the Q-SYS Core processor.
2. From the System Links page > Actions column, click the  icon to resync the Preset.

[Unlink a Preset](javascript:void(0))

**Note:** When a Preset for a settings category has been applied, the  icon appears in Q-SYS Reflect and Core Manager with a reminder that the settings are linked to a Preset. These settings cannot be modified outside of the Preset unless the Preset is unlinked from the System.

When you unlink a Preset, settings and files for that Preset remain on the Q-SYS Core processor but can then be managed individually, whether in Q-SYS Reflect or Core Manager.

1. From the Presets page, click the System Links button.
2. Deselect a Preset name associated with a System.
3. Click Save. "System Links Updated" appears when the Preset has been unlinked from the System.

## Editing and Deleting Presets

[Edit Preset Settings](javascript:void(0))

You can easily edit an existing Preset, regardless of if it is currently applied one or more Systems.

**Tip:** When you edit a Preset, synchronization of Preset settings is automatically paused. This is to avoid pushing updates at inopportune times, such as during busy times of the day or before all changes to the Preset have been completed.

1. From the Presets page, click a Preset name in the list.
2. From the left pane, update and save the new settings for each desired category.
3. From the Presets page, click the System Links buttons.
4. Systems that currently have Presets applied with updated settings are shown with the  (Resume Sync) button. Click the button to sync the updated settings.

[Edit a Preset's Name](javascript:void(0))

1. From the Presets page, select a row containing a Preset name (but do not click the name itself).
2. Click the  button.
3. Specify a new name and click Save.

[Delete a Preset](javascript:void(0))

**CAUTION:** When you delete a Preset, all Systems lose linking with the Preset and its data is deleted from Reflect. Settings and files for the deleted Preset remain on the Q-SYS Core processor, however.

1. From the Presets page, select a row containing a Preset name (but do not click the name itself).
2. Click the  button.
3. Confirm and click Delete.
