# SendMail

Name:

SendMail

Syntax:

SIGNED_INTEGER SendMail( STRING Server,

STRING UserLogonName,

STRING UserLogonPassword,

STRING From,

STRING To,

STRING CC,

STRING Subject,

STRING Message )

Description:

Send an email message using SMTP protocol.

Parameters:

Server \- Required. Specifies address of the mail server. It can either be an IP address in dot-decimal notation (ex: 192.168.16.3) or a name to be resolved with a DNS server (ex: mail.myisp.com). If a name is given, the control system must be configured with a DNS server (ADDDNS console command). Maximum field length: 40.

UserLogonName \- Optional, but use an empty string in its place if authentication is not required. If the mail server requires authentication, UserLogonName indicates the user name of the sender for the mail server. An empty string indicates that authentication is not required. Only "clear text" authentication is implemented. "Clear text" refers to the authentication method used by the mail server. If the mail server requires a higher level authentication, mail can not be sent to the mail server. Maximum field length: 254.

UserLogonPassword \- Optional, but put an empty string in it's place if not required. If the mail server requires authentication, UserLogonPassword indicates the password of the sender for the mail server. An empty string indicates that authentication is not required. Only "clear text" authentication is implemented. "Clear text" refers to the authentication method used by the mail server. If the mail server requires a higher level authentication, mail can not be sent to the mail server. Maximum field length: 254.

From \- Required. Specifies the e-mail address of the sender in the a@b.com format. Only one email address is allowed. Aliases or nicknames are not supported. This argument is mandatory. Maximum field length: 242.

To \- Required. Specifies the e-mail address of the recipient(s) in the a@b.com format. Multiple recipients may be specified delimited with a ";". This argument is mandatory. Maximum field length: 65535.

CC \- Optional, but use an empty string to indicate that there are no recipients. Specifies the e-mail address of the carbon copy recipient(s) in the a@b.com format. Multiple recipients may be specified delimited with a ";". Maximum field length: 65535.

Subject \- Optional, but use an empty string to indicate that there is no subject. Specifies the subject of the email message. Maximum field length: 989.

Message \- Optional, but use an empty string to indicate an empty message. Specifies the body of the email message. Maximum field length: 65535.

Return Value:

0 if successful. Otherwise, [Email Return Error Code](<Email_Function_Return_Error_Codes.htm>) is returned. Negative return error codes indicate that no part of the email was sent (example: user logon password was incorrect). Positive return error codes indicate a failure (example: one or more recipient email addresses was invalid), but the email was still sent. In the event of more than one failure, the return error code of the first failure is returned.

Example:

SIGNED_INTEGER nErr;

nErr = SendMail( "192.168.16.3",

"UserLogonName",

"UserLogonPassword", 

"SenderEmailAddress@crestron.com",

"RecipientEmailAddress@crestron.com",

"ccEmailAddress@crestron.com",

"This is the subject",

"This is the message" );

if ( nErr < 0 )

Print( "Error sending email\n" );

else

Print( "SendMail successful!\n );

Version:

X Generation: Not Supported

2-Series: SIMPL v2.03.18 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Email_Functions/SendMail.htm*
