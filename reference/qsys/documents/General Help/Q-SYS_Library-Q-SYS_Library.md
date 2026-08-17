# Q-SYS Library

> Source: https://help.qsys.com/Content/Q-SYS_Library/Q-SYS_Library.htm

# Q-SYS Library

Q-SYS Library is a one-stop hub for verified ready-to-use assets such as Q-SYS plugins, UCI templates, and sample designs.

## Accessing Q-SYS Library

There are two methods to access Q-SYS Library:

1. From Q-SYS Designer Software
2. Via web browser

**Note:** A login is not required to browse and search Q-SYS Library. If you would like to add assets to your personal account and/or write comments or reviews, you will need to click Log in. The Log in button is located in the upper right corner of Q-SYS Library, and uses your QSC ID account credentials. See Log In section for more details.

#### From Q-SYS Designer Software

In Designer, Q-SYS Library can be accessed from two locations:

* Click the Q-SYS Library icon in the toolbar.
* Click Tools, then select Open Q-SYS Library

Your web browser will then be launched opening the Q-SYS Library URL.

#### From Web Browser

Go to [https://library.qsys.com](https://library.qsys.com/).

[Q-SYS Library Toolbar](javascript:void(0))

The tools in this bar are accessible from all Q-SYS Library pages.

#### My Library

Takes you to your collection of checked out plugins.

#### Home

Returns you to the Q-SYS Library homepage.

#### Search

Takes you to the dedicated search page.

#### Help

Takes you to the Q-SYS Help topic for Q-SYS Library

#### Account

Allows you to review your Q-SYS Library account information or logout.

[Homepage](javascript:void(0))

Read below to learn about the available options on the Q-SYS Library homepage.

#### Search

Enter text here to find the desired plugin.

#### Browse by Name / Browse by Manufacturer

Takes you to the dedicated search page.

#### Featured

Shows currently highlighted plugins in the Q-SYS Library collection.

#### New Releases

Shows newly released content.

[My Library](javascript:void(0))

My Library is where you can access your checked out plugins and user packages.

[My Library](javascript:void(0))

This tab is for managing and organizing your checked out assets. It is only shown when you are logged into the site with your QSC ID.

#### Sort/Filter

Use the dropdowns to sort and filter your checked out content.

#### Name

Displays the name of checked out content.

#### Manufacturer

Displays the manufacturer of checked out content.

#### Download/Remove

* Select Download to download a .zip file of the package. You will be prompted to choose the version of the package you wish to install. This can be used when you need to downgrade an asset. You will need to unzip the file and add the assets to the proper Asset Directory folder that you have set in Q-SYS Designer preferences (default for plugins: Documents > QSC > Q-Sys Designer > Assets).
* Select Remove to remove the asset from your library. This will unsubscribe you from the asset. This does not remove the asset from the local Asset Directory on your PC, but it will no longer show up in Asset Installer if updates are released, or if the asset is uninstalled from your local PC.

[My Packages](javascript:void(0))

This tab is for managing and organizing your user packages.

#### Requirements

* NuGet Server that can be reached over the internet via HTTPS

  + Server must support NuGet v3 API
  + Feed/Package must be able to be read without credentials
* Package conforms to structure defined below

The following NuGet package managers have been tested with personal packages:

* MyGet
* Gitea

#### Package Structure

Minimum NuSpec contents used by Q-SYS Library for Personal Packages

* id - should be very unique and not conflict with other personal Packages or Q-SYS Library Packages
* version - This should follow Semantic versioning and only count up. the latest version a user has access to will be the version that they will see. NuGet Package Version Reference
* title - This will show in the Asset Installer in Q-SYS Designer Software
* icon - path to icon file in package
* iconUrl - path to public icon file accessible over the web
* description - short description of the asset

#### Sort

Use the dropdown to sort your packages.

#### Add Personal Package

Use to link to a user created package.

* Asset Name - Enter name for the asset
* Package URL - Enter URL for the package (i.e. OneDrive, Dropbox)

#### Steps to Add to your Library

1. Get your package registration URL.

   **Note:** Example: https://qsysassets.myget.org/F/bugfixing/api/v3/registration1/EugeneQsysCrossfadeRouter/index.json

   1. Go to V3 Feed URL https://qsysassets.myget.org/F/bugfixing/api/v3/index.json
   2. Grab first result with @type of RegistrationsBaseUrl
   3. Add <packageId>/index.json to end of that URL
   4. Test in a web browser, you should get json result with each version and the respective metadata
2. Navigate to Q-SYS Library
3. Log In and navigate to **My Library**.
4. On the **My Packages** tab press **Add Personal Package**.
5. Enter a name and the URL we formed in Step 1 and press **Add Package**.
6. You will see it show in the list and get a success popup.

#### Name

Displays the name of the user package.

#### Last Updated

Displays the date of the most recent update to the package.

**Note:** Packages are refreshed daily

**Note:** Packages can also be manually refreshed br hitting the menu icon on the right side of the package in the list.

[Search](javascript:void(0))

This page is used to search the Q-SYS Library for verified assets.

#### Search Field

Enter text here to find the desired asset.

#### Asset Type

Use to filter search by content type:

* CSS Style
* LUA Module
* Plugin
* Sample Design

#### Tags

Choose desired tags to filter search

#### Manufacturer

Choose available manufacturers to filter search

#### View Options

Choose how to display search results:

* Tile View
* List View

#### Sort

Use the dropdown to sort results by name, date, or manufacturer.

## Checking Out Assets

Adding plugins to your library is a simple process.

While viewing the plugin information, or plugin page, click Check Out. This will add the plugin to your library, which will make it available to install and update via Asset Installer in Q-SYS Designer 10.1 and above.
