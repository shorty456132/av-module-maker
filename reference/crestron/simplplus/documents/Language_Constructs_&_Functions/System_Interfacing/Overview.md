# System Interfacing Overview

These functions control the way the SIMPL+ program communicates with Cresnet network devices and the CPU.

Function |  Description  
---|---  
[GetCIP](<GetCIPDev.htm>) |  Retrieves the current state of the join number on a particular CIP ID.  
[GetCresnet](<GetCresnetDev.htm>) |  Retrieves the current state of the join number on a particular Cresnet Network ID.  
[GetModelNumber](<GetModelNumber.htm>) |  Returns the product name.  
[GetSeries](<GetSeries.htm>) |  Returns the product series. For example, the 3-series architecture will return 3 and the 2-series architecture will return 2.  
[GetSlot](<GetSlotDev.htm>) |  Retrieves the current state of the join number on a particular card.  
[GetSymbolInstanceName](<GetSymbolInstanceName.htm>) |  Returns the symbol "S-" and the number where this SIMPL+ symbol is located within the SIMPL program.  
[GetSymbolReferenceName](<GetSymbolReferenceName.htm>) |  Returns the string entered into the [Reference Name] SIMPL+ symbol in SIMPL corresponding to the SIMPL+ module.  
[IsSignalDefined](<IsSignalDefined.htm>) |  Retrieves the current SIMPL signal number associated with a particular input or output.  
[MakeProgramFilename](<MakeProgramFilename.htm>) |  Takes in the filename (which would be the program path or anything that the user wants) and prepends that with the Program ID Tag. The Program ID Tag is specified in the Header of the SIMPL program.  
[SendCresnetPacket](<SendCresnetPacket.htm>) |  Sends the string specified by PACKET onto the Cresnet network.  
[SendPacketToCPU](<SendPacketToCPU.htm>) |  Sends the string specified by PACKET to the Cresnet CPU.  
[SetCIP](<SetCIPDev.htm>) |  Sets the state of the join number on a particular CIP ID.  
[SetCresnet](<SetCresnetDev.htm>) |  Sets the state of the join number on a particular Cresnet Network ID.  
[SetSlot](<SetSlotDev.htm>) |  Sets the state of the join number on a particular card slot.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/System_Interfacing/Overview.htm*
