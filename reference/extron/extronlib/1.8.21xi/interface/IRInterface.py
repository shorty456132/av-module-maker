from typing import Optional

from ..device import AdapterDevice, ProcessorDevice, SPDevice
from . import Interface


class IRInterface(Interface):
    """This class provides an interface to an IR port. This class allows the
    user to transmit IR data through an IR or IR/Serial port.

    Notes
    -----
    If an IR/Serial port is passed in and it has already been instantiated as
    an `SerialInterface`, an exception will be raised.
    """

    def __init__(
        self,
        Host: AdapterDevice | ProcessorDevice | SPDevice,
        Port: str,
        File: str
    ):
        """
        Parameters
        ----------
        Host : AdapterDevice, ProcessorDevice, SPDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            name (e.g., ``'IRS1'``, ``'IRI1'``)
        File : str
            IR file name (e.g. ``'someDevice.eir'``)

        Examples
        --------
        ::

            VCR = IRInterface(ConfRoom, 'IRS1', 'sony_14_92.eir')
        """
        pass

    def Initialize(self, File: Optional[str]=None) -> None:
        """Initializes IR port to given file.  ``None`` leaves property
        unmodified.

        Parameters
        ----------
        File : str
            IR file name (e.g. ``'someDevice.eir'``) (Default value = None)

        Examples
        --------
        ::

            VCR.Initialize('pano_14_209.eir')
        """
        pass

    def PlayContinuous(self, irFunction: str) -> None:
        """Begin playback of an IR function. Function will play continuously
        until stopped. Will complete at least one header, one body, and the
        current body.

        Parameters
        ----------
        irFunction : str
            function within the driver to play

        Notes
        -----
        *PlayContinuous* is interruptable by subsequent Play function calls
        (`PlayCount`, `PlayTime`) and `Stop`.

        Examples
        --------
        ::

            @event(VolUp, ['Pressed', 'Released'])
            def IncVolume(button, state):
                if state == 'Pressed':
                    VCR.PlayContinuous('VOL+')
                elif state == 'Released':
                    VCR.Stop()
        """
        pass

    def PlayCount(
        self,
        irFunction: str,
        repeatCount: Optional[int]=None
    ) -> None:
        """Play an IR function Count times. Function will play the header once
        and the body 1 + the specified number of repeat times.

        Parameters
        ----------
        irFunction : str
            function within the driver to play
        repeatCount : int
            number of times to repeat the body (0-15) (Default value = None)

        Notes
        -----
        * *PlayCount* is uninterruptible, except by `Stop`.
        * *repeatCount* of ``None`` means play the number defined in the
          driver.

        Examples
        --------
        ::

            VCR.PlayCount('POWER')
        """
        pass

    def PlayTime(self, irFunction: str, duration: float) -> None:
        """Play an IR function for the specified length of time. Function will
        play the header once and the body as many times as it can. Playback
        will stop when the time runs out. Current body will be completed.

        Parameters
        ----------
        irFunction : str
            function within the driver to play
        duration : float
            time in seconds to play the function

        Notes
        -----
        *PlayTime* is uninterruptible, except by `Stop`.

        Examples
        --------
        ::

            VCR.PlayTime('POWER_OFF', 0.4)
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

    def Stop(self) -> None:
        """Stop the current playback. Will complete the current body."""
        pass

    @property
    def File(self) -> str:
        """Get the file name of the IR driver.

        Returns
        -------
        str
        """
        return str()
