# Too Much RAM Allocated

Too much RAM was allocated for the data structures. Approximately 60K is available for user data. When compiling a program, it will tell you how much memory is required for one instance of the module. Each instantiation of the module in a SIMPL program takes up that much more space. For example, if a module says it requires 100 bytes after it is compiled, two instances of that module will require 200 bytes. If this message is received, reduce the number of variables. If string or buffers have been declared overly large, this is an easy place to reduce memory requirements.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Common_Runtime_Errors/Too_much_ram_allocated.htm*
