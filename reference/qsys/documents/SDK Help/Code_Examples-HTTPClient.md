# HTTPClient

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/HTTPClient.htm

# HTTPClient

HTTPClient is an object included in the Q-SYS Designer Software's Lua environment for implementing HTTP requests. [Documentation of the HTTPClient extension can be found here.](https://q-syshelp.qsc.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/05a_HttpClient.htm)

The HTTPClient usage allows for GET, POST, and PUT requests over HTTP or HTTPS. This example builds each type of request.

[HTTPClient Usage](javascript:void(0))

```lua
-- Variables  
RequestTimeout = 10            -- Timeout of the connection in seconds  
Host = "https://httpbin.org"   -- HTTP server host name or IP address to use for connection  
IPAddress = "3.211.1.78"       -- IP address can be for host  
Path = "put"                   -- Path within the site to access  
Port = 443                     -- Port to use (if not 80 or 443)  
Username = "admin"             -- Login Data for the http server  
Password = "password"          -- Login Data for the http server  
QueryData = {                  -- Some Data for the http server  
  ["Hello"] = "World",   
  ["Value1"] = 1,   
  ["Ancilliary Data"] = "users/use-weird*characters."  
}  
PostData = "{'Hello':'world', 'Value1':1}"  
  
  
-- Function reads response code, sets status and prints received data.  
function ResponseHandler(tbl, code, data, err, headers)  
  print("HTTP Response Code: " .. code)  
  if code == 200 then  -- Vaild response  
    print("OK")  
    print("Rx: ", data)  
  
  elseif code == 401.0 or IPAddress.String == "" then  -- Invalid Address handler  
    print("MISSING", "Check TCP connection properties")   
  
  else   -- Other error cases  
    print("FAULT", err)   
  end  
end  
  
-- Send an HTTP GET request to the defined  
function GetRequest()  
  -- Define any HTTP headers to sent  
  headers = {  
    ["Content-Type"] = "text/html",  
    ["Accept"] = "text/html"  
  }  
  -- Generate the URL of the request using HTTPClient formatter  
  url = HttpClient.CreateUrl({  
    ["Host"] = Host,  
    ["Port"] = Port,  
    ["Path"] = "get",  
    ["Query"] = QueryData  
  })  
  
  print("Sending GET request to: " .. url.Host)  
  HttpClient.Download({   
    Url          = url,  
    Method       = "GET",  
    Headers      = headers,  
    User         = Username,  -- Only needed if device requires a sign in  
    Password     = Password,  -- Only needed if device requires a sign in  
    Timeout      = RequestTimeout,  
    EventHandler = ResponseHandler  
  })  
end  
  
-- Send a POST request to the HTTP server  
function PostRequest()  
  -- Define any HTTP headers to sent  
  headers = {    
    ["Content-Type"] = "text/html",  
    ["Accept"] = "text/html"  
  }  
  -- Generate the URL of the request using HTTPClient formatter  
  url = HttpClient.CreateUrl({  
    ["Host"] = Host,  
    ["Path"] = "post"  
  })  
  
  print("Sending POST request to: " .. url)  
  HttpClient.Upload({   
    Url          = url,  
    Headers      = headers,  
    User         = Username,  -- Only needed if device requires a sign in  
    Password     = Password,  -- Only needed if device requires a sign in  
    Data         = PostData,  
    Method       = "POST",  
    Timeout      = RequestTimeout,  
    EventHandler = ResponseHandler  
  })  
end  
  
-- Generate a simple put request to an IP Address  
function PutRequest()  
  -- Use the HTTPClient Encoder to format the PostData into an HTTP sendable string (Netscape encoding)  
  data = HttpClient.EncodeString(PostData)  
  
  print("Sending PUT request to: " .. string.format("http://%s/%s", IPAddress, cmd))  
  HttpClient.Upload({   
    Url          = string.format("http://%s/%s", IPAddress, Path), -- This format is an example and is not standard for all devices  
    Data         = data,  
    Method       = "PUT",  
    Timeout      = RequestTimeout,  
    EventHandler = ResponseHandler  
  })  
end
```

* The HttpClient is present by default and does not need to be instantiated. To set up a âGETâ request, a test siteâs information is added to the script, and HttpClient.Download() is used. For PUT and POST requests, HttpClient.Upload is used. HTTPClient supports both HTTP and HTTPS requests â use âhttpsâ in the url instead of âhttpâ.
* HTTPClient.CreateURL() function formats the URL string for the request to be sent to from the input data.
* Username and Password fields are used to access sites that use Basic or Digest Authentication type authentication when used in the Upload or Download commands.
* HttpClient.EncodeString(<string>) and HttpClient.DecodeString(<string>) can be used for handling data in URL Encoding (also known as netscape or percent-encoding).
* HTTPClient.EncodeParams(<table>) encodes a table of [name]=value pairs into URL-encoded data for HTTP messages.

