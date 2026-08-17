# HttpClient

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/HttpClient.htm

# HttpClient

Use the following methods to add URL references to your Lua script. Transfer data over a secure HTTP connection, or encode and decode a URL, parameters, and string data into a valid ASCII format without spaces.

**Tip:** Both HTTP and HTTPS are supported. To use HTTPS, prefix the URL with `https://` instead of `http://`. TLS 1.0, 1.1, 1.2, and 1.3 are supported with HTTPS.

[HttpClient.Download](javascript:void(0))

Specify a URL from which to download data.

### Syntax

HttpClient.Download( *table* )

### Arguments

*table* : A comma-separated list of parameters:

**Url =** *string* : The URL to download from.

**Headers =** *table* : A table of headers, (string --> string). If a header has a single value for a given key, it is represented as a string. If there are multiple values for a given key, itâs a table.

**User =** *string* : Username for authenticated sites.

**Password =** *string* : Password for authenticated sites.

**Auth = "any" | "basic" | "digest"** : Set the authorization mode on the HTTP request. This is only used if a User and Password are supplied.

Mode definitions:

"any" â Default. Automatically selects the most secure mode.

"basic" â HTTP Basic authentication. The only method that is in widespread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.

"digest" â HTTP Digest authentication. Digest authentication is defined in RFC 2617 and is a more secure way to do authentication over public networks than the Basic method.

**Timeout =** *number* : The timeout, in seconds, for the HttpClient call.

**EventHandler =** *function* : EventHandler to call with status. Signature is function( table, code, data, error, headers ). 'code' is the http return code (200 is good).

### Example

Get a web page and show the return code, the page source, all headers, and any errors in the debug window after a 30 second timeout.

```lua
function done(tbl, code, data, err, headers)  
  print(string.format( "HTTP response from '%s': Return Code=%i; Error=%s", tbl.Url, code, err or "None" ) )  
  print("Headers:")  
  for hName,Val in pairs(headers) do  
    if type(Val) == "table" then  
      print(string.format( "\t%s : ", hName ))   
      for k,v in pairs(Val) do  
        print(string.format( "\t\t%s", v ) )  
      end  
    else  
      print(string.format( "\t%s = %s", hName, Val ) )  
    end   
  end  
  print( "\rHTML Data: "..data )  
end  
HttpClient.Download { Url = "http://www.google.com", Headers = { ["Content-Type"] = "application/json" } , Timeout = 30, EventHandler = done }
```

[HttpClient.Upload](javascript:void(0))

Specify a URL to which to upload data.

### Syntax

HttpClient.Upload( *table* )

### Arguments

*table* : A comma-separated list of parameters:

**Url =** *string* : The URL to upload to.

**Headers =** *table* : A table of headers, (string --> string)

**User =** *string* : Username for authenticated sites.

**Password =** *string* : Password for authenticated sites.

**Auth = "any" | "basic" | "digest"** : Set the authorization mode on the HTTP request. This is only used if a User and Password are supplied.

Mode definitions:

"any" â Default. Automatically selects the most secure mode.

"basic" â HTTP Basic authentication. The only method that is in widespread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.

"digest" â HTTP Digest authentication. Digest authentication is defined in RFC 2617 and is a more secure way to do authentication over public networks than the Basic method.

**Data =** *string* : Data string to upload.

**Method =** **POST** | **PUT** | **PATCH** : The method for uploading.

**Timeout =** *number* : The timeout, in seconds, for the HttpClient call.

**EventHandler =** *function* : EventHandler to call with status. Signature is function( table, code, data, error, headers ). 'code' is the http return code (200 is good).

### Examples

