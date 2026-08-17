# Media Resources

> Source: https://help.qsys.com/Content/Management_APIs/media_resources.htm

# Media Resources

Use the Media Resources API endpoint to view and manage `/media` content on the Q-SYS Core processor, including folders and files.

[Variables](javascript:void(0))

Variables are marked with curly brackets { } in request commands:

* `core-ip` : the Core's IP address
* `bearer` : the token for `/api` endpoints authentication

[Requests](javascript:void(0))

Rules for submitting requests:

* All Media resource endpoints are protected with the Bearer Authentication type for Cores in "protected" Access Mode (i.e., Access Control is enabled). The "Authorization" header is not required for "open" Cores (i.e., Access Control is disabled). Refer to the [Authentication](authentication.htm) topic for instructions on obtaining a bearer token, if needed.
* Folders and files are referred to as a "resource" with a corresponding "type" in the payload. A resource is requested as JSON with a GET verb by its filesystem path and returns either an array of metadata describing its content (when the path is a folder) or a single file metadata (when the path points to an actual file).
* Any special characters within the resource endpoint path (spaces, slashes, etc.) must be URI encoded.

**Note:** If your client does not add the HTTP `Host` header by default, it must be provided with each request. Otherwise, the request won't pass security checks, resulting in HTTP code 406 ("Not Acceptable").

### List and Check

[List root folders and files](javascript:void(0))

Obtain a list of the folders and files in the root `/media` folder, including default folders and custom folders.

**Note:** The system default folders (Audio, Messages, PageArchives, Preambles, Ringtones) are read-only and cannot be modified in any way.

#### List root folders: success

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/media \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Accept: application/json"
```

Response

```lua
[  
  {  
    "created": 1570195890724,  
    "ext": null,  
    "name": "Audio",  
    "path": "/Audio",  
    "size": null,  
    "type": "folder",  
    "updated": 1613052655318  
  },  
  // ...other root folders  
]
```

#### Attempt to modify a default folder: fail

```lua
curl -k -X PATCH https://{core-ip}/api/v0/cores/self/media/Audio \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '{  
"name": "Audio-renamed"  
}'
```

Response

```lua
{  
  "code":403,  
  "message":"Forbidden",  
  "error": {  
    "code":"MEDIA_ACCESS_DENIED",  
    "message":"Cannot modify default resources in the root"  
  }  
}
```

**Note:** Operations on custom-created folders in the root `/media` location are allowed, however.

[List directory](javascript:void(0))

If the requested path is a folder, the resources contained within that folder are listed as an array of metadata describing each resource.

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/media/Audio \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Accept: application/json"
```

Response

```lua
[  
  {  
    "created": 1570195890724,  
    "ext": null,  
    "name": "example folder",  
    "path": "/Audio/example folder",  
    "size": null,  
    "type": "folder",  
    "updated": 1610554920070  
  },  
  {  
    "created": 1610554969982,  
    "ext": "mp3",  
    "name": "example file",  
    "path": "Audio/example file.mp3",  
    "size": 764176,  
    "type": "file",  
    "updated": 1610554970074  
  },  
]
```

