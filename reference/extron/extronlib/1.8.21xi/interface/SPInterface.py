from typing import Any, Callable, Optional

from ..device import SPDevice
from . import Interface


class SPInterface(Interface):
    """This class will provide a common interface for controlling and
    collecting data from AV components on Extron devices (`extronlib.device`)
    and Extron Secure Platform devices (`SPDevice`). The user can instantiate
    the class directly or create a subclass to add, remove, or alter behavior
    for different types of devices.

    Examples
    --------
    ::

        from extronlib import event, Version
        from extronlib.device import SPDevice
        from extronlib.interface import SPInterface

        print(Version())

        SystemSwitcher = SPDevice('SysSwitcher')

        SystemSwitcher_spi = SPInterface(SystemSwitcher)

        @event(SystemSwitcher_spi, ['Online', 'Offline'])
        def handleConnection(interface, state):
            print(interface.Host.DeviceAlias, state)

        @event(SystemSwitcher_spi, 'ReceiveData')
        def handleRecvData(interface, data):
            print(interface.Host.DeviceAlias, data)
    """

    def __init__(self, Host: SPDevice):
        """
        Parameters
        ----------
        Host : SPDevice
            handle to Extron device class that instantiated this interface
            class

        Examples
        --------
        ::

            # Create a System Switcher with Secure Platform Device
            SystemSwitcher = SPDevice('SysSwitcher')

            # Create a Secure Platform Interface to the System Switcher with Secure
            # Platform Device to allow for SIS control of the device.
            SystemSwitcher_spi = SPInterface(SystemSwitcher)
        """
        pass

    def Send(self, data: bytes | str) -> None:
        """Send string over secure, Extron channel.

        Parameters
        ----------
        data : bytes, string
            string to send out

        Examples
        --------
        ::

            SystemSwitcher_spi.Send('n\\r')
        """
        pass

    @property
    def Host(self) -> SPDevice:
        """Get the host device

        Returns
        -------
        SPDevice
        """
        return SPDevice('')

    @property
    def ReceiveData(
        self
    ) -> Optional[Callable[['SPInterface', bytes], Any]]:
        """``Event``: Assign or retrieve the handler for the `ReceiveData`
        event that triggers when asynchronous data is received.

        The assigned handler must accept two positional arguments. The first
        one is the `SPInterface` instance triggering the event and the second
        one is a bytes string.

        Notes
        -----
        The maximum amount of data per ``ReceiveData`` event that will be
        passed into the handler is 1024 bytes.  For payloads greater than 1024
        bytes, multiple events will be triggered.

        Returns
        -------
        Callable, None
            The assigned handler for the `ReceiveData` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            MainBuffer = ''

            # rcvString == 'Inf00*XYZ 1000\\r\\n12-3456-78\\r\\n192.168.1'
            @event(SystemSwitcher_spi, 'ReceiveData')
            def handleRecvData(interface, rcvString):
                global MainBuffer
                MainBuffer += rcvString.decode()

                while True:
                    status, delimiter, remainder = MainBuffer.partition('\\r\\n')
                    if not delimiter:
                        # No '\\r\\n' found in MainBuffer, no more complete responses to parse.
                        break

                    # Save any left over data for the next time around the loop.
                    MainBuffer = remainder

                    if status in '12-3456-78':
                        # Required polling received
                        doConnectionLogic('Connected')
                    elif status in AnotherCommand:
                        handleAnotherCommand()
        """
        pass

    @ReceiveData.setter
    def ReceiveData(
        self,
        handler: Optional[Callable[['SPInterface', bytes], Any]]
    ) -> None:
        pass
