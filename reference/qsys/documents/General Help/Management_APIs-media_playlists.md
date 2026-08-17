# Media Playlists

> Source: https://help.qsys.com/Content/Management_APIs/media_playlists.htm

# Media Playlists

Use the Media Playlists API endpoint to view and manage audio playlists on the Q-SYS Core processor.

[Variables](javascript:void(0))

Variables are marked with curly brackets { } in request commands:

* `core-ip` : the Core's IP address
* `bearer` : the token for `/api` endpoints authentication
* `playlist-id` : identifier of the playlist in UUID format

[Requests](javascript:void(0))

Rules for submitting requests:

* All Media playlist endpoints are protected with the Bearer Authentication type for Cores in "protected" Access Mode (i.e., Access Control is enabled). The "Authorization" header is not required for "open" Cores (i.e., Access Control is disabled). Refer to the [Authentication](authentication.htm) topic for instructions on obtaining a bearer token, if needed.
* Any special characters within the resource endpoint path (spaces, slashes, etc.) must be URI encoded.
* Only media files can be added to a playlist. If you attempt to add a folder, an error results.

**Note:** If your client does not add the HTTP `Host` header by default, it must be provided with each request. Otherwise, the request won't pass security checks, resulting in HTTP code 406 ("Not Acceptable").

### Requests

[List playlists](javascript:void(0))

This is a simple request to list all of the available playlists. Due to performance considerations, the response does not include nested linked media file arrays.

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/media_playlists \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Accept: application/json"
```

Response

```lua
[  
  {  
    "count": 2,  
    "id": "{playlist-id}",  
    "name": "example playlist 0"  
  },  
  {  
    "count": 2,  
    "id": "{playlist-id}",  
    "name": "example playlist 1"  
  }  
]
```

[Show playlist](javascript:void(0))

This is a detailed playlist view that includes an array of metadata describing media files linked to the playlist. If the original media file has been deleted, the available flag is set to false. Renaming files or moving them between folders automatically updates file paths across the playlists to which they are linked.

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/media_playlists/{playlist-id} \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Accept: application/json"
```

Response

```lua
{  
  "count": 2,  
  "id": "{playlist-id}",  
  "media": [  
    {  
      "available": true,  
      "created": 1613735618931,  
      "ext": ".mp3",  
      "id": "Audio/example file 0.mp3",  
      "name": "example file 0",  
      "path": "Audio/example file 0.mp3",  
      "size": 764176,  
      "type": "file",  
      "updated": 1613735619167  
    },  
    {  
      "available": true,  
      "created": 1613735618959,  
      "ext": ".mp3",  
      "id": "Audio/example file 1.mp3",  
      "name": "example file 1",  
      "path": "Audio/example file 1.mp3",  
      "size": 764176,  
      "type": "file",  
      "updated": 1613735619171  
    }  
  ],  
  "name": "example playlist 0"  
}
```

[Create playlist](javascript:void(0))

Apart from the name, a playlist has a unique identifier (UUID) that is automatically assigned on creation. However, attempting to create a playlist with a name that already exists results in an error.

```lua
curl -k -X POST https://{core-ip}/api/v0/cores/self/media_playlists \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '{  
"name": "example playlist 2"  
}'
```

Response

```lua
{  
  "id":"{playlist-id}",  
  "name":"example playlist 2",  
  "count":0  
}
```

[Update playlist](javascript:void(0))

The payload to change a playlist can contain only `name`, `media`, or both depending on the intention. Note that the `media` array completely overrides the media files list linked to the playlist, and it could therefore be used to re-order media in the playlist.

```lua
curl -k -X PUT https://{core-ip}/api/v0/cores/self/media_playlists/{playlist-id} \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '{  
"name": "example playlist 3",  
"media": [  
  { "path": "Audio/example file 1.mp3" },  
  { "path": "Audio/example file 2.mp3" }  
]}'
```

Response

