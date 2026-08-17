# Queue and Stack Classes

> Source: https://q-syshelp.qsc.com/DeveloperHelp/Content/Code_Examples/Queue_and_Stack_class.htm

# Queue and Stack Classes

Queues and Stacks are data storage that allow incremental additions and subtractions. For easy and quick implementation, these classes can be added to your scripts.

[Queue Class](javascript:void(0))

The Queue class uses the colon to access functions. Data is public in this class. In addition to the normal Queue functions, a PushFirst() is included to add to the front of the queue for priority usage. See the Code Example below for specific usage.

[Queue Class Code Example](javascript:void(0))

```lua
--A Simple Queue Class  
Queue = {}  
  
function Queue:New()  
  list = { first = 1, last = 0 }  
  self.__index = self  
  setmetatable(list, self)  
  return list  
end  
  
function Queue:Push(value)  
  self.last = self.last + 1   
  self[self.last] = value  
end  
  
function Queue:PushFirst(value)  
  self.first = self.first - 1   
  self[self.first] = value  
end  
  
function Queue:Pop()  
  if self.first > self.last then   
    error("Queue is empty!")   
  end  
  local value=self[self.first]  
  self[self.first] = nil  
  self.first = self.first + 1  
  return value  
end  
  
function Queue:IndexOf(value)  
  for i=self.first,self.last do  
    if self[i] == value then  
      return i  
    end  
  end  
  return nil  
end  
  
function Queue:Clear()  
  for i=self.first,self.last do  
    self[i] = nil  
  end  
  self.first = 1  
  self.last = 0  
end  
  
function Queue:IsEmpty()  
  return self.first > self.last  
end
```

[Queue Class Signature](javascript:void(0))

| Accessor | Description |
| --- | --- |
| :New() | Returns a new Queue object |
| :Push( value ) | Add a value to the end of the Queue |
| :Pop() | Return a value removed from the front of the queue |
| :PushFirst( value ) | Add a value at the head of the Queue |
| :IndexOf( value ) | Return the index within the Queue of the value, or nil. |
| :Clear() | Remove all data from the Queue |
| :IsEmpty() | Returns false if the Queue contains data, true otherwise |
| .first | Index of the first data in the Queue (oldest) |
| .last | Index of the last data in the Queue (newest) |

[Stack Class](javascript:void(0))

An alternative is a Stack data structure. This code can be used to add a Stack class to Lua code:

[Stack Class](javascript:void(0))

```lua
-- A Simple Stack Class  
Stack = {}  
  
function Stack:New()  
  list = {top = 0}  
  self.__index = self  
  setmetatable(list, self)  
  return list  
end  
  
function Stack:Push(value)  
  self.top = self.top + 1   
  self[self.top] = value  
end  
  
function Stack:Pop()  
  if self.top < 1 then   
    error("Stack is empty!")   
  end  
  local value = self[self.top]  
  self[self.top] = nil  
  self.top = self.top - 1  
  return value  
end  
  
function Stack:IndexOf(value)  
  for i=1,self.top do  
    if self[i] == value then  
      return i  
    end  
  end  
  return nil  
end  
  
function Stack:Clear()  
  for i=1,self.top do  
    self[i] = nil  
  end  
  self.top = 0  
end  
  
function Stack:IsEmpty()  
  return self.top < 1  
end
```

Similar to the Queue functionality, the Stack implementation does a Last On, First Off method for pushing and popping data.

[Stack Class Signature](javascript:void(0))

| Accessor | Description |
| --- | --- |
| :New() | Returns a new Stack object |
| :Push( value ) | Add a value to the top of the Stack |
| :Pop() | Return a value removed from the top of the Stack |
| :IndexOf( value ) | Return the index within the Stack of the value, or nil |
| :Clear() | Remove all data from the Stack |
| :IsEmpty() | Returns false if the Stack contains data, true otherwise |
| .top | Index of the top item of the Stack |

[Queue and Stack Control Script](javascript:void(0))

Using these classes in a control script allows sequential data handling with single function calls.

[Queue and Stack Control Script](javascript:void(0))

```lua
--Example Code  
myQ = Queue:New()  
myStack = Stack:New()  
  
Controls["Add"].EventHandler = function()  
  local value = math.random(10)  
  myQ:Push(value)  
  myStack:Push(value)  
end  
  
Controls["Remove"].EventHandler = function()  
  if not myQ:IsEmpty() then  
    Controls["QueueOutputText"].String = myQ:Pop()  
    Controls["StackOutputText"].String = myStack:Pop()  
  else  
    Controls["QueueOutputText"].String = "Queue is empty"  
    Controls["StackOutputText"].String = "Stack is empty"  
  end  
end
```

This control script uses two buttons, âAddâ and âRemoveâ, and two text fields, âQueueOutputTextâ and âStackOutputTextâ, to store and retrieve data following the queue and stack paradigms.

[Queue Class with TCPSocket](javascript:void(0))

Binding this class into the TCP example, the queue can be used to serialize TCP communication.

[Queue Class with TCPSocket](javascript:void(0))

