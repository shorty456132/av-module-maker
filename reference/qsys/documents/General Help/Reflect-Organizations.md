# Organizations

> Source: https://help.qsys.com/Content/Reflect/Organizations.htm

# Organizations

In the Q-SYS Reflect hierarchy, an Organization is the entity that is registered with Reflect. In most cases, this is a company name â for example, a hotel chain, restaurant chain, and so forth. Organizations can contain one or more [Domains](Reflect_Sites/Sites.htm).

**Note:** Refer to the [Overview](Reflect_Sites/Overview.htm) topic to understand the relationship between Organizations, Domains, Systems, and Peripherals.

## Add an Organization

Before adding an Organization to Q-SYS Reflect, you must have the Subscription ID that was generated during the Reflect subscription process.

1. From the Organizations page, click + New Organization.
2. Enter your Organization Name â for example, your company name.
3. Paste the Subscription ID.
4. Click Create.

Your new Organization appears in the table. Select it to perform management tasks, including renaming the default Domain name.

## Manage an Organization

To manage an Organization:

1. Click Organizations from the Q-SYS Reflect menu.
2. Select an Organization from the table.

[Overview](javascript:void(0))

The Overview tab contains Q-SYS Reflect subscription information and lists its associated Domains.

#### Renaming and Deleting the Organization

Click Rename to choose a new Organization name. Click Delete Organization to remove the Organization from Q-SYS Reflect.

**CAUTION:** When you delete an Organization, all of its Domains, membership information, and data are also deleted.

#### Subscription Details

* Software Tier: This indicates the purchased Reflect software subscription tier. For more information, see [Q-SYS Reflect Subscriptions](Reflect_Sites/Overview.htm#Software).
* 3rd Party API: 'Yes' indicates Third-Party API access is allowed as part of your subscription. For more information, see [API Tokens](#Tokens).
* Systems: This shows the number of Q-SYS Reflect System licenses that you have Purchased as part of your subscription, as well as the number currently In Use with actively registered Q-SYS Systems.
* Prevent System license use from exceeding purchased quantity: When enabled, no additional Cores can be registered with Q-SYS Reflect if the Systems "In Use" count is already at the maximum allowed under the purchased subscription.

**Tip:** If you have recently changed your Q-SYS Reflect subscription, such as upgrading or downgrading the Software Tier or the quantity of purchased Systems, click Refresh License Info to show the latest subscription details.

#### Domains

This area lists the Domains associated with the Organization. By default, a new Organization contains a single Domain named "Domain". Click Rename to give the Domain a new name. Other actions:

* Click a Domain name to see a list of its associated Systems. For more information, see [Systems](Reflect_Sites/Systems.htm).
* To create a new Domain , click + New Domain and give it a name.
* Click Delete to remove the Domain from the Organization.

  **CAUTION:** If you delete a Domain from an Organization, all Domain membership information and data from all associated Systems is removed.

[Owners](javascript:void(0))

This tab lists all the Owners of the Organization. As an Organization Owner, you can remove other owners and invite new owners from the [Invites](#Invites) tab.

**Tip:** For more information about Reflect user roles, including Organization Owners, see [Reflect Users and Roles](Reflect_Sites/Users_Roles.htm).

[Invites](javascript:void(0))

Use the Invites tab to invite individuals to become Organization Owners.

1. Click + Invite Owner.
2. Type the individual's Email Address and optionally write a custom message.
3. Click Send Invite.

Invites remain in Pending status until the individual accepts the invitation from the email. Other actions:

* Resend Invite: If the individual did not receive the original invite, click to send another invitation email.
* Cancel Invite: Click to rescind the invitation.

  **Note:** When you cancel an invite, the individual does not receive an email indicating the cancellation. Rather, the "Accept Invitation" button within the original invitation email links to a "Invitation Link Expired" page.

[API Tokens](javascript:void(0))

Use the API Tokens tab to manage access to the Q-SYS Reflect Third-Party API. The Third-Party API allows end-user monitoring applications (for example, SolarWinds) and managed service provider tools to obtain real-time status and events information from Q-SYS Reflect.

#### Download the API File

To use the API, download the YAML file to see what API requests are supported:

1. Click Download API File, or right-click [here](https://reflect.qsc.com/static/qrem-public-api.yaml).
2. Save the `qrem-public-api.yaml` file to a location on your PC.
3. Open the YAML file in a text editor to see what API requests are supported. See [API Requests](API_Example.htm) for more information.

#### Granting API Access

To grant API access to a third-party app:

1. Click + New Token.
2. Specify a Token Name, and then click Add.
3. Click Copy to copy the token to the clipboard.

   **CAUTION:** This is the only opportunity to copy the token. Once you close window, only the last four characters of the token are visible within the list.
4. Paste the token into an API request.

### Using the Reflect API in Postman

Now that the `qrem-public-api.yaml` file is downloaded and a token is generated, use Postman to explore and send requests to the Reflect API. Follow these steps:

#### Import the YAML File into Postman

1. Open Postman.
2. In the left navigation panel, click the Collections tab.
3. Click the Import button.
4. Drag the `qrem-public-api.yaml` file into the import window.
5. Postman will automatically create a collection with all supported Reflect API requests.

#### Add Your API Token

1. In the Collections tab, click the hamburger menu next to the Reflect API collection name and select Edit.
2. Open the Authorization tab.
3. Set **Auth Type** to **Bearer Token**.
4. Paste your API token into the Token field.
5. Click Update.

**Tip:** Adding the token at the collection level applies it to all requests within the collection.

#### Save the Token as a Variable (Recommended)

1. In Postman, click the gear icon and select Manage Environments.
2. Create a new environment with a variable named `reflect_api_token`.
3. Paste your token into the value fields and save.
4. In the Authorization tab, replace the token with `{{reflect_api_token}}`.
5. Select the environment using the dropdown in the upper-right corner of Postman.

#### Confirm Authorization

* A valid request should return a success response.
* If you get 401 Unauthorized, verify the token is correct and that youâve selected the proper environment.

#### Provide coreId or systemId (If Required)

* Some API requests require a `coreId` or `systemId` as a path variable.
* These IDs can be found in your Reflect organization details.
* If omitted or incorrect, requests may return a 404 Not Found.

#### Revoking API Access

1. Select a token name from the table.
2. Click Revoke.
