# Important SendMail Considerations  
  
  1. In the SIMPL+ function call to "Send Mail", the parameters "Mailserv", "To" and "From" fields are MANDATORY, whereas "cc", "subject" and "message" are not.

  2. Only the "SMTP AUTH" authentication type with "LOGIN" authentication scheme is supported for now.

  3. Questions for the ISP/e-mail service provider to determine compatibility with the SEND MAIL feature.  




  * Does the ISP/service provider support NON-WEB clients?

  * Does the ISP/service provider support "SMTP AUTH" authentication type with "LOGIN" authentication scheme?

  * For example: the e-mail provider SBC YAHOO supports web as well as non web clients. For non web clients, one of the mail servers to communicate with is SMTPAUTH.FLASH.NET. This mail server supports SMTP AUTH and LOGIN auth scheme.



  4. SEND MAIL client queries the mail server to determine the authentication type and scheme and returns an "unsupported" error (error # -9) if the mail-server does not support LOGIN scheme; however if the client is unable to determine information regarding the schemes supported, it will go ahead and try to send out the e-mail to the intended recipients, but the server may refuse to relay it to external destinations. This will return a "failure" code. (Refer to [Email Function Return Error Codes](<Email_Function_Return_Error_Codes.htm>) )

  5. For mail servers needing no authentication, the "username" and "password" field are set to an EMPTY STRING (""). Again, as in (4) above there is no guarantee that the mail-server will relay the e-mail to external destinations.

  6. In case of an error/failure, the first occurring error/failure code is returned.

  7. If the message line exceeds 998 characters without a <CR-LF> sequence, the SEND MAIL module automatically inserts one.

  8. The "Mail-server" parameter in the SIMPL+ function call to Send Mail can be an IP address, ex. "132.149.6.220" or a name "mail1.Mycompanyname.com". In case of a name, DNS will be used to resolve the name, and the control system must have a DNS server set up.

  9. REMINDER: Strings in SIMPL+ can only be 256 characters long. But internal to SIMPL+ they can be concatenated to a total length of 65536 characters, as long as a SIMPL+ BUFFER_INPUT type is used to accumulate the strings.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Email_Functions/Important_SendMail_Considerations.htm*
