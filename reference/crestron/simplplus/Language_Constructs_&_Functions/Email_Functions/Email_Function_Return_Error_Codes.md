# Email Function Return Error Codes

SMTP_OK |  0 |  Success  
---|---|---  
|  |   
SMTP ERRORS  
(NON-RECOVERABLE ERRORS) |   
Error |  Description  
SMTP_ERROR_FATAL |  -1 |  Any non-recoverable error from the e-mail module of the firmware (for example: if “mailserver”, “from” and “to” are empty).  
SMTP_ERROR_ILLEGAL_CMD |  -2 |  General internal error.  
SMTP_ERROR_CONNECT |  -3 |  Failure to connect to the mailserver.  
SMTP_ERROR_SEND |  -4 |  Internal error while actually sending out e-mail.  
SMTP_ERROR_RECV |  -5 |  Internal error while actually receiving out e-mail.  
SMTP_ERROR_NU_CONNECT |  -6 |  Internal error while processing the send.  
SMTP_ERROR_NU_BUFFERS |  -7 |  Lack of memory buffers while processing send or receive mail. Internal error.  
SMTP_ERROR_AUTHENTICATION |  -8 |  Authentication failure.  
SMTP_ERROR_AUTH_LOGIN_UNSUPPORTED |  -9 |  CLEAR TEXT login scheme is not supported.  
SMTP_INV_PARAM  |  -10 |  Bad parameters to SendMail. Must supply Server, From, and To.  
SMTP_ETHER_NOT_ENABLED |  -11 |  Ethernet not enabled. Cannot send mail.  
SMTP_NO_SERVER_ADDRESS |  -12 |  No DNS servers configured. Cannot resolve name.  
SMTP_SEND_FAILURE  |  -13 |  SendMail failed.  
|  |   
SMTP FAILURES  
(RECOVERABLE ERRORS) |   
Error |  Description  
IDS_SMTP_FAILURE_MAIL_COMMAND |  2 |  There was an error sending e-mail with the "from" recipient.  
SMTP_FAILURE_TO_RCPT_COMMAND |  3  |  There was an error sending e-mail to the “to” recipient.  
SMTP_FAILURE_CC_RCPT_COMMAND |  4 |  There was an error sending e-mail to the “CC” recipient.  
SMTP_FAILURE_DATA_COMMAND |  5 |  There was an error sending the message body.  
SMTP_FAILURE_ATTACHMENT_OPEN  |  6 |  Unable to open attachment file  
  
[Related Topics](<javascript:void\(0\);>)

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Email_Functions/Email_Function_Return_Error_Codes.htm*