Binding these methods to a plugin framework results in a working plugin that can make GET, PUT or POST commands and display the response to the user:

[HTTPClient Plugin](javascript:void(0))

```lua
-- HTTPClient Example Plugin  
-- by QSC  
-- October 2020  
  
PluginInfo = {  
  Name = "HTTPClient Example Plugin",  
  Version = "0.0",  
  BuildVersion = "0.0.0.1",  
  Id = "0e8bd8f2-ebd9-4e1a-bac7-cbf2541b11b8",  
  Author = "QSC",  
  Description = "An example of HTTPClient usage."  
}  
  
function GetColor(props)  
  return { 102, 102, 102 }  
end  
  
function GetPrettyName(props) --The name that will initially display when dragged into a design  
  return "HTTPCLient Example, ver. " .. PluginInfo.Version  
end  
  
function GetProperties()  
  local props = {}  
  table.insert(props, {  
    Name = "Debug Print",  
    Type = "enum",  
    Choices = {"None", "Tx/Rx", "Tx", "Rx", "Function Calls", "All"},  
    Value = "None"  
  })  
  return props  
end  
  
function RectifyProperties(props)  
  if props.plugin_show_debug.Value == false then   
    props["Debug Print"].IsHidden = true   
  end  
  return props  
end  
  
function GetControls(props)  
  local ctrls = {}  
  table.insert(ctrls, {  
    Name = "Status",  
    ControlType = "Indicator",  
    IndicatorType = "Status",  
    PinStyle = "Output",  
    UserPin = true,  
    Count = 1  
  })  
  table.insert(ctrls, {  
    Name = "SendGet",  
    ControlType = "Button",  
    ButtonType = "Momentary",  
    Count = 1,  
    UserPin = true,  
    PinStyle = "Input"  
  })  
  table.insert(ctrls, {  
    Name = "SendPut",  
    ControlType = "Button",  
    ButtonType = "Momentary",  
    Count = 1,  
    UserPin = true,  
    PinStyle = "Input"  
  })  
  table.insert(ctrls, {  
    Name = "SendPost",  
    ControlType = "Button",  
    ButtonType = "Momentary",  
    Count = 1,  
    UserPin = true,  
    PinStyle = "Input"  
  })  
  table.insert(ctrls, {  
    Name = "ResponseText",  
    ControlType = "Text",  
    Count = 1,  
    UserPin = true,  
    PinStyle = "Output"  
  })  
  return ctrls  
end  
  
function GetControlLayout(props)  
  local layout   = {}  
  local graphics = {}  
  -- Text display  
  table.insert(graphics, {  
    Type = "Header",  
    Text = "HTTP Client Command Test",  
    Position = {5, 5},  
    Size = {295, 16},  
    FontSize = 14,  
    HTextAlign = "Center"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Send GET",  
    Position = {5, 25},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Send POST",  
    Position = {5, 45},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Send PUT",  
    Position = {5, 65},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Status",  
    Position = {5, 85},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
  table.insert(graphics, {  
    Type = "Text",  
    Text = "Response",  
    Position = {5, 105},  
    Size = {95, 16},  
    FontSize = 14,  
    HTextAlign = "Right"  
  })  
    
  --Controls  
  layout["SendGet"] = {  
    PrettyName = "Send GET Request",  
    Legend = "Send",  
    FontSize = 12,  
    Style = "Button",  
    Position = {105, 25},  
    Size = {40, 16}  
  }  
  layout["SendPost"] = {  
    PrettyName = "Send POST Request",  
    Legend = "Send",  
    FontSize = 12,  
    Style = "Button",  
    Position = {105, 45},  
    Size = {40, 16}  
  }  
  layout["SendPut"] = {  
    PrettyName = "Send PUT Request",  
    Legend = "Send",  
    FontSize = 12,  
    Style = "Button",  
    Position = {105, 65},  
    Size = {40, 16}  
  }  
  layout["Status"] = {  
    PrettyName = "Connection Status",   
    Position = {105, 85},   
    Size = {200, 16}  
  }  
  layout["ResponseText"] = {  
    PrettyName = "Data",  
    Position = {105, 105},   
    Size = {200, 64},  
    HTextAlign = "Left"  
  }  
  return layout, graphics  
end  
  
--Start event based logic  
if Controls then  
  -- Aliases  
  Status = Controls.Status  
  SendGet = Controls.SendGet  
  SendPost = Controls.SendPost  
  SendPut = Controls.SendPut  
  ResponseText = Controls.ResponseText  
    
  -- Constants  
  StatusState = { OK = 0, COMPROMISED = 1, FAULT = 2, NOTPRESENT = 3, MISSING = 4, INITIALIZING = 5}  -- Status states in designer  
    
  -- Variables  
  RequestTimeout = 10            -- Timeout of the connection in seconds  
  Host = "https://httpbin.org"   -- HTTP server host name or IP address to use for connection  
  IPAddress = "3.211.1.78"       -- IP address can be for host  
  Path = "put"                   -- Path within the site to access  
  Port = 443                     -- Port to use (if not 80 or 443)  
  Username = "admin"             -- Login Data for the http server  
  Password = "password"          -- Login Data for the http server  
  QueryData = {                  -- Some Data for the http server  
    ["Hello"] = "World",   
    ["Value1"] = 1,   
    ["Ancilliary Data"] = "users/use-weird*characters."  
  }  
  PostData = "{'Hello':'world', 'Value1':1}"  
    
  --Debug level  
  DebugTx,DebugRx,DebugFunction = false, false, false  
  DebugPrint = Properties["Debug Print"].Value  
  if DebugPrint=="Tx/Rx" then  
    DebugTx,DebugRx=true,true  
  elseif DebugPrint=="Tx" then  
    DebugTx=true  
  elseif DebugPrint=="Rx" then  
    DebugRx=true  
  elseif DebugPrint=="Function Calls" then  
    DebugFunction=true  
  elseif DebugPrint=="All" then  
    DebugTx,DebugRx,DebugFunction=true,true,true  
  end  
    
  -- Functions  
  -- Function that sets plugin status  
  function ReportStatus(state, msg)  
    if DebugFunction then print("ReportStatus() called:" .. state) end  
    local msg = msg or ""  
    Status.Value = StatusState[state]  -- Sets status state  
    Status.String = msg  -- Sets status message  
  end  
    
  -- Function reads response code, sets status and prints received data.  
  function ResponseHandler(tbl, code, data, err, headers)  
    if DebugFunction then print("HTTP Response Handler called") end  
    if DebugRx then print("HTTP Response Code: " .. code) end  
    if code == 200 then  -- Vaild response  
      ReportStatus("OK")  
      if DebugRx then print("Rx: ", data) end  
      ResponseText.String = data  
    
    elseif code == 401.0 or IPAddress.String == "" then  -- Invalid Address handler  
      ReportStatus("MISSING", "Check TCP connection properties")   
    
    else   -- Other error cases  
      ReportStatus("FAULT", err)   
    end  
  end  
    
  -- Send an HTTP GET request to the defined  
  function GetRequest()  
    if DebugFunction then print("GetRequest() called") end  
    -- Define any HTTP headers to sent  
    headers = {  
      ["Content-Type"] = "text/html",  
      ["Accept"] = "text/html"  
    }  
    -- Generate the URL of the request using HTTPClient formatter  
    url = HttpClient.CreateUrl({  
      ["Host"] = Host,  
      ["Port"] = Port,  
      ["Path"] = "get",  
      ["Query"] = QueryData  
    })  
    
    if DebugTx then print("Sending GET request: " .. url) end  
    HttpClient.Download({   
      Url          = url,  
      Method       = "GET",  
      Headers      = headers,  
      User         = Username,  -- Only needed if device requires a sign in  
      Password     = Password,  -- Only needed if device requires a sign in  
      Timeout      = RequestTimeout,  
      EventHandler = ResponseHandler  
    })  
  end  
    
  -- Send a POST request to the HTTP server  
  function PostRequest()  
    if DebugFunction then print("PostRequest() called") end  
    -- Define any HTTP headers to sent  
    headers = {    
      ["Content-Type"] = "text/html",  
      ["Accept"] = "text/html"  
    }  
    -- Generate the URL of the request using HTTPClient formatter  
    url = HttpClient.CreateUrl({  
      ["Host"] = Host,  
      ["Path"] = "post"  
    })  
    
    if DebugTx then print("Sending POST request to: " .. url, PostData) end  
    HttpClient.Upload({   
      Url          = url,  
      Headers      = headers,  
      User         = Username,  -- Only needed if device requires a sign in  
      Password     = Password,  -- Only needed if device requires a sign in  
      Data         = PostData,  
      Method       = "POST",  
      Timeout      = RequestTimeout,  
      EventHandler = ResponseHandler  
    })  
  end  
    
  -- Generate a simple put request to an IP Address  
  function PutRequest()  
    if DebugFunction then print("PutRequest() called") end  
    -- Use the HTTPClient Encoder to format the PostData into an HTTP sendable string (Netscape encoding)  
    data = HttpClient.EncodeString(PostData)  
    
    if DebugTx then print("Sending PUT request to: " .. string.format("http://%s/%s", IPAddress, Path), data) end  
    HttpClient.Upload({   
      Url          = string.format("http://%s/%s", IPAddress, Path), -- This format is an example and is not standard for all devices  
      Data         = data,  
      Method       = "PUT",  
      Timeout      = RequestTimeout,  
      EventHandler = ResponseHandler  
    })  
  end  
    
  -- Control Event Handler Binding  
  SendGet.EventHandler = GetRequest    
  SendPost.EventHandler = PostRequest   
  SendPut.EventHandler = PutRequest   
end
```
