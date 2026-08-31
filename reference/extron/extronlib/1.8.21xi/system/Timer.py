from typing import Any, Callable, Optional


class Timer():
    """The Timer class allows the user to execute programmed actions on a
    periodic time schedule.

    Examples
    --------
    ::

        @Timer(5)
        def handlePolling(timer, count):
            mainProjector.Send('get Power\\r')

            if not count % 20:
                mainProjector.Send('get LampHours\\r')

    Notes
    -----
    * The handler (*Function*) must accept exactly two parameters, which are
      the `Timer` that called it and the *Count*.
    * If the handler (*Function*) has not finished by the time the *Interval*
      has expired, *Function* will not be called and *Count* will not be
      incremented (i.e. that interval will be skipped).
    """

    def __init__(
        self,
        Interval: float | int,
        Function: Optional[Callable[['Timer', int], Any]]=None
    ):
        """In addition to being used as a decorator, Timer can be named and
        modified.

        Parameters
        ----------
        Interval : float
            How often to call the handler in seconds (minimum interval is
            0.1s).
        Function : function
            Handler function to execute each *Interval*.

        Examples
        --------
        ::

            def handlePolling(timer, count):
                mainProjector.Send('get Power\\r')

                if not count % 20:
                    mainProjector.Send('get LampHours\\r')

            PollingTimer = Timer(5, handlePolling)
        """
        pass

    def Change(self, Interval: float | int) -> None:
        """Set a new *Interval* value for future events in this instance.

        Parameters
        ----------
        Interval : float
            How often to call the handler in seconds.

        Examples
        --------
        ::

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                PollingTimer.Change(60)
        """
        pass

    def Pause(self) -> None:
        """Pause the timer (i.e. stop calling the *Function*).

        Notes
        -----
        Does not reset the timer or the *Count*.

        Examples
        --------
        ::

            @event(mainProjector, 'Offline')
            def handleOfflineEvent(interface, state):
                PollingTimer.Pause()
        """
        pass

    def Restart(self) -> None:
        """Restarts the timer -- resets the *Count* and executes the *Function*
        in *Interval* seconds.

        Examples
        --------
        ::

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                PollingTimer.Restart()
        """
        pass

    def Resume(self) -> None:
        """Resume the timer after being paused or stopped.

        Examples
        --------
        ::

            @event(mainProjector, 'Online')
            def handleOnlineEvent(interface, state):
                PollingTimer.Resume()
        """
        pass

    def Stop(self) -> None:
        """Stop the timer.

        Notes
        -----
        Resets the timer and the *Count*.

        Examples
        --------
        ::

            @event(mainProjector, 'Online')
            def handleOfflineEvent(interface, state):
                PollingTimer.Stop()
        """
        pass

    @property
    def Count(self) -> int:
        """Number of events triggered by this timer.

        Returns
        -------
        int
        """
        return int()

    @property
    def Function(self) -> Optional[Callable[['Timer', int], Any]]:
        """Handler function to execute each *Interval*.

        Returns
        -------
        Callable, None
            Must accept exactly two parameters, which are the `Timer` that
            called it and the *Count*.
        """
        pass

    @Function.setter
    def Function(
        self,
        handler: Optional[Callable[['Timer', int], Any]]
    ) -> None:
        pass

    @property
    def Interval(self) -> float:
        """How often to call the handler in seconds.

        Returns
        -------
        float
        """
        return float()

    @property
    def State(self) -> str:
        """Current state of Timer (``'Running'``, ``'Paused'``, or
        ``'Stopped'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def StateChanged(self) -> Optional[Callable[['Timer', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `StateChanged`
        event that triggers when the timer state changes.

        The assigned handler must accept exactly two positional arguments. The
        first is the `Timer` instance triggering the event and the second is a
        string (``'Running'``, ``'Paused'``, ``'Stopped'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `StateChanged` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(TimerInstance, 'StateChanged')
            def HandleStateChanged(timer, state):
                if state == 'Running':
                    ShowTimerRunning()
                else:
                    ShowTimerNotRunning()
        """
        pass
