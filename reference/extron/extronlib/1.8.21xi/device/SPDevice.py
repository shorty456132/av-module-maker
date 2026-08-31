from typing import Any, Callable, List, Optional

from . import Device


class SPDevice(Device):
    """Defines a common interface to Extron Secure Platform Products"""

    def Reboot(self) -> None:
        """Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.
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
        This only applies to *SPDevice* featuring switched AC receptacles. It
        returns ``None`` otherwise.
        """
        pass

    @property
    def CombinedCurrentChanged(
        self
    ) -> Optional[Callable[['SPDevice', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `CombinedCurrentChanged` event that triggers when the switched AC
        power receptacle current draw changes.

        The assigned handler for the `CombinedCurrentChanged` event must
        accept exactly two positional arguments.  The first is the `SPDevice`
        that triggers the event and the second is the new current in Amperes
        as a float (e.g. ``10.5``).

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

            @event(spdevice, 'CombinedCurrentChanged')
            def HandleCombinedCurrent(device, current):
                print('Current draw changed to {}.'.format(current))
        """
        pass

    @CombinedCurrentChanged.setter
    def CombinedCurrentChanged(
        self,
        handler: Optional[Callable[['SPDevice', float], Any]]
    ) -> None:
        pass

    @property
    def CombinedLoadState(self) -> str:
        """Get the current power limit state. One of ``'Normal'``,
        ``'Limit'``, or ``'Over'``.

        .. versionadded:: 1.2

        Returns
        -------
        str

        Notes
        -----
        This only applies to `SPDevice` featuring DC power outputs. It returns
        ``None`` otherwise.
        """
        return str()

    @property
    def CombinedLoadStateChanged(
        self
    ) -> Optional[Callable[['SPDevice', str], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `CombinedLoadStateChanged` event that triggers when the combined load
        state changes.

        The assigned handler for the `CombinedLoadStateChanged` event must
        accept two positional arguments. The first is the `SPDevice` that
        triggers the event and the second is the new load state (e.g.
        ``'Normal'``).

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
        handler: Optional[Callable[['SPDevice', str], Any]]
    ) -> None:
        pass

    @property
    def CombinedWattage(self) -> float:
        """Get the current power usage across all DC power outputs in watts.

        .. versionadded:: 1.2

        Returns
        -------
        float

        Notes
        -----
        This only applies to `SPDevice` featuring DC power outputs. It returns
        ``None`` otherwise.
        """
        return float()

    @property
    def CombinedWattageChanged(
        self
    ) -> Optional[Callable[['SPDevice', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `CombinedWattageChanged` event that triggers when the DC power usage
        changes.

        The assigned handler for the `CombinedWattageChanged` event must
        exactly two positional arguments, which are the `SPDevice` that
        triggers the event and the second is the new power usage in watts as a
        float (e.g. ``10.5``).

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
        handler: Optional[Callable[['SPDevice', float], Any]]
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
        """Get the IP Address of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def LinkLicenses(self) -> List[str]:
        """Get the list of LinkLicense® part numbers applied to this
        device.

        Returns
        -------
        list of strings
        """
        return [str()]

    @property
    def MACAddress(self) -> str:
        """Get the MAC Address of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def ModelName(self) -> str:
        """Get the model name of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def SerialNumber(self) -> str:
        """Get the serial number of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def SystemSettings(self) -> dict:
        """Get a dictionary of data describing the settings (defined in
        Toolbelt) of this device.

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
                },
                'ProgramInformation': {
                    'Author': 'jdoe',
                    'DeviceName': 'TLP Pro 720T : 192.168.254.251',
                    'FileLoaded': 'GS Project.gs',
                    'LastUpdated': '1/23/2016 9:08:29 AM',
                    'SoftwareVersion': '1.0.2.195',
                }
            }
        """
        return dict()
