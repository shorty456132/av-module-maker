"""
This package contains libraries for Extron hardware interfaces.

Warning
-------
1. An exception will be raised if an attempt is made to instantiate any
   physical interface more than once.  Use the Initialize or Set*
   functions to change modes where applicable.
2. Instantiating a physical interface that the control processor does not
   have, will be logged.

    * Subsequent calls to that object's methods will fail silently.
    * Subsequent calls to read that object's properties will return ``None``.
"""

from typing import Any, Callable, Optional


class Interface():

    @property
    def Offline(self) -> Optional[Callable[['Interface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Offline` event.

        The assigned handler for the `Offline` event must accept two
        positional arguments. The first one is the
        `extronlib.interface` instance triggering the event and the second one
        is a string (``'Offline'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Offline` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(SomeInterface, ['Online', 'Offline'])
            def HandleConnection(interface, state):
                print('{} is now {}'.format(interface.Port, state))
        """
        pass

    @Offline.setter
    def Offline(
        self,
        handler: Optional[Callable[['Interface', str], Any]]
    ) -> None:
        pass

    @property
    def Online(self) -> Optional[Callable[['Interface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Online` event.

        The assigned handler for the `Online` event must accept two
        positional arguments. The first one is the `extronlib.interface`
        instance triggering the event and the second one is a string
        (``'Online'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Online` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(SomeInterface, ['Online', 'Offline'])
            def HandleConnection(interface, state):
                print('{} is now {}'.format(interface.Port, state))
        """
        pass

    @Online.setter
    def Online(
        self,
        handler: Optional[Callable[['Interface', str], Any]]
    ) -> None:
        pass

from .CircuitBreakerInterface import CircuitBreakerInterface
from .ContactInterface import ContactInterface
from .DanteInterface import DanteInterface
from .DigitalInputInterface import DigitalInputInterface
from .DigitalIOInterface import DigitalIOInterface
from .EthernetClientInterface import EthernetClientInterface
from .EthernetServerInterfaceEx import ClientObject, EthernetServerInterfaceEx
from .FlexIOInterface import FlexIOInterface
from .IRInterface import IRInterface
from .PoEInterface import PoEInterface
from .RelayInterface import RelayInterface
from .RoomSchedulingInterface import CalendarEvent, RoomSchedulingInterface
from .SerialInterface import SerialInterface
from .SPInterface import SPInterface
from .SWACReceptacleInterface import SWACReceptacleInterface
from .SWPowerInterface import SWPowerInterface
from .TallyInterface import TallyInterface
from .TemperatureInterface import TemperatureInterface
from .VolumeInterface import VolumeInterface
