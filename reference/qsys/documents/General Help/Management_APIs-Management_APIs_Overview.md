# Management APIs

> Source: https://help.qsys.com/Content/Management_APIs/Management_APIs_Overview.htm

# Management APIs

The following API endpoints are available on the Q-SYS Core processor for various management-related functions, including managing media content and playlists on the Core.

[How to Submit Requests](javascript:void(0))

To submit a request to these API endpoints, you can use an application (for example, [Postman](https://www.getpostman.com/)) or a cURL command line tool.

[Create an API Token](javascript:void(0))

An API "bearer" token is required when Access Control is enabled on the Core â i.e., specific Users have been created in Core Manager. This is referred to as "protected" mode. If Access Control is not enabled on the Core ("open" mode), you do not need to create a token, and API requests are submitted without an Authorization header.

**Note:** Refer to the [Authentication](authentication.htm) topic for details on what needs to be included in the request headers and body.

1. Open your API app.
2. Create a new POST request to the authentication URL. For example:

   `https://core-ip-address/api/v0/logon`
3. Verify that the appropriate headers are being sent with the request. (In Postman, this is in the Headers tab.)
4. In the request body, include your Core username and password as a JSON array. (In Postman, this is in the Body tab in raw > JSON format). For example:

   ```lua
   {  
       "username": "myusername",  
       "password": "mypassword"  
   }
   ```
5. Send the request.
6. The response is a single line that includes the token. Copy this token for subsequent API requests. For example:

   Response

   ```lua
   {  
       "token": "3e596de0251c802a34555e658a43180a748692b97278c729c5986392312ab373"  
   }
   ```

[Obtain the Request URL](javascript:void(0))

1. From the [API Endpoints](#API) section, select an endpoint â for example, Media Resources.
2. From the list of Requests, copy the URL for a request. For example, this is the URL for listing the folders and files in the root `/media` location:

   `https://core-ip-address/api/v0/cores/self/media`

[Submit the Request](javascript:void(0))

1. In your API app, create a new GET request to that URL.
2. If Access Control is enabled on the Core, configure the request to send the bearer token with it. (In Postman, this is in the Authorization tab, with "Bearer Token" as type. Paste the token into the Token field.)
3. Submit the request.

[View the Results](javascript:void(0))

You should now see a JSON-formatted response. For example, here is a response for requesting a listing of root files and folders:

Response

```lua
[  
    {  
        "path": "01 My Special Song.mp3",  
        "type": "file",  
        "name": "01 My Special Song",  
        "ext": "mp3",  
        "size": 14048450,  
        "created": 1619639517102,  
        "updated": 1619639519030,  
        "readOnly": false  
    },  
    {  
        "path": "Audio",  
        "type": "folder",  
        "name": "Audio",  
        "ext": null,  
        "size": null,  
        "created": 1511290661476,  
        "updated": 1607549583274,  
        "readOnly": true  
    },  
    {  
        "path": "Messages",  
        "type": "folder",  
        "name": "Messages",  
        "ext": null,  
        "size": null,  
        "created": 1511290661476,  
        "updated": 1614978982166,  
        "readOnly": true  
    },  
    {  
        "path": "MyFolder",  
        "type": "folder",  
        "name": "MyFolder",  
        "ext": null,  
        "size": null,  
        "created": 1619637060646,  
        "updated": 1619637060646,  
        "readOnly": false  
    },  
    {  
        "path": "PageArchives",  
        "type": "folder",  
        "name": "PageArchives",  
        "ext": null,  
        "size": null,  
        "created": 1511290661480,  
        "updated": 1551282017795,  
        "readOnly": true  
    },  
    {  
        "path": "Preambles",  
        "type": "folder",  
        "name": "Preambles",  
        "ext": null,  
        "size": null,  
        "created": 1511290661476,  
        "updated": 1511290661684,  
        "readOnly": true  
    },  
    {  
        "path": "Ringtones",  
        "type": "folder",  
        "name": "Ringtones",  
        "ext": null,  
        "size": null,  
        "created": 1511290661476,  
        "updated": 1535728270992,  
        "readOnly": true  
    },  
]
```

**Note:** If you see an "Unauthorized" response, it means you forgot to include the bearer token in the request.

[API Endpoints](javascript:void(0))

#### [Authentication](authentication.htm)

Request or revoke a bearer token for other API endpoint requests. A bearer token is required if Access Control is enabled on the Q-SYS Core processor.

#### [Media Resources](media_resources.htm)

View and manage `/media` content on the Core, including folders and files.

#### [Media Playlists](media_playlists.htm)

View and manage audio playlists on the Core
