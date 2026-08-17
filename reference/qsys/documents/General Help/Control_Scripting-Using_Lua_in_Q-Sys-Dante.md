# Dante API

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Dante.htm

# Dante API

The Dante API (DAPI) consists of two modules for communicating with a Dante device's GPIO interface from a Q-SYS Lua script.

**Note:** Initial Dante device support includes Audio-Technica microphones only. Other Dante devices that use the DAPI for GPIO might work but are not tested. This is a general interface and the actual usage of the GPIO on the device is specific to the device being controlled.

[Dante Domain Manager and Detected Devices](javascript:void(0))

If the Core is not enrolled in Dante Domain Manager (DDM):

* **Device Discovery**: The Core will discover all Dante devices on the same network that are not enrolled in any DDM domain. It will not find devices that are enrolled in a DDM domain because those devices are managed and isolated by DDM.

If the Core is enrolled in DDM:

* **Device Discovery**: The Core will discover devices based on the domain it is enrolled in:
  + **Same Domain**: It will find all devices enrolled in the same DDM domain.
  + **Different Domain**: It will not automatically discover devices in different DDM domains unless those domains are configured to allow cross-domain communication.
  + **Not Enrolled**: It will not find devices that are not enrolled in any DDM domain, as those devices are outside the managed scope of DDM.

DDM essentially creates a controlled environment where only devices within the same domain can communicate with each other, enhancing security and management capabilities.

[DanteBrowser](javascript:void(0))

Creates a browser object that discovers Dante devices on the network. This is useful for knowing whether a device exists on the network.

### Syntax

browser = DanteBrowser.New()

### Property/Function

.Browse

This returned object can be assigned a callback function. This function is called when a device is added or removed from the network. It takes two arguments - the name of the device and the event type ( `"ADDED","REMOVED"` ) .

**Note:** DanteBrowser depends on the underlying Audinate library to provide this information. The REMOVED callback can take an indeterminate amount of time after a device is removed.

[DanteDevice](javascript:void(0))

Creates an object that gives access to a specific device on the network. It allows the script to set the GPIO state of the device (for example, turn on LEDs) as well as receive GPIO events (for example, when a button is pressed on the device).

### Syntax

device = DanteDevice.New(*deviceName*)

### Property/Function

:SetGpio( value, mask )

Sets the GPIO state on the device. Value and mask are integers. Returns a numeric ID for the call.

:GetGpio()

Requests the current state of the GPIO. Returns a numeric ID for the call.

.Gpio

Function callback for when GPIO status changes on the device. Can take a single argument in the form of a table that contains details about the current state of the GPIO. The table contains:

* `.TriggerMask` - bit mask of what changed
* `.InputMask` - bit mask of pins set as input
* `.InputValue` - value of pins set as inputs
* `.OutputMask` - bit mask of pins set as output
* `.OutputValue` - value of pins set as outputs

.Response

Function callback to determine if the set call succeeded. It takes two arguments: `SetID` and `errorString`. The latter will be `nil` if the call is successful.

**Note:** Even if no errorString is returned, this does not guarantee that the call made it to the device. However, the existence of an error string definitely means an error occurred.

.EventHandler

Function callback to subscribe to the KeepAlive channel. Allows events when the device connection is lost and is established. It takes two arguments - the name of the device and the event type (`"CONNECTION"` , `"NO_CONNECTION"`).

[Example](javascript:void(0))

In this example, we are communicating with an Audio-Technica microphone with these GPIO assignments:

This chart tells us that GPIO 0, 2, 3, 4, 5, 6 and 7 are configured as inputs (i.e., can be set high or low externally) and GPIO 1 is configured as an output (can be read / notified externally).

GPIO 0 is used to switch between LOCAL and REMOTE mode. In LOCAL mode, the mute button locally mutes the microphone audio as well as locally controls the LED when the button is pressed. To control the microphone remotely from Lua, we need to first switch it to REMOTE mode by setting GPIO 0 to 1. This is done by sending the GPIO with a value of 0x1 and a mask of 0x1. The value can be any value as long as the lowest bit is 1 since the device uses the mask to determine which GPIO channels to set or unset. The microphone should remembers this setting through a power cycle, but probably safest to always set them.

This example script synchronizes a local mute state button with the remote button and LED on the microphone.

```lua
mic = "ATND8677-071142"  
    
-- some defines for the bits  
remoteMode = 0x1  
button = 0x2  
greenLED = 0x4  
redLED = 0x8  
    
browser = DanteBrowser.New()  
timer = Timer.New()  
device = nil  
    
timer.EventHandler = function()  
  if device then  
    device:GetGpio()  
  end  
end  
    
function dante_gpio(gpio)  
  print("got gpio message")  
  buttonWasPressed = gpio.TriggerMask & button == button  
  buttonIsDown = gpio.InputValue & button == button  
  if buttonWasPressed and buttonIsDown then  
    Controls.mute.Boolean = not Controls.mute.Boolean  
    updateLED()  
  end  
  Controls.led.Boolean = pressed  
end  
    
browser.Browse = function(name, br)  
  print(string.format("Browse %s %s", name, br))  
  if name == mic and br == "ADDED" then  
    device = DanteDevice.New(name)  
    device.Gpio = dante_gpio  
    
    -- make sure mic is in remote mode  
    device:SetGpio(remoteMode, remoteMode)  
    
    device.Response = function(id, res)  
      print("response : ", id, res)  
    end  
    
    -- every 10 seconds ask for the GPIO state  
    -- this could be used along with another timer  
    -- to determine if the device is alive on the network  
    timer:Start(10)  
  end  
end  
    
greenLED = 0x4  
redLED = 0x8  
    
function updateLED()  
  Controls.mute.Legend = Controls.mute.Boolean and "MUTED" or "UNMUTED"  
  if device then  
    id = device:SetGpio(Controls.mute.Boolean and redLED or greenLED, greenLED | redLED)  
  end  
end  
    
Controls.mute.EventHandler = function(ctl)  
  updateLED()  
end
```
