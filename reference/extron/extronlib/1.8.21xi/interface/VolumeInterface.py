from ..device import ProcessorDevice
from . import Interface


class VolumeInterface(Interface):
    """This class will provide a common interface for controlling and
    collecting data from Volume Ports on Extron devices (`extronlib.device`).
    The user can instantiate the class directly or create a subclass to add,
    remove, or alter behavior for different types of devices.
    """

    def __init__(self, Host: ProcessorDevice, Port: str):
        """
        Parameters
        ----------
        Host : ProcessorDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'VOL1'``)

        Examples
        --------
        ::

            ConfRoom = ProcessorDevice('ConfRoom 250')
            VolumeConfRoom = VolumeInterface(ConfRoom, 'VOL1')
        """
        pass

    def SetLevel(self, Level: int) -> None:
        """Sets Level of volume control port

        Parameters
        ----------
        Level : int
            Level (0 % <= Value <= 100 %).

        Examples
        --------
        ::

            currentLevel = 0

            @event(Inc, ['Pressed', 'Repeated'])
            def IncVolume(button, state):
                global currentLevel
                if currentLevel >= 100:
                    return
                currentLevel += 1
                VolumeConfRoom.SetLevel(currentLevel)

            @event(Dec, ['Pressed', 'Repeated'])
            def DecVolume(button, state):
                global currentLevel
                if currentLevel <= 0:
                    return
                currentLevel -= 1
                VolumeConfRoom.SetLevel(currentLevel)
        """
        pass

    def SetMute(self, Mute: str) -> None:
        """Sets the mute state.

        Parameters
        ----------
        Mute : str
            mute state (``'On'``, ``'Off'``).
        """
        pass

    def SetRange(self, Min: float | int, Max: float | int) -> None:
        """Set volume control object's voltage range.

        Parameters
        ----------
        Min : float, int
            minimum voltage
        Max : float, int
            maximum voltage

        Examples
        --------
        ::

            VolumeConfRoom.SetRange(1, 7.5)   # Voltage
        """
        pass

    def SetSoftStart(self, SoftStart: str) -> None:
        """Enable or Disable Soft Start.

        Parameters
        ----------
        SoftStart : str
            Soft Start state (``'Enabled'``, ``'Disabled'``).

        Examples
        --------
        ::

            VolumeConfRoom.SetSoftStart('Enabled')
        """
        pass

    @property
    def Host(self) -> ProcessorDevice:
        """Get the host device.

        Returns
        -------
        ProcessorDevice
        """
        return ProcessorDevice('')

    @property
    def Level(self) -> int:
        """Get the current volume level (percentage).

        Returns
        -------
        int
        """
        return int()

    @property
    def Max(self) -> float:
        """Get the maximum level (0.0 V < Max <= 10.0 V).

        Returns
        -------
        float
        """
        return float()

    @property
    def Min(self) -> float:
        """Get the minimum level (0.0 V <= Min < 10.0 V).

        Returns
        -------
        float
        """
        return float()

    @property
    def Mute(self) -> str:
        """Get the current state of volume port mute.  (``'On'``, ``'Off'``)

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
    def SoftStart(self) -> str:
        """Get the current state of Soft Start. (``'Enabled'``,
        ``'Disabled'``).

        Returns
        -------
        str
        """
        return str()
