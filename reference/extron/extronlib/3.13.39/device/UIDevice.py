from . import Device


class UIDevice(Device):
    '''
    Entity to communicate with Extron Device featuring user interactive input.
    '''

    def Click(self, count=1, interval=None):
        '''
        Play default buzzer sound on applicable device

        :param count: number of buzzer sound to play
        :type count: int
        :param interval: time gap between the starts of consecutive buzzer
            sounds
        :type interval: float

        .. note:: If *count* is greater than 1, *interval* must be provided.
        '''
        pass

    def GetHDCPStatus(self, videoInput):
        '''
        Return the current HDCP Status for the given input.

        :param videoInput: input (``'HDMI'`` or ``'XTP'``)
        :type videoInput: string
        :return: ``True`` or ``False``
        :rtype: bool

        .. code-block:: python

            HDCPStatus = PodiumTLP.GetHDCPStatus('XTP')
            if not HDCPStatus:
                PodiumTLP.ShowPopup('No HDCP')
        '''
        pass

    def GetInputPresence(self, videoInput):
        '''
        Return the current input presence status for the given input.

        :param videoInput: input (``'HDMI'`` or ``'XTP'``)
        :type videoInput: string
        :return: ``True`` or ``False``
        :rtype: bool

        .. code-block:: python

            InputPresence = PodiumTLP.GetInputPresence('XTP')
            if not InputPresence:
                PodiumTLP.ShowPopup('No XTP')
        '''
        pass

    def GetMute(self, name):
        '''
        Get the mute state for the given channel

        The defined channel names are:
            * ``'Master'`` - the master volume
            * ``'Speaker'`` - the built-in speakers
            * ``'Line'`` - the line out
            * ``'Click'`` - button click volume
            * ``'Sound'`` - sound track playback volume
            * ``'HDMI'`` - HDMI input volume
            * ``'XTP'`` - XTP input volume

        :param name: name of channel.
        :type name: string
        :return: mute state (``'On'`` or ``'Off'``)
        :rtype: string

        .. code-block:: python

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumTLP.GetMute('HDMI') == 'On':
                    PodiumTLP.SetMute('HDMI', 'Off')
                else:
                    PodiumTLP.SetMute('HDMI', 'On')

        .. versionadded:: 2.6
        '''
        pass

    def GetVolume(self, name):
        '''
        Return current volume level for the given channel

        The defined channel names are:
            * ``'Master'`` - the master volume
            * ``'Click'`` - button click volume
            * ``'Sound'`` - sound track playback volume
            * ``'HDMI'`` - HDMI input volume
            * ``'XTP'`` - XTP input volume

        :param name: name of volume channel.
        :type name: string
        :return: volume level
        :rtype: int

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def RefreshPage(button, state):
                currentVolume = PodiumTLP.GetVolume('HDMI')
                ...
        '''
        pass

    def HideAllPopups(self):
        '''Dismiss all popup pages'''
        pass

    def HidePopup(self, popup):
        '''
        Hide popup page

        :param popup: popup page number or name
        :type popup: int, string
        '''
        pass

    def HidePopupGroup(self, group):
        '''
        Hide all popup pages in a popup group

        :param group: popup group number
        :type group: int

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def Reset(button, state):
                PodiumTLP.HidePopupGroup(1)
        '''
        pass

    def PlaySound(self, filename):
        '''
        Play a sound file identified by the *filename*

        :param filename: name of sound file
        :type filename: string

        .. note::
            * Only WAV files can be played.
            * A subsequent call will preempt the currently playing file.
            * Sound file must be added to the project file.

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def OccupyRoom(button, state):
                PodiumTLP.SetLEDBlinking(65533, 'Slow', ['Red', 'Off'])
                PodiumTLP.PlaySound('startup.wav')
        '''
        pass

    def Reboot(self):
        '''
        Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.

        .. versionadded:: 3.11
        '''
        pass

    def SetAutoBrightness(self, state):
        '''
        Set auto brightness state

        Either ``'On'`` or ``True`` turns on auto brightness. ``'Off'`` or
        ``False`` turns off auto brightness.

        :param state: whether to enable auto brightness
        :type state: bool, string

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetAutoBrightness('On')
        '''
        pass

    def SetBrightness(self, level):
        '''
        Set LCD screen brightness level

        :param level: brightness level from 0 ~ 100
        :type level: int

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetAutoBrightness('Off')
                PodiumTLP.SetBrightness(50)
        '''
        pass

    def SetDisplayTimer(self, state, timeout):
        '''
        Enable/disable display timer

        Either ``'On'`` or ``True`` enables display timer. ``'Off'`` or
        ``False`` disables display timer.

        :param state: whether to enable the display timer
        :type state: bool, string
        :param timeout: time in seconds before turn off the display (1-120)
        :type timeout: int

        .. note:: Display timer is applicable to TLI only.

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetDisplayTimer(True, 180)
        '''
        pass

    def SetInactivityTime(self, times):
        '''
        Set the inactivity times of the |UIDevice|.  When each time expires,
        the :py:data:`InactivityChanged` event will be triggered.  All times
        are absolute.

        :param times: list of times.  Each time in whole seconds
        :type times: list of ints

        .. code-block:: python

            PodiumTLP = UIDevice('Podium TLP')
            PodiumTLP.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

            @event(PodiumTLP, 'InactivityChanged')
            def UnoccupyRoom(tlp, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()
        '''
        pass

    def SetInput(self, videoInput):
        '''
        Sets the input.  Inputs must be published for each device.

        :param videoInput: input to select (``'HDMI'`` or ``'XTP'``)
        :type videoInput: string

        .. code-block:: python

            PodiumTLP.SetInput('HDMI')
        '''
        pass

    def SetLEDBlinking(self, ledId, rate, stateList):
        '''
        Make the LED cycle, at ADA compliant rates, through each of the states
        provided.

        .. list-table::
            :widths: 20 20

            * - **Rate**
              - **Frequency**
            * - Slow
              - 0.5 Hz
            * - Medium
              - 1 Hz
            * - Fast
              - 2 Hz

        .. note:: Using this function will blink in unison with other LEDs.

        :param ledId: LED id
        :type ledId: int
        :param rate: ADA compliant blink rate. (``'Slow'``, ``'Medium'``,
            ``'Fast'``)
        :type rate: string
        :param stateList: List of colors
        :type stateList: list of strings

        .. note:: Available colors are ``Red``, ``Green``, and ``Off``.

        .. code-block:: python

            PodiumTLP = UIDevice('Podium TLP')

            @event(ButtonObject, 'Pressed')
            def UnoccupyRoom(button, state):
                PodiumTLP.SetLEDBlinking(65533, 'Slow', ['Off', 'Red'])
        '''
        pass

    def SetLEDState(self, ledId, state):
        '''
        Drive the LED to the given color

        :param ledId: LED id
        :type ledId: int
        :param state: LED color or 'Off'.
        :type state: string

        .. note:: Available colors are ``Red``, ``Green``, and ``Off``.

        .. code-block:: python

            @event(SomeOtherButton, 'Released')
            def UnoccupyRoom(button, state):
                PodiumTLP.SetLEDState(65533, 'Off')
        '''
        pass

    def SetMotionDecayTime(self, duration):
        '''
        Set the period of time to trigger :py:data:`MotionDetected` after last
        motion was detected.

        :param duration: time in seconds (minimum/default value is 10)
        :type duration: float

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetMotionDecayTime(30)
        '''
        pass

    def SetMute(self, name, mute):
        '''
        Set the mute state for the given channel

        The defined channel names are:
            * ``'Master'`` - the master volume
            * ``'Speaker'`` - the built-in speakers
            * ``'Line'`` - the line out
            * ``'Click'`` - button click volume
            * ``'Sound'`` - sound track playback volume
            * ``'HDMI'`` - HDMI input volume
            * ``'XTP'`` - XTP input volume

        :param name: name of channel.
        :type name: string
        :param mute: mute state (``'On'`` or ``'Off'``)
        :type mute: string

        .. code-block:: python

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumTLP.GetMute('HDMI') == 'On':
                    PodiumTLP.SetMute('HDMI', 'Off')
                else:
                    PodiumTLP.SetMute('HDMI', 'On')

        .. versionadded:: 2.6
        '''
        pass

    def SetSleepTimer(self, state, duration=None):
        '''
        Enable/disable sleep timer. Either ``'On'`` or ``True`` enables sleep
        timer. ``'Off'`` or ``False`` disables sleep timer.

        :param state: whether to enable the sleep timer
        :type state: bool, string
        :param duration: time in seconds to sleep (1-120)
        :type duration: int

        .. code-block:: python

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetSleepTimer('On', 60)
        '''
        pass

    def SetVolume(self, name, level):
        '''
        Adjust volume level for the given channel

        The defined channel names are:
            * ``'Master'`` - the master volume
            * ``'Click'`` - button click volume
            * ``'Sound'`` - sound track playback volume
            * ``'HDMI'`` - HDMI input volume
            * ``'XTP'`` - XTP input volume

        :param name: name of channel.
        :type name: string
        :param level: volume level 0 ~ 100
        :type level: int
        '''
        pass

    def SetWakeOnMotion(self, state):
        '''
        Enable/disable wake on motion.

        :param state: ``True`` (``'On'``) or ``False`` ('Off') to enable and
            disable wake on motion, respectively.
        :type state: bool, string
        '''
        pass

    def ShowPage(self, page):
        '''
        Show page on the screen

        :param page: absolute page number or name
        :type page: int, string
        '''
        pass

    def ShowPopup(self, popup, duration=0):
        '''
        Display pop-up page for a period of time.

        :param popup: pop-up page number or name
        :type popup: int, string
        :param duration: duration (in seconds) the pop-up remains on the
            screen. 0 means forever.
        :type duration: float

        .. note:: If a pop-up is already showing for a finite period of time,
            calling this method again with the same pop-up will replace the
            remaining period with the new period.
        '''
        pass

    def Sleep(self):
        '''Force the device to sleep immediately'''
        pass

    def StopSound(self):
        '''Stop playing sound file'''
        pass

    def Wake(self):
        '''Force the device to wake up immediately'''
        pass

    @property
    def AmbientLightValue(self):
        '''
        :return: current ambient light value
        :rtype: int
        '''
        pass

    @property
    def AutoBrightness(self):
        '''
        :return: current auto brightness state
        :rtype: bool
        '''
        pass

    @property
    def Brightness(self):
        '''
        :return: current LCD brightness level
        :rtype: int
        '''
        pass

    @property
    def BrightnessChanged(self):
        '''
        ``Event:`` Triggers when LCD brightness has changed.

        The callback takes two arguments. The first one is the |UIDevice|
        instance triggering the event and the second one is the current
        brightness level as an integer.

        .. code-block:: python

             @event(PodiumTLP, 'BrightnessChanged')
             def HandleBrightnessChanged(tlp, brightness):
                 print('{} Brightness Changed: {}'.format(tlp.DeviceAlias, brightness))
        '''
        pass

    @property
    def DisplayState(self):
        '''
        :return: the current display state of the device (``'On'``, ``'Off'``)
        :rtype: string

        .. note:: This property is applicable to TLI only.
        '''
        pass

    @property
    def DisplayTimer(self):
        '''
        :return: Return display timer timeout seconds
        :rtype: int
        '''
        pass

    @property
    def DisplayTimerEnabled(self):
        '''
        :return: current state of the display timer
        :rtype: bool
        '''
        pass

    @property
    def FirmwareVersion(self):
        '''
        :return: the firmware version of this device
        :rtype: string

        .. versionadded:: 2.4
        '''
        pass

    @property
    def HDCPStatusChanged(self):
        '''
        ``Event:`` Triggers when HDCP Status changes.

        The callback takes two arguments. The first one is the |UIDevice|
        instance triggering the event and state with a tuple: (Input, Status).

        .. code-block:: python

            @event(PodiumTLP, 'HDCPStatusChanged')
            def HandleHDCPStatusChangedChange(tlp, state):
                if state[0] == 'HDMI' and not state[1]:
                    PodiumTLP.ShowPopup('No HDCP')
        '''
        pass

    @property
    def Hostname(self):
        '''
        :return: the hostname of this device
        :rtype: string
        '''
        pass

    @property
    def InactivityChanged(self):
        '''
        ``Event:`` Triggers at times specified by :py:meth:`SetInactivityTime`
        after state transition of inactivity timer.

        The callback takes two arguments. The first one is the |UIDevice|
        instance triggering the event and time with a float value of
        inactivity time in seconds.

        .. code-block:: python

            PodiumTLP = UIDevice('Podium TLP')
            PodiumTLP.SetInactivityTime([3000, 3600])    # Fifty minutes and One hour

            @event(PodiumTLP, 'InactivityChanged')
            def UnoccupyRoom(tlp, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()
        '''
        pass

    @property
    def InactivityTime(self):
        '''
        :return: Seconds since last activity.
        :rtype: int

        .. note:: 0 = Active, Nonzero = Time of inactivity.
        '''
        pass

    @property
    def InputPresenceChanged(self):
        '''
        ``Event:`` Triggers when Input Presence changes.

        The callback takes two arguments. The first one is the |UIDevice|
        instance triggering the event and state with a tuple: (Input, Status).

        .. code-block:: python

            @event(PodiumTLP, 'InputPresenceChanged')
            def HandleInputPresenceChanged(tlp, state):
                if state[0] == 'HDMI' and not state[1]:
                    if PodiumTLP.GetInputPresence('XTP'):
                        PodiumTLP.SetInput('XTP')
                    else:
                        PodiumTLP.ShowPopup('No Input Available')
        '''
        pass

    @property
    def IPAddress(self):
        '''
        :return: IP address of this device
        :rtype: string
        '''
        pass

    @property
    def LidChanged(self):
        '''
        ``Event:`` Triggers when the Lid state changes.

        The callback takes two arguments. The first one is the |UIDevice|
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
    def LightChanged(self):
        '''
        ``Event:`` Triggers when ambient light changes

        The callback takes two arguments. The first one is the |UIDevice|
        instance triggering the event and the second is the ambient light
        level in the range of 0 ~ 255.
        '''
        pass

    @property
    def LightDetectedState(self):
        '''
        :return: State of light detection. (``'Detected'``, ``'Not Detected'``)
        :rtype: string
        '''
        pass

    @property
    def MACAddress(self):
        '''
        :return: MAC address of this device
        :rtype: string

        .. versionadded:: 2.4
        '''
        pass

    @property
    def MotionDecayTime(self):
        '''
        :return: the period of time to trigger :py:data:`MotionDetected` event
            after last motion was detected. The default (and minimum) value is
            10 seconds.
        :rtype: int
        '''
        pass

    @property
    def MotionDetected(self):
        '''
        ``Event:`` Triggers when Motion is detected.

        The callback takes two arguments. The first one is the |UIDevice|
        instance triggering the event and the second one is a string
        (``'Motion'`` or ``'No Motion'``).
        '''
        pass

    @property
    def MotionState(self):
        '''
        :return: the state of the Motion sensor (e.g. ``Motion``, ``No Motion``)
        :rtype: string
        '''
        pass

    @property
    def SerialNumber(self):
        '''
        :return: Serial number of this device
        :rtype: string

        .. versionadded:: 2.4
        '''
        pass

    @property
    def SleepChanged(self):
        '''
        ``Event:`` Triggers when sleep state changes.

        The callback takes two arguments. The first one is the |UIDevice|
        instance triggering the event and the second one is a string
        (``'Asleep'`` or ``'Awake'``).

        .. code-block:: python

             @event(PodiumTLP, 'SleepChanged')
             def HandleSleepChanged(tlp, state):
                 print('{} Sleep State Changed: {}'.format(tlp.DeviceAlias, state))
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

    @property
    def SystemSettings(self):
        '''
        :return: a dictionary of data describing the settings (defined in
            Toolbelt) of this device
        :rtype: dict

        .. code-block:: python
            :linenos:

            {
                'Network': {
                    'LAN': {
                        'DNSServers': ['192.168.1.1',],
                        'Gateway': '192.168.254.1',
                        'Hostname': 'ConfRoom',
                        'IPAddress': '192.168.254.250',
                        'SubnetMask': '255.255.255.0',
                        'SearchDomains': ['extron.com',],
                    },
                },
                'ProgramInformation': {
                    'Author': 'jdoe',
                    'DeviceName': 'TLP Pro 720T : 192.168.254.251',
                    'FileLoaded': 'GS Project.gs',
                    'LastUpdated': '1/23/2016 9:08:29 AM',
                    'SoftwareVersion': '1.0.2.195',
                }
            }

        .. versionadded:: 3.6
        '''
        pass

    @property
    def UserUsage(self):
        '''
        :return: user data usage of this device in KB ``(used, total)``.
        :rtype: tuple of ints

        .. versionadded:: 2.4
        '''
        pass

    @property
    def WakeOnMotion(self):
        '''
        :return: current wake on motion state
        :rtype: bool
        '''
        pass
