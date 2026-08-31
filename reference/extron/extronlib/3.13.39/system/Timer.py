class Timer():
    '''
    The Timer class allows the user to execute programmed actions on a
    periodic time schedule.

    .. versionadded:: 2.9

    .. code-block:: python

        @Timer(5)
        def handlePolling(timer, count):
            mainProjector.Send('get Power\\r')

            if not count % 20:
                mainProjector.Send('get LampHours\\r')

    .. note::
        * The handler (*Function*) must accept exactly two parameters, which
          are the :py:class:`Timer` that called it and the *Count*.
        * If the handler (*Function*) has not finished by the time the
          *Interval* has expired, *Function* will not be called and *Count*
          will not be incremented (i.e. that interval will be skipped).
    '''

    def __init__(self, Interval, Function=None):
        '''
        In addition to being used as a decorator, Timer can be named and
        modified.

        :param Interval: How often to call the handler in seconds (minimum
            interval is 0.1s).
        :type Interval: float
        :param Function: Handler function to execute each *Interval*.
        :type Function: function

        .. code-block:: python

            def handlePolling(timer, count):
                mainProjector.Send('get Power\\r')

                if not count % 20:
                    mainProjector.Send('get LampHours\\r')

            PollingTimer = Timer(5, handlePolling)
        '''
        pass

    def Change(self, Interval):
        '''
        Set a new *Interval* value for future events in this instance.

        :param Interval: How often to call the handler in seconds.
        :type Interval: float

        .. code-block:: python

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                PollingTimer.Change(60)
        '''
        pass

    def Pause(self):
        '''
        Pause the timer (i.e. stop calling the *Function*).

        .. note:: Does not reset the timer or the *Count*.

        .. code-block:: python

            @event(mainProjector, 'Offline')
            def handleOfflineEvent(interface, state):
                PollingTimer.Pause()
        '''
        pass

    def Restart(self):
        '''
        Restarts the timer -- resets the *Count* and executes the *Function*
        in *Interval* seconds.

        .. code-block:: python

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                PollingTimer.Restart()
        '''
        pass

    def Resume(self):
        '''
        Resume the timer after being paused or stopped.

        .. code-block:: python

            @event(mainProjector, 'Online')
            def handleOnlineEvent(interface, state):
                PollingTimer.Resume()
        '''
        pass

    def Stop(self):
        '''
        Stop the timer.

        .. note:: Resets the timer and the *Count*.

        .. code-block:: python

            @event(mainProjector, 'Online')
            def handleOfflineEvent(interface, state):
                PollingTimer.Stop()
        '''
        pass

    @property
    def Count(self):
        '''
        :return: Number of events triggered by this timer.
        :rtype: int
        '''
        pass

    @property
    def Function(self):
        '''
        :return: Handler function to execute each *Interval*.  *Function* must
            accept exactly two parameters, which are the :py:class:`Timer`
            that called it and the *Count*.
        :rtype: function
        '''
        pass

    @property
    def Interval(self):
        '''
        :return: How often to call the handler in seconds.
        :rtype: float
        '''
        pass

    @property
    def State(self):
        '''
        :return: Current state of Timer (``'Running'``, ``'Paused'``,
            ``'Stopped'``)
        :rtype: string
        '''
        pass

    @property
    def StateChanged(self):
        '''
        ``Event:`` Triggers when the timer state changes.

        The callback takes two arguments. The first is the
        :py:mod:`~extronlib.system.Timer` instance triggering the event
        and the second is a string (``'Running'``, ``'Paused'``,
        ``'Stopped'``).

        .. code-block:: python

            @event(TimerInstance, 'StateChanged')
            def HandleStateChanged(timer, state):
                if state == 'Running':
                    ShowTimerRunning()
                else:
                    ShowTimerNotRunning()
        '''
        pass
