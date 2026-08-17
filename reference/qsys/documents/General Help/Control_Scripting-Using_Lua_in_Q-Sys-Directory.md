# dir (Directory)

> Source: https://help.qsys.com/Content/Control_Scripting/Using_Lua_in_Q-Sys/Directory.htm

# dir (Directory)

Use the directory commands to list folders and files, create folders, and delete folders within the `media/` or `design/` locations on the file system. For security and stability reasons, these are the only locations accessible by the Lua libraries.

The `media/` folder is the location for all media files, while the `design/` folder is the location where uncompressed design configuration files reside while a design is being emulated or running on a Q-SYS Core processor. (It is not intended for storage of user-created design files, and is not remotely accessible.)

[dir.get()](javascript:void(0))

Lists directories and files in a `media/` or `design/` path based on the following criteria:

* If the specified folder does not exist, the function returns nil.
* If the specified folder exists but contains no files or folders, the function returns an empty table.
* If the specified folder exists and contains files and/or folders, the function returns a table in which each file or directory is listed in its own separate table with the following three parameters:

| Parameter Name | Description |
| --- | --- |
| name | The name of the file or directory |
| type | "file" for a file, "directory" for a directory |
| size | Size of the entry in bytes |

### Syntax

dir.get(*path*)

### Arguments

*path* : String. Must begin with `/media` or `design/`. Surround the path with quotes.

### Example

```lua
directory = "media/Audio"  
temp = dir.get(directory)  
if temp ~= nil then   
  if #temp ~= 0 then  
    for k,v in ipairs(temp) do  
      print("\t"..v.type, v.name, v.size)  
    end  
  else  
    print("No files or folders in specified folder")  
  end  
else  
  print("Specified folder does not exist")  
end
```

#### Debug Output

```lua
2025-09-08T09:18:39.526	Starting Script

2025-09-08T09:18:39.527		file	Speech Off.wav	188460

2025-09-08T09:18:39.527		file	Speech On.wav	147500

2025-09-08T09:18:39.527		directory	Test	4096
```

[dir.create()](javascript:void(0))

Create a new folder within a `media/` or `design/` path.

### Syntax

dir.create(*path*)

### Arguments

*path* : String. Must begin with `/media` or `design/`. Surround the path with quotes.

### Example

```lua
directory = "media/Audio/New"  
dir.create(directory)
```

[dir.remove()](javascript:void(0))

Remove an empty folder within a `media/` or `design/` path.

### Syntax

dir.remove(*path*)

### Arguments

*path* : String. Must begin with `/media` or `design/`. Surround the path with quotes.

**Note:** The folder you are removing must be empty. See the Example section for an iterative method to remove files before removing the folder.

### Example

If the folder you intend to delete contains files, you must remove them first using `os.remove()`. For example:

```lua
directory = "media/Audio/New"  
temp = dir.get(directory)  
for i,v in ipairs(temp) do  
  os.remove(directory.."/"..v.name)   
end
```

Then, use `dir.remove()` to remove the now empty folder:

```lua
dir.remove(directory)
```
