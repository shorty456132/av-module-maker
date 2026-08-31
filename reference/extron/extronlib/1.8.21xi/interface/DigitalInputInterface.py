from typing import Any, Callable, Optional

from ..device import AdapterDevice, UIDevice
from . import Interface


class DigitalInputInterface(Interface):
    """This class will provide a common interface for collecting data from
    Digital Input ports on Extron devices (`extronlib.device`). The user can
    instantiate the class directly or create a subclass to add, remove, or
    alter behavior for different types of devices.
    """

    def __init__(
        self,
        Host: AdapterDevice | UIDevice,
        Port: str,
        Pullup: bool=False
    ):
        """
        Parameters
        ----------
        Host : AdapterDevice, UIDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'DII1'``)
        Pullup : bool
            pull-up state on the port
        """
        pass

    def Initialize(self, Pullup: Optional[bool]=None) -> None:
        """Initializes Digital Input port to given values. User may provide
        any or all of the parameters.  ``None`` leaves property unmodified.

        Parameters
        ----------
        Pullup : bool
            pull-up state on the port (Default value = None)
        """
        pass

    @property
    def Host(self) -> AdapterDevice | UIDevice:
        """Get the device object that hosts this interface object.

        Returns
        -------
        AdapterDevice, UIDevice
        """
        return UIDevice('')

    @property
    def Port(self) -> str:
        """Get the port name this interface is attached to.

        Returns
        -------
        str
        """
        return str()

    @property
    def Pullup(self) -> bool:
        """Indicates if the Input port is being pulled up or not.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def State(self) -> str:
        """Get the current state of Input port (``'On'``, ``'Off'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def StateChanged(
        self
    ) -> Optional[Callable[['DigitalInputInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `StateChanged`
        event that triggers when the digital input state changes.

        The assigned handler must accept two positional arguments. The first
        one is the `DigitalInputInterface` instance triggering the event and
        the second is a string (``'On'`` or ``'Off'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `StateChanged` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(InputInterface, 'StateChanged')
            def HandleStateChanged(interface, state):
                if state == 'On':
                    StartCombinedInit()
                else:
                    StartSeparateInit()
        """
        pass

    @StateChanged.setter
    def StateChanged(
        self,
        handler: Optional[Callable[['DigitalInputInterface', str], Any]]
    ) -> None:
        pass
