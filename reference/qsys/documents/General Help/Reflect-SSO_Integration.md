# Identity Provider Setup â Federated SSO

> Source: https://help.qsys.com/Content/Reflect/SSO_Integration.htm

# Identity Provider Setup â Federated SSO

Read this topic to understand the requirements for integrating a corporate identity or SSO provider into QSC ID. Once integration is complete, users can seamlessly access QSC and Q-SYS services using their familiar corporate login credentials. This not only enhances security by centralizing identity management through your existing corporate policies, but also simplifies user provisioning, revocation, and ongoing maintenance. As a result, managing access is more efficient, and end users benefit from a consistent, streamlined login experience across QSCâs ecosystem, including Q-SYS Reflect.

## Process

To set up corporate IDP integration with QSC ID:

1. Go to the Q-SYS Knowledge Base at [support.qsys.com](https://support.qsys.com/).
2. Click Contact Support > Create a Case.
3. Log into the Self Help Portal using your QSC ID, and then click Create a Case.
4. Fill out the following fields first:
   * **Subject**: Enter the subject of your inquiry.
   * **Geographic Location**: Select your location from the dropdown.
   * **Type**: Choose "SSO Integration Request" from the dropdown.
   * **Timezone**: Select your timezone.
   * **Phone**: Enter your phone number.
   * **Product**: Search for or select the relevant product.
   * **Serial #**: Enter the serial number, if applicable.
   * **Customer Sales Order / RMA #**: Enter this number, if applicable.
5. In the **Description** field, provide these details:
   * Email domains of the IDP.
   * SSO service â for example: Azure Active Directory, Google OAuth, Okta, etc.
   * SSO protocol â QSC ID supports OpenID Connect and SAML 2.0:

   [OpenID Connect](javascript:void(0))

   **Note:** When creating a case, include only the most basic information necessary. Avoid sharing any user-specific details, such as Client ID or Client Secret. Once your case is created, QSC will provide a secure method to obtain and encrypt any additional information needed.

   For OpenID Connect services, you must provide:

   * Well-known Endpoint / Discovery Endpoint
   * Client ID
   * Client Secret

   [SAML 2.0](javascript:void(0))

   For SAML 2.0 services, you must provide:

   * Single Sign-On Service URL.
   * User's email as an assertion in the SAML response and what the assertion name for email will be.
   * What will be the NameID, whether it will be sent with an SPNameQualifier and/or NameQualifier attribute, and if so, what the value(s) of those attribute(s) that are sent will be.
   * Either the SAML metadata document or a URL pointed to a persistent copy of the SAML metadata document.
   * If the IDP supports signing both SAML response messages and assertions, and whether it supports assertion encryption.

   **Note:** If the SAML document is saved statically, any changes to our certificates will require manual updates to avoid breaking the federation. Saving the document dynamically ensures they are automatically updated, preventing disruptions.
6. Submit the new case.
7. After the case is submitted, you will receive an email from QSC, requesting additional information required for the setup. We also might reach out to schedule time to setup the configuration, if needed.

   [Example Email](javascript:void(0))

   Dear {!Contact.FirstName},

   Thank you for reaching out to us with your interest in integrating Single Sign-On (SSO) between our two businesses. To ensure a smooth and efficient integration process, we need to gather some preliminary information.

   Please provide the following details for setting up the SSO integration. You can fill out the information next to each item listed below and reply-all back to us. Due to the sensitive nature of the information, we ask that you send the Client ID and Client Secret in a secure encrypted email.

   Please review the instructions for either SAML 2.0 or OpenID Connect/OAuth (OIDC) below:

   **SAML 2.0:**

   1. Please provide us with the following:
      * Your SAML metadata document. It can be a URL or an XML document.
      * A list of assertions/claims that your platform will send to QSC in its SAML response, including the specific identifiers for each. At minimum, this must include a unique identifier for each user (as the subject NameID) and the user's email address.
      * Whether your identity provider will send the "SPNameQualifier" or "NameQualifier" attributes on the subject NameID in its SAML response, and if so, what the value of these attributes will be.
   2. Once received, we will provide you with our metadata URL.
   3. Configure the SAML relationship on your side.

   **OpenID Connect/OAuth (OIDC):**

   1. Create an application ID and secret, using the Redirect URL.
   2. Please provide us with the following:
      * OpenID Connect well-known metadata URL: [Your OAuth URL]
      * Client ID: [Your Client ID]
      * Client Secret: [secure channel for this information]
   3. A list of assertions/claims that your application will emit (Minimum: unique ID for the user, user's email address)

   Once we receive your request, we will configure the SSO on our side. If required, our team might reach out to schedule a call to discuss further steps, including testing and validation.

   We appreciate your reaching out to us and are looking forward to facilitating a successful SSO integration. Should you have any questions or need assistance, please do not hesitate to reach out to our team by responding to this email.
8. QSC will reply with a Redirect URI to be whitelisted (if using OpenID Connect) or the SAML metadata document URL (if using SAML 2.0).
