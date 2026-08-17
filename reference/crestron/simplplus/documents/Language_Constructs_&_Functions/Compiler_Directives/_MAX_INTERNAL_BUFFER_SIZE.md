# #MAX_INTERNAL_BUFFER_SIZE

Name: 

#MAX_INTERNAL_BUFFER_SIZE

Syntax:

#MAX_INTERNAL_BUFFER_SIZE <size>

Description:

2-Series only. Sets the maximum size in bytes for the compiler’s internal string allocations. By default, the compiler will allocate 65535 bytes when using STRING_OUTPUT variables. String arguments passed to User Functions may also result in a 65535 byte string allocation, depending the argument’s usage. #MAX_INTERNAL_BUFFER_SIZE can be used to specify a different upper allocation limit. The range can be from 1-65535.

NOTE: There are some conditions where this compiler directive can be useful:  
  
This compiler directive can be used to optimize the amount of memory used by a module. Strings such as STRING_OUTPUTs and function arguments have unknown values, forcing the compiler to allocate the maximum buffer length of 65535 bytes. If the approximate length is known for these types of variables, then this compiler directive can be used to specify a smaller amount.   
  
Due to some compiler optimizations that Crestron has chosen to implement, the use of some strings may result in a runtime string buffer overflow. This error might result in the following message, “String __FN_DST_STR__ overflow.” Setting this compiler directive will replace the compiler’s assumed number of bytes with the number of bytes specified by the directive.  
  
This compiler directive is also useful for large modules and/or when many instances of a module are running simultaneously on the control system.

Example:

#MAX_INTERNAL_BUFFER_SIZE 10000

Version:

X Generation: Not supported

2-Series: SIMPL v3.01.25 or later

3-Series: N/A

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/Compiler_Directives/_MAX_INTERNAL_BUFFER_SIZE.htm*
