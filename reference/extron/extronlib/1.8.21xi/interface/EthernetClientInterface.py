from re import Pattern
from typing import Any, Callable, Optional, Tuple


class EthernetClientInterface():
    """This class provides an interface to a client Ethernet socket. This class
    allows the user to send data over the Ethernet port in a synchronous or
    asynchronous manner.

    Notes
    -----
    * `SendAndWait` can be used to synchronously capture responses.
    * For asynchronous communication, a handler function is assigned to the
      `ReceiveData` event. Then responses and unsolicited messages will be
      sent to the user's ``ReceiveData`` handler.
    * ``SendAndWait`` cannot be called within the context of a
      ``ReceiveData`` event.
    * Using ``SendAndWait`` while unsolicited data transmission is
      possible, may cause data loss.

    Examples
    --------
    ::

        from extronlib import event, Version
        from extronlib.interface import EthernetClientInterface
        from extronlib.system import Timer, Wait

        import time     # For monotonic()

        print(Version())

        dmp128cpat = EthernetClientInterface('192.168.1.123', 23)

        connected = None    # Stores the last time data/connection

        def connect():
            \"\"\"Connect to host.  Reattempt on failure after 1s.\"\"\"
            if 'Connected' not in dmp128cpat.Connect(10):
                # Handle alternative workflow here, if needed.
                print('Unable to connect...')
                Wait(1, connect)

        @Timer(1)
        def checkTimer(timer, count):
            \"\"\"Check the time since last data/connection.  Reconnect if necessary.\"\"\"
            global connected
            if connected and time.monotonic() - connected > 15:
                connected = None
                dmp128cpat.Disconnect()
                connect()

        def Initialize():
            connect()

        @event(dmp128cpat, ['Connected', 'Disconnected'])
        def handleConnection(interface, state):
            global connected
            print(interface.IPAddress, state)
            if state == 'Connected':
                interface.StartKeepAlive(5, 'n')
            elif state == 'Disconnected':
                interface.StopKeepAlive()
            connected = time.monotonic()        # Mark the last activity.

        @event(dmp128cpat, 'ReceiveData')
        def handleRecvData(interface, data):
            global connected
            print(interface.IPAddress, data)
            if b'60-1179-10' in data:           # Valid data received.
                connected = time.monotonic()    # Mark the last activity.

        Initialize()
    """

    def __init__(
        self,
        Hostname: str,
        IPPort: int,
        Protocol: str='TCP',
        ServicePort: int=0,
        Credentials: Optional[Tuple[str, str]]=None,
        bufferSize: int=4096
    ):
        """
        Parameters
        ----------
        Hostname : str
            DNS Name of the connection. Can be an IP Address
        IPPort : int
            IP port number of the connection
        Protocol : str
            Value for either ``'TCP'``, ``'UDP'``, or ``'SSH'``
        ServicePort : int
            Sets the port on which to listen for response data
            (UDP only). Zero (``0``) means listen on an OS-assigned port. If
            non-zero, must be in the range of ``1024`` to ``65535``.
        Credentials : tuple
            Username and password for SSH connection.
        bufferSize : int
            Sets buffer size of ReceiveData (with UDP Protocol).

        Notes
        -----
        * A username and password are required for SSH connections.
          Password may be an empty string.
        * *bufferSize* applies to UDP protocol only.

        Examples
        --------
        ::

            MainProjector = EthernetClientInterface('192.168.1.50', 33336)

            BACnet = EthernetClientInterface('192.168.1.100', 0xBAC0, 'UDP')

            cli = EthernetClientInterface('192.168.1.150', 22, 'SSH',
                                          Credentials=('tom', 'tree123'))
        """
        pass

    def Connect(self, timeout: Optional[float]=None) -> str:
        """Connect to the server

        Parameters
        ----------
        timeout : float
            time in seconds to attempt connection before giving up. (Default
            value = None)

        Returns
        -------
        str
            ``'Connected'`` or  ``'ConnectedAlready'`` or reason for
            failure

        Notes
        -----
        Does not apply to UDP connections.

        Examples
        --------
        ::

            # Create an Ethernet Client Interface
            MainProjector = EthernetClientInterface('192.168.1.50', 33336)

            def ConnectProjector():
                result = MainProjector.Connect(5)
                if 'Connected' not in result:
                    Wait(30, ConnectProjector)
                else:
                    GetStatus(MainProjector)    # GetStatus() is a user function

            ConnectProjector()
        """
        return str()

    def Disconnect(self) -> None:
        """Disconnect the socket

        Notes
        -----
        Does not apply to UDP connections.

        Examples
        --------
        ::

            MainProjector.Disconnect()
        """
        pass

    def Send(self, data: bytes | str) -> None:
        """Send string over Ethernet port if it's open

        Parameters
        ----------
        data : bytes, str
            string to send out

        Raises
        ------
        TypeError, IOError

        Examples
        --------
        ::

            MainProjector.Send('GET POWER\\r')
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

        Examples
        --------
        ::

            response = MainProjector.SendAndWait('GET POWER\\r', 0.3, deliLen=16)
            response = MainProjector.SendAndWait('GET POWER\\r', 0.3, deliTag=b'\\r\\n')
            response = MainProjector.SendAndWait(
                'GET POWER\\r', 0.3,
                deliRex=re.compile(b'g:POWER=(ON|OFF|ON2OFF|OFF2ON)\\r\\n')
                )
        """
        return bytes()

    def SetBufferSize(self, bufferSize: int) -> None:
        """Sets the size of the RecieveData buffer for UDP communication.  This
        is the largest single packet size that can be received.

        Parameters
        ----------
        bufferSize : int
            Size of the buffer for ReceiveData

        Notes
        -----
        Applies to UDP protocol only.

        Examples
        --------
        ::

            MainProjector.SetBufferSize(2048)
        """
        pass

    def SSLWrap(
        self,
        certificate: Optional[str]=None,
        cert_reqs: str='CERT_NONE',
        ssl_version: str='TLSv2',
        ca_certs: Optional[str]=None
    ) -> None:
        """Wrap this connection in an SSL context.

        Parameters
        ----------
        certificate : str
            alias to a specific keyfile/certificate pair (Default value = None)
        cert_reqs : str
            specifies whether a certificate is required from the other side of
            the connection (``'CERT_NONE'``, ``'CERT_OPTIONAL'``, or
            ``'CERT_REQUIRED'``). If the value of this parameter is not
            ``'CERT_NONE'``, then the ca_certs parameter must point to a file
            of CA certificates. (Default value = 'CERT_NONE')
        ssl_version : str
            version from the supported SSL/TLS version table. Currently only
            TLS 1.2 is allowed. (Default value = 'TLSv2')
        ca_certs : str
            alias to a file that contains a set of concatenated “certification
            authority” certificates, which are used to validate certificates
            passed from the other end of the connection.
            (Default value = None)

        Notes
        -----
        * This method wraps the ``EthernetClientInterface`` using an
          `ssl.SSLContext
          <https://docs.python.org/3.11/library/ssl.html#ssl.SSLContext>`_.
          See python documentation for more details.  The following settings
          are applied:

            * Property ``ssl.PROTOCOL_TLS_CLIENT`` is used
            * Property ``cert_reqs`` applied per the *cert_reqs* parameter
            * Property ``ssl_version`` is ignored
            * Property ``do_handshake_on_connect`` is set to ``True``
            * Property ``suppress_ragged_eofs`` is set to ``True``
            * Property ``ciphers`` is fixed to the system default
            * Property ``check_hostname`` is fixed to False
        * Requires protocol ``'TCP'``.
        * **certificate** and **ca_certs** specify aliases to machine
          certificate/key pairs and CA certificates uploaded to the processor
          in Toolbelt.

        Warnings
        --------

        .. deprecated:: 1.8
            *ssl_version* is ignored in this version an will be removed in a
            future release. Now uses ``ssl.PROTOCOL_TLS_CLIENT`` to
            "Auto-negotiate the highest protocol version that both the client
            and server support, and configure the context server-side
            connections."

        Examples
        --------
        ::

            client = EthernetClientInterface('192.168.1.100', 10000, 'TCP')
            client.SSLWrap(
                certificate='client',
                cert_reqs='CERT_REQUIRED',
                ca_certs='rootca'
            )

            client.Connect(10)
        """
        pass

    def StartKeepAlive(
        self,
        interval: float,
        data: bytes | str
    ) -> None:
        """Repeatedly sends *data* at the given *interval*

        Parameters
        ----------
        interval : float
            Time in seconds between transmissions
        data : bytes, str
            data to send

        Examples
        --------
        ::

            # Query product code (model name).  Handle response in ReceiveData event.
            MainProjector.StartKeepAlive(5, 'GET PRODCODE\\r')
        """
        pass

    def StopKeepAlive(self) -> None:
        """Stop the currently running keep alive routine

        Examples
        --------
        ::

            MainProjector.StopKeepAlive()
        """
        pass

    @property
    def Connected(
        self
    ) -> Optional[Callable[['EthernetClientInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Connected` event
        that triggers when socket connection is established.

        The assigned handler must accept two positional arguments. The first
        one is the `EthernetClientInterface` instance triggering the event and
        the second one is a string (``'Connected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Connected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(MainProjector, 'Connected')
            def ConnectionHandler(interface, state):
                # Routine to execute when projector comes online.
                systemStates['ProjectorOffline'] = False
                interface.Send('GET POWER\\r')
        """
        pass

    @Connected.setter
    def Connected(
        self,
        handler: Optional[Callable[['EthernetClientInterface', str], Any]]
    ) -> None:
        pass

    @property
    def Credentials(self) -> Optional[tuple]:
        """Get the username and password for SSH connection.

        Returns
        -------
        tuple, None

        Notes
        -----
        * returns tuple: ``('username', 'password')`` if provided otherwise
          ``None``.
        * only applies when protocol ``'SSH'`` is used.
        """
        pass

    @property
    def Disconnected(
        self
    ) -> Optional[Callable[['EthernetClientInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Disconnected` event
        that triggers when socket connection is broken.

        The assigned handler must accept two positional arguments. The first
        one is the `EthernetClientInterface` instance triggering the event and
        the second one is a string (``'Disconnected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Disconnected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(MainProjector, 'Disconnected')
            def ConnectionHandler(interface, state):
                # Routine to execute when projector goes offline.
                systemStates['ProjectorOffline'] = True
                @Wait(3)
                def Reconnect():
                    res = MainProjector.Connect(3)
                    if res == 'Connected':
                        MainProjector.Send('GET POWER\\r')
                    else:
                        Wait(30, Reconnect)
        """
        pass

    @Disconnected.setter
    def Disconnected(
        self,
        handler: Optional[Callable[['EthernetClientInterface', str], Any]]
    ) -> None:
        pass

    @property
    def Hostname(self) -> str:
        """Hostname of the targeted device.

        Returns
        -------
        str

        Notes
        -----
        If unavailable, returns the IP address.
        """
        return str()

    @property
    def IPAddress(self) -> str:
        """IP Address of the targeted device.

        Returns
        -------
        str
        """
        return str()

    @property
    def IPPort(self) -> int:
        """IP Port of the targeted service.

        Returns
        -------
        int
        """
        return int()

    @property
    def Protocol(self) -> str:
        """Protocol defined at instantiation. Value for either ``'TCP'``,
        ``'UDP'``, ``'SSH'`` connection.

        Returns
        -------
        str
        """
        return str()

    @property
    def ReceiveData(
        self
    ) -> Optional[Callable[['EthernetClientInterface', bytes], Any]]:
        """``Event``: Assign or retrieve the handler for the `ReceiveData`
        event that triggers when asynchronous data is received.

        The assigned handler must accept two positional arguments. The first
        one is the `EthernetClientInterface` instance triggering the event and
        the second one is a bytes object.

        Returns
        -------
        Callable, None
            The assigned handler for the `ReceiveData` event or `None` if no
            handler has been assigned.

        Notes
        -----
        * The maximum amount of data per ``ReceiveData`` event that
          will be passed into the handler is 1024 bytes.  For payloads
          greater than 1024 bytes, multiple events will be triggered.
        * When UDP protocol is used, the data will be truncated to the
          buffer size (4096 by default).

        Examples
        --------
        ::

            MainProjector = EthernetClientInterface('192.168.1.50', 33336)
            MainProjector.Connect()
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
        handler: Optional[Callable[['EthernetClientInterface', bytes], Any]]
    ) -> None:
        pass

    @property
    def ServicePort(self) -> int:
        """Get the port on which the socket is listening for response data.

        Returns
        -------
        int

        Notes
        -----
        When protocol is UDP, the service port is not known until
        communication is active.  ServicePort will return 0 when unknown.
        """
        return int()
