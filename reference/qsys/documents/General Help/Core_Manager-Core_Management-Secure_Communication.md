# Network > Secure Communication

> Source: https://help.qsys.com/Content/Core_Manager/Core_Management/Secure_Communication.htm

# Network > Secure Communication

Q-SYS communication between Cores and Peripherals can be secured by encryption and mutual authentication using X.509 certificates. Secure mode of communication applies to two types of connections:

â¢ Control connections â Design controls and other control traffic between cores and peripherals.

â¢ Device-to-device web connections â Operations such as design deploy, firmware update, device status, and other web/API based interactions.

[Mutual Authentication and Trust Management Between Cores and Peripherals](javascript:void(0))

[Mutual Authentication](javascript:void(0))

In secure mode, two devices can communicate securely only if they can mutually authenticate each other:

â¢ Each device must find the peerâs certificate in its trusted list.

â¢ The peer must prove ownership of the private key associated with the certificate it presents.

This mutual authentication is what ensures that both ends of the connection are who they claim to be.

[Automatic and Manual Certificate Management](javascript:void(0))

Q-SYS manages device trust using three lists: Trusted, Pending, and Declined certificates.

**Trusted**

In typical configurations, certificates can be added to the trusted list automatically. By default:

â¢ The Coreâs trusted list includes all peripheral certificates.

â¢ Each Peripheral automatically trusts the Coreâs certificate (or both certificates in a redundant core pair).

This allows cores and peripherals to establish secure communication seamlessly without user intervention.

**Pending**

If automatic trust is not possibleâfor example, because of a configuration or policy restrictionâthe peerâs certificate is placed on the Pending list for manual approval. Once a Peripheralâs trusted list includes at least one certificate, it switches to secure mode and restricts communication to only the associated core (or core pair).

**Declined Certificates**

Certificates that are on, or that chain to one on, the Declined list are denied communication entirely. They are not allowed onto the Pending list and cannot be used to establish secure communication.

In a redundant Core pairs:

â¢ The two Cores must first establish mutual trust with each other.

â¢ After that trust is in place, both Core certificates are shared with Peripherals.

â¢ Peripherals then add both certificates to their trusted lists, allowing them to maintain secure communication if a failover occurs from the primary Core to the backup.

[Prerequisites](javascript:void(0))

1. Update the firmware on all Q-SYS devices to version 10.0 (or higher) to support secure communication.

2. Install the required certificates on the Core and Peripherals. If no new certificates are installed, the currently installed ones will be used. Refer to [Network > Certificates](Certificates.htm) for instructions on installing certificates.

3. Set up Access Control of all Cores and all Peripherals. For more details, see [Access Management > Users](Users.htm)in Core Manager and [Device Password](../../Peripheral_Manager/Device_Password.htm) in Peripheral Manager.

**Note:** Since primary and backup (redundant) Cores automatically sync, ensure Access Control is enabled on the backup Core.

[Configure Trust Options](javascript:void(0))

**Trust On First Usage (TOFU)**

â¢ Peripheral

A Peripheral with TOFU enabled will automatically add a Core's certificate to its trusted list if the list is empty. Once secured, the Peripheral requires manual approval for any new Core certificates via Peripheral Manager.

â¢ Core

The Core adds each Peripheral's certificate to its trusted list automatically. If a Peripheral device is swapped but retains the same name, manual approval for the new certificate is needed through Core Manager.

**Rollover**

Disabled in the Core by default. This option, enabled by default on Peripherals but not on the Core, facilitates automatic replacement of certificates, avoiding need for manual approvals when a certificate is updated.

[Further Secure Your Q-SYS System](javascript:void(0))

1. Disable Non-Authentication-Supporting Networking Services.

Navigate to Network > Services > Managementt and disable the following services:

â¢ Q-SYS External Control Protocol - ASCII

â¢ Q-SYS Remote Control Protocol - JSONRPC

**Note:** Consider certificate expiration by checking the 'Verify Validity Period' to block expired certificates from authenticating.

[Enable Secure Communication](javascript:void(0))

1. Click the Enable Secure Communication button on the Core to initiate secure mode.

[Disable Secure Communication](javascript:void(0))

1. To disable secure communication, click Disable Secure Communication on the Core. The core attempts to withdraw its certificate from the peripherals. By clearing a peripheralâs trusted list, the device reverts to non-secure mode of communication.

