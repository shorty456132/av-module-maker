from . import Device


class ProcessorDevice(Device):
    '''Defines common interface to Extron Control Processors'''

    def Reboot(self):
        '''
        Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.

        .. warning:: Any unsaved data will be lost, including Program Log.
            Follow the example below.

        .. code-block:: python
            :linenos:

            from extronlib.system import File, SaveProgramLog
            from datetime import datetime

            # Save the ProgramLog for later inspection.
            dt = datetime.now()
            filename = 'ProgramLog {}.txt'.format(dt.strftime('%Y-%m-%d %H%M%S'))

            with File(filename, 'w') as f:
                SaveProgramLog(f)

            device.Reboot()

        .. versionadded:: 3.11
        '''
        pass

    def SetExecutiveMode(self, ExecutiveMode):
        '''
        Sets the desired Executive Mode.

        .. note:: See product manual for list of available modes.

        :param ExecutiveMode: The mode to set. 0 to *n*.
        :type ExecutiveMode: int

        .. versionadded:: 3.1
        '''
        pass

    @property
    def CurrentLoad(self):
        '''
        :return: the current load of 12V DC power supply in watts
        :rtype: float

        .. note:: This only applies to *ProcessorDevice* featuring 12V DC power
            supply. It returns ``None`` otherwise.
        '''
        pass

    @property
    def ExecutiveMode(self):
        '''
        :return: The current executive mode number.
        :rtype: int

        .. versionadded:: 3.1
        '''
        pass

    @property
    def ExecutiveModeChanged(self):
        '''
        ``Event:`` Triggers when executive mode changes.

        The callback takes two arguments. The first is the
        :py:mod:`extronlib.device` instance triggering the event and the
        second is the executive mode number.

        .. code-block:: python

            @event(proc, 'ExecutiveModeChanged')
            def HandleExecutiveMode(device, ExecutiveMode):
                print('Executive mode changed to {}.'.format(ExecutiveMode))

        .. versionadded:: 3.1
        '''
        pass

    @property
    def FirmwareVersion(self):
        '''
        :return: the firmware version of this device
        :rtype: string

        .. versionadded:: 2.4
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

        .. note:: For control processors with AV LAN, the LAN address is
            returned.
        '''
        pass

    @property
    def LinkLicenses(self):
        '''
        :return: List of LinkLicense\ :sup:`®`\  part numbers.
        :rtype: list of strings

        .. versionadded:: 2.6
        '''
        pass

    @property
    def MACAddress(self):
        '''
        :return: MAC address of this device
        :rtype: string

        .. note:: For control processors with AV LAN, the LAN address is
            returned.

        .. versionadded:: 2.4
        '''
        pass

    @property
    def SerialNumber(self):
        '''
        :return: Serial number of this device
        :rtype: string

        .. versionadded:: 2.4
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
                    'AVLAN': {
                        'DHCPServer': 'Off',
                        'DNSServers': ['192.168.1.1',],
                        'Hostname': 'ConfRoom',
                        'IPAddress': '192.168.253.251',
                        'SubnetMask': '255.255.255.0',
                        'SearchDomains': ['extron.com',],
                    },
                },
                'MailServer': {
                    'IPAddress': '192.168.254.100',
                    'SMTPPort': 25,
                    'SSLEnabled': True,
                    'UserID': 'jdoe',
                },
                'DateTime': {
                    'NTPSettings': {
                        'Enabled': True,
                        'Server': '192.168.254.101',    # '' if Enable == False
                    },
                    'TimeZone': '(UTC-08:00/UTC-07:00) Pacific Time',
                }
                'ProgramInformation': {
                    'Author': 'jdoe',
                    'DeviceName': 'IPCP Pro 550 : 192.168.254.250',
                    'FileLoaded': 'GS Project.gs',
                    'LastUpdated': '1/23/2016 9:08:29 AM',
                    'SoftwareVersion': '1.0.2.195',
                }
            }

        .. versionadded:: 3.6
        '''
        pass

    @property
    def UserUsage(self):
        '''
        :return: user data usage of this device in KB ``(used, total)``.
        :rtype: tuple of ints

        .. versionadded:: 2.4
        '''
        pass
