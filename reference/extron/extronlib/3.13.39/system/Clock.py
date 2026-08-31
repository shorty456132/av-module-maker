class Clock():
    '''
    The clock is used to create timed events. It will allow the user to
    schedule programmed actions to occur based on calendar time.

    .. note::
        * When DST causes the clock to spring forward one hour, events
          scheduled within the skipped hour do not fire.
        * When DST causes the clock to fall back an hour, events scheduled
          within the repeated hour fire twice.
    '''

    def __init__(self, Times, Days=None, Function=None):
        '''
        :param Times: list of times (e.g. ``'HH:MM:SS'``) of day to call
            `Function`
        :type Times: list of strings
        :param Days: list of weekdays to set alarm. If Days is omitted, the
            alarm is set for every weekday
        :type Days: list of strings
        :param Function: function to execute when alarm time is up
        :type Function: function

        .. code-block:: python

            def ShutdownSystems(clock, dt):
                print('Shutting down...')
                ...

            nightlyShutdown = Clock(['19:00:00'], None, ShutdownSystems)
            nightlyShutdown.Enable()
        '''
        pass

    def Disable(self):
        '''
        Disable alarm

        .. code-block:: python

            nightlyShutdown.Disable()
        '''
        pass

    def Enable(self):
        '''
        Enable alarm

        .. code-block:: python

            nightlyShutdown.Enable()
        '''
        pass

    def SetDays(self, Days):
        '''
        Set new alarm days

        :param Days: a list of Calendar days, as listed in :py:const:`WEEKDAYS`
        :type Days: list of strings

        .. code-block:: python

            nightlyShutdown.SetDays(['Monday', 'Wednesday', 'Friday'])
        '''
        pass

    def SetTimes(self, Times):
        '''
        Set new alarm times

        :param Times: list of times (e.g. ``'HH:MM:SS'``) of day to call
            `Function`
        :type Times: list of strings

        .. code-block:: python

            nightlyShutdown.SetTimes(['20:00:00'])
        '''
        pass

    @property
    def Days(self):
        '''
        :return: list of days to execute
        :rtype: list of strings

        .. note:: list will be empty if it was not provided to the constructor
            (i.e. the Clock is set for every day).
        '''
        pass

    @property
    def Function(self):
        '''
        :return: Code to execute at given Times.
        :rtype: function

        .. note:: Function must accept two parameters: the Clock object and
            datetime object.
        '''
        pass

    @property
    def State(self):
        '''
        :return: State of the clock device.  (``'Enabled'``, ``'Disabled'``)
        :rtype: string
        '''
        pass

    @property
    def Times(self):
        '''
        :return: list of times to execute.
        :rtype: list of strings
        '''
        pass

    @property
    def WEEKDAYS(self):
        '''
        Calendar weekdays

        :param WEEKDAYS: days of the week dictionary: ``{'Monday': 0,
            'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4,
            'Saturday': 5, 'Sunday': 6}``
        :type WEEKDAYS: dict
        '''
        pass
