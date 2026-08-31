class SummitConnect():
    '''
    This class provides an interface to Extron Unified Communications
    solutions.

    .. note:: System limits 15 SummitConnect clients per system.

    .. versionadded:: 3.2
        CodecConnect renamed to SummitConnect.
    '''

    def __init__(self, Hostname, IPPort=None):
        '''
        :param Hostname: Hostname of the host computer.  Can be an IP Address.
        :type Hostname: string
        :param IPPort: IP Port the software is listening on (default is
            ``5000``)
        :type IPPort: int

        .. note:: Only one object can be instantiated for a given Hostname or
            IP Address.

        .. code-block:: python

            from extronlib.software import SummitConnect
            ConferencePC = SummitConnect('192.168.1.110')
        '''
        pass

    @classmethod
    def SetListeningPorts(self, portList=None):
        '''
        Set the ports to listen for received data.

        :param portList: list of ports (e.g. [10000, 10001, 10002]). ``None``
            will set to default range.
        :type portList: list of ints
        :return: ``'Listening'`` or a reason for failure
            (e.g. ``'PortUnavailable:<port>, ...'``)

        .. note::
            * A maximum of 15 ports can be specified.
            * Default port range is ``5001 - 5008``

        .. code-block:: python

            # Listen on ports 10000, 10001, and 10002
            SummitConnect.SetListeningPorts(range(10000, 10003))
            ...
            SummitConnect.SetListeningPorts()    # Reset to default.
        '''
        pass

    def Connect(self, timeout=None):
        '''
        Connect to the software

        :param timeout: time in seconds to attempt connection before giving up.
        :type timeout: float
        :return: ``'Connected'`` or reason for failure (``'TimedOut'``,
            ``'HostError'``, ``'PortUnavailable:<port>, ...'``).
        :rtype: string

        .. code-block:: python

            def ConnectToSoftware():
                result = ConferencePC.Connect(5)
                if result in ['TimedOut', 'HostError']:
                    Wait(30, ConnectToSoftware)
                else:
                    GetStatus(ConferencePC)    # GetStatus() is a user function

            ConnectToSoftware()
        '''
        pass

    def Disconnect(self):
        '''
        Disconnect the socket

        .. code-block:: python

            ConferencePC.Disconnect()
        '''
        pass

    def Send(self, data):
        '''
        Send string to licensed software

        :param data: string to send out
        :type data: bytes, string

        .. code-block:: python

            ConferencePC.Send(A_MESSAGE)
        '''
        pass

    @property
    def Connected(self):
        '''
        ``Event:`` Triggers when communication is established.

        The callback takes two arguments. The first one is the
        :py:class:`SummitConnect` instance triggering the event and the second
        one is a string (``'Connected'``).

        .. code-block:: python

            @event(ConferencePC, 'Connected')
            def ConnectionHandler(interface, state):
                # Routine to execute when ConferencePC comes online.
                systemStates['ConferencePCOffline'] = False
                interface.Send(A_MESSAGE)
        '''
        pass

    @property
    def Disconnected(self):
        '''
        ``Event:`` Triggers when the communication is broken

        The callback takes two arguments. The first one is the
        :py:class:`SummitConnect` instance triggering the event and the second
        one is a string (``'Disconnected'``).

        .. code-block:: python

            @event(ConferencePC, 'Disconnected')
            def ConnectionHandler(interface, state):
                # Routine to execute when ConferencePC goes offline.
                systemStates['ConferencePCOffline'] = True
                @Wait(3)
                def Reconnect():
                    res = ConferencePC.Connect(3)
                    if res == 'Connected':
                        ConferencePC.Send(A_MESSAGE)
                    else:
                        Wait(30, Reconnect)
        '''
        pass

    @property
    def Hostname(self):
        '''
        :return: Hostname of the host computer
        :rtype: string

        .. note:: If unavailable, returns the IP Address.
        '''
        pass

    @property
    def IPAddress(self):
        '''
        :return: IP Address of the host computer
        :rtype: string
        '''
        pass

    @property
    def IPPort(self):
        '''
        :return: IP Port the software is listening on (default is
            ``5000``)
        :rtype: int
        '''
        pass

    @property
    def ListeningPort(self):
        '''
        :return: IP Port this SummitConnect instance is listening on for
            received data
        :rtype: int
        '''
        pass

    @property
    def ReceiveData(self):
        '''
        ``Event:`` Receive Data event handler used for asynchronous
        transactions

        The callback takes two arguments. The first one is the
        :py:class:`SummitConnect` instance triggering the event and the second
        one is a bytes object.

        .. code-block:: python
            :linenos:

            import json

            ConferencePC.Connect()

            SummitStates = {}

            # rcvString == {'Some': 'JSON Data'}
            @event(ConferencePC, 'ReceiveData')
            def MainFeedbackHandler(interface, rcvString):
                # Turn rcvString into a dictionary
                msg = json.loads(rcvString)
                # Handle responses
                for response in responses:
                    ...
        '''
        pass
