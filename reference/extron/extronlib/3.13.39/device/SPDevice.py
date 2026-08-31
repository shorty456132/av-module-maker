from . import Device


class SPDevice(Device):
    '''
    Defines a common interface to Extron Secure Platform Products

    .. versionadded:: 3.8
    '''

    def Reboot(self):
        '''
        Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.

        .. versionadded:: 3.11
        '''
        pass

    @property
    def FirmwareVersion(self):
        '''
        :return: the firmware version of this device
        :rtype: string
        '''
        pass

    @property
    def Hostname(self):
        '''
        :return: the hostname of this device
        :rtype: string
        '''
        pass

    @property
    def IPAddress(self):
        '''
        :return: IP address of this device
        :rtype: string
        '''
        pass

    @property
    def LinkLicenses(self):
        '''
        :return: List of LinkLicense\ :sup:`®`\  part numbers.
        :rtype: list of strings
        '''
        pass

    @property
    def MACAddress(self):
        '''
        :return: MAC address of this device
        :rtype: string
        '''
        pass

    @property
    def ModelName(self):
        '''
        :return: Model name of this device
        :rtype: string
        '''
        pass

    @property
    def SerialNumber(self):
        '''
        :return: Serial number of this device
        :rtype: string
        '''
        pass

    @property
    def SystemSettings(self):
        '''
        :return: a dictionary of data describing the settings (defined in
            Toolbelt) of this device
        :rtype: dict

        .. code-block:: python
            :linenos:

            {
                'Network': {
                    'LAN': {
                        'DNSServers': ['192.168.1.1',],
                        'Gateway': '192.168.254.1',
                        'Hostname': 'ConfRoom',
                        'IPAddress': '192.168.254.250',
                        'SubnetMask': '255.255.255.0',
                        'SearchDomains': ['extron.com',],
                    },
                },
                'ProgramInformation': {
                    'Author': 'jdoe',
                    'DeviceName': 'TLP Pro 720T : 192.168.254.251',
                    'FileLoaded': 'GS Project.gs',
                    'LastUpdated': '1/23/2016 9:08:29 AM',
                    'SoftwareVersion': '1.0.2.195',
                }
            }
        '''
        pass
