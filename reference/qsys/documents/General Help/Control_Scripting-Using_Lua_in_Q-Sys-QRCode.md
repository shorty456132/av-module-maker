# QRCode

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/QRCode.htm

# QRCode

Use the QRCode library to generate a QR code graphic that links to a specified URL. For example, you could generate a QR code for a UCI button that, when scanned with a smartphone, takes the user to a website that provides instructions for using a conference room.

## QRCode.GenerateSVG

Generate a QR code SVG graphic.

### Syntax

QRCode.GenerateSVG('*url*', ['*mode*'])

### Arguments

*url* : The URL string to encode.

*mode* : Optional [error correction](https://www.bing.com/search?FORM=U527DF&PC=U527&q=QR+code+error+correction) mode string. Replace with low, medium, quartile, or high. Defaults to "medium" if not passed.

* low = Level L, up to 7% error correction.
* medium = Level M, up to 15% error correction.
* quartile = Level Q, up to 25% error correction.
* high = Level H, up to 30% error correction.

### Example

In this example, Text Controller is configured as follows to generate a QR code:

* A text box ("url") for specifying the URL.
* A combo box ("mode") for specifying the level of error correction.
* A toggle button ("graphic") for displaying the QR code itself.
* A Lua script that calls the `QRCode.GenerateSVG` library.

Text Controller Script

```lua
json = require("rapidjson")  
Controls.mode.Choices = {"low", "medium", "quartile", "high"}  
  
  
function generate()  
  
  local svg = QRCode.GenerateSVG(Controls.url.String, Controls.mode.String)  
    
  legend = {  
    DrawChrome = false,  
    IconData = Crypto.Base64Encode(svg)  
  }  
  
  Controls.graphic.Legend = json.encode(legend)  
end  
  
Controls.mode.EventHandler = generate  
Controls.url.EventHandler = generate  
  
generate()
```
