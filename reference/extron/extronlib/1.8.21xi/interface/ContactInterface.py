from typing import Any, Callable, Optional

from ..device import SPDevice, eBUSDevice
from . import Interface


class ContactInterface(Interface):
    """This class will provide a common interface for controlling and
    collecting data from Contact Input ports on Extron devices
    (`extronlib.device`). The user can instantiate the class directly or
    create a subclass to add, remove, or alter behavior for different types of
    devices.
    """

    def __init__(
        self,
        Host: SPDevice | eBUSDevice,
        Port: str
    ):
        """
        Parameters
        ----------
        Host : SPDevice, eBUSDevice
            handle to Extron device class that instantiated this
            interface class
        Port : str
            port name (e.g. ``'CII1'``)
        """
        pass

    @property
    def Host(self) -> eBUSDevice | SPDevice:
        """Get the device object that hosts this interface object.

        Returns
        -------
        SPDevice, eBUSDevice
        """
        return SPDevice('')

    @property
    def Port(self) -> str:
        """Get the port name this interface is attached to.

        Returns
        -------
        str
        """
        return str()

    @property
    def State(self) -> str:
        """Get the current state of IO port (``'On'``, ``'Off'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def StateChanged(
        self
    ) -> Optional[Callable[['ContactInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `StateChanged`
        event that triggers when the contact input state changes.

        The assigned handler must accept two positional arguments. The first
        one is the `ContactInterface` instance triggering the event and the
        second is a string (``'On'`` or ``'Off'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `StateChanged` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(SomeInterface, 'StateChanged')
            def HandleStateChanged(interface, state):
                if state == 'On':
                    TrippedAlert()
        """
        pass

    @StateChanged.setter
    def StateChanged(
        self,
        handler: Optional[Callable[['ContactInterface', str], Any]]
    ) -> None:
        pass
