class EthernetServerInterface():
    '''
    This class provides an interface to a server Ethernet socket.  After
    instantiation, the server is started by calling :py:meth:`StartListen`.
    This class allows the user to send data over the Ethernet port in an
    asynchronous manner using :py:meth:`Send` and :py:data:`ReceiveData` after
    a client has connected.

    .. warning:: This class is no longer supported.  For any new development,
        :py:class:`EthernetServerInterfaceEx` should be used.

    .. deprecated:: 3.1
        Use :class:`EthernetServerInterfaceEx` instead.
    '''

    def __init__(self, IPPort, Protocol='TCP', Interface='Any', ServicePort=0):
        '''
        :param IPPort: IP port number of the listening service.
        :type IPPort: int
        :param Protocol: communication protocol (``'TCP'`` or ``'UDP'``)
        :type Protocol: string
        :param Interface: Defines the network interface on which to listen
            (``'Any'``, ``'LAN'``, or ``'AVLAN'``)
        :type Interface: string
        :param ServicePort: sets the port from which the client will send data.
            Zero means any service port is valid.
        :type ServicePort: int

        .. note:: *ServicePort* is only applicable to ``'UDP'`` protocol type.

        .. code-block:: python
            :linenos:

            from extronlib import event, Version
            from extronlib.interface import EthernetServerInterface
            from extronlib.system import Timer, Wait

            import time     # For monotonic()

            print(Version())

            serv = EthernetServerInterface(10000, 'TCP')

            def startServer():
                """Start the server.  Reattempt on failure after 1s."""
                if serv.StartListen() != 'Listening':   # Port unavailable
                    print('Port unavailable')
                    Wait(1, startServer)

            @Timer(1)
            def checkTimer(timer, count):
                """
                Check the time since last keepalive received from client. Reconnect if
                necessary.
                """
                global connected
                # If connected and keepalive not received in last 15 seconds,
                # disconnect and listen again.
                if connected and time.monotonic() - connected > 15:
                    serv.Disconnect()
                    startServer()
                    connected = None

            def Initialize():
                startServer()

            @event(serv, 'ReceiveData')
            def HandleReceiveData(interface, data):
                global connected
                print('Rx: {}'.format(data.decode()))

                # This simulates a condition where the server has determined to end the
                # session and close the connection.
                if b'end' in data:                  # Disconnect on data
                    print('End signal received.')
                    interface.Disconnect()
                    startServer()

                # This simulates a keepalive message received from the client.  Check
                # for missed keepalives in checkTimer()
                elif b'ping' in data:               # Record last keepalive time
                    connected = time.monotonic()

            @event(serv, 'Connected')
            def HandleClientConnect(interface, state):
                global connected
                print('Client connected ({}).'.format(interface.IPAddress))
                interface.Send(b'Hello.\\n')
                connected = time.monotonic()        # Reset the keepalive time

            @event(serv, 'Disconnected')
            def HandleClientDisconnect(interface, state):
                global connected
                print('Server/Client disconnected.')
                connected = None                    # Clear the keepalive

            Initialize()

        '''
        pass

    def Disconnect(self):
        '''
        Closes the connection gracefully.

        .. code-block:: python

            def checkTimer():
                global connected
                # If connected and keepalive not received in last 15 seconds,
                # disconnect and listen again.
                if connected and time.monotonic() - connected > 15:
                    serv.Disconnect()
                    startServer()
                    connected = None
                Wait(1, checkTimer)
        '''
        pass

    def Send(self, data):
        '''
        Send string over Ethernet port if it's open

        :param data: string to send out
        :type data: bytes, string
        :raise: TypeError, IOError

        .. code-block:: python

            interface.Send(b'Hello.\\n')
        '''
        pass

    def StartListen(self, timeout=0):
        '''
        Start the listener

        :param timeout: how long to listen for connections (0=Forever)
        :type timeout: float
        :return: ``'Listening'`` or a reason for failure
            (e.g. ``'PortUnavailable'``)
        :raises: IOError

        .. code-block:: python

            def startServer():
                if serv.StartListen() != 'Listening':   # Port unavailable
                    print('Port unavailable')
                    Wait(1, startServer)
        '''
        pass

    def StopListen(self):
        '''
        Stop the listener

        .. code-block:: python
            :linenos:

            @event(serv, 'ReceiveData')
            def HandleReceiveData(interface, data):
                global connected
                print('Rx: {}'.format(data.decode()))

                # This simulates a condition where the server has determined to end the
                # session and close the connection.
                if b'end' in data:                  # Disconnect on data
                    print('End signal received.')
                    interface.Disconnect()
                    interface.StopListen()
        '''
        pass

    @property
    def Connected(self):
        '''
        ``Event:`` Triggers when socket connection is established.

        The callback takes two arguments. The first one is the
        :py:class:`EthernetServerInterface` instance triggering the event and
        the second one is a string (``'Connected'``).
        '''
        pass

    @property
    def Disconnected(self):
        '''
        ``Event:`` Triggers when the socket connection is broken

        The callback takes two arguments. The first one is the
        :py:class:`EthernetServerInterface` instance triggering the event and
        the second one is a string (``'Disconnected'``).
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
    def Interface(self):
        '''
        :return: name of interface on which the server is listening
            (``'Any'``, ``'LAN'``, or ``'AVLAN'``)
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
    def IPPort(self):
        '''
        :return: IP Port number of the listening service
        :rtype: int
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
        :py:class:`EthernetServerInterface` instance triggering the event and
        the second one is a bytes object.

        .. code-block:: python
            :linenos:

            CLIServer = EthernetServerInterface(1024)
            CLIServer.StartListen()

            CLIServerCommands = ['HELP', 'RESTART', 'REPORT']

            CLIBuffer = ''

            # rcvString == 'HELP\\rREPORT\\rRESTA'
            @event(CLIServer, 'ReceiveData')
            def CLIServerFeedbackHandler(interface, rcvString):
                global CLIBuffer
                tempBuffer = CLIBuffer + rcvString.decode()
                if tempBuffer[-1] != '\\r':              # Partial message
                    last = tempBuffer.rfind('\\r')       # Find last <CR>
                    CLIBuffer = tempBuffer[last+1:]     # Save the leftovers
                    tempBuffer = tempBuffer[:last]      # Deal with the complete strings
                else:
                    CLIBuffer = ''                      # All data handled

                Commands = tempBuffer.split('\\r')

                # Handle Commands
                for Command in Commands:
                    if Command in CLIServerCommands:
                        if Command == 'HELP':
                            ShowCLIHelp()
                        elif Command == 'REPORT':
                            GenerateSystemReport()
                        elif Command == 'RESTART':
                            RestartCLIService()
                    else:
                        print('Unreferenced command:', response)
        '''
        pass

    @property
    def ServicePort(self):
        '''
        :return: ServicePort port on which the client will listen for data
        :rtype: int
        '''
        pass
