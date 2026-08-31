from re import Pattern
from typing import Any, Callable, Optional

from ..device import AdapterDevice, ProcessorDevice, SPDevice
from . import Interface


class SerialInterface(Interface):
    """This class provides an interface to a serial port. This class allows
    the user to send data over the serial port in a synchronous or
    asynchronous manner. This class is used for all ports capable of serial
    communication (e.g., Serial Ports, IR Serial Ports).

    Notes
    -----
    * `SendAndWait` can be used to synchronously capture responses.
    * For asynchronous communication, a handler function is assigned to the
      `ReceiveData` event. Then responses and unsolicited messages will be
      sent to the user's `ReceiveData` handler.
    * `SendAndWait` cannot be called within the context of a `ReceiveData`
      event.
    * Using `SendAndWait` while unsolicited data transmission is possible, may
      cause data loss.
    * If an IR/Serial port is passed in and it has already been instantiated
      as an `IRInterface`, an exception will be raised.
    """

    def __init__(
        self,
        Host: AdapterDevice | ProcessorDevice | SPDevice,
        Port: str,
        Baud: int=9600,
        Data: int=8,
        Parity: str='None',
        Stop: int=1,
        FlowControl: str='Off',
        CharDelay: float | int=0,
        Mode: str='RS232'
    ):
        """
        Parameters
        ----------
        Host : AdapterDevice, ProcessorDevice, SPDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g., ``'COM1'``, ``'IRS1'``)
        Baud : int
            baudrate
        Data : int
            number of data bits
        Parity : str
            ``'None'``, ``'Odd'`` or ``'Even'``
        Stop : int
            number of stop bits
        FlowControl : str
            ``'HW'``, ``'SW'``, or ``'Off'``
        CharDelay : float, int
            time between each character sent to the connected device
        Mode : str
            mode of the port, ``'RS232'``, ``'RS422'`` or ``'RS485'``
        """
        pass

    def Initialize(
        self,
        Baud: Optional[int]=None,
        Data: Optional[int]=None,
        Parity: Optional[str]=None,
        Stop: Optional[int]=None,
        FlowControl: Optional[str]=None,
        CharDelay: Optional[float | int]=None,
        Mode: Optional[str]=None
    ) -> None:
        """Initializes Serial port to given values. User may provide any or all of
        the parameters.  ``None`` leaves property unmodified.

        Parameters
        ----------
        Baud : int
            baudrate (Default value = None)
        Data : int
            number of data bits (Default value = None)
        Parity : string
            ``'None'``, ``'Odd'`` or ``'Even'`` (Default value = None)
        Stop : int
            number of stop bits (Default value = None)
        FlowControl : string
            ``'HW'``, ``'SW'``, or ``'Off'`` (Default value = None)
        CharDelay : float, int
            time between each character sent to the connected device (Default
            value = None)
        Mode : string
            mode of the port, ``'RS232'``, ``'RS422'`` or ``'RS485'`` (Default
            value = None)
        """
        pass

    def Send(self, data: bytes | str) -> None:
        """Send string over serial port if it's open

        Parameters
        ----------
        data : bytes, string
            data to send

        Raises
        ------
        TypeError, IOError
        """
        pass

    def SendAndWait(
        self,
        data: bytes | str,
        timeout: float,
        **kwargs: int | bytes | Pattern
    ) -> bytes:
        """Send data to the controlled device and wait (blocking) for
        response. It returns after *timeout* seconds expires or immediately if
        the optional condition is satisfied.

        Notes
        -----
        * In addition to *data* and *timeout*, the method accepts an optional
          delimiter, which is used to compare against the received response.
          It supports any one of the following conditions:

          * *deliLen* (int) - length of the response
          * *deliTag* (bytes) - suffix of the response
          * *deliRex* (regular expression object) - regular expression
        * The function will return an empty bytes object if *timeout* expires
          and nothing is received, or the condition (if provided) is not met.

        Parameters
        ----------
        data : bytes, str
            data to send.
        timeout : float
            amount of time to wait for response.
        kwargs : see above
            optional conditions to look for in response.

        Returns
        -------
        bytes
            Response received data (may be empty)
        """
        return bytes()

    def StartKeepAlive(
        self,
        interval: float | int,
        data: bytes | str
    ) -> None:
        """Repeatedly sends *data* at the given *interval*

        Parameters
        ----------
        interval : float, int
            Time in seconds between transmissions
        data : bytes, str
            data to send
        """
        pass

    def StopKeepAlive(self) -> None:
        """Stop the currently running keep alive routine"""
        pass

    @property
    def Baud(self) -> int:
        """Get the baud rate.

        Returns
        -------
        int
        """
        return int()

    @property
    def CharDelay(self) -> float:
        """Get the inter-character delay.

        Returns
        -------
        float
        """
        return float()

    @property
    def Data(self) -> int:
        """Get the number of data bits.

        Returns
        -------
        int
        """
        return int()

    @property
    def FlowControl(self) -> str:
        """Get the flow control.

        Returns
        -------
        str
        """
        return str()

    @property
    def Host(self) -> AdapterDevice | ProcessorDevice | SPDevice:
        """Get the host device

        Returns
        -------
        AdapterDevice, ProcessorDevice, SPDevice
        """
        return ProcessorDevice('')

    @property
    def Mode(self) -> str:
        """Get the current Mode.

        Returns
        -------
        str
        """
        return str()

    @property
    def Parity(self) -> str:
        """Get the parity.

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
    def ReceiveData(
        self
    ) -> Optional[Callable[['SerialInterface', bytes], Any]]:
        """``Event``: Assign or retrieve the handler for the `ReceiveData`
        event that triggers when asynchronous data is received.

        The assigned handler must accept two positional arguments. The first
        is the `SerialInterface` instance triggering the event and the second
        is a bytes object.

        Returns
        -------
        Callable, None
            The assigned handler for the `ReceiveData` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            MainProjector = SerialInterface(ConfRoom, 'COM1')
            MainProjectorBuffer = ''

            ProjectorStates = {
                'POWER': ['OFF', 'WARMING', 'ON', 'COOLING'],
                'INPUT': ['VGA', 'HDMI1', 'HDMI2', 'WIRELESS'],
                }

            # rcvString == 'g:POWER=ON\\rg:INPUT=HDMI1\\rg:KEYLOCK=OFF\\rg:PMM=EX'
            @event(MainProjector, 'ReceiveData')
            def MainFeedbackHandler(interface, rcvString):
                global MainProjectorBuffer
                MainProjectorBuffer += rcvString.decode()

                while True:
                    # partition() finds the first occurance of '\\r' and returns everything
                    # before it, the '\\r' itself, and everything after it.
                    status, delimiter, remainder = MainProjectorBuffer.partition('\\r')
                    if not delimiter:
                        # No '\\r' found in MainProjectorBuffer, no more complete responses
                        # to parse.
                        break

                    # Save any left over data for the next time around the loop.
                    MainProjectorBuffer = remainder

                    Command, State = status.split(':')[1].split('=')
                    try:
                        if Command == 'POWER':
                            PowerOn.SetState(ProjectorStates[Command].index(State))
                        elif Command == 'INPUT':
                            InputGroup.SetCurrent(ProjectorStates[Command].index(State))
                        else:
                            print('Unreferenced command:', Command)
                    except ValueError:
                        print('Command', Command, 'State', State, 'undefined')
        """
        pass

    @ReceiveData.setter
    def ReceiveData(
        self,
        handler: Optional[Callable[['SerialInterface', bytes], Any]]
    ) -> None:
        pass

    @property
    def Stop(self) -> int:
        """Get the number of stop bits.

        Returns
        -------
        int
        """
        return int()
