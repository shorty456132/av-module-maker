from typing import Any, Callable, Optional

from ..device import ProcessorDevice
from . import Interface


class PoEInterface(Interface):
    """This is the interface class for the Power over Ethernet ports on Extron
    devices (`extronlib.device`). The user can instantiate the class directly
    or create a subclass to add, remove, or alter behavior for different types
    of devices.
    """

    def __init__(self, Host: ProcessorDevice, Port: str):
        """
        Parameters
        ----------
        Host : ProcessorDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'POE1'``)
        """
        pass

    def SetState(self, State: int | str) -> None:
        """
        Parameters
        ----------
        State : int, str
            output state to be set (``'On'`` or ``1``, ``'Off'`` or
            ``0``)

        Examples
        --------
        ::

            OutputInterface.SetState('On')
        """
        pass

    def Toggle(self) -> None:
        """Changes the state to the logical opposite of the current state."""
        pass

    @property
    def CurrentLoad(self) -> float:
        """Get the measured power of the PoE port in watts.

        Returns
        -------
        float
        """
        return float()

    @property
    def Host(self) -> ProcessorDevice:
        """Get the device object that hosts this interface object.

        Returns
        -------
        ProcessorDevice
        """
        return ProcessorDevice('')

    @property
    def PowerStatus(self) -> str:
        """Get the state of power transmission on the port (``'Active'``,
        ``'Inactive'``).  ``'Active'`` if there is a device being powered by
        the port.

        Returns
        -------
        str
        """
        return str()

    @property
    def PowerStatusChanged(
        self
    ) -> Optional[Callable[['PoEInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `PowerStatusChanged` event that triggers when the state of power
        transmission on the port changes (e.g. a PoE device is plugged into
        the port).

        The assigned handler must accept two positional arguments. The first
        one is the `PoEInterface` instance triggering the event and the
        second one is a string (``'Active'`` or ``'Inactive'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `PowerStatusChanged` event or `None`
            if no handler has been assigned.

        Examples
        --------
        ::

            @event(poeInterface, 'PowerStatusChanged')
            def HandlePowerStatusChanged(interface, status):
                if status == 'Active':
                    LecternInUse()
                else:
                    LecternNotInUse()
        """
        pass

    @PowerStatusChanged.setter
    def PowerStatusChanged(
        self,
        handler: Optional[Callable[['PoEInterface', str], Any]]
    ) -> None:
        pass

    @property
    def Port(self) -> str:
        """Get the port name.

        Returns
        -------
        str
        """
        return str()

    @property
    def State(self) -> str:
        """Get the port state (``'On'``, ``'Off'``).

        Returns
        -------
        str
        """
        return str()
