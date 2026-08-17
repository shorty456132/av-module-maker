# Software Requirements

> Source: https://help.qsys.com/Content/Q-SYS_Compatibility/Software_Requirements.htm

# Software Requirements

For software and firmware updates, see the QSC [Software and Firmware](https://www.qsys.com/resources/software-and-firmware/) page.

[Host Operating System](javascript:void(0))

**Note:** Before installing Q-SYS apps, ensure that your Windows operating system is fully updated via [Windows Update](https://support.microsoft.com/en-us/windows/get-the-latest-windows-update-7d20e88c-0568-483a-37bc-c3885390d212). This step is crucial to ensure compatibility and optimal performance.

* Windows 11 Pro
* Windows 11 Home (version 21H2) x64

[Display](javascript:void(0))

If you are using a high DPI monitor resolution, such as 4K60, you might need to adjust the Windows Compatibility settings so that Q-SYS Designer Software displays properly:

1. Right-click the Designer shortcut on the desktop and select Properties.
2. In the Compatibility tab, click the "Change high DPI settings" button.
3. In the DPI settings window, select the following:
   * Select "Use this setting to fix scaling problems...".
   * In the "Use the DPI..." drop-down menu, select "I open this program".
   * Select "Override high DPI scaling behavior".
   * In the "Scaling performed by" drop-down menu, select "Application".

[Virtual Environment](javascript:void(0))

Q-SYS Designer Software (QDS) has been tested to work when running in a virtual Windows 11 environment via the Parallels Desktop for Mac hypervisor. Use the following test environment and settings as a guideline for your setup.

[Windows 11](javascript:void(0))

### Mac Hardware

* MacBook Pro with M3 Chip
* 8 GB RAM
* MacOS Version: Sonoma 14.1
* Parallels Desktop 19.3

### Windows Virtual Environment

* Windows 11 (64 bit)
* Processor: 3.2 GHz x 4 Cores
* RAM: 4 GB (Dynamic allocation)

### Other Notes

* For full functionality of QDS features, the hypervisor must have native support for WebGL.
* For complex designs or those requiring more resources, allocating 8 GB of RAM is functional but may result in slower performance with large designs. It is recommended to allocate 16 GB of RAM for smoother operation.
* Ensure sleep settings are disabled in the Windows virtual environment to preserve RDP access.
* If there is no intention to use RDP, default sleep/Energy Saver settings may be left as is.
* After any network setting changes, such as switching network NICs, a restart of Parallels is required.
* Hard Links functionality has been tested and confirmed to work in the Windows 11 virtual environment.
* MacOS Big Sur (11.1) has not been tested by QSC as a host MacOS version for a virtual Windows installation.

[Installation Dependencies](javascript:void(0))

The Q-SYS Designer and Q-SYS Administrator installation programs automatically install the following components if not currently installed on the Windows PC. Internet access is required to download these dependencies.

* Microsoft .NET Framework 8.0
* Microsoft Visual C++ Runtime 14.40 (2015-2024)

[Web Browser](javascript:void(0))

These web browsers are tested to work with Q-SYS Core Manager and Q-SYS Reflect on Windows, MacOS, and Linux:

* Microsoft Edge
* Mozilla Firefox
* Google Chrome
* Apple Safari

**Note:** Internet Explorer is not supported.