[Check for a resource's existence](javascript:void(0))

If you need to check for the resource's existence without reading actual metadata or content, a HEAD request can be made to minimize file system operations and HTTP traffic.

```lua
curl -k -I 'https://{core-ip}/api/v0/cores/self/media/Audio/example%20file.mp3' \  
  -H "Authorization: Bearer {bearer}"
```

Response

```lua
HTTP/1.1 200 OK  
Date: Mon, 15 Feb 2021 17:04:58 GMT  
Connection: keep-alive  
# ...other headers
```

[Read file meta description](javascript:void(0))

If the requested path is a file, its meta description is returned.

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/media/Audio/example%20file.mp3 \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Accept: application/json"
```

Response

```lua
{  
  "created": 1610554969982,  
  "ext": "mp3",  
  "name": "example file",  
  "path": "Audio/example file.mp3",  
  "size": 764176,  
  "type": "file",  
  "updated": 1610554970074  
}
```

### Create Folders

[Create a folder](javascript:void(0))

A path specifies the parent folder where the new folder should be created.

**Note:** An attempt to create a folder that already exists results in an HTTP 400 error.

```lua
curl -k -X POST https://{core-ip}/api/v0/cores/self/media/Audio \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '{  
"name": "example folder"  
}'
```

Response

```lua
{  
  "created": 1613474548847,  
  "ext": null,  
  "name": "example folder",  
  "path": "Audio/example folder",  
  "size": null,  
  "type": "folder",  
  "updated": 1613474548847  
}
```

[Create multiple folders](javascript:void(0))

The same request can be used to create multiple folders at once by providing an array of new resources in the payload.

```lua
curl -k -X POST https://{core-ip}/api/v0/cores/self/media/Audio \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '[  
{  
  "name": "example folder 0"  
},  
{  
  "name": "example folder 1"  
},  
{  
  "name": "example folder 2"  
}  
]'
```

Response

```lua
[  
  {  
    "created": 1613475346326,  
    "ext": null,  
    "name": "example folder 0",  
    "path": "Audio/example folder 0",  
    "size": null,  
    "type": "folder",  
    "updated": 1613475346326  
  },  
  // ...other folders  
]
```

### Download, Play Back, and Upload Files

[Download a file (read file data as a stream)](javascript:void(0))

To download the actual file, it must be requested as a stream of raw data. File binary content can be redirected to an output file using the `-o` argument.

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/media/Audio/example%20file.mp3 \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Accept: application/octet-stream" \  
  -o "example file.mp3"
```

The response is a binary data stream.

[Play back a file (read file data as audio)](javascript:void(0))

