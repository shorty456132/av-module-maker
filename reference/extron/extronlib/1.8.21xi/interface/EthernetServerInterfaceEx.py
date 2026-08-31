from typing import Any, Callable, List, Optional


class ClientObject():
    """This class provides a handle to connected clients to an
    `EthernetServerInterfaceEx`.

    Notes
    -----
    This class cannot be instantiated by the programmer.  It is only created
    by the `EthernetServerInterfaceEx` object.
    """

    def Disconnect(self) -> None:
        """Closes the connection gracefully on client."""
        pass

    def Send(self, data: bytes | str) -> None:
        """Send string to the client.

        Parameters
        ----------
        data : bytes, string
            string to send out

        Raises
        ------
        TypeError, IOError

        Examples
        --------
        ::

            client.Send(b'Hello.\\n')
        """
        pass

    @property
    def Hostname(self) -> str:
        """Get the hostname of the client.

        Returns
        -------
        str
        """
        return str()

    @property
    def IPAddress(self) -> str:
        """Get the IP Address of the client.

        Returns
        -------
        str
        """
        return str()

    @property
    def ServicePort(self) -> int:
        """Get the service port on which the client will listen for data.

        Returns
        -------
        int
        """
        return int()


class EthernetServerInterfaceEx():
    """This class provides an interface to an Ethernet server that allows a
    user-defined amount of client connections.  After instantiation, the
    server is started by calling `StartListen`. This class allows the user to
    send data over the Ethernet port in an asynchronous manner using
    `ClientObject.Send` and `ReceiveData` after a client has connected.
    """

    def __init__(
        self,
        IPPort: int,
        Protocol: str='TCP',
        Interface: str='Any',
        MaxClients: Optional[int]=None
    ):
        """
        Parameters
        ----------
        IPPort : int
            IP port number of the listening service in the range of ``1024``
            to ``65535``.
        Protocol : str
            communication protocol (``'TCP'`` or ``'UDP'``)
        Interface : str
            Defines the network interface on which to listen (``'Any'``,
            ``'LAN'``, or ``'AVLAN'``)
        MaxClients : int
            maximum number of client connections to allow
            (``None`` == Unlimited, 0 == Invalid)

        Examples
        --------
        ::

            from extronlib import event, Version
            from extronlib.interface import EthernetServerInterfaceEx

            print(Version())

            serv = EthernetServerInterfaceEx(10000, 'TCP')
            if serv.StartListen() != 'Listening':
                raise ResourceWarning('Port unavailable') # this is not likely to recover

            @event(serv, 'ReceiveData')
            def HandleReceiveData(client, data):
                print('Rx: {}'.format(data.decode()))

                # This simulates a condition where the server has determined to end the
                # session and close the connection.
                if b'end' in data:                  # Disconnect on data
                    print('End signal received.')
                    client.Disconnect()

                # This simulates a Single User mode where you do not want to accept any
                # other connections.
                elif b'singleuser' in data:         # Disconnect all other clients
                    serv.StopListen()
                    for client_ in serv.Clients:
                        if client_ is not client:
                            client_.Disconnect()
                elif b'multiuser' in data:
                    serv.StartListen()

            @event(serv, 'Connected')
            def HandleClientConnect(client, state):
                print('Client connected ({}).'.format(client.IPAddress))
                client.Send(b'Hello.\\n')

            @event(serv, 'Disconnected')
            def HandleClientDisconnect(client, state):
                print('Server/Client {} disconnected.'.format(client.IPAddress))
        """
        pass

    def Disconnect(self, client: ClientObject) -> None:
        """Closes the connection gracefully on specified client.

        Parameters
        ----------
        client : ClientObject
            handle to client object

        Examples
        --------
        ::

            @event(serv, 'ReceiveData')
            def HandleReceiveData(client, data):
                print('Rx: {}'.format(data.decode()))

                # This simulates a condition where the server has determined to end the
                # session and close the connection.
                if b'end' in data:                  # Disconnect on data
                    print('End signal received.')
                    serv.Disconnect(client)
        """
        pass

    def SSLWrap(
        self,
        certificate: Optional[str]=None,
        cert_reqs: str='CERT_NONE',
        ssl_version: str='TLSv2',
        ca_certs: Optional[str]=None
    ) -> None:
        """Wrap all connections to this server instance in an SSL context.

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
        * This method wraps the ``EthernetServerInterfaceEx`` using an
          `ssl.SSLContext
          <https://docs.python.org/3.11/library/ssl.html#ssl.SSLContext>`_.
          See python documentation for more details.  The following settings
          are applied:

            * Property ``ssl.PROTOCOL_TLS_SERVER`` is used
            * Property ``cert_reqs`` applied per the *cert_reqs* parameter
            * Property ``ssl_version`` is ignored
            * Property ``do_handshake_on_connect`` is set to ``True``
            * Property ``suppress_ragged_eofs`` is set to ``True``
            * Property ``ciphers`` is fixed to the system default
            * Property ``check_hostname`` is fixed to False
        * Requires protocol ``'TCP'``.
        * **certificate** and **ca_certs** specify aliases to machine
          certificate/key pairs and CA certificates uploaded to the
          processor in Toolbelt.

        Warnings
        --------

        .. deprecated:: 1.8
            *ssl_version* is ignored in this version an will be removed in a
            future release. Now uses ``ssl.PROTOCOL_TLS_SERVER`` to
            "Auto-negotiate the highest protocol version that both the client
            and server support, and configure the context server-side
            connections."

        Examples
        --------
        ::

            serv = EthernetServerInterfaceEx(10000, 'TCP')
            serv.SSLWrap(
                certificate='server',
                cert_reqs='CERT_REQUIRED',
                ca_certs='rootca'
            )

            if serv.StartListen() != 'Listening':
                raise ResourceWarning('Port unavailable') # this is not likely to recover
        """
        pass

    def StartListen(self, timeout: float | int=0) -> str:
        """Start the listener

        Parameters
        ----------
        timeout : float, int
            how long to listen for connections (Default value = 0)

        Returns
        -------
        str
            ``'Listening'`` or a reason for failure
        """
        return str()

    def StopListen(self) -> None:
        """Stop the listener

        Examples
        --------
        ::

            @event(serv, 'ReceiveData')
            def HandleReceiveData(client, data):
                print('Rx: {}'.format(data.decode()))

                # This simulates a Single User mode where you do not want to accept any
                # other connections.
                if b'singleuser' in data:         # Disconnect all other clients
                    serv.StopListen()
                    for client_ in serv.Clients:
                        if client_ is client:
                            continue
                        client_.Disconnect()
                elif b'multiuser' in data:
                    serv.StartListen()
        """
        pass

    @property
    def Clients(self) -> List[ClientObject]:
        """Get the connected clients.

        Returns
        -------
        list of ClientObject
        """
        return [ClientObject()]

    @property
    def Connected(
        self
    ) -> Optional[Callable[['ClientObject', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Connected` event
        that triggers when the socket connection is established.

        The assigned handler must accept two positional arguments. The first
        one is the `ClientObject` instance triggering the event and the second
        one is a string (``'Connected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Connected` event or `None` if no
            handler has been assigned.
        """
        pass

    @Connected.setter
    def Connected(
        self,
        handler: Optional[Callable[['ClientObject', str], Any]]
    ) -> None:
        pass

    @property
    def Disconnected(
        self
    ) -> Optional[Callable[['ClientObject', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Disconnected`
        event that triggers when the socket connection is broken.

        The assigned handler must accept two positional arguments. The first
        one is the `ClientObject` instance triggering the event and the second
        one is a string (``'Disconnected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Disconnected` event or `None` if no
            handler has been assigned.
        """
        pass

    @Disconnected.setter
    def Disconnected(
        self,
        handler: Optional[Callable[['ClientObject', str], Any]]
    ) -> None:
        pass

    @property
    def Interface(self) -> str:
        """Get the name of interface on which the server is listening
        (``'Any'``, ``'LAN'``, or ``'AVLAN'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def IPPort(self) -> int:
        """Get the IP Port of the listening service.

        Returns
        -------
        int
        """
        return int()

    @property
    def MaxClients(self) -> Optional[int]:
        """Get the maximum allowed clients for this service
        (``None`` == Unlimited, 0 == Invalid).

        Returns
        -------
        int, None
        """
        pass

    @property
    def Protocol(self) -> str:
        """Get the communication protocol (``'TCP'`` or ``'UDP'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def ReceiveData(
        self
    ) -> Optional[Callable[['ClientObject', bytes], Any]]:
        """``Event``: Assign or retrieve the handler for the `ReceiveData`
        event that triggers when asynchronous data is received.

        The assigned handler must accept two positional arguments. The first
        one is the `ClientObject` instance triggering the event and the second
        one is a bytes object.

        Returns
        -------
        Callable, None
            The assigned handler for the `ReceiveData` event or `None` if no
            handler has been assigned.

        Notes
        -----
        * The maximum amount of data per ``ReceiveData`` event that will be
          passed into the handler is 1024 bytes.  For payloads greater than
          1024 bytes, multiple events will be triggered.
        * When UDP protocol is used, the data will be truncated to the buffer
          size of 4096.

        Examples
        --------
        ::

            @event(serv, 'ReceiveData')
            def HandleReceiveData(client, data):
                print('Rx: {}'.format(data.decode()))

                # This simulates a Single User mode where you do not want to accept any
                # other connections.
                if b'singleuser' in data:         # Disconnect all other clients
                    serv.StopListen()
                    for client_ in serv.Clients:
                        if client_ is client:
                            continue
                        client_.Disconnect()
                elif b'multiuser' in data:
                    serv.StartListen()
        """
        pass

    @ReceiveData.setter
    def ReceiveData(
        self,
        handler: Optional[Callable[['ClientObject', bytes], Any]]
    ) -> None:
        pass
