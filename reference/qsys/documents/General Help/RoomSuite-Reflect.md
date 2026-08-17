# Reflect

> Source: https://help.qsys.com/Content/RoomSuite/Reflect.htm

# Reflect

Q-SYS Reflect extends RoomSuite beyond the room by providing secure, cloud-based management for all your RoomSuite modular systems. When you connect a RoomSuite modular room to Q-SYS Reflect, the system automatically pushes control and data to the cloud so you can monitor and manage your high performance workplaces from a single interface. Once youâve configured a room to your requirements, you can save those settings as a preset and quickly deploy the same configuration to other RoomSuite modular rooms via the cloud, helping you standardize experiences, simplify large-scale rollouts, and maintain consistency across your meeting spaces.

## Specific Capabilities

Once a RoomSuite Modular System is registered to your Reflect organization and domain, you can take advantage of Reflect features designed for Room Managerâbased rooms, including mass firmware updates and large scale configuration management accessed from Q-SYS Reflect (not from RoomSuite Modular System). For example, you can apply firmware updates across many RoomSuite rooms at once using Mass Firmware Update, and use Mass Deployment and related tools to roll out common RoomSuite presets and room standards to multiple systems from a single Reflect interface. For Q-SYS Reflect information, go to: Q-SYS Reflect [Overview](../Reflect/Reflect_Sites/Overview.htm).

#### Mass Firmware Update for RoomSuite Systems

You can schedule or trigger firmware updates for multiple RoomSuite rooms from a single Reflect interface. This lets you keep the RMP-100 processor and supported RoomSuite endpoints aligned on the firmware version across your deployment, instead of updating each room individually through Room Manager.

#### Mass Deployment of RoomSuite Presets and Standards

You can take a RoomSuite configuration you have already validatedâsuch as a standardized audio layout, camera behavior, and UCI brandingâand roll it out to many rooms at once. For RoomSuite, this means you can treat a tuned room as a template and apply its settings or presets to additional RMS rooms via the cloud, helping you keep room behavior consistent as you scale. For more information on Q-SYS Reflect Presets, go to: [Presets](../Reflect/Reflect_Sites/Presets.htm).

## Reflect Registration

RoomSuite Modular System connects to Reflect through a simple registration process that links local room configurations to enterprise-level management. From RoomSuite Modular System, go to Utilities > Reflect Registration, which securely integrates the device with the corporate network and Reflect Enterprise Manager.

Once registered, the RoomSuite system appears in Reflect as a managed device with a dedicated Preset Type and unique labeling. This ensures Reflect recognizes it as a RoomSuite Modular System, enabling RoomSuite-specific options in the Q-SYS Reflect interface.

#### Register RoomSuite Modular System to Reflect

**Note:** RMP-100's AUX A or AUX B network port should be used to make the internet connection to Reflect.

1. From RoomSuite Modular System, go to Reflect Registration.
2. Verify Access level.

   * Confirm that the Access Level is set to Administrator in the drop-down menu. The system will initiate the process to connect the RoomSuite Modular System to Reflect.
3. Start Registration.

   * Click Start Registration.
4. Test Connection.

   * Use the Test Connection button to verify that the system can communicate with Reflect.
   * If the test fails, check network settings and ensure the device has internet access.
5. Complete Registration.

   * Once the connection is successful, the system will appear in Q-SYS Reflect as a managed device.

### Processor Registration Details

#### Reflect Server Address

Displays the URL of the Reflect server this processor uses for cloud connectivity.

#### Maximum Reflect Access Level

Shows the maximum Reflect role that can be used when managing this processor.

### Reflect Registration Details

#### Organization

Shows the name of the Q SYS Reflect organization that this processor is registered to.

#### Domain

Displays the Reflect domain associated with the registered organization.

#### Registered On

Indicates the date and time when this processor successfully completed registration with Q SYS Reflect.

#### Unregister Button

Removes this processorâs registration from the current Reflect organization and domain. After you unregister, the system stops reporting to Reflect until it is registered again. Local RoomSuite operation in the room is not affected.
