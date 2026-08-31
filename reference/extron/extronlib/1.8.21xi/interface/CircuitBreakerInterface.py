from typing import Any, Callable, Optional

from ..device import ProcessorDevice, SPDevice
from . import Interface


class CircuitBreakerInterface(Interface):
    """This class provides a common interface to a circuit breaker on an
    Extron product (`extronlib.device`). The user can instantiate the class
    directly or create a subclass to add, remove, or alter behavior for
    different types of devices.
    """

    def __init__(
        self,
        Host: ProcessorDevice | SPDevice,
        Port: str
    ):
        """
        Parameters
        ----------
        Host : ProcessorDevice, SPDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'CBR1'``)
        """
        pass

    @property
    def Host(self) -> ProcessorDevice | SPDevice:
        """Get the device object that hosts this interface object.

        Returns
        -------
        ProcessorDevice, SPDevice
        """
        return ProcessorDevice('')

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
        """Get the current state of the circuit breaker (``'Closed'``,
        ``'Tripped'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def StateChanged(
        self
    ) -> Optional[Callable[['CircuitBreakerInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `StateChanged`
        event that triggers when the circuit breaker state changes.

        The assigned handler must accept two positional arguments. The first
        one is the `CircuitBreakerInterface` instance triggering the event and
        the second is a string (``'Closed'`` or ``'Tripped'``).

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
                if state == 'Tripped':
                    TrippedAlert()
        """
        pass

    @StateChanged.setter
    def StateChanged(
        self,
        handler: Optional[Callable[['CircuitBreakerInterface', str], Any]]
    ) -> None:
        pass
