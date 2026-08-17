# SendMailAdvance

Name:

SendMailAdvance

Syntax:

SIGNED_INTEGER SendMailAdvance( STRING Server,

INTEGER PortNumber

STRING UserLogonName,

STRING UserLogonPassword,

STRING From,

STRING To,

STRING CC,

STRING Subject,

STRING Message,

INTEGER NumberOfAttachments,

STRING Attachment )

Description:

Programatically sends an email message to the specified IP address on the specified port using the SMTP protocol.

Parameters:

Server \- Required. Specifies address of the mail server. It can either be an IP address in dot-decimal notation (ex: 192.168.16.3) or a name to be resolved with a DNS server (ex: mail.myisp.com). If a name is given, the control system must be configured with a DNS server (ADDDNS console command). Maximum field length: 40.

PortNumber \- Required. Specifies the port number used to send the email.

UserLogonName \- Optional. Use an empty string in its place if authentication is not required. If the mail server requires authentication, UserLogonName indicates the user name of the sender for the mail server. An empty string indicates that authentication is not required. Only "clear text" authentication is implemented. "Clear text" refers to the authentication method used by the mail server. If the mail server requires a higher level authentication, mail can not be sent to the mail server. Maximum field length: 254.

UserLogonPassword \- Optional. Use an empty string in it's place if not required. If the mail server requires authentication, UserLogonPassword indicates the password of the sender for the mail server. An empty string indicates that authentication is not required. Only "clear text" authentication is implemented. "Clear text" refers to the authentication method used by the mail server. If the mail server requires a higher level authentication, mail can not be sent to the mail server. Maximum field length: 254.

From \- Required. Specifies the e-mail address of the sender in the a@b.com format. Only one email address is allowed. Aliases or nicknames are not supported. This argument is mandatory. Maximum field length: 242.

To \- Required. Specifies the e-mail address of the recipient(s) in the a@b.com format. Multiple recipients may be specified delimited with a ";". This argument is mandatory. Maximum field length: 65535.

CC \- Optional. An empty string indicates that there are no recipients. Specifies the e-mail address of the carbon copy recipient(s) in the a@b.com format. Multiple recipients may be specified delimited with a ";". Maximum field length: 65535.

Subject \- Optional. An empty string indicates that there is no subject. Specifies the subject of the email message. Maximum field length: 989.

Message \- Optional. An empty string indicates an empty message. Specifies the body of the email message. Maximum field length: 65535.

NumberOfAttachments \- Optional. 0 specifies that there are no attachments. Specifies the number of attachments to be sent.

Attachment \- Optional. An empty string indicates that no attachments are to be sent. Specifies the files to be attached. Multiple filenames may be specified, delimited by ';'. Max field length is 65534.

Return Value:

0 if successful. Otherwise, Email Return [Error Code](<Email_Function_Return_Error_Codes.htm>) is returned. Negative return [error codes](<Email_Function_Return_Error_Codes.htm>) indicate that no part of the email was sent (example: user logon password was incorrect). Positive return [error codes](<Email_Function_Return_Error_Codes.htm>) indicate a failure (example: one or more recipient email addresses was invalid), but the email was still sent. In the event of more than one failure, the return [error code](<Email_Function_Return_Error_Codes.htm>) of the first failure is returned.

Example:

SIGNED_INTEGER nErr;

nErr = SendMailAdvance( "192.168.16.3",

80

"UserLogonName",

"UserLogonPassword", 

"SenderEmailAddress@crestron.com",

"RecipientEmailAddress@crestron.com",

"ccEmailAddress@crestron.com",

"This is the subject",

"This is the message",

2,

"\\\CF0\\\test.pdf;\\\CF0\\\test.img" );

if ( nErr < 0 )

Print( "Error sending email\n" );

else

Print( "SendMail successful!\n );

NOTE: If the attachment count is 0 but the "attachment" parameter is not empty, OR if the attachment count is positive, but the "attachment" parameter is empty, an SMTP_INV_PARM error will be returned with the following error in the error log, ""Bad Attachment parameters to SendMail".   
  
NOTE: If the attachment count does not match the number of files in the "attachment" parameter (separated by a delimiter) then the following will happen. If the attachment count parameter is less than the number of files specified in the "attachment" parameter, then the function will attempt to send out valid files specified by the attachment count parameter(INTEGER).  
  
NOTE: If the attachment count parameter is more than the number of files specified in the "attachment" parameter, then the function will attempt to send the valid files specified by the "attachment" parameter(STRING).

Version:

X Generation: Not Supported

2-Series: SIMPL v2.05.17 and later. CUZ 4.001 or later.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Email_Functions/SendMailAdvance.htm*
