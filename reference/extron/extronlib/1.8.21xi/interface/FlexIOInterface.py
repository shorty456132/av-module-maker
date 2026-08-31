from typing import Any, Callable, Optional

from ..device import ProcessorDevice
from . import Interface


class FlexIOInterface(Interface):
    """This class will provide a common interface for controlling and
    collecting data from Flex IO ports on Extron devices (`extronlib.device`).
    The user can instantiate the class directly or create a subclass to add,
    remove, or alter behavior for different types of devices.
    """

    def __init__(
        self,
        Host: ProcessorDevice,
        Port: str,
        Mode: str='DigitalInput',
        Pullup: bool=False,
        Upper: float=2.8,
        Lower: float=2.0
    ):
        """
        Parameters
        ----------
        Host : ProcessorDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'FIO1'``)
        Mode : str
            Possible modes are: ``'AnalogInput'``, ``'DigitalInput'``
            (default), and ``'DigitalOutput'``.
        Pullup : bool
            pull-up state on the port
        Upper : float
            upper threshold in volts
        Lower : float
            lower threshold in volts
        """
        pass

    def Initialize(
        self,
        Mode: Optional[str]=None,
        Pullup: Optional[bool]=None,
        Upper: Optional[float]=None,
        Lower: Optional[float]=None
    ) -> None:
        """Initializes Flex IO port to given values. User may provide any or all
        of the parameters.  ``None`` leaves property unmodified.

        Parameters
        ----------
        Mode : str
            Possible modes are: ``'AnalogInput'``, ``'DigitalInput'``, and
            ``'DigitalOutput'``. (Default value = None)
        Pullup : bool
            pull-up state on the port (Default value = None)
        Upper : float
            upper threshold in volts (Default value = None)
        Lower : float
            lower threshold in volts (Default value = None)
        """
        pass

    def Pulse(self, duration: float) -> None:
        """Turns the port on for the specified time in seconds with 10ms accuracy
        and a 100ms minimum value.

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
        """Set the output state.

        Parameters
        ----------
        State : int, string
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
    def AnalogVoltage(self) -> float:
        """Get the measured voltage applied to the port.

        Returns
        -------
        float
        """
        return float()

    @property
    def AnalogVoltageChanged(
        self
    ) -> Optional[Callable[['FlexIOInterface', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `AnalogVoltageChanged` event that triggers when the input voltage
        changes.

        The assigned handler must accept two positional arguments. The first
        one is the `FlexIOInterface` instance triggering the event and the
        second one is the voltage.

        Returns
        -------
        Callable, None
            The assigned handler for the `AnalogVoltageChanged` event or
            `None` if no handler has been assigned.

        Notes
        -----
        Minimum voltage change required to trigger event is 0.05V.
        """
        pass

    @AnalogVoltageChanged.setter
    def AnalogVoltageChanged(
        self,
        handler: Optional[Callable[['FlexIOInterface', float], Any]]
    ) -> None:
        pass

    @property
    def Host(self) -> ProcessorDevice:
        """Get the device object that hosts this interface object.

        Returns
        -------
        ProcessorDevice
        """
        return ProcessorDevice('')

    @property
    def Lower(self) -> float:
        """Get the lower threshold for digital input in volts.

        Returns
        -------
        float

        Notes
        -----
        Only applicable when Flex IO is in ``'DigitalInput'`` mode.

        """
        return float()

    @property
    def Mode(self) -> str:
        """Get the mode of the interface (``'AnalogInput'``,
        ``'DigitalInput'``, ``'DigitalOutput'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def Port(self) -> str:
        """Get the port name.

        Returns
        -------
        str
        """
        return str()

    @property
    def Pullup(self) -> bool:
        """Get the pullup state. Indicates if the input port is being pulled
        up or not.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def State(self) -> str:
        """Get the current state of the port (``'On'``, ``'Off'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def StateChanged(
        self
    ) -> Optional[Callable[['FlexIOInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `StateChanged`
        event that triggers when the digital input state changes.

        The assigned handler must accept two positional arguments. The first
        one is the `FlexIOInterface` instance triggering the event and the
        second is a string (``'On'`` or ``'Off'``).

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
        handler: Optional[Callable[['FlexIOInterface', str], Any]]
    ) -> None:
        pass

    @property
    def Upper(self) -> float:
        """Get the upper threshold for digital input in volts.

        Returns
        -------
        float

        Notes
        -----
        Only applicable when Flex IO is in ``'DigitalInput'`` mode.
        """
        return float()
