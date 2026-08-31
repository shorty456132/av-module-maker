from ..device import ProcessorDevice, SPDevice
from . import Interface


class SWPowerInterface(Interface):
    """This is the interface class for the Switched Power ports on Extron
    devices (`extronlib.device`). The user can instantiate the class directly
    or create a subclass to add, remove, or alter behavior for different types
    of devices.
    """

    def __init__(self, Host: ProcessorDevice | SPDevice, Port: str):
        """
        Parameters
        ----------
        Host : ProcessorDevice, SPDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'SPI1'``)
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
    def Host(self) -> ProcessorDevice | SPDevice:
        """Get the host device

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
        """Get the current state of IO port (``'On'``, ``'Off'``).

        Returns
        -------
        str
        """
        return str()