```lua
--A Simple Queue Class  
Queue = {}  
  
function Queue:New()  
  list = { first = 1, last = 0 }  
  self.__index = self  
  setmetatable(list, self)  
  return list  
end  
  
function Queue:Push(value)  
  self.last = self.last + 1   
  self[self.last] = value  
end  
  
function Queue:PushFirst(value)  
  self.first = self.first - 1   
  self[self.first] = value  
end  
  
function Queue:Pop()  
  if self.first > self.last then   
    error("Queue is empty!")   
  end  
  local value = self[self.first]  
  self[self.first] = nil  
  self.first = self.first + 1  
  return value  
end  
  
function Queue:IndexOf(value)  
  for i = self.first,self.last do  
    if self[i] == value then  
      return i  
    end  
  end  
  return nil  
end  
  
function Queue:Clear()  
  for i = self.first,self.last do  
    self[i] = nil  
  end  
  self.first = 1  
  self.last = 0  
end  
  
function Queue:IsEmpty()  
  return self.first > self.last  
end  
  
  
-- Connection Variables  
IPAddress = "192.168.1.1"  
Port = 10001  
UserName = "user"  
Password = "password"  
EOL = "\r"                      -- End of line character as defined in device's API  
LoginPrompt = "login"           -- Match user prompt string as defined in the API  
PasswordPrompt = "Password"     -- Match password prompt as defined in the API  
LoginMatch = "Login successful" -- Match sucessful login string as defined in the API  
ResponseText = ""               -- Hold the last message received from the remote device  
  
-- Timers  
PollTimer = Timer.New() -- Timer for polling commands  
PollTime = 3            -- Time between polls in seconds   
  
-- Sockets  
TCP = TcpSocket.New()     -- Create new TcpSocket object  
TCP.ReadTimeout = 5       -- Set the timeout to 5 seconds  
TCP.WriteTimeout = 5      -- Set the timeout to 5 seconds  
TCP.ReconnectTimeout = 5  -- Set the wait time bfore reconnecting  
CommandQueue = Queue:New()  
CommandInFlight = false  
  
-- Variables  
LoggedIn = false  -- Flag for when a successful login is made  
  
  
-- Functions  
-- Helper Functions  
-- Returns true if TCP Socket is connected  
function IsConnected()    
  return TCP.IsConnected  
end  
  
-- On connect functionality  
function Connected()    
  --Start ending any command hanging in the queue on connect  
  if not CommandInFlight and not CommandQueue:IsEmpty() then  
    CommandInFlight = true  
    TCP:Write( CommandQueue:Pop() )   
  end  
  PollTimer:Start(PollTime)  
end  
  
-- On disconnect functionality  
function Disconnected()    
  PollTimer:Stop()  
  CommandInFlight = false  
  LoggedIn = false  
end  
  
-- TCP socket callbacks  
-- Called when TCP socket is connected  
TCP.Connected = function()    
  print("TCP Connected")  
  Connected()  
end  
  
-- Called when TCP socket is reconnecting  
TCP.Reconnect = function()    
  print("Socket reconnecting...")  
  Disconnected()  
end  
  
-- Called when TCP socket is closed  
TCP.Closed = function()  
  print("Socket closed")  
  Disconnected()  
end  
  
-- Called when TCP socket has an error  
TCP.Error = function()    
  print("Socket error")  
  Disconnected()  
end  
  
-- Called when TCP socket times out  
TCP.Timeout = function()  
  print("Socket timeout")  
  Disconnected()  
end  
  
-- Called when TCP socket receives data  
TCP.Data = function()  
  print("Data received")  
  ParseResponse()  -- Call ParseResponse when the TCP socket has data  
end  
  
-- Use the TCPSocket object to send a string (cmd)  
function Send(cmd)  
  if TCP.IsConnected then   -- If the TCP socket is connected write the command and EOL to the socket  
    local command = cmd .. EOL  
    print("Sending: " .. command)  
    CommandQueue:Push(command)  
    if not CommandInFlight then  
      CommandInFlight = true  
      TCP:Write( CommandQueue:Pop() )   
    end  
  else  
    print("Error - Disconnected; unable to send " .. cmd .. EOL)  
  end  
end  
  
-- If the Username or Password prompt is matched then the Username or Password is sent  
function Authenticate(rx)    
  if rx:match(LoginPrompt) then   
    print("Found \"" .. LoginPrompt .. "\" Sending UserName: " .. UserName.String)   
    Send(UserName.String)  
  elseif rx:match(PasswordPrompt) then   
    print("Found \"" .. PasswordPrompt .. "\" Sending Password: " .. Password.String)   
    Send(Password.String)  
  end  
end  
  
--Parsers  
function ParseResponse()  
  -- Read the data in the buffer  
  local rx = TCP:Read(TCP.BufferLength)  
  --Send the next command if the queue is not empty  
  if CommandQueue:IsEmpty() then  
    CommandInFlight = false  
  else  
    TCP:Write( CommandQueue:Pop() )   
  end  
  if not LoggedIn then  
    if rx:find(LoginMatch) then  -- If sucessful login string matched set LoggedIn high and call Connected()  
      print("Logged in")  
      LoggedIn = true  
      Connected()  
    elseif rx:find(LoginPrompt) or rx:find(PasswordPrompt) then  -- If sucessful Password or Username string matched set LoggedIn low and call Authenticate()  
      LoggedIn = false  
      Authenticate(rx)  
    else  
      print("Waiting for login prompt...")  
    end  
  else   
    print("Rx: " .. rx)  -- Print recieved data  
    ResponseData = rx  -- Show the received data through the user interface  
  
    -- Add data handling routines here  
  
  end  
end  
  
-- Event Handlers  
PollTimer.EventHandler = function PollDevice()  -- Call PollDevice when the PollTimer EventHandler is called  
  Send("PING")  
end  
  
-- Run at start  
Connect()
```

The Queue is used to build a list of commands in the Send() function. A flag is set when a command is in flight, and in case of a response, the next command is sent. Connect() and Disconnect() are also bound to start and stop sends from the Queue to handle those states cleanly.

[Notes](javascript:void(0))

* Indexing uses Lua numbers, which will encounter a rollover error at 2^52 consecutive pushes to the object.
* While the Stack and Queue objects data list can be indexed directly, it is not advisable because it may break stack/queue functionality.
