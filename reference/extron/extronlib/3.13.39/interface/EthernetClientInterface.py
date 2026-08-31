class EthernetClientInterface():
    '''
    This class provides an interface to a client Ethernet socket. This class
    allows the user to send data over the Ethernet port in a synchronous or
    asynchronous manner.

    .. note::
        * :py:meth:`SendAndWait` can be used to synchronously capture
          responses.
        * For asynchronous communication, a handler function is assigned to
          the :py:data:`ReceiveData` event. Then responses and unsolicited
          messages will be sent to the user's ``ReceiveData`` handler.
        * ``SendAndWait`` cannot be called within the context of a
          ``ReceiveData`` event.
        * Using ``SendAndWait`` while unsolicited data transmission is
          possible, may cause data loss.

    .. code-block:: python
        :linenos:

        from extronlib import event, Version
        from extronlib.interface import EthernetClientInterface
        from extronlib.system import Timer, Wait

        import time     # For monotonic()

        print(Version())

        dmp128cpat = EthernetClientInterface('192.168.1.123', 23)

        connected = None    # Stores the last time data/connection

        def connect():
            """Connect to host.  Reattempt on failure after 1s."""
            if 'Connected' not in dmp128cpat.Connect(10):
                # Handle alternative workflow here, if needed.
                print('Unable to connect...')
                Wait(1, connect)

        @Timer(1)
        def checkTimer(timer, count):
            """Check the time since last data/connection.  Reconnect if necessary."""
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
    '''

    def __init__(self, Hostname, IPPort, Protocol='TCP', ServicePort=0, Credentials=None, bufferSize=4096):
        '''
        :param Hostname: DNS Name of the connection. Can be an IP Address
        :type Hostname: string
        :param IPPort: IP port number of the connection
        :type IPPort: int
        :param Protocol: Value for either ``'TCP'``, ``'UDP'``, or ``'SSH'``
        :type Protocol: string
        :param ServicePort: Sets the port on which to listen for response
            data, UDP only, zero means listen on port OS assigns
        :type ServicePort: int
        :param Credentials: Username and password for SSH connection.
        :type Credentials: tuple
        :param bufferSize: Sets buffer size of ReceiveData (with UDP Protocol).
        :type bufferSize: int

        .. note::
            * A username and password are required for SSH connections.  Password may be an empty string.
            * *bufferSize* applies to UDP protocol only.

        .. code-block:: python

            mainProjector = EthernetClientInterface('192.168.1.50', 33336)

            BACnet = EthernetClientInterface('192.168.1.100', 0xBAC0, 'UDP')

            cli = EthernetClientInterface('192.168.1.150', 22, 'SSH',
                                          Credentials=('tom', 'tree123'))

        .. versionadded:: 2.4
            SSH protocol

        .. versionadded:: 3.8
            BufferSize for UDP
        '''
        pass

    def Connect(self, timeout=None):
        '''
        Connect to the server

        :param timeout: time in seconds to attempt connection before giving
            up.
        :type timeout: float
        :return: ``'Connected'`` or  ``'ConnectedAlready'`` or reason for
            failure
        :rtype: string

        .. note:: Does not apply to UDP connections.

        .. code-block:: python
            :linenos:

            # Create an Ethernet Client Interface
            mainProjector = EthernetClientInterface('192.168.1.50', 33336)

            def ConnectProjector():
                result = mainProjector.Connect(5)
                if 'Connected' not in result:
                    Wait(30, ConnectProjector)
                else:
                    GetStatus(mainProjector)    # GetStatus() is a user function

            ConnectProjector()

        .. versionadded:: 2.9
            ConnectedAlready
        '''
        pass

    def Disconnect(self):
        '''
        Disconnect the socket

        .. note:: Does not apply to UDP connections.

        .. code-block:: python

            mainProjector.Disconnect()
        '''
        pass

    def Send(self, data):
        '''
        Send string over Ethernet port if it's open

        :param data: string to send out
        :type data: bytes, string
        :raise: TypeError, IOError

        .. code-block:: python

            mainProjector.Send('GET POWER\\r')
        '''
        pass

    def SendAndWait(self, data, timeout, **delimiter):
        '''
        Send data to the controlled device and wait (blocking) for response. It
        returns after *timeout* seconds expires or immediately if the optional
        condition is satisfied.

        .. note:: In addition to *data* and *timeout*, the method accepts an
            optional delimiter, which is used to compare against the received
            response.  It supports any one of the following conditions:

                * *deliLen* (int) - length of the response
                * *deliTag* (bytes) - suffix of the response
                * *deliRex* (regular expression object) - regular expression

        .. note:: The function will return an empty bytes object if *timeout*
            expires and nothing is received, or the condition (if provided) is
            not met.

        :param data: data to send.
        :type data: bytes, string
        :param timeout: amount of time to wait for response.
        :type timeout: float
        :param delimiter: optional conditions to look for in response.
        :type delimiter: see above
        :return: Response received data (may be empty)
        :rtype: bytes

        .. code-block:: python

            response = mainProjector.SendAndWait('GET POWER\\r', 0.3, deliLen=16)
            response = mainProjector.SendAndWait('GET POWER\\r', 0.3, deliTag=b'\\r\\n')
            response = mainProjector.SendAndWait(
                'GET POWER\\r', 0.3,
                deliRex=re.compile(b'g:POWER=(ON|OFF|ON2OFF|OFF2ON)\\r\\n')
                )
        '''
        pass

    def SetBufferSize(self, bufferSize):
        '''
        Sets the size of the RecieveData buffer for UDP communication.  This
        is the largest single packet size that can be received.

        :param bufferSize: Size of the buffer for ReceiveData
        :type bufferSize: int

        .. code-block:: python

            mainProjector.SetBufferSize(2048)

        .. note:: Applies to UDP protocol only.

        .. versionadded:: 3.8
        '''
        pass

    def SSLWrap(self, certificate=None, cert_reqs='CERT_NONE', ssl_version='TLSv2',
                ca_certs=None):
        '''
        Wrap this connection in an SSL context.

        .. note:: This is almost a direct call to `ssl.wrap_socket()
            <https://docs.python.org/3.5/library/ssl.html?highlight=ssl#ssl.wrap_socket>`_.
            See python documentation for more details.  The following changes
            are applied:

                * Property ``server_side`` is set to ``False``
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

            client = EthernetClientInterface('192.168.1.100', 10000, 'TCP')

            client.SSLWrap(
                certificate='client',
                cert_reqs='CERT_REQUIRED',
                ssl_version='TLSv2',
                ca_certs='rootca'
            )

            client.Connect(10) != 'Connected':

        .. versionadded:: 3.4
        '''
        pass

    def StartKeepAlive(self, interval, data):
        '''
        Repeatedly sends *data* at the given *interval*

        :param interval: Time in seconds between transmissions
        :type interval: float
        :param data: data to send
        :type data: bytes, string

        .. code-block:: python

            # Query product code (model name).  Handle response in ReceiveData event.
            mainProjector.StartKeepAlive(5, 'GET PRODCODE\\r')
        '''
        pass

    def StopKeepAlive(self):
        '''
        Stop the currently running keep alive routine

        .. code-block:: python

            mainProjector.StopKeepAlive()
        '''
        pass

    @property
    def Connected(self):
        '''
        ``Event:`` Triggers when socket connection is established.

        The callback takes two arguments. The first one is the
        :py:class:`EthernetClientInterface` instance triggering the event and
        the second one is a string (``'Connected'``).

        .. code-block:: python

            @event(mainProjector, 'Connected')
            def ConnectionHandler(interface, state):
                # Routine to execute when projector comes online.
                systemStates['ProjectorOffline'] = False
                interface.Send('GET POWER\\r')
        '''
        pass

    @property
    def Credentials(self):
        '''
        :return: Username and password for SSH connection.
        :rtype: tuple, None

        .. note::
           * returns tuple: ``('username', 'password')`` if provided
             otherwise ``None``.
           * only applies when protocol ``'SSH'`` is used.

        .. versionadded:: 2.4
        '''
        pass

    @property
    def Disconnected(self):
        '''
        ``Event:`` Triggers when the socket connection is broken

        The callback takes two arguments. The first one is the
        :py:class:`EthernetClientInterface` instance triggering the event and
        the second one is a string (``'Disconnected'``).

        .. code-block:: python
            :linenos:

            @event(mainProjector, 'Disconnected')
            def ConnectionHandler(interface, state):
                # Routine to execute when projector goes offline.
                systemStates['ProjectorOffline'] = True
                @Wait(3)
                def Reconnect():
                    res = mainProjector.Connect(3)
                    if res == 'Connected':
                        mainProjector.Send('GET POWER\\r')
                    else:
                        Wait(30, Reconnect)
        '''
        pass

    @property
    def Hostname(self):
        '''
        :return: server Host name
        :rtype: string

        .. note:: If unavailable, returns the IP address.
        '''
        pass

    @property
    def IPAddress(self):
        '''
        :return: server IP Address
        :rtype: string
        '''
        pass

    @property
    def IPPort(self):
        '''
        :return: IP port number of the connection
        :rtype: int
        '''
        pass

    @property
    def Protocol(self):
        '''
        :return: Value for either ``’TCP’``, ``’UDP’``, ``'SSH'`` connection.
        :rtype: string
        '''
        pass

    @property
    def ReceiveData(self):
        '''
        ``Event:`` Receive Data event handler used for asynchronous
        transactions

        The callback takes two arguments. The first one is the
        :py:class:`EthernetClientInterface` instance triggering the event and
        the second one is a bytes object.

        .. note::
            * The maximum amount of data per ``ReceiveData`` event that
              will be passed into the handler is 1024 bytes.  For payloads
              greater than 1024 bytes, multiple events will be triggered.
            * When UDP protocol is used, the data will be truncated to the
              buffer size (4096 by default).

        .. code-block:: python
            :linenos:

            mainProjector = EthernetClientInterface('192.168.1.50', 33336)
            mainProjector.Connect()

            ProjectorStates = {
                'POWER': ['OFF', 'OFF2ON', 'ON', 'ON2PMM', 'PMM', 'PMM2ON', 'ON2OFF'],
                'INPUT': [
                    'D-RGB', 'A-RGB1', 'A-RGB2', 'COMP', 'VIDEO', 'S-VIDEO', 'HDMI', 'USB'
                    ],
                'PMM': ['OFF', 'STANDBY']
                }
            ProjectorStatus = {}
            mainBuffer = ''

            # rcvString == 'g:POWER=ON\\rg:INPUT=HDMI\\rg:KEYLOCK=OFF\\rg:PMM=EX'
            @event(mainProjector, 'ReceiveData')
            def MainFeedbackHandler(interface, rcvString):
                global mainBuffer
                tempBuffer = mainBuffer + rcvString.decode()
                if tempBuffer[-1] != '\\r':              # Partial message
                    last = tempBuffer.rfind('\\r')       # Find last <CR>
                    mainBuffer = tempBuffer[last+1:]    # Save the leftovers
                    tempBuffer = tempBuffer[:last]      # Deal with the complete strings
                else:
                    mainBuffer = ''                     # All data handled

                # Turn rcvString into:
                #   [['POWER', 'ON'], ['INPUT', 'HDMI'], ['KEYLOCK', 'OFF]]
                responses = [
                    msg.split(':')[1].split('=') \\
                    for msg in tempBuffer.split('\\r') \\
                    if not msg == ''
                    ]
                # Handle responses
                for response in responses:
                    Command, State = response[0], response[1]
                    ProjectorStatus[Command] = State    # Store data for use elsewhere
                    if Command in ProjectorStates:      # Set feedback for each
                        try:
                            if Command == 'POWER':
                                PowerOn.SetState(ProjectorStates[Command].index(State))
                            elif Command == 'INPUT':
                                InputGroup.SetCurrent(
                                    ProjectorStates[Command].index(State)
                                    )
                            elif Command == 'PMM':
                                PowerM.SetState(ProjectorStates[Command].index(State))
                        except:
                            print('State', response, 'undefined.')
                    else:
                        print('Unreferenced command:', response)
        '''
        pass

    @property
    def ServicePort(self):
        '''
        :return: the port on which the socket is listening for response data
        :rtype: int

        .. note:: When protocol is UDP, the service port is not known until
            communication is active.  ServicePort will return 0 when unknown.
        '''
        pass