2. If some peripherals do not switch to non-secure mode automatically, manually clear their trusted lists. In scenarios where a peripheral trusts devices beyond the current core (or redundant core pair), the current core does not revoke those certificates. You may need to remove trust for that peripheral from other cores as well to maintain consistent security across different Q-SYS setups.

**Note:** If you plan to downgrade the Q-SYS system to firmware that does not support secure communication, ensure that secure mode is disabled on the core and that all peripheral trusted lists are cleared. A core running firmware that does not support secure communication will fail to connect to peripherals still operating in secure mode.

[Verify Secure Connections](javascript:void(0))

1. Ensure secure connections are established between Cores and Peripherals.

â¢ If automatic trust does not apply, review pending certificates and verify their authenticity by comparing fingerprints. See [Network > Certificates](Certificates.htm) for more information.

â¢ To ensure Cores and Peripherals engage in a trusted relationship, visit the Troubleshooting section below.

[Advanced Secure Communication Behaviors and Best Practices](javascript:void(0))

**Behavior in Special Scenarios**

â¢ Once secure mode is activated, you cannot remove the device password without first disabling secure mode.

â¢ Automatic rollover may fail if a device installs a new certificate while its peer is offline. When rollover fails, manual approval of the certificate is required.

â¢ For inter-design communications, manual certificate exchanges are necessary to gain trust.

â¢ In a setup with two Cores where Secure Communication is enabled on only one, if a Peripheral is added to both designs, the core with Secure Communication will establish a connection, while the other core will show Authentication failure.

â¢ Security configuration options are synced between active and backup Cores: you can change the security configuration only on the active core. Trusted lists of certificates are also synced between active and backup cores; only the certificates of the currently running design are exchanged between the cores. At all times, the active Core ensures that trusted Peripherals also trust the backup Core.

**Security Best Practices**

â¢ Disabling both TOFU and Rollover is advised if there is any perceived security threat during deployment.

[Secure Communication Page](javascript:void(0))

The Secure Communication page in the side navigation lets you configure these behaviors and manage certificate trust:

â¢ The Security Options section controls how trust is established and maintained.

â¢ The Trusted Certificates, Pending Certificates, and Declined Certificates tabs show the current trust state for connected devices and let you upload, approve, or decline certificates.

The following sections describe each security option and certificate list in more detail.

Enable Secure Communication Button

Allows administrators to enforce HTTPS and related secure protocols for management traffic.

Security Options

Defines how trust and certificate validation are handled.

â¢ Trust On First Use

Automatically establishes trust with a remote device the first time it connects.

â¢ Rollover

Enables automatic replacement of an existing trusted certificate with the new one.

â¢ Verify Validity Period

Stop trusting devices with expired certificates.

â¢ Control Server Authentication

Requires the client to provide a certificate and verify it against the trusted list.

Certificate Management

Below the security options, there are three tabs for managing certificates:

â¢ Trusted Certificates

Displays certificates that have been accepted and are currently trusted.

â¢ Pending Certificates

Shows certificates awaiting approval.

â¢ Declined Certificates

Lists certificates that were explicitly rejected to communicate with this device.

Upload Certificate Button

Allows you to manually add a certificate to the trusted list. This is useful for preloading certificates before deployment.

Decline Button

Allows you to reject a pending certificate request.

[Troubleshooting Authentication Failures](javascript:void(0))

When devices do not trust each other, a control connection cannot be established. In this case, the device status shows Fault â Authentication Failure. You can examine the Coreâs log for error messages that describe the cause of the authentication failure for each device.

Common causes and resolutions:

**Device password not set**

Secure mode is not available for devices without a user password.

â¢ Ensure Access Control is enabled on both Cores in a redundant pair.

â¢ Verify that all peripherals have a user password set.

**Certificate pending manual approval**

The offered certificate may be on the Pending list in the core or peripheral.

â¢ In Core Manager and Peripheral Manager, review the list of pending certificates.

â¢ Approve the certificate only after confirming that its fingerprint is correct.

**Certificate declined**

The offered certificate may be on the Declined list.

â¢ In Core Manager and Peripheral Manager, review declined certificates.

â¢ Remove any declined certificate that was added by mistake so it can move to Pending or Trusted.

**Certificate expired**

The offered certificate may have expired.

â¢ Regenerate and install a new certificate on the device whose certificate has expired.

**Redundant cores not trusted by each other**

In a redundant system, the two Cores must first trust each other before Peripherals can fully establish trust.

â¢ Verify that primary and backup Core certificates are on each otherâs trusted lists.

â¢ Once mutual trust is established between the Cores, trust establishment with peripherals is unblocked.
