from typing import Any, Callable, List, Optional


class SummitConnect():
    """This class provides an interface to Extron Unified Communications
    solutions.

    Notes
    -----
    System limits 15 SummitConnect clients per system.
    """

    def __init__(self, Hostname: str, IPPort: Optional[int]=None):
        """
        Parameters
        ----------
        Hostname : str
            Hostname of the host computer.  Can be an IP Address.
        IPPort : int
            IP Port the software is listening on (default is ``5000``)

        Notes
        -----
        Only one object can be instantiated for a given Hostname or IP
        Address.

        Examples
        --------
        ::

            from extronlib.software import SummitConnect
            ConferencePC = SummitConnect('192.168.1.110')
        """
        pass

    @classmethod
    def SetListeningPorts(cls, portList: Optional[List[int]]=None) -> str:
        """Set the ports to listen for received data.

        Parameters
        ----------
        portList : list of ints, None
            list of ports (e.g. ``[10000, 10001, 10002]``). ``None`` will set
            to default range.  Ports must be within the range of ``1024`` to
            ``65535``.

        Returns
        -------
        str
            ``'Listening'`` or a reason for failure
            (e.g. ``'PortUnavailable:<port>, ...'``)

        Notes
        -----
        * A maximum of 15 ports can be specified.
        * Default port range is ``5001 - 5008``

        Examples
        --------
        ::

            # Listen on ports 10000, 10001, and 10002
            SummitConnect.SetListeningPorts(range(10000, 10003))
            ...
            SummitConnect.SetListeningPorts()    # Reset to default.

        """
        return str()

    def Connect(self, timeout: Optional[float]=None) -> str:
        """Connect to the software

        Parameters
        ----------
        timeout : float
            time in seconds to attempt connection before giving up. (Default
            value = None)

        Returns
        -------
        str
            Connected'`` or reason for failure (``'TimedOut'``,
            ``'HostError'``, ``'PortUnavailable:<port>, ...'``).

        Examples
        --------
        ::

            def ConnectToSoftware():
                result = ConferencePC.Connect(5)
                if result in ['TimedOut', 'HostError']:
                    Wait(30, ConnectToSoftware)
                else:
                    GetStatus(ConferencePC)    # GetStatus() is a user function

            ConnectToSoftware()
        """
        return str()

    def Disconnect(self) -> None:
        """Disconnect the socket

        Examples
        --------
        ::

            ConferencePC.Disconnect()
        """
        pass

    def Send(self, data: bytes | str) -> None:
        """Send string to licensed software

        Parameters
        ----------
        data : bytes, str
            string to send out

        Examples
        --------
        ::

            ConferencePC.Send(A_MESSAGE)
        """
        pass

    @property
    def Connected(self) -> Optional[Callable[['SummitConnect', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Connected` event
        that triggers when communication is established.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `SummitConnect` instance triggering the event and the
        second one is a string (``'Connected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Connected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(ConferencePC, 'Connected')
            def ConnectionHandler(interface, state):
                # Routine to execute when ConferencePC comes online.
                systemStates['ConferencePCOffline'] = False
                interface.Send(A_MESSAGE)
        """
        pass

    @Connected.setter
    def Connected(
        self,
        handler: Optional[Callable[['SummitConnect', str], Any]]
    ) -> None:
        pass

    @property
    def Disconnected(
        self
    ) -> Optional[Callable[['SummitConnect', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Disconnected`
        event that triggers when communication is lost.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `SummitConnect` instance triggering the event and the
        second one is a string (``'Disconnected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Disconnected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

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
        """
        pass

    @Disconnected.setter
    def Disconnected(
        self,
        handler: Optional[Callable[['SummitConnect', str], Any]]
    ) -> None:
        pass

    @property
    def Hostname(self) -> str:
        """Hostname of the host computer

        Returns
        -------
        str

        Notes
        -----
        If unavailable, returns the IP Address.
        """
        return str()

    @property
    def IPAddress(self) -> str:
        """IP Address of the host computer

        Returns
        -------
        str
        """
        return str()

    @property
    def IPPort(self) -> int:
        """IP Port the software is listening on (default is ``5000``).

        Returns
        -------
        int
        """
        return int()

    @property
    def ListeningPort(self) -> int:
        """IP Port this SummitConnect instance is listening on for received
        data.

        Returns
        -------
        int
        """
        return int()

    @property
    def ReceiveData(
        self
    ) -> Optional[Callable[['SummitConnect', bytes], Any]]:
        """``Event``: Assign or retrieve the handler for the `ReceiveData`
        event that triggers when data is received for asynchronously.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `SummitConnect` instance triggering the event and the
        second one is a bytes object.

        Returns
        -------
        Callable, None
            The assigned handler for the `ReceiveData` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            import json

            ConferencePC.Connect()

            SummitStates = {}

            # rcvString == {'Some': 'JSON Data'}
            @event(ConferencePC, 'ReceiveData')
            def MainFeedbackHandler(interface, rcvString):
                # Turn rcvString into a dictionary
                responses = json.loads(rcvString)
                # Handle responses
                for response in responses:
                    ...
        """
        pass

    @ReceiveData.setter
    def ReceiveData(
        self,
        handler: Optional[Callable[['SummitConnect', bytes], Any]]
    ) -> None:
        pass