```lua
{  
  "count": 2,  
  "id": "{playlist-id}",  
  "media": [  
    {  
      "available": true,  
      "created": 1613735618959,  
      "ext": ".mp3",  
      "id": "Audio/example file 1.mp3",  
      "name": "example file 1",  
      "path": "Audio/example file 1.mp3",  
      "size": 764176,  
      "type": "file",  
      "updated": 1613735619171  
    },  
    {  
      "available": true,  
      "created": 1613735618935,  
      "ext": ".mp3",  
      "id": "Audio/example file 2.mp3",  
      "name": "example file 2",  
      "path": "Audio/example file 2.mp3",  
      "size": 764176,  
      "type": "file",  
      "updated": 1613735619155  
    }  
  ],  
  "name": "example playlist 3"  
}
```

[Delete playlist](javascript:void(0))

Targets to delete the playlist by its identifier. The request has no response body.

```lua
curl -k -X DELETE https://{core-ip}/api/v0/cores/self/media_playlists/{playlist-id} \  
  -H "Authorization: Bearer {bearer}"
```

[Add media to a playlist](javascript:void(0))

Links new media to the playlist. It accepts only a valid media file path as `path`.

#### Single file

```lua
curl -k -X POST https://{core-ip}/api/v0/cores/self/media_playlists/{playlist-id}/media \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '{  
"path": "Audio/example file 0.mp3"  
}'
```

#### Multiple files

The payload could instead be an array to add multiple media files to the playlist in a single request.

```lua
curl -k -X POST https://{core-ip}/api/v0/cores/self/media_playlists/{playlist-id}/media \  
  -H "Authorization: Bearer {bearer}" \  
  -H "Content-Type: application/json" \  
  -d '[  
{ "path": "Audio/example file 0.mp3" },  
{ "path": "Audio/example file 1.mp3" },  
{ "path": "Audio/example file 2.mp3" }  
]'
```

Response

```lua
{  
  "count": 3,  
  "id": "{playlist-id}",  
  "media": [  
    {  
      "available": true,  
      "created": 1613735618959,  
      "ext": ".mp3",  
      "id": "Audio/example file 1.mp3",  
      "name": "example file 1",  
      "path": "Audio/example file 1.mp3",  
      "size": 764176,  
      "type": "file",  
      "updated": 1613735619171  
    },  
    // ...other media  
  ],  
  "name": "example playlist 1"  
}
```

[Remove media from a playlist](javascript:void(0))

Removes a media file link from the playlist. The request has no response body.

```lua
curl -k -X DELETE https://{core-ip}/api/v0/cores/self/media_playlists/{playlist-id}/media/Audio/example%20file%200.mp3 \  
  -H "Authorization: Bearer {bearer}"
```

[Example Script (.sh)](javascript:void(0))

Example Script: media\_playlists.sh

