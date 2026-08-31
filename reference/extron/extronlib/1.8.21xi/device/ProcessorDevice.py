from typing import Any, Callable, List, Optional, Tuple

from . import Device


class ProcessorDevice(Device):
    """Defines common interface to Extron Control Processors"""

    def Reboot(self) -> None:
        """Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.

        Warning
        -------
        Any unsaved data will be lost, including Program Log. Follow the
        example below.

        Examples
        --------
        ::

            from extronlib.system import File, SaveProgramLog
            from datetime import datetime

            # Save the ProgramLog for later inspection.
            dt = datetime.now()
            filename = 'ProgramLog {}.txt'.format(dt.strftime('%Y-%m-%d %H%M%S'))

            with File(filename, 'w') as f:
                SaveProgramLog(f)

            device.Reboot()
        """
        pass

    def SetExecutiveMode(self, ExecutiveMode: int) -> None:
        """Sets the desired Executive Mode.

        Parameters
        ----------
        ExecutiveMode : int
            The mode to set. 0 to *n*.

        Notes
        -----
        See product manual for list of available modes.
        """
        pass

    @property
    def CombinedCurrent(self) -> float | None:
        """Get the instantaneous current draw across all switched AC power
        receptacles in Amperes.

        .. versionadded:: 1.2

        Returns
        -------
        float

        Notes
        -----
        This only applies to *ProcessorDevice* featuring switched AC
        receptacles. It returns ``None`` otherwise.
        """
        pass

    @property
    def CombinedCurrentChanged(
        self
    ) -> Optional[Callable[['Device', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `CombinedCurrentChanged` event that triggers when the switched AC
        power receptacle current draw changes.

        The assigned handler must accept exactly two parameters, which are the
        `ProcessorDevice` that triggers the event and the new current in
        Amperes as a float (e.g. ``10.5``).

        .. versionadded:: 1.2

        Returns
        -------
        Callable, None
            The assigned handler for the `CombinedCurrentChanged` event or
            `None` if no handler has been assigned.

        Notes
        -----
        This event triggers for each 0.1 Amp change but no more than once
        every 10 seconds if the current draw is oscillating.

        Examples
        --------
        ::

            @event(proc, 'CombinedCurrentChanged')
            def HandleCombinedCurrent(device, current):
                print('Current draw changed to {}.'.format(current))
        """
        pass

    @CombinedCurrentChanged.setter
    def CombinedCurrentChanged(
        self,
        handler: Optional[Callable[['Device', float], Any]]
    ) -> None:
        pass

    @property
    def CombinedLoadState(self) -> str:
        """Get the present power limit state. One of ``'Normal'``,
        ``'Limit'``, or ``'Over'``.

        .. versionadded:: 1.2

        Returns
        -------
        str

        Notes
        -----
        This only applies to *ProcessorDevice* featuring DC power outputs. It
        returns ``None`` otherwise.
        """
        return str()

    @property
    def CombinedLoadStateChanged(
        self
    ) -> Optional[Callable[['Device', str], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `CombinedLoadStateChanged` event that triggers when the combined load
        state changes.

        The assigned handler must accept exactly two parameters, which are the
        `ProcessorDevice` that triggers the event and the the new load state
        (e.g. ``'Normal'``).

        .. versionadded:: 1.2

        Returns
        -------
        Callable, None
            The assigned handler for the `CombinedLoadStateChanged` event or
            `None` if no handler has been assigned.

        Examples
        --------
        ::

            @event(proc, 'CombinedLoadStateChanged')
            def HandleCombinedLoad(device, LoadState):
                print('Load state changed to {}.'.format(LoadState))
        """
        pass

    @CombinedLoadStateChanged.setter
    def CombinedLoadStateChanged(
        self,
        handler: Optional[Callable[['Device', str], Any]]
    ) -> None:
        pass

    @property
    def CombinedWattage(self) -> float:
        """Get the present power usage across all DC power outputs in watts.

        .. versionadded:: 1.2

        Returns
        -------
        float

        Notes
        -----
        This only applies to *ProcessorDevice* featuring DC power
        outputs. It returns ``None`` otherwise.
        """
        return float()

    @property
    def CombinedWattageChanged(
        self
    ) -> Optional[Callable[['Device', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `CombinedWattageChanged` event that triggers when the DC power usage
        changes.

        The assigned handler must accept exactly two parameters, which are the
        `ProcessorDevice` that triggers the event and the new power usage in
        watts as a float (e.g. ``10.5``).

        .. versionadded:: 1.2

        Returns
        -------
        Callable, None
            The assigned handler for the `CombinedWattageChanged` event or
            `None` if no handler has been assigned.

        Notes
        -----
        This event triggers for each 0.1 watt change but no more than once
        every 10 seconds if the power usage is oscillating.

        Examples
        --------
        ::

            @event(proc, 'CombinedWattageChanged')
            def HandleCombinedWattage(device, CombinedWattage):
                print('Power usage changed to {}.'.format(CombinedWattage))
        """
        pass

    @CombinedWattageChanged.setter
    def CombinedWattageChanged(
        self,
        handler: Optional[Callable[['Device', float], Any]]
    ) -> None:
        pass

    @property
    def CurrentLoad(self) -> float:
        """Get the current load across all DC power outputs in watts.

        Returns
        -------
        float

        Warnings
        --------
        This method will be deprecated in a future release of ControlScript.
        For any new development, `CombinedWattage` should be used.

        Notes
        -----
        This only applies to *ProcessorDevice* featuring DC power outputs. It
        returns ``None`` otherwise.
        """
        return float()

    @property
    def ExecutiveMode(self) -> int:
        """Get the current executive mode number.

        Returns
        -------
        int
        """
        return int()

    @property
    def ExecutiveModeChanged(
        self
    ) -> Optional[Callable[['ProcessorDevice', int], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `ExecutiveModeChanged` event that triggers when executive mode
        changes.

        The assigned handler must accept exactly two positional arguments. The
        first is the `ProcessorDevice` instance triggering the event and the
        second is the executive mode number.

        Returns
        -------
        Callable, None
            The assigned handler for the `ExecutiveModeChanged` event or
            `None` if no handler has been assigned.

        Examples
        --------
        ::

            @event(proc, 'ExecutiveModeChanged')
            def HandleExecutiveMode(device, ExecutiveMode):
                print('Executive mode changed to {}.'.format(ExecutiveMode))
        """
        pass

    @ExecutiveModeChanged.setter
    def ExecutiveModeChanged(
        self,
        handler: Optional[Callable[['ProcessorDevice', int], Any]]
    ) -> None:
        pass

    @property
    def FirmwareVersion(self) -> str:
        """Get the firmware version of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def Hostname(self) -> str:
        """Get the hostname of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def IPAddress(self) -> str:
        """Get the IP address of this device.

        Returns
        -------
        str

        Notes
        -----
        For control processors with AV LAN, the LAN address is returned.
        """
        return str()

    @property
    def LinkLicenses(self) -> List[str]:
        """Get a list of LinkLicense® part numbers.

        Returns
        -------
        list of str
        """
        return [str()]

    @property
    def MACAddress(self) -> str:
        """Get the MAC address of this device

        Returns
        -------
        str

        Notes
        -----
        For control processors with AV LAN, the LAN address is returned.
        """
        return str()

    @property
    def SerialNumber(self) -> str:
        """Get the serial number of this device

        Returns
        -------
        str
        """
        return str()

    @property
    def SystemSettings(self) -> dict:
        """Get a dictionary of data describing the settings (defined in
        Toolbelt) of this device

        .. versionadded:: 1.4
            'Mode' property added to 'NTPSettings'.

        .. versionadded:: 1.7
            'Gateway' property added to 'Network.AVLAN' when applicable.
            'Servers' property added to 'NTPSettings'.

        .. warning::

            .. deprecated:: 1.7
                The 'Server' property will be removed in a future version. Please
                use the 'Servers' property which supports multiple servers.

        Returns
        -------
        dict

        Examples
        --------
        ::

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
                        'Gateway': '192.168.253.1',
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
                        'Enabled': True,                # NTP cannot be disabled
                        'Mode': 'Automatic',            # Manual or Automatic
                        'Server': '192.168.254.101',    # '127.127.1.0' if Mode == Manual
                        'Servers': ['192.168.254.101', 'time.example.com'],
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
        """
        return dict()

    @property
    def UserUsage(self) -> Tuple[int, int]:
        """Get the user data usage of this device in KB ``(used, total)``.

        Returns
        -------
        tuple of int
        """
        return int(), int()
