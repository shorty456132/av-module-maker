from typing import Any, Callable, Optional

from ..device import ProcessorDevice, SPDevice, eBUSDevice
from . import Interface


class DigitalIOInterface(Interface):
    """This class will provide a common interface for controlling and
    collecting data from Digital IO ports on Extron devices
    (`extronlib.device`). The user can instantiate the class directly or
    create a subclass to add, remove, or alter behavior for different types of
    devices.
    """

    def __init__(
        self,
        Host: ProcessorDevice | SPDevice | eBUSDevice,
        Port: str,
        Mode: str='DigitalInput',
        Pullup: bool=False
    ):
        """
        Parameters
        ----------
        Host : ProcessorDevice, SPDevice, eBUSDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'DIO1'``)
        Mode : str
            Possible modes are: ``'DigitalInput'`` (default), and
            ``'DigitalOutput'``
        Pullup : bool
            pull-up state on the port
        """
        pass

    def Initialize(
        self,
        Mode: Optional[str]=None,
        Pullup: Optional[bool]=None
    ) -> None:
        """Initializes Digital IO port to given values. User may provide any or
        all of the parameters.  ``None`` leaves property unmodified.

        Parameters
        ----------
        Mode : str
            Possible modes are: ``'DigitalInput'``, and ``'DigitalOutput'``
            (Default value = None)
        Pullup : bool
            pull-up state on the port (Default value = None)
        """
        pass

    def Pulse(self, duration: float) -> None:
        """Turns the port on for the specified time in seconds with 10ms
        accuracy and a 100ms minimum value.

        Parameters
        ----------
        duration : float
            pulse duration

        Examples
        --------
        ::

            OutputInterface.Pulse(0.3)
        """
        pass

    def SetState(self, State: int | str) -> None:
        """
        Parameters
        ----------
        State : int, str
            output state to be set (``'On'`` or ``1``, ``'Off'`` or ``0``)

        Examples
        --------
        ::

            OutputInterface.SetState('On')
        """
        pass

    def Toggle(self) -> None:
        """Changes the state of the IO Object to the logical opposite of the
        current state.
        """
        pass

    @property
    def Host(
        self
    ) -> eBUSDevice | ProcessorDevice | SPDevice:
        """Get the device object that hosts this interface object.

        Returns
        -------
        ProcessorDevice, SPDevice, eBUSDevice
        """
        return ProcessorDevice('')

    @property
    def Mode(self) -> str:
        """Get the mode of the Digital IO port (``'DigitalInput'``,
        ``'DigitalOutput'``).

        Returns
        -------
        str
        """
        return str()

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
        """Indicates if the port is being pulled up or not.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def State(self) -> str:
        """Get the current state of port (``'On'``, ``'Off'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def StateChanged(
        self
    ) -> Optional[Callable[['DigitalIOInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `StateChanged`
        event that triggers when the digital input state changes.

        The assigned handler must accept two positional arguments. The first
        one is the `DigitalIOInterface` instance
        triggering the event and the second is a string (``'On'`` or
        ``'Off'``).

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
        handler: Optional[Callable[['DigitalIOInterface', str], Any]]
    ) -> None:
        pass
