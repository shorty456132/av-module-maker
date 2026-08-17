# Timer

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Timer.htm

# Timer

The Timer object is used to create delays or trigger events after a defined elapsed time.  It should be used instead of Lua's native delay and time functions.

[Timer.New()](javascript:void(0))

Creates a named timer using Start and Stop methods.

**Note:** Do not scope your Timer locally. This causes the object to be managed by Lua's garbage collector, which may lead to its removal even if it is still in use.

### Description

Each Timer must be named when created which is then the means by which you manipulate each specific timer. The `Timer:Start` method is used to start the timer and set the delay time.  When the delay time has elapsed, the function specified in `Timer.EventHandler` is called. By default, Timer repeats when it has elapsed. `Timer:Stop` is used to stop the timer. `Timer:IsRunning` prints if timer is running. Each Control Script has a single Timer.

### Syntax

Timer.New()

Creates a new timer object.

.EventHandler

Calls a specified function when the delay time has elapsed.

:Start(*period in seconds*)

Starts the timer.

:Stop()

Stops the timer.

:IsRunning()

Returns true if the timer is running.

### Examples

```lua
timer1 = Timer.New()  
timer2 = Timer.New()  
   
function timerFunc(timer)  
    if timer == timer1 then  
        print( "timer 1!" )  
    elseif timer == timer2 then  
        print ( "timer 2" )  
    end  
end  
  
timer1.EventHandler = timerFunc  
timer2.EventHandler = timerFunc  
   
timer1:Start(1)  
timer2:Start(2)
```

```lua
TestTimer = Timer.New()  
  
TestTimer:Start(1)  
  
print(TestTimer:IsRunning()) -- should print true  
  
TestTimer:Stop()  
  
print(TestTimer:IsRunning()) -- should print false
```

[Timer.CallAfter()](javascript:void(0))

Creates a simple timer that calls a named function after a specified delay time.

### Description

As an alternative to creating a traditional named timer, you can create a simple timer to call a named function after a given delay period. Unlike named timer objects created with Timer.New(), there is no need to issue a :Stop() command to halt repetition of this timer.

### Syntax

Timer.CallAfter(*function*, *delay*)

### Arguments

*function* : The named function to call after the specified delay time.

*delay* : [seconds.milliseconds]

[Timer.Now()](javascript:void(0))

Returns the number of seconds since epoch.

### Description

Timer.Now() returns the number of seconds since the epoch. It can be useful to calculate the difference between a current value and a previous value.

**Note:** The returned epoch value differs between Emulation mode (from Windows) and Run mode (from the Q-SYS Core processor).

### Syntax

Timer.Now()

### Example

```lua
print (Timer.Now())
```

#### Debug Output

```lua
2021-11-22T23:16:08.884 Starting Script
2021-11-22T23:16:08.884 13282096568.884
```

[Troubleshooting](javascript:void(0))

### Issues with Timers Stalling or Stopping

Do not scope your Timers locally. If you do so, the scripting engine will eventually delete the timer and the event callback, forcing it to stop.

**Note:** If you see issues with Timers stalling and have your Timer scoped locally, try removing the âlocalâ from the Timer declaration.

[Example 1: Timer Stops Erroneously](javascript:void(0))

In the following example, an `EventHandler` will print an `Event` at 1 second intervals; however, since it is prefixed by `local`, the Timer was stopped after 22 iterations.

```lua
local tmr = Timer.New()  
count = 0  
tmr.EventHandler = function()  
  print("Event:"..count)  
  count=count+1  
end  
  
tmr:Start(1)
```

#### Debug Output

```lua

2023-01-31T18:23:47.061	Starting Script
2023-01-31T18:23:49.060	Event:1
2023-01-31T18:23:50.059	Event:2
2023-01-31T18:23:51.060	Event:3
2023-01-31T18:23:52.059	Event:4
2023-01-31T18:23:53.060	Event:5
2023-01-31T18:23:54.060	Event:6
2023-01-31T18:23:55.060	Event:7
2023-01-31T18:23:56.060	Event:8
2023-01-31T18:23:57.059	Event:9
2023-01-31T18:23:58.059	Event:10
2023-01-31T18:23:59.059	Event:11
2023-01-31T18:24:00.060	Event:12
2023-01-31T18:24:01.060	Event:13
2023-01-31T18:24:02.060	Event:14
2023-01-31T18:24:03.059	Event:15
2023-01-31T18:24:04.060	Event:16
2023-01-31T18:24:05.059	Event:17
2023-01-31T18:24:06.060	Event:18
2023-01-31T18:24:07.060	Event:19
2023-01-31T18:24:08.060	Event:20
2023-01-31T18:24:09.059	Event:21
2023-01-31T18:24:10.059	Event:22
```

[Example 2: Removing Local Resolves Timer](javascript:void(0))

```lua
tmr = Timer.New()  
count = 0  
tmr.EventHandler = function()  
  print("Event:"..count)  
  count=count+1  
end  
  
tmr:Start(1)
```

#### Debug Output

```lua

2023-01-31T17:33:18.522	Starting Script
....
2023-01-31T18:23:18.522	Event:90
2023-01-31T18:23:19.522	Event:91
2023-01-31T18:23:20.522	Event:92
2023-01-31T18:23:21.522	Event:93
2023-01-31T18:23:22.523	Event:94
2023-01-31T18:23:23.523	Event:95
2023-01-31T18:23:24.522	Event:96
2023-01-31T18:23:26.522	Event:98
2023-01-31T18:23:27.523	Event:99
2023-01-31T18:23:28.523	Event:100
2023-01-31T18:23:29.522	Event:101
2023-01-31T18:23:30.522	Event:102
2023-01-31T18:23:31.522	Event:103
2023-01-31T18:23:32.523	Event:104
2023-01-31T18:23:33.523	Event:105
2023-01-31T18:23:34.522	Event:106
2023-01-31T18:23:35.523	Event:107
2023-01-31T18:23:36.522	Event:108
2023-01-31T18:23:37.523	Event:109
2023-01-31T18:23:38.523	Event:110
2023-01-31T18:23:40.523	Event:112
2023-01-31T18:23:41.523	Event:113
2023-01-31T18:23:42.522	Event:114
2023-01-31T18:23:43.523	Event:115
2023-01-31T18:23:44.522	Event:116
2023-01-31T18:23:45.522	Event:117
2023-01-31T18:23:46.522	Event:118
....
```
