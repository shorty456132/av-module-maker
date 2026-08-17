# Getting Started with Reflect

> Source: https://help.qsys.com/Content/Reflect/Reflect_Sites/Getting_Started.htm

# Getting Started with Reflect

It's easy to get yourself and your Q-SYS system registered with [Q-SYS Reflect](../reflect_overview.htm)!

* If you will be the Administrator for your Q-SYS Reflect Organization, go to [qsc.com/reflect](https://www.qsc.com/reflect) to begin the process of starting an Q-SYS Reflect trial or purchasing a subscription. Then, proceed to the first section below.
* If you have been designated as a [Technical Contact Technical Contacts can manage the connection of Q-SYS Cores and use Q-SYS Reflect to manage and monitor Q-SYS systems.](javascript:void(0)) or [Billing Contact Billing Contacts can access the Reflect Subscription page and can view or manage payment methods as well as view previous payment history.](javascript:void(0)), proceed to [Technical and Billing Contact Initial Sign-Up](#Technica).

**Tip:** Go to [https://uptime.reflect.qsc.com](https://uptime.reflect.qsc.com/) to see the current status of the Q-SYS Reflect servers and see availability percentages and service interruptions over time. You can also set up email notifications based on service downtime.

[Sign In](javascript:void(0))

1. When prompted, sign in with your QSC account. If you do not have a QSC account, click Sign Up Now to create one.
2. After registering your QSC account, you will receive a verification email. Click Confirm my account to verify.

**Note:** QSC accounts must be registered using a business email domain. Generic email domains such as Gmail, Outlook, Hotmail, Yahoo, and AOL are not valid for use with Q-SYS Reflect registration.

[Register with Q-SYS Reflect](javascript:void(0))

1. Specify the number of Systems (Cores) and Peripherals for Q-SYS Reflect to monitor.
2. Select a subscription â Q-SYS Reflect or Q-SYS Reflect Plus. For more information, see [Q-SYS Reflect Subscriptions](Overview.htm#Software).
3. Click Order Now.
4. Provide the required profile, contact information, and payment information to complete the registration. If you have additional Technical contacts or Billing contacts, enter that information. (The contact email domain must be the same as yours.)
5. On the Reflect Subscription page, copy your Subscription ID, and then click Go to Q-SYS Reflect.
6. From the navigation menu, click Organizations > New Organization.
7. Specify an Organization Name (for example, your company name), paste your Subscription ID, and click Create.
8. Select your new Organization from the table. You'll see that your first Domain has automatically been created. Click Rename to give a proper name to your first Domain.

**Tip:** See [Overview](Overview.htm) to learn about the relationship between Organizations, Domain, and Systems.

[Optional: Granting Configuration Access for a Technical Contact](javascript:void(0))

If you added a technical contact to your account during initial registration, this person is granted access to your Reflect Subscription page only. If you would also like this person to have technical access to configure Systems within Q-SYS Reflect, complete these steps:

1. On the Organizations page, click the Invites tab.
2. Click + Invite Owner.
3. Enter your technical contact's email address and provide a custom message.

[Configure Network and Firewall](javascript:void(0))

To ensure proper communication with the Reflect servers, check with your IT administrator to ensure that these network prerequisites are followed.

### Critical URLs

The Q-SYS Core processor uses an outbound connection on port 443 (HTTPS and WSS) to connect with the Q-SYS Reflect cloud. All cloud-facing communication uses HTTPS/TLS (TLS 1.2+). Firewalls should be configured to allow access to these URLs via DNS, not hard-coded IP addresses.

| URL | Purpose |
| --- | --- |
| https://reflect.qsc.com | Reflect web portal and APIs |
| https://ciam.qsc.com | SSO via OIDC/SAML2 federation through CIAM and APIs |
| https://api.sendgrid.com | Email service (for transactional auth emails) |

### DNS, NTP, Proxies

* Reflect services use DNS-based endpoints behind load balancers and CDNs. IPs may change without notice. Do not hardcode IP addresses. Allow outbound 443/TCP to the [Critical URLs](#Critical), and rely on corporate egress policies. Use enterprise DNS with split-horizon, if applicable.
* Steps for enabling DNS on the Core are explained in [Prepare the Q-SYS Core for Monitoring](#Prepare).
* Enable NTP (e.g., time1.google.com, time2.google.com) to avoid token and TLS clock drift issues. Steps for enabling NTP on the Core are explained in [Prepare the Q-SYS Core for Monitoring](#Prepare).
* If a proxy is required, allow HTTPS tunneling and WebSocket over TLS (no TLS inspection).

### Wildcard Rules

Adding these URL rules allow flexibility for different URL variations within Reflect while maintaining restricted access.

* \*.reflect.qsc.com
* reflect.qsc.com/

[Prepare the Q-SYS Core for Monitoring](javascript:void(0))

Before proceeding, open Q-SYS Core Manager by typing the Core's IP address into a web browser.

### Configure Network Settings

Q-SYS Reflect Manager requires that your Q-SYS Core can securely access the Q-SYS Reflect Cloud servers.

1. From the Core Manager menu, click Network Settings > Basic.
2. Click Edit to modify the values. Consult your IT administrator and enter the appropriate IP Address, Net Mask, and Gateway to enable Internet access for the Q-SYS Core.
3. Enable DNS. DNS servers are available from your IT administrator, or you can use public DNS servers such as those provided by Google (8.8.8.8 and 8.8.4.4).
4. Click Save.

For more information, see the [Network > Basic](../Core_Management/Network_Settings.htm) topic.

### Enable Time Synchronization (Recommended)

Time Synchronization helps to ensure that logs across multiple systems can be compared accurately.

1. From the Core Manager menu, click Date & Time.
2. Click Edit.
3. Enable Time Synchronization and specify valid NTP servers. NTP servers are available from your IT administrator, or use time1.google.com and time2.google.com.
4. Click Save.

For more information, see the [Network > Date & Time](../Core_Management/Date_Time.htm) topic.

### Enable Access Control (Recommended)

Access Control enables secure, user name and password authentication for access to Core Manager.

1. From the Core Manager menu, click Users.
2. Click Enable Access Control, and follow the on-screen instructions to create an Administrator user for your Core.
3. Log back into the Core with your new credentials.

For more information, see the [Access Management > Users](../Core_Management/Users.htm) topic.

### Configure Network Services (Recommended)

Disabling unnecessary services on all network interface ports helps to harden the Core from an IT security perspective.

1. From the Core Manager menu, click Network Services.
2. Click the Management tab, and then click Edit.
3. For the LAN interface with Internet access, deselect all services except for Q-SYS Designer Communications - Secure.
4. Click Save.

For more information, see the [Network > Services](../Core_Management/Network_Services.htm) topic.

[Register the Core with Q-SYS Reflect](javascript:void(0))

1. From the Core Manager menu, click Reflect.
2. Click Test Connection to verify that the Core has a valid communication channel to the Reflect servers.

   **Note:** If you see any errors, see this [troubleshooting article](https://support.qsys.com/en_US/troubleshooting/troubleshooting-|-error-when-testing-connection-to-reflect-servers) in the Q-SYS Knowledge Base.
3. Select a Maximum Reflect Access Level. The level you select becomes the highest permitted access level allowed to this Core, regardless of the Q-SYS Reflect user role:

* Administrators can view and modify all Core settings and features, deploy design files, and update Core firmware. They can also launch pin-protected User Control Interfaces (UCIs) without entering a PIN.
* Technicians have the same access as Administrators, but without the ability to manage Core users. They can view Core users, but cannot enable or disable Access Control or create, edit, or remove users.
* Viewers can view all settings and launch PIN-protected UCIs (with the appropriate PIN). They cannot edit any settings, preview audio files from the Files page, or download system information from the Utilities page.

**Note:** Administrators and Technicians can also enable user access for the External Control Protocol and File Management Protocol. These permissions are set in Q-SYS Administrator using separate user PINs specifically for these purposes.

4. Click Start Registration.
5. Click Copy to copy the Authorization Code.
6. Return to Q-SYS Reflect and navigate to the Domain to which you want to add this Core.
7. Click Add Core and paste the Authorization Code.
8. Click Add.

The Core is now registered with the Q-SYS Reflect Organization and Domain.

[Technical and Billing Contact Initial Sign-Up](javascript:void(0))

If your Administrator has designated you as a Technical or Billing Contact, follow these steps.

1. From the invitation email, click Sign In.
2. Sign in with your existing QSC account using the same email from which you received the invitation or, if you do not have a QSC account, click Sign Up Now to create one.

   **Note:** QSC accounts must be registered using a business email domain. Generic domains, such as Gmail, Outlook, Hotmail, Yahoo, and AOL, are not valid for use with Q-SYS Reflect registration.
3. On the MyQSC page, click the Q-SYS Reflect icon. (MyQSC is also accessible at qsc.com/login)
4. On the Subscription page, click Go To Q-SYS Reflect.

If you are a Billing Contact, the initial sign-up is complete. Technical Contacts, proceed to the next step to confirm Domain invitation.

1. From the email inviting you to a Domain (sent from your Administrator), click Accept Invitation.
2. You are redirected to the Q-SYS Reflect dashboard, where your Organization and Domain (to which you were invited) are now visible.
