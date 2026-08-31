from ..device import AdapterDevice, ProcessorDevice, SPDevice
from . import Interface


class RelayInterface(Interface):
    """This class provides a common interface for controlling relays on Extron
    devices (`extronlib.device`).  The user can instantiate the class directly
    or create a subclass to add, remove, or alter behavior for different types
    of devices.
    """

    def __init__(
        self,
        Host: AdapterDevice | ProcessorDevice | SPDevice,
        Port: str
    ):
        """
        Parameters
        ----------
        Host : AdapterDevice, ProcessorDevice, SPDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'RLY1'``)
        """
        pass

    def Pulse(self, duration: float | int) -> None:
        """Turns the port on for the specified time in seconds with 10ms accuracy
        and a 100ms minimum value.

        Parameters
        ----------
        duration : float, int
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
            output state to be set (``'Close'`` or ``1``, ``'Open'`` or
            ``0``)

        Examples
        --------
        ::

            Relay1.SetState('Close')
        """
        pass

    def Toggle(self) -> None:
        """Changes the state of the IO Object to the logical opposite of the
        current state.
        """
        pass

    @property
    def Host(self) -> AdapterDevice | ProcessorDevice | SPDevice:
        """Get the device object that hosts this interface object.

        Returns
        -------
        AdapterDevice, ProcessorDevice, SPDevice
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
        """Get the current port state (``'Close'``, ``'Open'``).

        Returns
        -------
        str
        """
        return str()
