class Wait():
    '''
    The wait class allows the user to execute programmed actions after a
    desired delay without blocking other processor activity.

    .. versionadded:: 3.12
        Improved backend handling of Wait object.

    .. code-block:: python

        @event(PowerOn, 'Pressed')
        def HandlePowerButton(button, state):
            mainProjector.Send('Power=On\\r')
            @Wait(30)
            def CheckPowerState():
                mainProjector.Send('get Power\\r')
    '''

    def __init__(self, Time, Function=None):
        '''
        In addition to being used as a one-shot (decorator), *Wait* can be
        named and reusable.

        :param Time: Expiration time of the wait in seconds
        :type Time: float
        :param Function: Code to execute when Time expires
        :type Function: function

        .. code-block:: python

            closeWait = None    # Delay to hide Setup Page

            @event(ShowSetup, 'Released')
            def handleShowSetup(button, state):
                global closeWait
                def CloseSetupPage():
                    ConfRoomWall.ShowPage('Main')
                closeWait = Wait(60, CloseSetupPage)
                ConfRoomWall.ShowPage('Setup')
        '''
        pass

    def Add(self, Time):
        '''
        Add time to current interval.

        .. note:: Add() does not modify :py:attr:`Time`.

        :param Time: Time in seconds
        :type Time: float

        .. code-block:: python

            QueryDelay = Wait(3)

            def ErrorRecieved():    # Called by received data handler
                QueryDelay.Add(1)
        '''
        pass

    def Cancel(self):
        '''
        Stop *Function* from executing when the *Time* expires.

        .. code-block:: python

            @event(CloseSetup, 'Released')
            def CloseSetup(button, state):
                global closeWait
                if closeWait:
                    closeWait.Cancel()
                    closeWait = None
                ConfRoomWall.ShowPage('Main')
        '''
        pass

    def Change(self, Time):
        '''
        Set a new *Time* value for current and subsequent runs of this
        instance.

        .. note:: Change() will modify :py:attr:`Time`.

        :param Time: Time in seconds
        :type Time: float

        .. code-block:: python

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                closeWait.Change(60)
        '''
        pass

    def Restart(self):
        '''
        Restarts the *Wait* (i.e. executes the *Function* in *Time* seconds).
        If the *Wait* is active, Restart() cancels that *Wait* before starting
        a new one.

        .. code-block:: python

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                closeWait.Restart()
        '''
        pass

    @property
    def Function(self):
        '''
        :return: Code to execute when *Time* expires.
        :rtype: function
        '''
        pass

    @property
    def Time(self):
        '''
        :return: Expiration time of the *Wait* in seconds with 10ms precision.
        :rtype: float
        '''
        pass
