from typing import Any, Callable, Optional

from ..device import ProcessorDevice, SPDevice
from . import Interface


class SWACReceptacleInterface(Interface):
    """This class provides a common interface to a switched AC power
    receptacle on an Extron product (`extronlib.device`). The user can
    instantiate the class directly or create a subclass to add, remove, or
    alter behavior for different types of devices.
    """

    def __init__(self, Host: ProcessorDevice | SPDevice, Port: str):
        """
        Parameters
        ----------
        Host : ProcessorDevice, SPDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'SAC1'``)
        """
        pass

    def SetState(self, State: int | str) -> None:
        """
        Parameters
        ----------
        State : int, string
            output state to be set (``'On'`` or ``1``, ``'Off'`` or ``0``)

        Examples
        --------
        ::

            SomeInterface.SetState('On')
        """
        pass

    def Toggle(self) -> None:
        """Changes the state of the receptacle to the logical opposite of the
        current state.
        """
        pass

    @property
    def Current(self) -> float:
        """Get the instantaneous current draw in Amperes.

        Returns
        -------
        float

        Warnings
        --------
        This property will be deprecated in a future release of ControlScript
        Pro xi. For any new development, `ProcessorDevice.CombinedCurrent`
        (`ProcessorDevice`) or `SPDevice.CombinedCurrent` (`SPDevice`) should
        be used depending on the receptacle's `Host` type.
        """
        return float()

    @property
    def CurrentChanged(
        self
    ) -> Optional[Callable[['SWACReceptacleInterface', float], Any]]:
        """``Event``: Assign or retrieve the handler for the `CurrentChanged`
        event that triggers when the current draw changes.

        The assigned handler must accept two positional arguments. The first
        one is the `SWACReceptacleInterface` instance triggering the event,
        and the second is the current.

        Returns
        -------
        Callable, None
            The assigned handler for the `CurrentChanged` event or `None`
            if no handler has been assigned.

        Warnings
        --------
        This event will be deprecated in a future release of ControlScript Pro
        xi. For any new development, `ProcessorDevice.CombinedCurrentChanged`
        (`ProcessorDevice`) or `SPDevice.CombinedCurrentChanged` (`SPDevice`)
        should be used depending on the receptacle's `Host` type.
        """
        pass

    @CurrentChanged.setter
    def CurrentChanged(
        self,
        handler: Optional[Callable[['SWACReceptacleInterface', float], Any]]
    ) -> None:
        pass

    @property
    def Host(self) -> ProcessorDevice | SPDevice:
        """Get the host device

        Returns
        -------
        ProcessorDevice, SPDevice
        """
        return ProcessorDevice('')

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
        """Get the current state of the receptacle (``'On'``, ``'Off'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def StateChanged(
        self
    ) -> Optional[Callable[['SWACReceptacleInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `StateChanged`
        event that triggers when the receptacle state changes.

        The assigned handler must accept two positional arguments. The first
        one is the `SWACReceptacleInterface` instance triggering the event,
        and the second is a string (``'On'`` or ``'Off'``).

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
                print('{} is now {}.'.format(interface.Port, state))
        """
        pass

    @StateChanged.setter
    def StateChanged(
        self,
        handler: Optional[Callable[['SWACReceptacleInterface', str], Any]]
    ) -> None:
        pass
