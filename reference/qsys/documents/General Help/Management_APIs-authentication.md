# Authentication

> Source: https://help.qsys.com/Content/Management_APIs/authentication.htm

# Authentication

Use the Authentication API endpoint to request a bearer token for other API endpoint requests, which is required if Access Control is enabled on the Q-SYS Core processor.

[Variables](javascript:void(0))

Variables are marked with curly brackets { } in request commands:

* `core-ip` : the Core's IP address
* `bearer` : the token for `/api` endpoints authentication

[Requests](javascript:void(0))

**Note:** If your client does not add the HTTP `Host` header by default, it must be provided with each request. Otherwise, the request won't pass security checks, resulting in HTTP code 406 ("Not Acceptable").

[Request a bearer token (log in)](javascript:void(0))

With the correct user credentials, this request issues a new temporary Bearer token for `/api` endpoint access. The token expires within 1 hour if the user does not perform any API requests with it. This expiration timeout is reset on every request.

```lua
curl -k -X POST https://{core-ip}/api/v0/logon \  
  -H "Accept: application/json" \  
  -H "Content-Type: application/json" \  
  -d '{  
"username": "qrcm-user",  
"password": "this-is-not-secure"  
}'
```

Response

```lua
{token: "{bearer}"}
```

Every subsequent request to the `/api` endpoints must include this token in the Authorization header. For example:

```lua
curl -k -X GET https://{core-ip}/api/v0/cores/self/users \  
  -H "Accept: application/json"  
  -H "Authorization: Bearer {bearer}"
```

[Revoke a bearer token (log out)](javascript:void(0))

This request revokes a bearer token and prevents further `/api` endpoint requests with it.

```lua
curl -k -X DELETE https://{core-id}/api/v0/logon \  
  -H "Authorization: Bearer {bearer}"
```
