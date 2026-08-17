# Email

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Email.htm

# Email

Similar to the [E-mailer](../../Schematic_Library/email.htm) component, the Email library allows creation of emails directly from a Lua script.

**Note:** Messages can be a maximum of 16 KB in size.

## Email.Send

Send an email using specified parameters.

### Syntax

Email.Send ( *table* )

### Arguments

*table* : A table containing the details of the email to be sent. Use these parameters:

| Parameter | Type |
| --- | --- |
| From | string |
| Subject | string |
| Body | string |
| To | array of strings |
| CC | array of strings |
| Server | string |
| Username[1](#username) | string |
| Password | string |
| EventHandler | function to call with status, signature is 'function( table, error ),' where 'table' is the table passed into Send and 'error' is a string (if error occurred) or nil. |

**Note:** The Email library always attempts to use Secure Sockets Layer (SSL), if available.

### Example

```lua
Email.Send  
{  
  To = { "somebody@somecompany.com" },  
  From = "myemail@mycompany.com",  
  Subject = "the date should be correct...",  
  Body = "just testing email out, will this work??",  
  EventHandler = function(t, err)  
    if err then print( "ERROR", err )  
    else print( "ALL GOOD!" ) end  
    end,  
  Server = "smtp.mycompany.com",  
  Username = "username",  
  Password = "<XXXXXXXX>"  
}
```

###### 1. If a 'Username' is not specified, it will be taken from the 'From' field.
