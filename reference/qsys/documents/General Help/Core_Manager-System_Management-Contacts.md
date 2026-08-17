# Telephony > Contacts

> Source: https://help.qsys.com/Content/Core_Manager/System_Management/Contacts.htm

# Telephony > Contacts

Use the Contacts page to create Local and LDAP contact books for use by the Contact List component, which you can then use to feed dial strings into a Softphone.

By default, Q-SYS Cores do not have any contact books configured. To get started, click Create Local Book or Create LDAP Book.

## Local Books

A Local book contains contact names that are stored on the Q-SYS Core. Select a Local book, and then click Edit to begin adding contacts.

1. Provide a unique Book Name to identify the book.
2. Click Add First Contact.
3. Type a contact Name and phone Number.
4. Click + Add Contact to continue adding more names and numbers.
5. Click Save.

## LDAP Books

An LDAP book is a connection to a networked contact list stored on an LDAP server, such as Microsoft Exchange. Select an LDAP book from the list, and then click Edit to enter the connection credentials. If you don't have your LDAP server information, contact your network administrator.

**Note:** You must enable DNS so that the Q-SYS Core can communicate with the LDAP server. When enabling DNS, specify the LDAP server IP address. Enable DNS in Q-SYS Core Manager or Q-SYS Reflect > Network Settings. For more information, see [Network > Basic](../Core_Management/Network_Settings.htm).

* Book Name: A unique name identifying this LDAP contact list.
* Server: Hostname or IP address of the LDAP server.
* User: User name for LDAP server access.
* Password: Password for LDAP server access.
* DN: Uniquely identifies an entry in the directory. A DN is made up of relative distinguished names (RDNs) of the entry and each of the entry's parent entries, up to the root of the directory tree. RDNs are usually separated by commas and optional spaces. For example: `uid=JohnDoe, ou=People, dc=company, dc=com`
* Filter: A logical expression specifying the attributes that the requested LDAP entries must have. For example: `(&(objectClass=person)(displayName=*)(ipPhone=*))`
* Display Attribute: LDAP attribute to use as the Display Name of the contact. For example: `displayName`
* Number Attribute: LDAP attribute to use as the Phone Number of the contact. For example: `ipPhone`
* Sub: When enabled, the query recursively moves down the tree.

Click Save to add the configured LDAP book to the list.