```lua
#!/bin/bash  
  
printf "Q-SYS Core Manager Media playlists API probe\n\n"  
  
## Info describing script usage  
  
if [ $# -lt 4 ]; then  
    printf "Script usage:\n\n"  
    printf "$0 <protocol> <core-ip> <test-file-name> <test-playlist-name> [username] [password]\n"  
    exit 1  
fi  
  
## Script parameters  
  
PROTOCOL=$1  
CORE_IP=$2  
TEST_FILE=$3  
TEST_PLAYLIST=$4  
  
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
  
## Create several test files (100KB each)  
  
for i in {1..3}; do  
  dd if=/dev/zero of=$TEST_FILE-$i.mp3 bs=1KB count=100 status=none  
done  
  
## Upload test files  
  
TEST_FILES=''  
  
for i in {1..3}; do  
  TEST_FILES+=" -F media=@$TEST_FILE-$i.mp3"  
done  
  
curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio \  
 -o /dev/null \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: multipart/form-data" \  
 $TEST_FILES  
  
# ----------------------------------------------------------------------------  
# Step 1 - create playlist  
# ----------------------------------------------------------------------------  
  
PLAYLIST_LIST_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media_playlists \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "name": "'$TEST_PLAYLIST'"  
}')  
  
printf "\n"  
  
printf "Media playlists #1: Create playlist response: $PLAYLIST_LIST_RESP\n"  
  
## Exit if Login failed  
  
if [[ $PLAYLIST_LIST_RESP != *id* ]]; then  
  printf "Playlist creation failed. The playlist probably already exists! Exiting...\n"  
  exit 1  
fi  
  
## Parse id out of response  
  
ID_REGEX='"id":"([a-f0-9\-]+)"'  
[[ $PLAYLIST_LIST_RESP =~ $ID_REGEX ]]  
PLAYLIST_ID=${BASH_REMATCH[1]}  
  
# ----------------------------------------------------------------------------  
# Step 2 - rename playlist  
# ----------------------------------------------------------------------------  
  
PLAYLIST_RENAME_RESP=$(curl -k -X PUT $PROTOCOL://$CORE_IP/api/v0/cores/self/media_playlists/$PLAYLIST_ID \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "name": "'$TEST_PLAYLIST'-renamed"  
}')  
  
printf "\n"  
  
printf "Media playlists #2: Rename playlist response: $PLAYLIST_RENAME_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 3 - add media file to the playlist  
# ----------------------------------------------------------------------------  
  
PLAYLIST_LINK_MEDIA_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media_playlists/$PLAYLIST_ID/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "path": "Audio/'$TEST_FILE-1.mp3'"  
}')  
  
printf "\n"  
  
printf "Media playlists #3: Link media response: $PLAYLIST_LINK_MEDIA_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 4 - add multiple media files to the playlist  
# ----------------------------------------------------------------------------  
  
PLAYLIST_LINK_MEDIA_RESP=$(curl -k -X POST $PROTOCOL://$CORE_IP/api/v0/cores/self/media_playlists/$PLAYLIST_ID/media \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '[  
  { "path": "Audio/'$TEST_FILE-2.mp3'" },  
  { "path": "Audio/'$TEST_FILE-3.mp3'" }  
]')  
  
printf "\n"  
  
printf "Media playlists #4: Link multiple media response: $PLAYLIST_LINK_MEDIA_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 5 - re-order media files in playlist  
# ----------------------------------------------------------------------------  
  
PLAYLIST_REORDER_MEDIA_RESP=$(curl -k -X PUT $PROTOCOL://$CORE_IP/api/v0/cores/self/media_playlists/$PLAYLIST_ID \  
 $SILENCED \  
 -H "$AUTHORIZATION" \  
 -H "Content-Type: application/json" \  
 -d '{  
  "media": [  
   { "path": "Audio/'$TEST_FILE-1.mp3'" },  
   { "path": "Audio/'$TEST_FILE-2.mp3'" },  
   { "path": "Audio/'$TEST_FILE-3.mp3'" }  
  ]  
}')  
  
printf "\n"  
  
printf "Media playlists #5: Re-order playlist media response: $PLAYLIST_REORDER_MEDIA_RESP\n"  
  
# ----------------------------------------------------------------------------  
# Step 6 - remove media files from the playlist  
# ----------------------------------------------------------------------------  
  
for i in {1..3}; do  
  curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media_playlists/$PLAYLIST_ID/media/Audio/$TEST_FILE-$i.mp3 \  
    $SILENCED \  
    -H "$AUTHORIZATION"  
done  
  
printf "\n"  
  
printf "Media playlists #6: Media unlinked from playlist\n"  
  
# ----------------------------------------------------------------------------  
# Step 7 - remove playlist  
# ----------------------------------------------------------------------------  
  
curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media_playlists/$PLAYLIST_ID \  
    $SILENCED \  
    -H "$AUTHORIZATION"  
  
printf "\n"  
  
printf "Media playlists #7: Playlist removed\n"  
  
## Delete uploaded test files  
  
for i in {1..3}; do  
  curl -k -X DELETE $PROTOCOL://$CORE_IP/api/v0/cores/self/media/Audio/$TEST_FILE-$i.mp3 \  
    $SILENCED \  
    -H "$AUTHORIZATION"  
done  
  
## Delete test files  
  
rm $TEST_FILE-*
```
