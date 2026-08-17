# Access Management > Security

> Source: https://help.qsys.com/Content/Reflect/Core_Management/Security.htm

# Access Management > Security

Use this topic to enable and configure security policies efficiently and promptly. This page is only visible when **Access Control** is turned **On**.

**Note:** Only Administrators have access to this page, the lower Roles do not. Refer to the Roles topic to learn more.

## Sign In

The security settings help maximize system protection and user account integrity by providing configurable options for sign in attempts, session management, and concurrent access control. The following options allow flexibility to safeguard your setup.

Delay between attempts

Allows for a deliberate approach to retries by introducing a brief waiting period. By default, this option is disabled. When enabled, the default delay is 5 seconds. You can choose a delay duration from 1 - 86400 seconds.

Number of failed attempts before lock

Allows you to set the number of consecutive failed sign-in attempts you can make before the account profile is locked. The default value is 6 failed attempts before lockout. This security prevents brute-force attacks by limiting the number of guesses that can be made before being locked out.

Lock profile after the last attempt for

Allows you to limit sign-in attempts. By default, this option is disabled. When enabled, the default is 6 sign-in attempts and a subsequent lockout of 30 minutes. You can specify the number of attempts ranging from 1 - 100 and a lockout duration between 1 â 1440 minutes. During this time, you cannot sign in, even with the correct password. After the lockout period, you can try again. This enforces a âcool-downâ period, which makes it more difficult for hackers to continue guessing passwords.

Session timeout

Allows you to end a userâs session after a specified period of inactivity; the session will expire and the user will be logged out, preventing unauthorized access if a user leaves. An authorized user can simply sign in again to regain access. The default value is 5 minutes of inactivity.

Max concurrent sessions

Allows you to set the number of simultaneous sessions that an account has open with the devicesâsuch as through SSH or HTTPs. For example, if you log into the device from your laptop using a web browser, at the same time from a different computer or browser, this will count as two concurrent sessions for that account. The system can be configured to limit the number of these simultaneous sessions per user account (e.g., to 1, 2, up to 5), and any attempt to exceed this limit will be blocked.

## Password Requirements

Password requirements are rules and criteria that dictate how passwords must be structured and created to enhance security. These requirements often include factors such as password length and complexity (combining letters, numbers, and symbols). They serve to protect accounts and sensitive information by making it more challenging for unauthorized individuals to guess or crack passwords.

The default characters requirement is 8, but can be adjusted to demand up to 100 characters. The following criteria can be implemented:

* At least one uppercase character.
* At least one lowercase character .
* At least one numeric character.
* At least one special character from the following set:

! @ # $ % ^ & \* ( ) , . ? " : { } | < >

* A password cannot contain a user's own username or account name as a substring. For example, if the username is jsmith, do not set the password to jsmith1972 or myjsmithpassword.
* Do not reuse any of your last 4 passwords.

## File Upload Permissions

The security policies implemented enable the restriction of specific file formats when uploading to the Core. These measures are designed to enhance data security by allowing only authorized and safe file types, mitigating potential security risks and data vulnerabilities. There is the option to select **Allow All file types** or specify the desired file types.

The available file formats are categorized into four sections: Files, Audio, Video, and Images, which are listed as follows:

| Files | Audio | Video | Images |
| --- | --- | --- | --- |
| PDF | MP3 | MP4 | JPEG[1](#1.Allowed) |
| DOCX | WAV | AVI | PNG |
| XLSX | FLAC | MKV | GIF |
| PPTX | AAC | MOV | BMP |
| ODT | OGG | MPEG | SVG |
| ODS | AIFF | 3GP | WebP |
| ODP |  |  | RAW |
| TXT |  |  |  |
| JSON |  |  |  |
| EDID[1](#1.Allowed) |  |  |  |

###### 1. Allowed to upload in the Files, Cameras, and Video Endpoints features.

## Reset to Default

Every Security section has a **Reset to Default** option which allows users to restore a setting or configuration to its original, factory-defined state. When this button is clicked or activated, it will undo any changes or customizations that have been made to the setting, reverting it to the standard default configuration.
