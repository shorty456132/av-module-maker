# API Requests

> Source: https://help.qsys.com/Content/Reflect/API_Example.htm

# API Requests

The free Q-SYS Reflect API allows you to obtain a list of Q-SYS Cores, Systems, and items with relevant status. To submit a request to the Reflect API, you can use an application (for example, [Postman](https://www.getpostman.com/)) or a cURL command line tool.

## Prerequisites

* All Reflect subscriptions include access to the Reflect API.
* To understand what requests the Reflect API supports, download the `qrem-public-api.yaml` file by right-clicking [here](https://reflect.qsc.com/static/qrem-public-api.yaml), and then save it to your PC. (Alternatively, you can download it from the API Tokens tab of the Organizations page.) Open the YAML file using any text editor to see a list of supported paths and the information returned.
* Requests must include a valid API token. Obtain an API token from the Organizations page. For more information and to get started, see [API Tokens](Organizations.htm#Tokens).

**Note:** Refer to the YAML file for the latest API support, as this feature is subject to change.

## Example: Retrieve Info About All Cores in the Organization

This example uses the [Postman](https://www.getpostman.com/) application to submit an API request to obtain a list of Q-SYS Cores (and their details) within an Organization. Refer to the YAML file for a complete list of supported requests.

[Create an API Token](javascript:void(0))

1. Log in to Q-SYS Reflect as an Organization Owner.
2. From the Q-SYS Reflect menu, click Organizations.
3. Select an Organization from the list.
4. Click API Tokens > + New Token.
5. Specify a Token Name, and then click Add.
6. Copy the token to a text file for use later.

[Obtain the Request URL](javascript:void(0))

1. Open the YAML file (`qrem-public-api.yaml`) that you downloaded from Q-SYS Reflect.
2. In the `servers` section, you'll see that the base URL for submitting API requests is `https://reflect.qsc.com/api/public/v0`. Your request will always include this URL, plus a supported path from the `paths` section.
3. You'll see that one of the supported paths is `/cores`, which retrieves information for all Q-SYS Cores within an Organization. SoOr, the complete URL for the API request is thus:

   `https://reflect.qsc.com/api/public/v0/cores`
4. Copy this URL and proceed to the next section.

[Submit the Request](javascript:void(0))

1. Open the Postman application.
2. Import the YAML file by clicking on **Import**.
3. Create and save a new Request:
   * Request Name: OrgCores
   * Request Description: "This request obtains a list of all Cores within my organization."
4. In the GET field, paste the request URL: `https://reflect.qsc.com/api/public/v0/cores`
5. Click the Authorization tab.
6. In the Type drop-down menu, select Bearer Token.
7. In the Token field, paste the token you created from Q-SYS Reflect.
8. Click Send.

[View the Results](javascript:void(0))

You should now see JSON text with a list of Q-SYS Cores in your Organization. For example:

```lua
[  
    {  
        "id": 855,  
        "serial": "3-12345A9B98CDEF9G1234GHI123JK987L2",  
        "name": "MyCore-510i",  
        "model": "Core 510i",  
        "modelNumber": "Core 510i",  
        "firmware": "8.2.0",  
        "accessMode": "open",  
        "uptime": 1570090458039,  
        "status": {  
            "code": 0,  
            "message": "Running",  
            "details": ""  
        },  
        "redundancy": null  
    },  
    {  
        "id": 858,  
        "serial": "1-2ABC01D2EF1234ZH9876GH6I123I1234",  
        "name": "MyCore-110f",  
        "model": "Core 110f",  
        "modelNumber": "Core 110f",  
        "firmware": "8.2.0",  
        "accessMode": "open",  
        "uptime": 1570138527982,  
        "status": {  
            "code": 7,  
            "message": "Offline",  
            "details": ""  
        },  
        "redundancy": null  
    }  
]
```

## Example: Retrieve Media Playlists

This example uses the [Postman](https://www.getpostman.com/) application to submit an API request to obtain media playlists from a Q-SYS Core within an Organization. Refer to the YAML file for a complete list of supported requests.

[Create an API Token](javascript:void(0))

1. Log in to Q-SYS Reflect as an Organization Owner.
2. From the Q-SYS Reflect menu, click Organizations.
3. Select an Organization from the list.
4. Click API Tokens > + New Token.
5. Specify a Token Name, and then click Add.
6. Copy the token to a text file for use later.

[Obtain the Request URL](javascript:void(0))

1. Open the YAML file (`qrem-public-api.yaml`) that you downloaded from Q-SYS Reflect.
2. In the `servers` section, you'll see that the base URL for submitting API requests is `https://reflect.qsc.com/api/public/v0`. Your request will always include this URL, plus a supported path from the `paths` section.
3. You'll see that one of the supported paths is `/cores/{coreId}/media_playlists`, which retrieves the media playlists for all users within an Organization. So, the complete URL for the API request is thus:

   `https://reflect.qsc.com/api/public/v0/cores/{coreId}/media_playlists`
4. Copy this URL and proceed to the next section.

[Submit the Request](javascript:void(0))

1. Open the Postman application.
2. Import the YAML file by clicking on **Import**.
3. Create and save a new Request:
   * Request Name: Media Playlists
   * Request Description: "This request obtains a list of all Media Playlists within my organization."
4. In the GET field, paste the request URL: `https://reflect.qsc.com/api/public/v0/cores/{coreId}/media_playlists`
5. Click the Authorization tab.
6. In the Type drop-down menu, select Bearer Token.
7. In the Token field, paste the token you created from Q-SYS Reflect.
8. Click Send.

[View the Results](javascript:void(0))

You should now see JSON text with media playlist data on your Q-SYS Core in your Organization. For example:

```lua
{  
  "id": "<uuid>",  
  "count": "<integer>",  
  "name": "<string>"  
}
```

## Example: Retrieve Users Sign In Audit Records

This example uses the [Postman](https://www.getpostman.com/) application to submit an API request to obtain sign in records of a user on a Q-SYS Core within an Organization. Refer to the YAML file for a complete list of supported requests.

[Create an API Token](javascript:void(0))

1. Log in to Q-SYS Reflect as an Organization Owner.
2. From the Q-SYS Reflect menu, click Organizations.
3. Select an Organization from the list.
4. Click API Tokens > + New Token.
5. Specify a Token Name, and then click Add.
6. Copy the token to a text file for use later.

[Obtain the Request URL](javascript:void(0))

1. Open the YAML file (`qrem-public-api.yaml`) that you downloaded from Q-SYS Reflect.
2. In the `servers` section, you'll see that the base URL for submitting API requests is `https://reflect.qsc.com/api/public/v0`. Your request will always include this URL, plus a supported path from the `paths` section.
3. You'll see that one of the supported paths is `/users/audit-events'`, which retrieves sign in information for all users within an Organization. So, the complete URL for the API request is thus:

   `https://reflect.qsc.com/api/public/v0/users/audit-events`
4. Copy this URL and proceed to the next section.

[Submit the Request](javascript:void(0))

1. Open the Postman application.
2. Import the YAML file by clicking on **Import**.
3. Create and save a new Request:
   * Request Name: Audit Events
   * Request Description: "This request obtains a list of all Audit Events within my organization."
4. In the GET field, paste the request URL: `https://reflect.qsc.com/api/public/v0/users/audit-events`
5. Click the Authorization tab.
6. In the Type drop-down menu, select Bearer Token.
7. In the Token field, paste the token you created from Q-SYS Reflect.
8. Click Send.

[View the Results](javascript:void(0))

You should now see JSON text with user sign in data on your Q-SYS Core in your Organization. For example:

```lua
{  
    "items": [  
        {  
            "id": 1652016,  
            "dateTime": "2023-08-15T13:51:49Z",  
            "message": "Jane Doe has signed in",  
            "organizationName": "Fake Hotel, LLC",  
            "siteName": "Oceanview",  
            "systemName": "Core-610-Rack1",  
            "userEmail": null,  
            "userName": "Jane Doe",  
            "userSystemRole": null,  
            "userSiteRole": null,  
            "userOrganizationRole": null  
        },  
        {  
            "id": 1651910,  
            "dateTime": "2023-08-14T21:58:35Z",  
            "message": "SpecialK has signed in",  
            "organizationName": "Fake Hotel, LLC",  
            "siteName": "Oceanview",  
            "systemName": "Core-610-Rack1",  
            "userEmail": null,  
            "userName": "John Doe",  
            "userSystemRole": null,  
            "userSiteRole": null,  
            "userOrganizationRole": null  
        },  
        {  
            "id": 1651907,  
            "dateTime": "2023-08-14T21:43:17Z",  
            "message": "John Doe has signed in",  
            "organizationName": "Fake Hotel, LLC",  
            "siteName": "Oceanview",  
            "systemName": "Core-610-Rack1",  
            "userEmail": null,  
            "userName": "John Doe",  
            "userSystemRole": null,  
            "userSiteRole": null,  
            "userOrganizationRole": null  
        },  
        {  
            "id": 1651906,  
            "dateTime": "2023-08-14T21:42:17Z",  
            "message": "John Doe has signed in",  
            "organizationName": "Fake Hotel, LLC",  
            "siteName": "Oceanview",  
            "systemName": "Core-610-Rack1",  
            "userEmail": null,  
            "userName": "John Doe",  
            "userSystemRole": null,  
            "userSiteRole": null,  
            "userOrganizationRole": null  
        },  
        {  
            "id": 1651905,  
            "dateTime": "2023-08-14T21:42:12Z",  
            "message": "John Doe has signed in",  
            "organizationName": "Fake Hotel, LLC",  
            "siteName": "Oceanview",  
            "systemName": "Core-610-Rack1",  
            "userEmail": null,  
            "userName": "John Doe",  
            "userSystemRole": null,  
            "userSiteRole": null,  
            "userOrganizationRole": null  
        },  
        {  
            "id": 1651904,  
            "dateTime": "2023-08-14T21:42:11Z",  
            "message": "John Doe has signed in",  
            "organizationName": "Fake Hotel, LLC",  
            "siteName": "Oceanview",  
            "systemName": "Core-610-Rack1",  
            "userEmail": null,  
            "userName": "John Doe",  
            "userSystemRole": null,  
            "userSiteRole": null,  
            "userOrganizationRole": null  
        }  
    ],  
    "total": 6  
}
```

## Troubleshooting

[Response: Code 401, "Unauthorized"](javascript:void(0))

If your request returns "Unauthorized", check that you are sending the correct authorization:

* Authorization Type is always Bearer Token.
* Send the complete 64-character token. The token must still be active in the Tokens list within Q-SYS Reflect.

[Response: "Not found"](javascript:void(0))

If your request returns "Not found", it means that the URL is incorrect.

* The base URL (`https://reflect.qsc.com/api/public/v0`) is not a valid URL. You must append a valid path, such as `/cores`.
* Refer to the YAML file for valid paths.