Request for a raw data stream with a response MIME type that allows for interpretation as audio by the requesting client.

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/media/Audio/example%20file.mp3 \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Accept: audio/*"
```

The response is a binary data stream with the audio MIME type.

[Upload a file](javascript:void(0))

The request sends the `multipart/form-data` body where the `media` form-field specifies the source and the file name.

**Note:** An attempt to upload a file that already exists safely replaces the existing file with the new one. The original file is left untouched until the upload is finished â therefore, there must be enough drive space for both files while the operation is in progress.

In this example request, `example file.mp3` is in the shell working directory.

```lua
curl -k -X POST https://{core-ip}/api/v0/cores/self/media/Audio \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: multipart/form-data" \  
  -F 'media=@example file.mp3'
```

Response

```lua
{  
  "created": 1613475166397,  
  "ext": "mp3",  
  "name": "example file",  
  "path": "Audio/example file.mp3",  
  "size": 764176,  
  "type": "file",  
  "updated": 1613475166421  
}
```

[Upload multiple files](javascript:void(0))

Itâs also possible to initiate a batch upload by providing more files for the `media` form-field.

```lua
curl -k -X POST https://{core-ip}/api/v0/cores/self/media/Audio \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: multipart/form-data" \  
  -F 'media=@example file 0.mp3' \  
  -F 'media=@example file 1.mp3' \  
  -F 'media=@example file 2.mp3'
```

Response

```lua
[  
  {  
    "created": 1613477354019,  
    "ext": "mp3",  
    "name": "example file 0",  
    "path": "Audio/example file 0.mp3",  
    "size": 764176,  
    "type": "file",  
    "updated": 1613477354079  
  },  
  // ...other files  
]
```

### Rename, Move, and Delete Resources

[Rename a resource](javascript:void(0))

The endpoint path is a resource-unique identifier, and the payload contains a new `name` for the resource.

**Note:** The resource `id` (path) naturally changes after a successful rename.

```lua
curl -k -X PATCH https://{core-ip}/api/v0/cores/self/media/Audio/example%20folder \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '{  
"name": "example folder 0"  
}'
```

Response

```lua
{  
  "created": 1613474548847,  
  "ext": null,  
  "name": "example folder 0",  
  "path": "Audio/example folder 0",  
  "size": null,  
  "type": "folder",  
  "updated": 1613474548847  
}
```

[Rename multiple resources](javascript:void(0))

The endpoint path targets the root folder. The payload is an array of resource objects with `id` (the full resource path, including extension if the resource is a file) and a new name for it.

```lua
curl -k -X PATCH https://{core-ip}/api/v0/cores/self/media \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '[  
{  
  "id": "Audio/example folder",  
  "name": "example folder 0"   
},  
{  
  "id": "Audio/example file.mp3",  
  "name": "example file 0"  
}  
]'
```

Response

```lua
[  
  {  
    "created": 1613479883289,  
    "ext": null,  
    "name": "example folder 0",  
    "path": "Audio/example folder 0",  
    "size": null,  
    "type": "folder",  
    "updated": 1613479883289  
  },  
  {  
    "created": 1613477726987,  
    "ext": "mp3",  
    "name": "example file 0",  
    "path": "Audio/example file 0.mp3",  
    "size": 764176,  
    "type": "file",  
    "updated": 1613477727015  
  }  
]
```

[Move a resource](javascript:void(0))

The path sets the target resource, and the payload contains a new `path` for it.

```lua
curl -k -X PUT https://{core-ip}/api/v0/cores/self/media/Audio/example%20folder \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '{  
"path": "Messages/example folder"  
}'
```

Response

```lua
{  
  "created": 1613479883289,  
  "ext": null,  
  "name": "example folder 0",  
  "path": "Messages/example folder 0",  
  "size": null,  
  "type": "folder",  
  "updated": 1613479883289  
}
```

[Move multiple resources](javascript:void(0))

The endpoint path targets the root folder. The payload is composed as an array of objects where each has a key that equals the resource `id` (path), and its value is an object that contains a new `path` for that resource.

```lua
curl -k -X PUT https://{core-ip}/api/v0/cores/self/media \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '[  
{ "Audio/example folder": { "path": "Messages/example folder" } },  
{ "Audio/example file.mp3": { "path": "Messages/example file.mp3" } }  
]'
```

Response

```lua
[  
  {  
    "created": 1613481234196,  
    "ext": null,  
    "name": "example folder",  
    "path": "Messages/example folder",  
    "size": null,  
    "type": "folder",  
    "updated": 1613481234196  
  },  
  {  
    "created": 1613477726987,  
    "ext": "mp3",  
    "name": "example file",  
    "path": "Messages/example file.mp3",  
    "size": 764176,  
    "type": "file",  
    "updated": 1613477727015  
  }  
]
```

[Delete a resource](javascript:void(0))

The delete request simply targets the resource by its path with the DELETE command. The request has no response body.

```lua
curl -k -X DELETE https://{core-ip}/api/v0/cores/self/media/Audio/example%20file.mp3 \  
  -H "Authorization: Bearer {bearer}"
```

[Delete multiple resource](javascript:void(0))

The endpoint path targets the root folder. The payload is an array of resource paths. The request has no response body.

```lua
curl -k -X DELETE https://{core-ip}/api/v0/cores/self/media \  
  -H "Authorization: Bearer {bearer}"  
  -H "Content-Type: application/json" \  
  -d '[  
"Audio/example folder", "Audio/example file.mp3"   
]'
```

[Example Script (.sh)](javascript:void(0))

Example Script: media\_resources.sh

```lua
#!/bin/bash  
  
printf "Q-SYS Core Manager Media resources API probe\n\n"  
  
## Info describing script usage  
  
if [ $# -lt 4 ]; then  
    printf "Script usage:\n\n"  
    printf "$0 <protocol> <core-ip> <test-folder-name> <test-file-name> [username] [password]\n"  
    exit 1  
fi  
  
## Script parameters  
  
PROTOCOL=$1  
CORE_IP=$2  
TEST_FOLDER=$3  
TEST_FILE=$4  
  
USERNAME=$5  
PASSWORD=$6  
  
## No cURL output  
  
SILENCED="-s"  
  
# ----------------------------------------------------------------------------  
# Auth 1 - check Core Access Mode  
# ----------------------------------------------------------------------------  
  
ACCESS_MODE_RESP=$(curl -k -X GET $PROTOCOL://$CORE_IP/api/v0/cores/self/access_mode \  
 $SILENCED \  
 -H "Accept: application/json")  
  
printf "Auth #1: Core Access Mode response: $ACCESS_MODE_RESP\n"  
  
## Log in if Access Mode "protected"; set empty header otherwise  
  
if [[ $ACCESS_MODE_RESP = *open* ]]  
then  
  AUTHORIZATION=""  
else  
  if [ -z "$USERNAME" ] || [ -z "$PASSWORD" ]; then  
    printf "\nLogin failed - no User credentials provided! Exiting...\n"  
    exit 1  
  fi  
  
  # --------------------------------------------------------------------------  
  # Auth 2 - Log in using provided credentials  
  # --------------------------------------------------------------------------  
  
  LOGIN_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/logon \  
   $SILENCED \  
   -H "Accept: application/json" \  
   -H "Content-Type: application/json" \  
   -d '{  
    "username": "'$USERNAME'",  
    "password": "'$PASSWORD'"  
   }')  
  
  printf "Auth #2: Login response: $LOGIN_RESP\n"  
  
  ## Exit if Login failed  
  
  if [[ $LOGIN_RESP != *token* ]]; then  
    printf "\nLogin failed - invalid User credentials provided! Exiting...\n"  
    exit 1  
  fi  
  
  ## Parse Bearer token out of Login response  
  
  TOKEN_REGEX='"token":"([a-f0-9]+)"'  
  [[ $LOGIN_RESP =~ $TOKEN_REGEX ]]  
  ACCESS_TOKEN=${BASH_REMATCH[1]}  
  
  AUTHORIZATION="Authorization: Bearer $ACCESS_TOKEN"  
fi  
  
## Create single test file (1MB)  
  
dd if=/dev/zero of="$TEST_FILE.dat" bs=1MB count=1 status=none  
  
# ----------------------------------------------------------------------------  
# Step 0.1 - list contents of the root folder  
# ----------------------------------------------------------------------------  
  
MEDIA_ROOT_LIST_RESP=$(curl -k -X GET $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json")  
  
printf "\n"  
  
printf "Media resources #0.1: List root folder response: $MEDIA_ROOT_LIST_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 0.2 - attempt to overwrite one of the default root folders  
# ----------------------------------------------------------------------------  
  
MEDIA_ROOT_CREATE_DEFAULT_FOLDER_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "name": "Audio"  
}')  
  
printf "\n"  
  
printf "Media resources #0.2: Attempt to overwrite the default 'Audio' root folder response: $MEDIA_ROOT_CREATE_DEFAULT_FOLDER_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 0.3 - create custom folder in the root directory  
# ----------------------------------------------------------------------------  
  
MEDIA_ROOT_CREATE_FOLDER_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "name": "'$TEST_FOLDER'"  
}')  
  
printf "\n"  
  
printf "Media resources #0.3: Create custom root folder response: $MEDIA_ROOT_CREATE_FOLDER_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 0.4 - attempt to upload the file with an existing root folder name  
# ----------------------------------------------------------------------------  
  
dd if=/dev/zero of="Audio" bs=1KB count=1 status=none  
  
MEDIA_ROOT_UPLOAD_DEFAULT_FILE_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: multipart/form-data" \  
 -F 'media=@Audio')  
  
printf "\n"  
  
printf "Media resources #0.4: Attempt to upload the file with default 'Audio' root folder name: $MEDIA_ROOT_UPLOAD_DEFAULT_FILE_RESP\n"  
  
rm "Audio"  
  
# ----------------------------------------------------------------------------  
# Step 0.5 - create custom file in the root folder  
# ----------------------------------------------------------------------------  
  
MEDIA_ROOT_UPLOAD_FILE_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: multipart/form-data" \  
 -F 'media=@'$TEST_FILE'.dat')  
  
printf "\n"  
  
printf "Media resources #0.5: Upload file to the root folder response: $MEDIA_ROOT_UPLOAD_FILE_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 0.6 - rename custom file in the root folder  
# ----------------------------------------------------------------------------  
  
MEDIA_ROOT_RENAME_FOLDER_RESP=$(curl -k -X PATCH $PROTOCOL://$CORE_IP/api/v0/cores/self/media/$TEST_FILE.dat \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "name": "'$TEST_FILE'-renamed"  
}')  
  
printf "\n"  
  
printf "Media resources #0.6: Rename file in the root folder response: $MEDIA_ROOT_RENAME_FOLDER_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 0.7 - move custom file from the root folder  
# ----------------------------------------------------------------------------  
  
MEDIA_ROOT_MOVE_FOLDER_FROM_RESP=$(curl -k -X PUT $PROTOCOL://$CORE_IP/api/v0/cores/self/media/$TEST_FILE-renamed.dat \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "path": "Audio/'$TEST_FILE'-renamed.dat"  
}')  
  
printf "\n"  
  
printf "Media resources #0.7: Move file from the root folder response: $MEDIA_ROOT_MOVE_FOLDER_FROM_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 0.8 - move custom file to the root folder  
# ----------------------------------------------------------------------------  
  
MEDIA_ROOT_MOVE_FOLDER_INTO_RESP=$(curl -k -X PUT $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio/$TEST_FILE-renamed.dat \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "path": "'$TEST_FILE'-renamed.dat"  
}')  
  
printf "\n"  
  
printf "Media resources #0.8: Move file to the root folder response: $MEDIA_ROOT_MOVE_FOLDER_INTO_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 0.9 - delete custom resources from the root folder  
# ----------------------------------------------------------------------------  
  
curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media/$TEST_FOLDER \  
 $SILENCED \  
 -H "$AUTHORIZATION"  
  
curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media/$TEST_FILE-renamed.dat \  
 $SILENCED \  
 -H "$AUTHORIZATION"  
  
printf "\n"  
  
printf "Media resources #0.9: Deleted custom resources from the root folder\n"  
  
# ---  
  
printf "\n"  
  
printf "> Part 1 - Single resource operations:\n"  
  
# ----------------------------------------------------------------------------  
# Step 1.1 - create test folder in Audio root folder  
# ----------------------------------------------------------------------------  
  
MEDIA_CREATE_FOLDER_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "name": "'$TEST_FOLDER'"  
}')  
  
printf "\n"  
  
printf "Media resources #1.1: Create folder response: $MEDIA_CREATE_FOLDER_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 1.2 - upload media file to the test folder  
# ----------------------------------------------------------------------------  
  
MEDIA_UPLOAD_FILE_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio/$TEST_FOLDER \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: multipart/form-data" \  
 -F 'media=@'$TEST_FILE'.dat')  
  
printf "\n"  
  
printf "Media resources #1.2: Upload file response: $MEDIA_UPLOAD_FILE_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 1.3 - rename the test folder  
# ----------------------------------------------------------------------------  
  
MEDIA_RENAME_FOLDER_RESP=$(curl -k -X PATCH $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio/$TEST_FOLDER \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "name": "'$TEST_FOLDER'-renamed"  
}')  
  
printf "\n"  
  
printf "Media resources #1.3: Rename folder response: $MEDIA_RENAME_FOLDER_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 1.4 - move the test folder to Messages folder  
# ----------------------------------------------------------------------------  
  
MEDIA_MOVE_FOLDER_RESP=$(curl -k -X PUT $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio/$TEST_FOLDER-renamed \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "path": "Messages/'$TEST_FOLDER'-renamed"  
}')  
  
printf "\n"  
  
printf "Media resources #1.4: Move folder response: $MEDIA_MOVE_FOLDER_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 1.5 - download the uploaded media file  
# ----------------------------------------------------------------------------  
  
curl -k -X GET $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Messages/$TEST_FOLDER-renamed/$TEST_FILE.dat \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/octet-stream" \  
 -o "$TEST_FILE-copy.dat"  
  
printf "\n"  
  
printf "Media resources #1.5: Downloaded test media file as $TEST_FILE-copy.dat\n"  
  
# ----------------------------------------------------------------------------  
# Step 1.6 - delete the test folder  
# ----------------------------------------------------------------------------  
  
curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Messages/$TEST_FOLDER-renamed \  
 $SILENCED \  
 -H "$AUTHORIZATION"  
  
printf "\n"  
  
printf "Media resources #1.6: Deleted test folder $TEST_FOLDER-renamed\n"  
  
## Delete test file  
  
rm $TEST_FILE.dat $TEST_FILE-copy.dat  
  
# ---  
  
## Create multiple test files (100KB each)  
  
for i in {1..10}; do  
  dd if=/dev/zero of=$TEST_FILE-$i.dat bs=1KB count=100 status=none  
done  
  
printf "\n"  
  
printf "> Part 2 - Multiple resources operations:\n"  
  
# ----------------------------------------------------------------------------  
# Step 2.1 - create multiple test folders in Audio root folder  
# ----------------------------------------------------------------------------  
  
TEST_FOLDERS=()  
  
for i in {1..3}; do  
  TEST_FOLDERS+=('{"name":"'$TEST_FOLDER-$i'"}')  
done  
  
TEST_FOLDERS_JSON=$(printf %s, ${TEST_FOLDERS[@]})  
TEST_FOLDERS_JSON="[${TEST_FOLDERS_JSON::-1}]"  
  
MEDIA_CREATE_FOLDERS_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d $TEST_FOLDERS_JSON)  
  
printf "\n"  
  
printf "Media resources #2.1: Create folders response: $MEDIA_CREATE_FOLDERS_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 2.2 - upload multiple media files to the Audio root folder  
# ----------------------------------------------------------------------------  
  
TEST_FILES=''  
  
for i in {1..10}; do  
  TEST_FILES+=" -F media=@$TEST_FILE-$i.dat"  
done  
  
MEDIA_UPLOAD_FILES_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: multipart/form-data" \  
 $TEST_FILES)  
  
printf "\n"  
  
printf "Media resources #2.2: Upload files response: $MEDIA_UPLOAD_FILES_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 2.3 - rename the test resources  
# ----------------------------------------------------------------------------  
  
TEST_FOLDERS=()  
  
for i in {1..3}; do  
  TEST_FOLDERS+=('{"id":"Audio/'$TEST_FOLDER-$i'","name":"'$TEST_FOLDER-$i'-renamed"}')  
done  
  
TEST_FOLDERS_JSON=$(printf %s, ${TEST_FOLDERS[@]})  
TEST_FOLDERS_JSON="[${TEST_FOLDERS_JSON::-1}]"  
  
MEDIA_RENAME_FOLDERS_RESP=$(curl -k -X PATCH $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d $TEST_FOLDERS_JSON)  
  
printf "\n"  
  
printf "Media resources #2.3: Rename test folders response: $MEDIA_RENAME_FOLDERS_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 2.4 - move the test folders to Messages folder  
# ----------------------------------------------------------------------------  
  
TEST_FOLDERS=()  
  
for i in {1..3}; do  
  TEST_FOLDERS+=('{"Audio/'$TEST_FOLDER-$i'-renamed":{"path":"Messages/'$TEST_FOLDER-$i'-renamed"}}')  
done  
  
TEST_FOLDERS_JSON=$(printf %s, ${TEST_FOLDERS[@]})  
TEST_FOLDERS_JSON="[${TEST_FOLDERS_JSON::-1}]"  
  
MEDIA_MOVE_FOLDERS_RESP=$(curl -k -X PUT $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d $TEST_FOLDERS_JSON)  
  
printf "\n"  
  
printf "Media resources #2.4: Move test folders response: $MEDIA_MOVE_FOLDERS_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 2.5 - delete the test files  
# ----------------------------------------------------------------------------  
  
TEST_FILES=()  
  
for i in {1..10}; do  
  TEST_FILES+=("Audio/$TEST_FILE-$i.dat")  
done  
  
TEST_FILES_JSON=$(printf '"%s",' "${TEST_FILES[@]}")  
TEST_FILES_JSON="[${TEST_FILES_JSON::-1}]"  
  
curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d $TEST_FILES_JSON  
  
printf "\n"  
  
printf "Media resources #2.5: Deleted test files\n"  
  
# ----------------------------------------------------------------------------  
# Step 2.6 - delete the test folders  
# ----------------------------------------------------------------------------  
  
TEST_FOLDERS=()  
  
for i in {1..3}; do  
  TEST_FOLDERS+=("Messages/$TEST_FOLDER-$i-renamed")  
done  
  
TEST_FOLDERS_JSON=$(printf '"%s",' "${TEST_FOLDERS[@]}")  
TEST_FOLDERS_JSON="[${TEST_FOLDERS_JSON::-1}]"  
  
curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d $TEST_FOLDERS_JSON  
  
printf "\n"  
  
printf "Media resources #2.6: Deleted test folders\n"  
  
## Delete test files  
  
rm $TEST_FILE-*
```
