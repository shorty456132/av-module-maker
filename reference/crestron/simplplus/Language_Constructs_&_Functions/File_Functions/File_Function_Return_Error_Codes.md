# File Function Return Error Codes

KEYWORD |  VALUE |  FUNCTION  
---|---|---  
FILE_BAD_USER |  -3000 |  Calling task is not a file user. Use StartFileOperations() first.  
FILE_NO_DISK |  -3004 |  Disk is removed.  
FILE_LONGPATH |  -3017 |  Path or directory name too long.  
FILE_INVNAME |  -3018 |  Path or filename includes invalid character.  
FILE_PEMFILE |  -3019 |  No file descriptors available (Too many files open).  
FILE_BADFILE |  -3020 |  Invalid file descriptor.  
FILE_ACCES |  -3021 |  Attempt to open a read-only file or special (directory). Also the error code you get when trying to make a directory on a volume that does not support it (i.e. NVRAM or internal flash).  
FILE_NOSPC |  -3022 |  No space to create file in this disk.  
FILE_SHARE |  -3023 |  The access conflicts from multiple tasks to a specific file. Can also occur when attempting to write multiple files to the NVRAM disk at the same time.  
FILE_NOFILE |  -3024 |  File not found.  
FILE_EXIST |  -3025 |  Exclusive access requested, but file already exists.  
FILE_NVALFP |  -3026 |  Seek to negative file pointer.  
FILE_MAXFILE_SIZE |  -3027 |  Over the maximum file size.  
FILE_NOEMPTY |  -3028 |  Directory is not empty.  
FILE_INVPARM |  -3029 |  Invalid Flag/Mode is specified.  
FILE_INVPARCMB |  -3030 |  Invalid Flag/Mode combination.  
FILE_NO_MEMORY |  -3031 |  Can't allocate internal buffer.  
FILE_NO_BLOCK |  -3032 |  No block buffer available.  
FILE_NO_FINODE |  -3033 |  No FINODE buffer available.  
FILE_NO_DROBJ |  -3034 |  No DROBJ buffer available.  
FILE_IO_ERROR |  -3035 |  Driver I/O function routine returned.  
FILE_INTERNAL |  -3036 |  Internal error.  
FILE_UNAUTH  |  -4000 |  Unauthorized access.  
FILE_TYPEUNSUPP  |  -4001 |  Type not supported.  
FILE_INVENC |  -4002 |  Invalid encoding found when reading a string.  
FILE_BINERR |  -4003 |  Cannot write binary data to file opened with TEXT flag.  
FILE_CORRUPT |  -4004 |  Header on the file is invalid - file cannot be opened.  
FILE_NEWER_VERSION |  -4005 |  The file version number is greater than what is supported. Compile Simpl+.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/File_Function_Return_Error_Codes.htm*
