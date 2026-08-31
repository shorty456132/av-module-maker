from . import Device


class eBUSDevice(Device):
    '''
    Defines common interface to Extron eBUS panels

    .. versionadded:: 2.5
    '''

    def __init__(self, Host, DeviceAlias):
        '''
        :param Host: handle to Extron *ProcessorDevice* to which the
            *eBUSDevice* is connected
        :type Host: |ProcessorDevice|
        :param DeviceAlias: Device Alias of the Extron device
        :type DeviceAlias: string

        .. code-block:: python

            # Create Primary Processor
            ConfRoom = ProcessorDevice('Main')

            # Create eBUSDevice
            ConfRoomPanel = eBUSDevice(ConfRoom, 'ConfEBP')
        '''
        pass

    def Click(self, count=1, interval=None):
        '''
        Play default buzzer sound on applicable device

        :param count: number of buzzer sound to play
        :type count: int
        :param interval: time gap in millisecond between consecutive sounds
        :type interval: int

        .. note:: If *count* is greater than 1, *interval* must be provided to
            indicate the time gap in ms between consecutive buzzer sounds.
        '''
        pass

    def GetMute(self, name):
        '''
        Get the mute state for the given channel

        The defined channel names are:
            * ``'Click'`` - button click volume

        :param name: name of channel.
        :type name: string
        :return: mute state (``'On'`` or ``'Off'``)
        :rtype: string

        .. code-block:: python

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumEBP.GetMute('Click') == 'On':
                    PodiumEBP.SetMute('Click', 'Off')
                else:
                    PodiumEBP.SetMute('Click', 'On')

        .. versionadded:: 2.6
        '''
        pass

    def Reboot(self):
        '''
        Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.

        .. versionadded:: 3.11
        '''
        pass

    def SendCommand(self, command, value=None):
        '''
        Send command to eBUSDevice.

        :param command: command name to issue
        :type command: string
        :param value: command specific value to pass with commend
        :type value: int, tuple of ints

        .. code-block:: python

            VoiceLiftDevice.SendCommand('Chime', 1)     # Enable Chime
            VoiceLiftDevice.SendCommand('Usage')        # Query usage

        .. note::
            * For supported eBUS devices.
            * See device documentation for supported commands.

        .. versionadded:: 3.8
        '''
        pass

    def SetInactivityTime(self, times):
        '''
        Set the inactivity times of the |eBUSDevice|.  When each time expires,
        the :py:data:`InactivityChanged` event will be triggered.  All times
        are absolute.

        :param times: list of times.  Each time in whole seconds
        :type times: list of ints

        .. code-block:: python

            PodiumPanel = eBUSDevice('Podium Panel')
            PodiumPanel.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

            @event(PodiumPanel, 'InactivityChanged')
            def UnoccupyRoom(Panel, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()

        .. note:: Applies to EBP models only.
        '''
        pass

    def SetMute(self, name, mute):
        '''
        Set the mute state for the given channel

        The defined channel names are:
            * ``'Click'`` - button click volume

        :param name: name of channel.
        :type name: string
        :param mute: mute state (``'On'`` or ``'Off'``)
        :type mute: string

        .. code-block:: python

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumEBP.GetMute('Click') == 'On':
                    PodiumEBP.SetMute('Click', 'Off')
                else:
                    PodiumEBP.SetMute('Click', 'On')

        .. versionadded:: 2.6
        '''
        pass

    def SetSleepTimer(self, state, duration=None):
        '''
        Enable/disable sleep timer. Either ``'On'`` or ``True`` enables sleep
        timer. ``'Off'`` or ``False`` disables sleep timer.

        :param state: whether to enable the sleep timer
        :type state: bool, string
        :param duration: time in seconds to sleep
        :type duration: int

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumPanel.SetSleepTimer('On', 60)
        '''
        pass

    def Sleep(self):
        '''Force the device to sleep immediately'''
        pass

    def Wake(self):
        '''Force the device to wake up immediately'''
        pass

    @property
    def Host(self):
        '''
        :return: Handle to the Extron *ProcessorDevice* to which the
            *eBUSDevice* is connected.
        :rtype: |ProcessorDevice|
        '''
        pass

    @property
    def ID(self):
        '''
        :return: device's ID (set by DIP switch)
        :rtype: int
        '''
        pass

    @property
    def InactivityChanged(self):
        '''
        ``Event:`` Triggers at times specified by :py:meth:`SetInactivityTime`
        after state transition of inactivity timer.

        The callback takes two arguments. The first one is the |eBUSDevice|
        instance triggering the event and time with a float value of
        inactivity time in seconds.

        .. code-block:: python

            PodiumPanel = eBUSDevice('Podium Panel')
            PodiumPanel.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

            @event(PodiumPanel, 'InactivityChanged')
            def UnoccupyRoom(Panel, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()

        .. note:: Applies to EBP models only.
        '''
        pass

    @property
    def InactivityTime(self):
        '''
        :return: Seconds since last activity.
        :rtype: int

        .. note::
            * 0 = Active, Nonzero = Time of inactivity.
            * Applies to EBP models only.
        '''
        pass

    @property
    def LidChanged(self):
        '''
        ``Event:`` Triggers when the Lid state changes.

        The callback takes two arguments. The first one is the |eBUSDevice|
        instance triggering the event and the second is the current lid state
        (``'Opened'`` or ``'Closed'``).
        '''
        pass

    @property
    def LidState(self):
        '''
        :return: the current lid state (``'Opened'`` or ``'Closed'``)
        :rtype: string
        '''
        pass

    @property
    def ReceiveResponse(self):
        '''
        ``Event:`` Receive Response event handler used for asynchronous
        transactions

        The callback takes three arguments. The first one is the
        :py:class:`eBUSDevice` instance triggering the event, the second one
        is a the command (string), and the third is a tuple of context
        specific integers.

        .. code-block:: python
            :linenos:

            # Receive Response == 'Mute', (1,)
            @event(VoiceLiftDevice, 'ReceiveResponse')
            def MainFeedbackHandler(interface, command, value):
                if command == 'Mute':
                    state = value[0]
                    ...

        .. note::
            * For supported eBUS devices.
            * See device documentation for supported commands.

        .. versionadded:: 3.8
        '''
        pass

    @property
    def SleepChanged(self):
        '''
        ``Event:`` Triggers when sleep state changes.

        The callback takes two arguments. The first one is the |eBUSDevice|
        instance triggering the event and the second one is a string
        (``'Asleep'`` or ``'Awake'``).

        .. code-block:: python

             @event(PodiumPanel, 'SleepChanged')
             def HandleSleepChanged(Panel, state):
                 print('{} Sleep State Changed: {}'.format(Panel.DeviceAlias, state))
        '''
        pass

    @property
    def SleepState(self):
        '''
        :return: the current sleep state of the device (``'Asleep'``,
            ``'Awake'``)
        :rtype: string
        '''
        pass

    @property
    def SleepTimer(self):
        '''
        :return: sleep timer timeout
        :rtype: int
        '''
        pass

    @property
    def SleepTimerEnabled(self):
        '''
        :return: ``True`` if sleep timer is enabled
        :rtype: bool
        '''
        pass
