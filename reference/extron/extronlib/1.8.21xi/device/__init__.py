"""This package contains libraries to interact with Extron Control Devices."""

from typing import Any, Callable, Optional


class Device():
    """The base class for all Extron devices."""

    def __init__(
        self,
        DeviceAlias: str,
        PartNumber: Optional[str] = None
    ):
        """
        Parameters
        ----------
        DeviceAlias : str
            The device alias of the Extron device.
        PartNumber : str, optional
            The part number of the Extron device, by default `None`.

        Notes
        -----
        * `DeviceAlias` must be a valid device Device Alias of an Extron
          device in the system.
        * If the part number is provided, the device will trigger a warning
          message in the program log if it does not match the connected
          device.

        Examples
        --------
        ::

            # Create Primary Processor
            ConfRoom = ProcessorDevice('Main')

            # Create Secondary Processor, Confirm Partnumber
            ConfRoom3 = ProcessorDevice('profRobertsRm', '60-1234-01')

            # Create Touch Panel
            PodiumTLP = UIDevice('Podium TLP')

            # Create System Switcher AV Device
            SystemSwitcher = SPDevice('SysSwitcher')
        """
        pass

    @property
    def DeviceAlias(self) -> str:
        """
        Get the `DeviceAlias` assigned to this object.

        Returns
        -------
        str
        """
        return str()

    @property
    def ModelName(self) -> str:
        """
        Get the `ModelName` assigned to this object.

        Returns
        -------
        str
        """
        return str()

    @property
    def Online(self) -> Optional[Callable[['Device', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Online` event.

        The assigned handler for the `Online` event must accept two positional
        arguments. The first is the instance of the `extronlib.device`
        triggering event and the second one is a string (``'Online'``).

        Raises
        ------
        TypeError
            If handler is neither `callable` nor `None`.

        Returns
        -------
        Callable, None
            The assigned handler for the `Online` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            MyDevice = ProcessorDevice("MyDevice")

            def MyOnlineHandler(device: Device, state: str) -> None:
                print("{} is now {}".format(device, state))

            # Set directly
            MyDevice.Online = MyOnlineHandler

            # Or use the `event` decorator
            @event(MyDevice, 'Online')
            def MyOnlineHandler(device: Device, state: str) -> None:
                print("{} is now {}".format(device, state))
        """
        pass

    @Online.setter
    def Online(
        self,
        handler: Optional[Callable[['Device', str], Any]]
    ) -> None:
        pass

    @property
    def Offline(self) -> Optional[Callable[['Device', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Offline` event.

        The assigned handler for the `Offline` event must accept two
        positional arguments. The first is the instance of the
        `extronlib.device` triggering event and the second one is a string
        (``'Offline'``).

        Raises
        ------
        TypeError
            If handler is neither `callable` nor `None`.

        Returns
        -------
        Callable, None
            The assigned handler for the `Offline` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            MyDevice = ProcessorDevice("MyDevice")

            def MyOfflineHandler(device: Device, state: str) -> None:
                print("{} is now {}".format(device, state))

            # Set directly
            MyDevice.Offline = MyOnlineHandler

            # Or use the `event` decorator
            @event(MyDevice, 'Offline')
            def MyOfflineHandler(device: Device, state: str) -> None:
                print("{} is now {}".format(device, state))
        """
        pass

    @Offline.setter
    def Offline(
        self,
        handler: Optional[Callable[['Device', str], Any]]
    ) -> None:
        pass

    @property
    def PartNumber(self) -> str:
        """
        Get the `PartNumber` assigned to this object.

        Returns
        -------
        str
        """
        return str()

from .AdapterDevice import AdapterDevice
from .eBUSDevice import eBUSDevice
from .ProcessorDevice import ProcessorDevice
from .SPDevice import SPDevice
from .UIDevice import UIDevice
