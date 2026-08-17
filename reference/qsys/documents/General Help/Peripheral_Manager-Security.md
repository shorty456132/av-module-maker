# Security

> Source: https://help.qsys.com/Content/Peripheral_Manager/Security.htm

# Security

Use this topic to enable and configure security policies efficiently and promptly.

## Sign In

The security settings help maximize system protection and user account integrity by providing configurable options for sign in attempts, session management, and concurrent access control. The following options allow flexibility to safeguard your setup.

Delay between attempts

Allows for a deliberate approach to retries by introducing a brief waiting period. By default, this option is disabled. When enabled, the default delay is 1 second. You can choose a delay duration from 1 - 3600 seconds.

Number of failed attempts before lock

Allows you to set the number of consecutive failed sign-in attempts you can make before the account profile is locked. The default value is 5 failed attempts before lockout. This security prevents brute-force attacks by limiting the number of guesses that can be made before being locked out.

Lock profile after the last attempt for

Allows you to limit sign-in attempts. By default, this option is disabled. When enabled, the default is 5 sign-in attempts and a subsequent lockout of 2 minutes. You can specify the number of attempts ranging from 1 - 100 and a lockout duration between 1 â 1440 minutes. During this time, you cannot sign in, even with the correct password. After the lockout period, you can try again. This enforces a âcool-downâ period, which makes it more difficult for hackers to continue guessing passwords.

Session timeout

Allows you to end a userâs session after a specified period of inactivity; the session will expire and the user will be logged out, preventing unauthorized access if a user leaves. An authorized user can simply sign in again to regain access. The default value is 5 minutes of inactivity.

Max concurrent sessions

Allows you to set the number of simultaneous sessions that an account has open with the devices. For example, if you log into the device from your laptop using a web browser, at the same time from a different computer or browser, this will count as two concurrent sessions for that account. The system can be configured to limit the number of these simultaneous sessions per user account (e.g., to 1, 2, up to 5), and any attempt to exceed this limit will be blocked.

## Password Requirements

Password requirements are rules and criteria that dictate how passwords must be structured and created to enhance security. These requirements often include factors such as password length and complexity (combining letters, numbers, and symbols). They serve to protect accounts and sensitive information by making it more challenging for unauthorized individuals to guess or crack passwords.

The default characters requirement is 8, but can be adjusted to demand up to 128 characters. The following criteria can be implemented:

* At least one uppercase character.
* At least one lowercase character .
* At least one numeric character.
* At least one special character from the following set:

! @ # $ % ^ & \* ( ) , . ? " : { } | < >

* A password cannot contain a user's own username or account name as a substring. For example, if the username is jsmith, do not set the password to jsmith1972 or myjsmithpassword.
* Disallow reuse of your last 4 passwords.
* Disallow resuse of 4 consecutive characters.
