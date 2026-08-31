class ClientObject():
    '''
    This class provides a handle to connected clients to an
    :py:class:`EthernetServerInterfaceEx`.

    .. note:: This class cannot be instantiated by the programmer.  It is only
        created by the :py:class:`EthernetServerInterfaceEx` object.

    .. versionadded:: 2.4
    '''

    def Disconnect(self):
        '''
        Closes the connection gracefully on client.
        '''
        pass

    def Send(self, data):
        '''
        Send string to the client.

        :param data: string to send out
        :type data: bytes, string
        :raise: TypeError, IOError

        .. code-block:: python

            client.Send(b'Hello.\\n')
        '''
        pass

    @property
    def Hostname(self):
        '''
        :return: Hostname DNS name of the connection. Can be the IP Address
        :rtype: string
        '''
        pass

    @property
    def IPAddress(self):
        '''
        :return: the IP Address of the connected device
        :rtype: string
        '''
        pass

    @property
    def ServicePort(self):
        '''
        :return: ServicePort port on which the client will listen for data
        :rtype: int
        '''
        pass


class EthernetServerInterfaceEx():
    '''
    This class provides an interface to an Ethernet server that allows a
    user-defined amount of client connections.  After instantiation, the
    server is started by calling :py:meth:`StartListen`. This class allows the
    user to send data over the Ethernet port in an asynchronous manner using
    :py:meth:`~extronlib.interface.ClientObject.Send` and
    :py:data:`ReceiveData` after a client has connected.

    .. versionadded:: 2.4
    '''

    def __init__(self, IPPort, Protocol='TCP', Interface='Any', MaxClients=None):
        '''
        :param IPPort: IP port number of the listening service.
        :type IPPort: int
        :param Protocol: communication protocol (``'TCP'`` or ``'UDP'``)
        :type Protocol: string
        :param Interface: Defines the network interface on which to listen
            (``'Any'``, ``'LAN'``, or ``'AVLAN'``)
        :type Interface: string
        :param MaxClients: maximum number of client connections to allow
            (``None`` == Unlimited, 0 == Invalid)
        :type MaxClients: int

        .. code-block:: python
            :linenos:

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
        '''
        pass

    def Disconnect(self, client):
        '''
        Closes the connection gracefully on specified client.

        :param client: handle to client object
        :type client: :py:class:`ClientObject`

        .. code:: python

            @event(serv, 'ReceiveData')
            def HandleReceiveData(client, data):
                print('Rx: {}'.format(data.decode()))

                # This simulates a condition where the server has determined to end the
                # session and close the connection.
                if b'end' in data:                  # Disconnect on data
                    print('End signal received.')
                    serv.Disconnect(client)
        '''
        pass

    def SSLWrap(self, certificate=None, cert_reqs='CERT_NONE', ssl_version='TLSv2',
                ca_certs=None):
        '''
        Wrap all connections to this server instance in an SSL context.

        .. note:: This is almost a direct call to `ssl.wrap_socket()
            <https://docs.python.org/3.5/library/ssl.html?highlight=ssl#ssl.wrap_socket>`_.
            See python documentation for more details.  The following changes
            are applied:

                * Property ``server_side`` is set to ``True``
                * Property ``cert_reqs`` is a string
                * Property ``ssl_version`` is a string
                * Property ``do_handshake_on_connect`` is set to ``True``
                * Property ``suppress_ragged_eofs`` is set to ``True``
                * Property ``ciphers`` is fixed to the system default

        :param certificate: alias to a specific keyfile/certificate pair
        :type certificate: string
        :param cert_reqs: specifies whether a certificate is required from the
            other side of the connection (``'CERT_NONE'``,
            ``'CERT_OPTIONAL'``, or ``'CERT_REQUIRED'``). If the value of this
            parameter is not ``'CERT_NONE'``, then the ca_certs parameter must
            point to a file of CA certificates.
        :type cert_reqs: string
        :param ssl_version: version from the supported SSL/TLS version table
            (``'TLSv2'``). Currently only TLS 1.2 is allowed.
        :type ssl_version: string
        :param ca_certs: alias to a file that contains a set of concatenated
            “certification authority” certificates, which are used to validate
            certificates passed from the other end of the connection.
        :type ca_certs: string

        .. note::
            * Requires protocol ``'TCP'``.
            * **certificate** and **ca_certs** specify aliases to machine
              certificate/key pairs and CA certificates uploaded to the
              processor in Toolbelt.

        .. code-block:: python

            serv = EthernetServerInterfaceEx(10000, 'TCP')
            serv.SSLWrap(
                certificate='client',
                cert_reqs='CERT_REQUIRED',
                ssl_version='TLSv2',
                ca_certs='rootca'
            )

            if serv.StartListen() != 'Listening':
                raise ResourceWarning('Port unavailable') # this is not likely to recover

        .. versionadded:: 3.4
        '''
        pass

    def StartListen(self, timeout=0):
        '''
        Start the listener

        :param timeout: how long to listen for connections
        :type timeout: float
        :return: ``'Listening'`` or a reason for failure
        :raises: IOError

        .. note:: Return examples:

                * ``'Listening'``
                * ``'ListeningAlready'``
                * ``'PortUnavailable'``
                * ``'InterfaceUnavailable: LAN'``
                * ``'InterfaceUnavailable: LAN, AVLAN'``


        .. code-block:: python

            res = serv.StartListen()
            if res == 'Listening':
                pass # Listening
            elif res == 'PortUnavailable':
                raise ResourceWarning('Port unavailable') # this is not likely to recover
            elif 'InterfaceUnavailable' in res:
                raise ResourceWarning('Interface Unavailable') # listen on another
                                                               # interface

        .. note:: If ``'Listening'`` not in result, the server will not be
            listening.

        .. versionadded:: 3.1
            ListeningAlready and InterfaceUnavailable
        '''
        pass

    def StopListen(self):
        '''
        Stop the listener

        .. code-block:: python
            :linenos:

            @event(serv, 'ReceiveData')
            def HandleReceiveData(client, data):
                print('Rx: {}'.format(data.decode()))

                # This simulates a Single User mode where you do not want to accept any
                # other connections.
                if b'singleuser' in data:         # Disconnect all other clients
                    serv.StopListen()
                    for client_ in serv.Clients:
                        if client_ is not client:
                            client_.Disconnect()
                elif b'multiuser' in data:
                    serv.StartListen()
        '''
        pass

    @property
    def Clients(self):
        '''
        :return: List of connected clients.
        :rtype: list of :py:class:`ClientObject`
        '''
        pass

    @property
    def Connected(self):
        '''
        ``Event:`` Triggers when socket connection is established.

        The callback takes two arguments. The first one is the
        :py:class:`ClientObject` instance triggering the event and the second
        one is a string (``'Connected'``).
        '''
        pass

    @property
    def Disconnected(self):
        '''
        ``Event:`` Triggers when the socket connection is broken

        The callback takes two arguments. The first one is the
        :py:class:`ClientObject` instance triggering the event and the second
        one is a string (``'Disconnected'``).
        '''
        pass

    @property
    def Interface(self):
        '''
        :return: name of interface on which the server is listening
            (``'Any'``, ``'LAN'``, or ``'AVLAN'``)
        :rtype: string
        '''
        pass

    @property
    def IPPort(self):
        '''
        :return: IP Port number of the listening service
        :rtype: int
        '''
        pass

    @property
    def MaxClients(self):
        '''
        :return: maximum number of client connections to allow
            (``None`` == Unlimited, 0 == Invalid)
        :rtype: int or None
        '''
        pass

    @property
    def Protocol(self):
        '''
        :return: communication protocol (``'TCP'`` or ``'UDP'``)
        :rtype: string
        '''
        pass

    @property
    def ReceiveData(self):
        '''
        ``Event:`` Receive Data event handler used for asynchronous
        transactions

        The callback takes two arguments. The first one is the
        :py:class:`ClientObject` instance triggering the event and
        the second one is a bytes object.

        .. note::
            * The maximum amount of data per ``ReceiveData`` event that
              will be passed into the handler is 1024 bytes.  For payloads
              greater than 1024 bytes, multiple events will be triggered.
            * When UDP protocol is used, the data will be truncated to the
              buffer size of 4096.

        .. code-block:: python
            :linenos:

            @event(serv, 'ReceiveData')
            def HandleReceiveData(client, data):
                print('Rx: {}'.format(data.decode()))

                # This simulates a Single User mode where you do not want to accept any
                # other connections.
                if b'singleuser' in data:         # Disconnect all other clients
                    serv.StopListen()
                    for client_ in serv.Clients:
                        if client_ is not client:
                            client_.Disconnect()
                elif b'multiuser' in data:
                    serv.StartListen()
        '''
        pass
