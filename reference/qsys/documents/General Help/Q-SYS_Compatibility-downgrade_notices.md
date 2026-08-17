# Downgrade Notices

> Source: https://help.qsys.com/Content/Q-SYS_Compatibility/downgrade_notices.htm

# Downgrade Notices

To ensure a smooth firmware downgrade, follow the specified downgrade path in order, until the desired firmware version is reached. Skipping steps may cause errors or loss of functionality. See the Downgrading Paths section below.

[Downgrade Notice for Core 8 Flex and Core Nano Units](javascript:void(0))

Core 8 Flex and Core Nano units with the i226-LM LAN controller cannot be downgraded below v9.12.

[Downgrade Notice for NC Cameras (Firmware 10.1+)](javascript:void(0))

Version 10.0 is required as a downgrade bridge because it safely transitions the camera's internal state and files from the new format (10.0+) back to the old format (pre-10.0), preventing firmware corruption and upgrade loops. Skipping version 10.0 when downgrading can leave the camera in a firmware loop, bricked, or in a compromised state, with lost settings and failed downgrade attempts. Always use 10.0 as a bridge to ensure a safe and supported downgrade path.

As a result, cameras running firmware version 10.1 or later cannot be directly downgraded to any firmware version earlier than version 10.0. To downgrade a camera from 10.1 (or higher) to a pre-10.0 version, you must first downgrade to version 10.0, then downgrade again to the desired pre-10.0 version.

Required Downgrade Path:

10.1+ â 10.0 â pre-10.0

## Downgrading Paths

[Step 1: Downgrading form Version 10.2 to 10.1](javascript:void(0))

When downgrading from version 10.2 to 10.1, the initial firmware package is transferred, and the Core will reboot. After the reboot is complete, manually re-push the design to finish the downgrade process.

[Step 2: Downgrading from Version 10.1 to 10.0](javascript:void(0))

When downgrading from version 10.1 to 10.0, the initial firmware package is transferred, and the Core will reboot. After the reboot is complete, manually re-push the design to finish the downgrade process.

[Step 3: Downgrading from Version 10.0 to 9.13.x](javascript:void(0))

When downgrading from version 10.0 to 9.13.x, the initial firmware package is transferred, and the Core will reboot. After the reboot is complete, manually re-push the design to finish the downgrade process.

[Step 4: Downgrading from Version 9.13.x to 9.10.x](javascript:void(0))

To downgrade from 9.13.x to 9.10.x, it is essential to check the "Allow old authentication method for Q-SYS Designer" box in Core Manager. This ensures compatibility with version 9.10.x.

[Step 5: Downgrading from Version 9.10.x to 9.4.x](javascript:void(0))

Proceed with the downgrade to version 9.4.x without additional requirements. Access Control will be disabled and User Accounts will be lost.

**Note:**  Core 8 Flex or Core Nano units with serial numbers starting with 21TW2419400001 or 21MX2420300117 (or blue network ports) use an upgraded LAN controller. To avoid network communication problems or instability with Q-LAN, Dante, or AES67, do not downgrade these upgraded units to a version earlier than v9.10.x. If you have already downgraded, we recommend upgrading the firmware back to version 9.10 or later.

[Step 6: Downgrading from Version 9.4.x to 9.0.x](javascript:void(0))

When downgrading to version 9.0.x, it is essential to check the "Allow Legacy Unsigned Firmware (9.0.1 or lower)" box in Core Manager to ensure the system functions correctly.

[Step 7: Downgrading to Versions Prior to 9.0.x](javascript:void(0))

Follow the standard downgrade procedures for versions earlier than 9.0.x.
