from typing import Any, Callable, Optional

from ..software.DanteDomainManager import DanteDomainManager


class DanteInterface():
    """This class provides an interface to Dante controlled devices.

    .. versionadded:: 1.2

    Examples
    --------
    ::

        from extronlib import event, Version
        from extronlib.interface import DanteInterface

        print(Version())

        # Always required once per project
        DanteInterface.StartService('AVLAN')

        axi22at = DanteInterface('AXI22-AB-CD-EF')

        def ConnectAXI22at():
            result = axi22at.Connect(5)
            if 'Connected' not in result:
                Wait(30, ConnectAXI22at)
            else:
                GetStatus(axi22at)    # GetStatus() is a user function

        ConnectAXI22at()

        @event(axi22at, ['Connected', 'Disconnected'])
        def handleConnection(interface, state):
            print(interface.Hostname, state)

        @event(axi22at, 'ReceiveData')
        def handleRecvData(interface, data):
            print(interface.Hostname, data)
    """

    def __init__(
        self,
        DeviceName: str,
        Protocol: str='Extron',
        DanteDomainManager: Optional[DanteDomainManager]=None,
        Domain: Optional[str]=None
    ):
        """
        Parameters
        ----------
        DeviceName : str
            Device name of the Dante controlled device.
        Protocol : str
            Protocol type used.  ('Extron' is the only supported protocol at
            this time)
        DanteDomainManager : DanteDomainManager
            Dante Domain Manager of the Dante controlled device.
        Domain : str
            Dante domain this device is assigned to.

        Notes
        -----
        If used without a **Dante Domain Manager**, the Dante device
        identified by **DeviceName** must be on the same subnet.

        Examples
        --------
        ::

            # Always required once per project
            DanteInterface.StartService()

            # Direct connection
            axi22at = DanteInterface('AXI22-AB-CD-EF')
            axi22at.Connect()

            # With a Domain Manager
            from extronlib.software import DanteDomainManager

            DomainManager = DanteDomainManager(manager_hostname, ('username',
                                                                  'password'))

            axi22at2 = DanteInterface('AXI22-AB-CD-EF',
                                      DanteDomainManager=DomainManager,
                                      Domain='Auditorium')
            axi22at2.Connect()
        """
        pass

    def Connect(
        self,
        timeout: Optional[float]=None
    ) -> str:
        """Connect to the device

        Parameters
        ----------
        timeout : float
            time in seconds to attempt connection before giving
            up. (Default value = None)

        Returns
        -------
        str
            ``'Connected'`` or  ``'ConnectedAlready'`` or reason for failure.

        Examples
        --------
        ::

            # Always required once per project
            DanteInterface.StartService()

            # Create an Dante Interface
            axi22at = DanteInterface('AXI22-AB-CD-EF')

            def Connectaxi22at():
                result = axi22at.Connect(5)
                if 'Connected' not in result:
                    Wait(30, Connectaxi22at)
                else:
                    GetStatus(axi22at)    # GetStatus() is a user function

            Connectaxi22at()
        """
        return str()

    def Disconnect(self) -> None:
        """Disconnect the session.

        Examples
        --------
        ::

            axi22at.Disconnect()
        """
        pass

    def Send(self, data: bytes | str) -> None:
        """Send string over Dante port

        Parameters
        ----------
        data : bytes, string
            string to send out

        Examples
        --------
        ::

            axi22at.Send('n')
        """
        pass

    @classmethod
    def StartService(cls, interface: str='LAN') -> str:
        """Start the Dante Service.

        Parameters
        ----------
        interface : str
            Defines the network interface connected to the Dante
            network (``'LAN'``, or ``'AVLAN'``) (Default value = 'LAN')


        Notes
        -----
        * The possible return values are:

          * ``'ServiceStarted'``
          * ``'ServiceStartedAlready'``
          * ``'PortUnavailable'``
          * ``'InterfaceUnavailable: LAN'``
          * ``'InterfaceUnavailable: AVLAN'``
        * If ``'ServiceStarted'`` is not in the result, the service will not
          be running.
        * Calling this method is required only once in your project but must
          be done before creating a DanteInterface instance.

        Returns
        -------
        str
            ``'ServiceStarted'`` or a reason for failure

        Examples
        --------
        ::

            res = DanteInterface.StartService('LAN')

            if res == 'ServiceStarted':
                pass # Service Started
            elif res == 'PortUnavailable':
                raise ResourceWarning('Port unavailable')       # this is not likely to recover
            elif 'InterfaceUnavailable' in res:
                raise ResourceWarning('Interface Unavailable')  # listen on another
                                                                # interface
        """
        return str()

    @property
    def Connected(
        self
    ) -> Optional[Callable[['DanteInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Connected`
        event that triggers when a connection is established.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `DanteInterface` instance triggering the event and
        the second one is a string (``'Connected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Connected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(axi22at, 'Connected')
            def ConnectionHandler(interface, state):
                print('{} is now {}'.format(interface.Hostname, state))
        """
        pass

    @Connected.setter
    def Connected(
        self,
        handler: Optional[Callable[['DanteInterface', str], Any]]
    ) -> None:
        pass

    @property
    def DanteDomainManager(self) -> DanteDomainManager:
        """Dante Domain Manager of the Dante controlled device.

        Returns
        -------
        DanteDomainManager
        """
        return DanteDomainManager(str())

    @property
    def DeviceName(self) -> str:
        """Device name of the Dante controlled device.

        Returns
        -------
        str
        """
        return str()

    @property
    def Disconnected(
        self
    ) -> Optional[Callable[['DanteInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Disconnected`
        event that triggers when a connection is established.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `DanteInterface` instance triggering the event and
        the second one is a string (``'Disconnected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Disconnected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(axi22at, 'Disconnected')
            def ConnectionHandler(interface, state):
                print('{} is now {}'.format(interface.Hostname, state))
        """
        pass

    @Disconnected.setter
    def Disconnected(
        self,
        handler: Optional[Callable[['DanteInterface', str], Any]]
    ) -> None:
        pass

    @property
    def Domain(self) -> str:
        """Dante domain this device is assigned to.

        Returns
        -------
        str
        """
        return str()

    @property
    def Protocol(self) -> str:
        """Protocol type used.

        Returns
        -------
        str

        Notes
        -----
        'Extron' is the only supported protocol at this time.
        """
        return str()

    @property
    def ReceiveData(
        self
    ) -> Optional[Callable[['DanteInterface', bytes], Any]]:
        """``Event``: Assign or retrieve the handler for the `ReceiveData`
        event that triggers when data is received asynchronously.

        The assigned handler must accept exactly two arguments. The first one
        is the `DanteInterface` instance triggering the event and the second
        one is a bytes object.

        Returns
        -------
        Callable, None
            The assigned handler for the `ReceiveData` event or `None` if no
            handler has been assigned.

        Notes
        -----
        * Dante controlled devices always provide verbose, tagged responses.
        * The maximum amount of data per ``ReceiveData`` event that will be
          passed into the handler is 1024 bytes.  For payloads greater than
          1024 bytes, multiple events will be triggered.

        Examples
        --------
        ::

            @event(axi22at, 'ReceiveData')
            def handleRecvData(interface, data):
                print(interface.Hostname, data)
        """
        pass

    @ReceiveData.setter
    def ReceiveData(
        self,
        handler: Optional[Callable[['DanteInterface', bytes], Any]]
    ) -> None:
        pass