[Example 1: Send Post data to a web site (Henry's Post Test Server V2)](javascript:void(0))

```lua
URL = Controls.URL  
post = Controls.Post  
TestID = Controls.TestID  
  
function done(tbl, code, d, e)  
  print( string.format("Response Code: %i\t\tErrors: %s\rData: %s",code, e or "None", d))  
end  
  
function Upload()  
  local BaseURL = string.format("https://ptsv2.com/t/%s",TestID.String)  
  print(string.format("Go to "..BaseURL.." to view the dump information"))  
  HttpClient.Upload {  
    Url = BaseURL.."/post",  
    Method = "POST", -- Can be either POST, PUT, or PATCH. For PATCH, set Custom here, then define below  
    -- Custom = âPATCHâ  
    User = "user123", -- Used only for Basic or Digest Authentication  
    Password = "mypassword", -- Used only for Basic or Digest Authentication  
    Data = "this is a test", -- This can be anything  
    Headers = {  
      ["Content-Type"] = "text/html",  
      Larry = "another larry",  
      Authentication = "If it is here, it isn't Basic or Digest authentication"  
    },  
    EventHandler = done -- The function to call upon response  
  }  
end  
  
post.EventHandler = Upload
```

[Example 2: Send Post data with the Auth option](javascript:void(0))

```lua
HttpClient.Upload {  
    Url = "https://some.web.site/",  
    Method = "POST",  
    User = user,  
    Password = token,  
    Auth = "basic",  
    Headers = {  
     ["Content-Type"] = "application/json"  
    },  
    Data = qsc_json.encode(data),  
    EventHandler = function(a,b,c)  
      print(a,b,c)  
  }  
end
```

[HttpClient.CreateUrl](javascript:void(0))

Combine URL components into a complete encoded URL string.

### Syntax

HttpClient.CreateUrl( *table* )

### Arguments

*table* : A comma-separated list of parameters containing, at minimum, a URL name. Optionally specify a port, path, and query. See the example for proper syntax.

**Host =** "*url\_name*"

**Port =** *url\_port*

**Path =** *"url\_path*"

**Query =** "*url\_query*"

### Example

```lua
print( HttpClient.CreateUrl( { Host =  "http://www.go.com" } ))   
=> http://www.go.com  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Port = 1234 } ))  
=> http://www.go.com:1234  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Path = "this/is/a/path" } ))  
=> http://www.go.com:1234/this/is/a/path  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Port = 1234, Path = "this/is/a/path" } ))  
=> http://www.go.com:1234/this/is/a/path  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Path = "this/is/a/path with space" } ))  
=> http://www.go.com/this/is/a/path%20with%20space  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Path = "this/is/a/path with space", Query = { sky = "blue" }}))  
=> http://www.go.com/this/is/a/path%20with%20space?sky=blue  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Path = "this/is/a/path with space", Query = { sky = "blue", term = "hellothere" }}))  
=> http://www.go.com/this/is/a/path%20with%20space?sky=blue&term=hellothere  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Path = "this/is/a/path with space", Query = { sky = "blue", term = "hello | there" }}))  
=> http://www.go.com/this/is/a/path%20with%20space?sky=blue&term=hello%20%7c%20there  
  
print( HttpClient.CreateUrl( { Host =  "http://www.go.com", Path = "this/is/a/path with space", Query = { ["name with space"] = "blue", term = "hello | there" }}))  
=> http://www.go.com/this/is/a/path%20with%20space?term=hello%20%7c%20there&name%20with%20space=blue
```

[HttpClient.EncodeParams](javascript:void(0))

Specify a comma-separated list of parameters to encode.

### Syntax

HttpClient.EncodeParams( *table* )

### Arguments

*table* : A comma-separated list of parameters to encode. See the example for proper syntax.

### Example

```lua
print( HttpClient.EncodeParams( { ["name with space"] = "blue", term = "hello | there" }))  
=> term=hello%20%7c%20there&name%20with%20space=blue
```

[HttpClient.EncodeString](javascript:void(0))

Specify a string to encode.

### Syntax

HttpClient.EncodeString( *string* )

### Arguments

*string* : The string to encode.

### Example

```lua
print( HttpClient.EncodeString( "this is | some test"))  
=> this%20is%20%7c%20some%20test
```

[HttpClient.DecodeString](javascript:void(0))

Specify an encoded string to decode.

### Syntax

HttpClient.DecodeString( *string* )

### Arguments

*string* : The encoded string to decode.

### Example

```lua
print( HttpClient.DecodeString("this%20is%20%7c%20some%20test"))  
=> this is | some test
```

[HttpClient.Get](javascript:void(0))

Retrieves data from the URL specified in <table> using the GET request method.

### Syntax

HttpClient.Get( *table* )

### Arguments

*table* : A comma-separated list of parameters:

**Url =** *string* : The URL to download from.

**Headers =** *table* : A table of headers, (string --> string). If a header has a single value for a given key, it is represented as a string. If there are multiple values for a given key, itâs a table.

**User =** *string* : Username for authenticated sites.

**Password =** *string* : Password for authenticated sites.

**Auth = "any" | "basic" | "digest"** : Set the authorization mode on the HTTP request. This is only used if a User and Password are supplied.

Mode definitions:

"any" â Default. Automatically selects the most secure mode.

"basic" â HTTP Basic authentication. The only method that is in widespread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.

"digest" â HTTP Digest authentication. Digest authentication is defined in RFC 2617 and is a more secure way to do authentication over public networks than the Basic method.

**Timeout =** *number* : The timeout, in seconds, for the HttpClient call.

**EventHandler =** *function* : EventHandler to call with status. Signature is function( table, code, data, error, headers ). 'code' is the http return code (200 is good).

### Example

```lua
function done(tbl, code, data, err, headers)  
  print(string.format( "HTTP response from '%s': Return Code=%i; Error=%s", tbl.Url, code, err or "None" ) )  
  print("Headers:")  
  for hName,Val in pairs(headers) do  
    if type(Val) == "table" then  
      print(string.format( "\t%s : ", hName ))   
      for k,v in pairs(Val) do  
        print(string.format( "\t\t%s", v ) )  
      end  
    else  
      print(string.format( "\t%s = %s", hName, Val ) )  
    end   
  end  
  print( "\rHTML Data: "..data )  
end  
HttpClient.Get { Url = "http://www.google.com", Headers = { ["Content-Type"] = "application/json" } , Timeout = 30, EventHandler = done }
```

[HttpClient.Put](javascript:void(0))

Transfers data to the URL specified in <table> using the PUT request method.

### Syntax

HttpClient.Put( *table* )

### Arguments

*table* : A comma-separated list of parameters:

**Url =** *string* : The URL to download from.

**Headers =** *table* : A table of headers, (string --> string). If a header has a single value for a given key, it is represented as a string. If there are multiple values for a given key, itâs a table.

**User =** *string* : Username for authenticated sites.

**Password =** *string* : Password for authenticated sites.

**Auth = "any" | "basic" | "digest"** : Set the authorization mode on the HTTP request. This is only used if a User and Password are supplied.

Mode definitions:

"any" â Default. Automatically selects the most secure mode.

"basic" â HTTP Basic authentication. The only method that is in widespread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.

"digest" â HTTP Digest authentication. Digest authentication is defined in RFC 2617 and is a more secure way to do authentication over public networks than the Basic method.

**Data =***string* : Data string to upload.

**Timeout =** *number* : The timeout, in seconds, for the HttpClient call.

**EventHandler =** *function* : EventHandler to call with status. Signature is function( table, code, data, error, headers ). 'code' is the http return code (200 is good).

### Example

```lua
function done(tbl, code, d, e)  
  print( string.format("Response Code: %i\t\tErrors: %s\rData: %s",code, e or "None", d))  
end  
  
function Put()  
  url = string.format("https://posttestserver.dev/p/ms3mb6ij4bk2y5s8/post")  
  HttpClient.Put{  
    Url = url,  
    Data = "this is a test", -- This can be anything  
    Headers = {  
      ["Content-Type"] = "text/html",  
    },  
    EventHandler = done -- The function to call upon response  
  }  
end  
  
Put()
```

[HttpClient.Post](javascript:void(0))

Transfers data to the URL specified in <table> using the POST request method.

### Syntax

HttpClient.Post( *table* )

### Arguments

*table* : A comma-separated list of parameters:

**Url =** *string* : The URL to download from.

**Headers =** *table* : A table of headers, (string --> string). If a header has a single value for a given key, it is represented as a string. If there are multiple values for a given key, itâs a table.

**User =** *string* : Username for authenticated sites.

**Password =** *string* : Password for authenticated sites.

**Auth = "any" | "basic" | "digest"** : Set the authorization mode on the HTTP request. This is only used if a User and Password are supplied.

Mode definitions:

"any" â Default. Automatically selects the most secure mode.

"basic" â HTTP Basic authentication. The only method that is in widespread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.

"digest" â HTTP Digest authentication. Digest authentication is defined in RFC 2617 and is a more secure way to do authentication over public networks than the Basic method.

**Data =***string* : Data string to upload.

**Timeout =** *number* : The timeout, in seconds, for the HttpClient call.

**EventHandler =** *function* : EventHandler to call with status. Signature is function( table, code, data, error, headers ). 'code' is the http return code (200 is good).

### Example

```lua
function done(tbl, code, d, e)  
  print( string.format("Response Code: %i\t\tErrors: %s\rData: %s",code, e or "None", d))  
end  
  
function Post()  
  url = string.format("https://posttestserver.dev/p/ms3mb6ij4bk2y5s8/post")  
  HttpClient.Post {  
    Url = url,  
    Data = "this is a test", -- This can be anything  
    Headers = {  
      ["Content-Type"] = "text/html",  
    },  
    EventHandler = done -- The function to call upon response  
  }  
end  
  
Post()
```

[HttpClient.Patch](javascript:void(0))

Modifies data at the URL specified in <table> using the PATCH request method.

### Syntax

HttpClient.Patch( *table* )

### Arguments

*table* : A comma-separated list of parameters:

**Url =** *string* : The URL to download from.

**Headers =** *table* : A table of headers, (string --> string). If a header has a single value for a given key, it is represented as a string. If there are multiple values for a given key, itâs a table.

**User =** *string* : Username for authenticated sites.

**Password =** *string* : Password for authenticated sites.

**Auth = "any" | "basic" | "digest"** : Set the authorization mode on the HTTP request. This is only used if a User and Password are supplied.

Mode definitions:

"any" â Default. Automatically selects the most secure mode.

"basic" â HTTP Basic authentication. The only method that is in widespread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.

"digest" â HTTP Digest authentication. Digest authentication is defined in RFC 2617 and is a more secure way to do authentication over public networks than the Basic method.

**Data =***string* : Data string to upload.

**Timeout =** *number* : The timeout, in seconds, for the HttpClient call.

**EventHandler =** *function* : EventHandler to call with status. Signature is function( table, code, data, error, headers ). 'code' is the http return code (200 is good).

### Example

```lua
function done(tbl, code, d, e)  
  print( string.format("Response Code: %i\t\tErrors: %s\rData: %s",code, e or "None", d))  
end  
  
function Patch()  
  url = string.format("https://posttestserver.dev/p/ms3mb6ij4bk2y5s8/post")  
  HttpClient.Patch{  
    Url = url,  
    Data = "this is a test", -- This can be anything  
    Headers = {  
      ["Content-Type"] = "text/html",  
    },  
    EventHandler = done -- The function to call upon response  
  }  
end  
  
Patch()
```

[HttpClient.Delete](javascript:void(0))

Modifies data at the URL specified in <table> using the DELETE request method.

### Syntax

HttpClient.Delete( *table* )

### Arguments

*table* : A comma-separated list of parameters:

**Url =** *string* : The URL to download from.

**Headers =** *table* : A table of headers, (string --> string). If a header has a single value for a given key, it is represented as a string. If there are multiple values for a given key, itâs a table.

**User =** *string* : Username for authenticated sites.

**Password =** *string* : Password for authenticated sites.

**Auth = "any" | "basic" | "digest"** : Set the authorization mode on the HTTP request. This is only used if a User and Password are supplied.

Mode definitions:

"any" â Default. Automatically selects the most secure mode.

"basic" â HTTP Basic authentication. The only method that is in widespread use and supported virtually everywhere. This sends the user name and password over the network in plain text, easily captured by others.

"digest" â HTTP Digest authentication. Digest authentication is defined in RFC 2617 and is a more secure way to do authentication over public networks than the Basic method.

**Timeout =** *number* : The timeout, in seconds, for the HttpClient call.

**EventHandler =** *function* : EventHandler to call with status. Signature is function( table, code, data, error, headers ). 'code' is the http return code (200 is good).

### Example

```lua
function done(tbl, code, d, e)  
  print( string.format("Response Code: %i\t\tErrors: %s\rData: %s",code, e or "None", d))  
end  
  
function Delete()  
  url = string.format("https://posttestserver.dev/p/ms3mb6ij4bk2y5s8/post")  
  HttpClient.Delete{  
    Url = url,  
    Headers = {  
      ["Content-Type"] = "text/html",  
    },  
    EventHandler = done -- The function to call upon response  
  }  
end  
  
Delete()
```

Portions of this topic are reprinted under permission of the [HttpClient](../../Legal.htm#HttpClie) license.
