from datetime import datetime, timedelta, timezone
from typing import Any, Callable, List, Optional, Tuple


class CalendarEvent():
    """This class provides a handle to calendar events.

    .. versionadded:: 1.5

    Notes
    -----
    This class cannot be instantiated by the programmer.  It is only created
    by `RoomSchedulingInterface` objects.
    """

    def GetBody(self, html: bool=False) -> str:
        """Query and return the body of the event.

        Parameters
        ----------
        html : bool
            boolean to choose html version instead of text. (Default value = False)

        Returns
        -------
        str
            the event body (html if selected)

        Notes
        -----
        Call this when needed.  The event body content size and transfer time
        is unpredictable.

        Examples
        --------
        ::

            bodytext = calendarevent.GetBody()
        """
        return str()

    @property
    def Calendar(self) -> 'RoomSchedulingInterface':
        """Get the Room scheduling interface.

        Returns
        -------
        RoomSchedulingInterface
        """
        return RoomSchedulingInterface('', Credentials=('', ''))

    @property
    def CheckedIn(self) -> bool:
        """Get the checked in state.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def End(self) -> datetime:
        """Get the event end time.

        Returns
        -------
        datetime

        Notes
        -----
        See Python documentation for
        `datetime <https://docs.python.org/3.11/library/datetime.html#datetime-objects>`_.
        """
        return datetime.now()

    @property
    def Location(self) -> str:
        """Get the event location.

        Returns
        -------
        str
        """
        return str()

    @property
    def Organizer(self) -> str:
        """Get the event organizer.

        Returns
        -------
        str
        """
        return str()

    @property
    def Start(self) -> datetime:
        """Get the event start time.

        Returns
        -------
        datetime

        Notes
        -----
        See Python documentation for
        `datetime`_.
        """
        return datetime.now()

    @property
    def Subject(self) -> str:
        """Get the event subject.

        Returns
        -------
        str
        """
        return str()


class RoomSchedulingInterface():
    """This returns a Room Scheduling Interface object capable of interacting
    with a room scheduling device as well as creating, modifying, and
    discovering calendar events on the associated calendar.

    .. versionadded:: 1.5
    """

    def __init__(self, Hostname: str, Credentials: Tuple[str, str]):
        """
        Parameters
        ----------
        Hostname : str
            DNS Name of the room scheduling device. Can be IP Address.
        Credentials : tuple
            Username and password ('username', 'password')

        Warnings
        --------
        Extron strongly recommends that the "user" account is enabled for
        access to the calendar on this device.  Use of the admin account is
        not recommended.

        Notes
        -----
        * For all *Get Event* methods, an event will be included in results if
          any part of the event falls within the range.
        * Extron room scheduling devices are only capable of displaying a
          single event at a time. ``RoomSchedulingInterface`` will represent
          what is displayed on the device.
        * Changed Events will occur when any attribute of any event meeting
          the criteria is changed.
        * New calendar events may not appear on the TouchLink Scheduling Panel
          immediately. The amount of time for the event to appear can vary
          depending on the calendaring system and the method used to create
          the event (i.e. from a *RoomSchedulingInterface* instance, a
          computer, a mobile device, etc.). For this reason *Changed* events
          should be used to get calendar events for display on TouchLink
          Panels or other user interfaces.

        Examples
        --------
        ::

            from extronlib.interface import RoomSchedulingInterface

            schedulingdevice = RoomSchedulingInterface(
                '192.168.254.251',
                ('user', 'extron')
            )
        """
        pass

    def CheckIn(self) -> str:
        """Check in to the pending or active event.  Call is ignored if check
        in option is currently unavailable.

        Returns
        -------
        str


        ========================  =============================================
        **Return value**          **Description**
        ========================  =============================================
        ``'CheckedIn'``           Check in successful.
        ``'CheckedInAlready'``    Event is already checked in.
        ``'CheckInDisallowed'``   Event check in is not enabled in RoomAgent.
        ``'CheckInUnavailable'``  The time is outside the allowed check in
                                  range.
        ``'Disconnected'``        The interface is currently disconnected.
        ========================  =============================================

        Examples
        --------
        ::

            # Check in to the current event.
            ret = schedulingdevice.CheckIn()
            if ret == 'CheckedIn':
                # handle success
            else:
                 # handle failure
        """
        return str()

    def Connect(self, timeout: Optional[float | int]=None) -> str:
        """Open the network connection to the room scheduling device.

        Parameters
        ----------
        timeout : float, int
            time in seconds to attempt connection before giving up.
            (Default value = None)

        Returns
        -------
        str


        =========================  ============================================
        **Return value**           **Description**
        =========================  ============================================
        ``'Connected'``            Connection successful.
        ``'ConnectedAlready'``     The control processor connection the room
                                   scheduling device was already established.
        ``'InvalidCredentials'``   The given username and/or password is
                                   incorrect.
        ``'CalendarAPIDisabled'``  To enable this function, the “Share Calendar
                                   access” box must be checked within the Room
                                   Agent configuration for this device.
        ``'ConnectionFailed'``     Unable to connect to the room scheduling
                                   device.
        =========================  ============================================

        Examples
        --------
        ::

            if 'Connected' not in schedulingdevice.Connect():
                # handle failure
                ...
        """
        return str()

    def Disconnect(self) -> None:
        """Close the network connection to the room scheduling device.

        Notes
        -----
        While disconnected from the room scheduling device all event read
        methods will return an empty list.
        """
        pass

    def Extend(
        self,
        duration: Optional[int]=None,
        event: Optional['CalendarEvent']=None
    ) -> str:
        """Extend an event *duration* minutes. If *duration* is ``None``, the
        room scheduling device behavior will be used (e.g. 30 minute
        boundaries). If no event is provided, the current event is extended if
        one is in progress.

        Parameters
        ----------
        duration : integer
            The length of time, in minutes, to extend the event. (Default value = None)
        event : CalendarEvent
            The event to extend if not the current event. (Default value = None)

        Returns
        -------
        str


        ======================  ===============================================
        **Return value**        **Description**
        ======================  ===============================================
        ``'Extended'``          Event successfully extended.
        ``'ExtendDisallowed'``  Extending events is not enabled in RoomAgent.
        ``'TimeConflict'``      The requested *time* would cause this event to
                                overlap with the start of the next event.
        ``'NoEvent'``           There is no active event (when *event* is
                                None), or the given *event* no longer exists
                                (i.e. it was canceled).
        ``'PastEvent'``         The given *event*'s end time is in the past.
        ``'ExtendFailed'``      Extend failed for an unknown reason.
        ``'Disconnected'``      The interface is currently disconnected.
        ======================  ===============================================

        Examples
        --------
        ::

            # Extend the current event by 30 minutes.
            ret = schedulingdevice.Extend()
            if ret == 'Extended':
                # handle success
            else:
                # handle failure

            # Extend the next event by 1 hour.
            nextevent = schedulingdevice.GetNextEvent(todayonly=False)[0]
            ret = schedulingdevice.Extend(60, nextevent)
            if ret == 'Extended':
                # handle success
            else:
                # handle failure
        """
        return str()

    def GetActiveEvent(self) -> List['CalendarEvent']:
        """Get the currently active event(s).

        Returns
        -------
        list of CalendarEvent
            the currently active event(s) or an empty list
        """
        return [CalendarEvent()]

    @property
    def ActiveEventChanged(
        self
    ) -> Optional[
        Callable[
            [
                'RoomSchedulingInterface',
                List[CalendarEvent]
            ],
            Any
            ]
        ]:
        """``Event``: Assign or retrieve the handler for the
        `ActiveEventChanged` event that triggers when the active event
        changes.

        The assigned handler must accept two positional arguments. The first
        one is the `RoomSchedulingInterface` instance triggering the event,
        and the second is a list of `CalendarEvent`.  List will be empty when
        there are no active events.

        Returns
        -------
        Callable, None
            The assigned handler for the `ActiveEventChanged` event or `None`
            if no handler has been assigned.

        Examples
        --------
        ::

            @event(shedulingdevice, 'ActiveEventChanged')
            def HandleActiveEventChanged(interface, activeevents):
                for event in activeevents:
                    print('{}, {}, {}.'.format(event.Subject,
                                               event.Start,
                                               event.End))
        """
        pass

    @ActiveEventChanged.setter
    def ActiveEventChanged(
        self,
        handler: Optional[
            Callable[['RoomSchedulingInterface', List[CalendarEvent]], Any]
        ]
    ) -> None:
        pass

    def GetNextEvent(self, todayonly: bool=True) -> List['CalendarEvent']:
        """
        Parameters
        ----------
        todayonly : bool
            If *todayonly* is ``True``, it will only return the next event if
            it starts today, else an empty list will be returned.  If
            *todayonly* is ``False`` the next meeting that starts within 30
            days will be returned. (Default value = True)

        Returns
        -------
        list of CalendarEvent
            the next event(s).
        """
        return [CalendarEvent()]

    @property
    def NextEventChanged(
        self
    ) -> Optional[
        Callable[
            [
                'RoomSchedulingInterface',
                List[CalendarEvent]
            ],
            Any
            ]
        ]:
        """``Event``: Assign or retrieve the handler for the
        `NextEventChanged` event that triggers when the next event changes.

        The assigned handler must accept two positional arguments. The first
        one is the `RoomSchedulingInterface` instance triggering the event,
        and the second is a list of `CalendarEvent`.  List will be empty when
        there are no next events.

        Returns
        -------
        Callable, None
            The assigned handler for the `NextEventChanged` event or `None` if
            no handler has been assigned.

        Examples
        --------
        ::

            @event(shedulingdevice, 'NextEventChanged')
            def HandleNextEventChanged(interface, nextevents):
                for event in nextevents:
                    print('{}, {}, {}.'.format(event.Subject,
                                               event.Start,
                                               event.End))
        """
        pass

    @NextEventChanged.setter
    def NextEventChanged(
        self,
        handler: Optional[
            Callable[['RoomSchedulingInterface', List[CalendarEvent]], Any]
        ]
    ) -> None:
        pass

    def GetPreviousEvent(self, todayonly: bool=True) -> List['CalendarEvent']:
        """
        Parameters
        ----------
        todayonly : bool
            If *todayonly* is ``True``, it will only return the
            previous event if it started today, else an empty list will be
            returned.  If *todayonly* is ``False`` the previous meeting that
            started within 30 days will be returned. (Default value = True)

        Returns
        -------
        list of CalendarEvent
            the previous event(s).

        """
        return [CalendarEvent()]

    @property
    def PreviousEventChanged(
        self
    ) -> Optional[
        Callable[
            [
                'RoomSchedulingInterface',
                List[CalendarEvent]
            ],
            Any
            ]
        ]:
        """``Event``: Assign or retrieve the handler for the
        `PreviousEventChanged` event that triggers when the previous event
        changes.

        The assigned handler must accept two positional arguments. The first
        one is the `RoomSchedulingInterface` instance triggering the event,
        and the second is a list of `CalendarEvent`.  List will be empty when
        there are no active events.

        Returns
        -------
        Callable, None
            The assigned handler for the `PreviousEventChanged` event or
            `None` if no handler has been assigned.

        Examples
        --------
        ::

            @event(shedulingdevice, 'PreviousEventChanged')
            def HandlePreviousEventChanged(interface, previousevents):
                for event in previousevents:
                    print('{}, {}, {}.'.format(event.Subject,
                                               event.Start,
                                               event.End))
        """
        pass

    @PreviousEventChanged.setter
    def PreviousEventChanged(
        self,
        handler: Optional[
            Callable[['RoomSchedulingInterface', List[CalendarEvent]], Any]
        ]
    ) -> None:
        pass

    def GetTodaysEvents(
        self,
        excludeExpired: bool=True
    ) -> List['CalendarEvent']:
        """
        Parameters
        ----------
        excludeExpired : bool
            exclude expired events in results if ``True``
            else do not. (Default value = True)

        Returns
        -------
        list of CalendarEvent
            all of today's events
        """
        return [CalendarEvent()]

    @property
    def TodaysEventsChanged(
        self
    ) -> Optional[
        Callable[
            [
                'RoomSchedulingInterface',
                List[CalendarEvent]
            ],
            Any
            ]
        ]:
        """``Event``: Assign or retrieve the handler for the
        `TodaysEventsChanged` event that triggers when the today's events
        change.

        The assigned handler must accept two positional arguments. The first
        one is the `RoomSchedulingInterface` instance triggering the event,
        and the second is a list of `CalendarEvent`.  List will be empty when
        there are no active events.

        Returns
        -------
        Callable, None
            The assigned handler for the `TodaysEventsChanged` event or `None`
            if no handler has been assigned.

        Examples
        --------
        ::

            @event(shedulingdevice, 'TodaysEventsChanged')
            def HandleTodaysEventsChanged(interface, todaysevents):
                for event in todaysevents:
                    print('{}, {}, {}.'.format(event.Subject,
                                               event.Start,
                                               event.End))
        """
        pass

    @TodaysEventsChanged.setter
    def TodaysEventsChanged(
        self,
        handler: Optional[
            Callable[['RoomSchedulingInterface', List[CalendarEvent]], Any]
        ]
    ) -> None:
        pass

    def Release(self, event: Optional['CalendarEvent']=None) -> str:
        """Ends an event now. If no event is provided, the current event ends
        if one is in progress.

        Parameters
        ----------
        event : CalendarEvent
            The event to end if not the current event. (Default value = None)

        Returns
        -------
        str


        =======================  ==============================================
        **Return value**         **Description**
        =======================  ==============================================
        ``'Released'``           Event released successfully.
        ``'ReleaseDisallowed'``  Releasing events is not enabled in RoomAgent.
        ``'NoEvent'``            There is no active event (when *event* is
                                 None), or the given *event* no longer exists
                                 (i.e. it was canceled).
        ``'PastEvent'``          The given *event*'s end time is in the past.
        ``'ReleaseFailed'``      Release failed for an unknown reason.
        ``'Disconnected'``       The interface is currently disconnected.
        =======================  ==============================================

        Examples
        --------
        ::

            # Release the current event.
            res = schedulingdevice.Release()
            if res == 'Released':
                # handle success
            else:
                # handle failure

            # Release the next event
            nextevent = schedulingdevice.GetNextEvent(todayonly=False)[0]
            schedulingdevice.Release(nextevent)
        """
        return str()

    def Reserve(
        self,
        start: Optional[datetime]=None,
        duration: Optional[int]=None
    ) -> str:
        """Reserve the space.  Creates an event *duration* minutes long at the
        specified *start* time or now if start is not specified.  If
        *duration* is ``None``, the room scheduling device behavior will be
        used (e.g. 30 minute boundaries).

        Parameters
        ----------
        start : datetime
            When to reserve the space.  Start now if ``None``, otherwise start
            according to the specified datetime object. (Default value = None)
        duration : int
            The length of time, in minutes, to reserve the space. The default
            time configured in RoomAgent will be used if ``None``.

        Returns
        -------
        str


        =======================  ==============================================
        **Return value**         **Description**
        =======================  ==============================================
        ``'Reserved'``           Space successfully reserved.
        ``'ReserveDisallowed'``  Reserving the space is not enabled in
                                 RoomAgent.
        ``'TimeConflict'``       The requested *start* and *time* would cause
                                 this event to overlap with the start or end of
                                 an existing event.
        ``'PastEvent'``          The given *start* time is in the past.
        ``'ReserveFailed'``      Reserve failed for an unknown reason.
        ``'Disconnected'``       The interface is currently disconnected.
        =======================  ==============================================

        Notes
        -----
        For durations greater than 30 minutes, *Reserve* will set the meeting
        end time to the closest half-hour increment that is not longer than
        the requested duration.

        Examples
        --------
        ::

            # Reserve the space now
            ret = schedulingdevice.Reserve()
            if ret == 'Reserved':
                # handle success
            else:
                # handle failure

            # Reserve today from 5-6pm
            import datetime

            def todayat(hour, minute=0):
                return datetime.datetime.combine(
                    datetime.date.today(),
                    datetime.time(hour, minute)
                )

            schedulingdevice.Reserve(todayat(17), 60))
        """
        return str()

    @property
    def CalendarConnected(self) -> bool:
        """Get the state of the connection from the room scheduling device to
        the calendar server.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def CalendarConnectedChanged(
        self
    ) -> Optional[Callable[['RoomSchedulingInterface', bool], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `CalendarConnectedChanged` event that triggers when the connection
        from the room scheduling device to the calendar server changes state.

        The assigned handler must accept two positional arguments, which are
        the `RoomSchedulingInterface` instance that triggers the
        event and the new connection state as a bool (e.g. ``True``).

        Returns
        -------
        Callable, None
            The assigned handler for the `CalendarConnectedChanged` event or
            `None` if no handler has been assigned.

        Notes
        -----
        This event will be triggered after establishing a connection from the
        controller to the room scheduling device (i.e. `Connect`) and at any
        time the room scheduling device's connection to the calendar server
        changes thereafter.

        Examples
        --------
        ::

            @event(schedulingdevice, 'CalendarConnectedChanged')
            def CalendarServerConnected(schedulingdevice, connected):
                if connected:
                    print('Room scheduling device connected to the calendar server.')
                else:
                    print('Room scheduling device disconnected from the calendar server.')
        """
        pass

    @CalendarConnectedChanged.setter
    def CalendarConnectedChanged(
        self,
        handler: Optional[Callable[['RoomSchedulingInterface', bool], Any]]
    ) -> None:
        pass

    @property
    def Connected(
        self
    ) -> Optional[Callable[['RoomSchedulingInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Connected` event
        that triggers when the connection to the room scheduling device is
        established.

        The assigned handler must accept two positional arguments, which are
        the `RoomSchedulingInterface` instance that triggers the event and the
        new connection state (e.g. ``'Connected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Connected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(schedulingdevice, 'Connected')
            def schedulingDeviceConnected(schedulingdevice, state):
                print('Connected to room scheduling device.')
        """
        pass

    @Connected.setter
    def Connected(
        self,
        handler: Optional[Callable[['RoomSchedulingInterface', str], Any]]
    ) -> None:
        pass

    @property
    def Credentials(self) -> Tuple[str, str]:
        """Get the credentials for the room scheduling device ``('username',
        'password')``.

        Returns
        -------
        tuple
        """
        return (str(), str())

    @property
    def Disconnected(
        self
    ) -> Optional[Callable[['RoomSchedulingInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Disconnected`
        event that triggers when the connection to the room scheduling device
        is broken.

        The assigned handler must accept two positional arguments, which are
        the `RoomSchedulingInterface` instance that triggers the event and the
        new connection state (e.g. ``'Disconnected'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `Disconnected` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(schedulingdevice, 'Disconnected')
            def schedulingDeviceDisconnected(schedulingdevice, state):
                print('Disconnected from room scheduling device.')
        """
        pass

    @Disconnected.setter
    def Disconnected(
        self,
        handler: Optional[Callable[['RoomSchedulingInterface', str], Any]]
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
    def RoomName(self) -> str:
        """Get the configured room name of the targeted device.

        Returns
        -------
        str
        """
        return str()

    @property
    def Timezone(self) -> timezone:
        """Get the timezone of the targeted device.

        Returns
        -------
        timezone

        Notes
        -----
        See Python documentation for
        `timezone <https://docs.python.org/3.11/library/datetime.html#timezone-objects>`_.
        """
        return timezone(timedelta(), str())

    @property
    def TimezoneOffset(self) -> timedelta:
        """Get the time zone offset of the room scheduling device relative to
        UTC.

        Returns
        -------
        timedelta

        Notes
        -----
        See Python documentation for
        `timedelta <https://docs.python.org/3.11/library/datetime.html?highlight=timedelta#timedelta-objects>`_.
        """
        return timedelta()
