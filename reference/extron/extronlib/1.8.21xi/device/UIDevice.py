from typing import Any, Callable, List, Optional, Tuple

from . import Device


class UIDevice(Device):
    """Entity to communicate with Extron Devices featuring user interactive
    input."""

    def Click(
        self,
        count: int=1,
        interval: Optional[float]=None
    ) -> None:
        """Play default buzzer sound on this device

        Parameters
        ----------
        count : int
            number of buzzer sound to play (Default value = 1)
        interval : float
            time gap between the starts of consecutive buzzer sounds (Default
            value = None)

        Notes
        -----
        If *count* is greater than 1, *interval* must be provided.
        """
        pass

    def GetHDCPStatus(
        self,
        videoInput: str
    ) -> bool:
        """Return the current HDCP Status for the given input.

        Parameters
        ----------
        videoInput : str
            input (``'HDMI'`` or ``'XTP'``)

        Returns
        -------
        bool
            ``True`` if HDCP is active, else ``False``

        Examples
        --------
        ::

            HDCPStatus = PodiumTLP.GetHDCPStatus('XTP')
            if not HDCPStatus:
                PodiumTLP.ShowPopup('No HDCP')
        """
        return bool()

    def GetInputPresence(
        self,
        videoInput: str
    ) -> bool:
        """Return the current input presence status for the given input.

        Parameters
        ----------
        videoInput : str
            input (``'HDMI'`` or ``'XTP'``)

        Returns
        -------
        bool
            ``True`` if input is present, else ``False``

        Examples
        --------
        ::

            InputPresence = PodiumTLP.GetInputPresence('XTP')
            if not InputPresence:
                PodiumTLP.ShowPopup('No XTP')
        """
        return bool()

    def GetMute(
        self,
        name: str
    ) -> str:
        """Get the mute state for the given channel

        The defined channel names are:
            * ``'Master'`` - the master volume
            * ``'Speaker'`` - the built-in speakers
            * ``'Line'`` - the line out
            * ``'Click'`` - button click volume
            * ``'Sound'`` - sound track playback volume
            * ``'HDMI'`` - HDMI input volume
            * ``'XTP'`` - XTP input volume

        Parameters
        ----------
        name : str
            name of channel.

        Returns
        -------
        str
            mute state (``'On'`` or ``'Off'``)

        Examples
        --------
        ::

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumTLP.GetMute('HDMI') == 'On':
                    PodiumTLP.SetMute('HDMI', 'Off')
                else:
                    PodiumTLP.SetMute('HDMI', 'On')
        """
        return str()

    def GetVolume(
        self,
        name: str
    ) -> int:
        """Return current volume level for the given channel

        The defined channel names are:
            * ``'Master'`` - the master volume
            * ``'Click'`` - button click volume
            * ``'Sound'`` - sound track playback volume
            * ``'HDMI'`` - HDMI input volume
            * ``'XTP'`` - XTP input volume

        Parameters
        ----------
        name : str
            name of volume channel

        Returns
        -------
        int
            volume level

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def RefreshPage(button, state):
                currentVolume = PodiumTLP.GetVolume('HDMI')
                ...
        """
        return int()

    def HideAllPopups(self) -> None:
        """Dismiss all popup pages"""
        pass

    def HidePopup(
        self,
        popup: int | str
    ) -> None:
        """Hide popup page

        Parameters
        ----------
        popup : int, str
            popup page number or name
        """
        pass

    def HidePopupGroup(
        self,
        group: int
    ) -> None:
        """Hide all popup pages in a popup group

        Parameters
        ----------
        group : int
            popup group number

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def Reset(button, state):
                PodiumTLP.HidePopupGroup(1)
        """
        pass

    def PlaySound(
        self,
        filename: str
    ) -> None:
        """Play a sound file identified by the *filename*

        Parameters
        ----------
        filename : str
            name of sound file

        Notes
        -----
        * Only WAV files can be played.
        * A subsequent call will preempt the currently playing file.
        * Sound file must be added to the project file.

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def OccupyRoom(button, state):
                PodiumTLP.SetLEDBlinking(65533, 'Slow', ['Red', 'Off'])
                PodiumTLP.PlaySound('startup.wav')
        """
        pass

    def Reboot(self) -> None:
        """Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.
        """
        pass

    def SetAutoBrightness(
        self,
        state: str | bool
    ) -> None:
        """Set auto brightness state

        Either ``'On'`` or ``True`` turns on auto brightness. ``'Off'`` or
        ``False`` turns off auto brightness.

        Parameters
        ----------
        state : bool, str
            whether to enable auto brightness

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetAutoBrightness('On')
        """
        pass

    def SetBrightness(
        self,
        level: int
    ) -> None:
        """Set screen brightness level

        Parameters
        ----------
        level : int
            brightness level from 0 ~ 100

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetAutoBrightness('Off')
                PodiumTLP.SetBrightness(50)
        """
        pass

    def SetDisplayTimer(
        self,
        state: str | bool,
        timeout: int
    ) -> None:
        """Enable/disable display timer

        Either ``'On'`` or ``True`` enables display timer. ``'Off'`` or
        ``False`` disables display timer.

        Parameters
        ----------
        state : bool, str
            whether to enable the display timer
        timeout : int
            time in seconds before turn off the display

        Notes
        -----
        Display timer is applicable to TLI only.

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetDisplayTimer(True, 180)
        """
        pass

    def SetInactivityTime(
        self,
        times: List[int]
    ) -> None:
        """Set the inactivity times of the `UIDevice`.  When each time expires,
        the `InactivityChanged` event will be triggered.  All times are
        absolute.

        Parameters
        ----------
        times : list of ints
            list of times.  Each time in whole seconds

        Examples
        --------
        ::

            PodiumTLP = UIDevice('Podium TLP')
            PodiumTLP.SetInactivityTime([3000, 3600])    # 50 min and 1 hr

            @event(PodiumTLP, 'InactivityChanged')
            def UnoccupyRoom(tlp, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()
        """
        pass

    def SetInput(
        self,
        videoInput: str
    ) -> None:
        """Sets the input.  Inputs must be published for each device.

        Parameters
        ----------
        videoInput : str
            input to select (``'HDMI'`` or ``'XTP'``)

        Examples
        --------
        ::

            PodiumTLP.SetInput('HDMI')
        """
        pass

    def SetLEDBlinking(
        self,
        ledId: int,
        rate: str,
        stateList: List[str]
    ) -> None:
        """Make the LED cycle, at ADA compliant rates, through each of the states
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

        Parameters
        ----------
        ledId : int
            LED id
        rate : str
            ADA compliant blink rate. (``'Slow'``, ``'Medium'``,
            ``'Fast'``)
        stateList : list of str
            List of colors

        Notes
        -----
        * Using this function will blink in unison with other LEDs.
        * Available colors are ``Red``, ``Green``, and ``Off``.

        Examples
        --------
        ::

            PodiumTLP = UIDevice('Podium TLP')

            @event(ButtonObject, 'Pressed')
            def UnoccupyRoom(button, state):
                PodiumTLP.SetLEDBlinking(65533, 'Slow', ['Off', 'Red'])
        """
        pass

    def SetLEDState(
        self,
        ledId: int,
        state: str
    ) -> None:
        """Drive the LED to the given color

        Parameters
        ----------
        ledId : int
            LED id
        state : str
            LED color or 'Off'.

        Notes
        -----
        Available colors are ``Red``, ``Green``, and ``Off``.

        Examples
        --------
        ::

            @event(SomeOtherButton, 'Released')
            def UnoccupyRoom(button, state):
                PodiumTLP.SetLEDState(65533, 'Off')
        """
        pass

    def SetMotionDecayTime(
        self,
        duration: float
    ) -> None:
        """Set the period of time to trigger `MotionDetected` after last
        motion was detected.

        Parameters
        ----------
        duration : float
            time in seconds (minimum/default value is 10)

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetMotionDecayTime(30)
        """
        pass

    def SetMute(
        self,
        name: str,
        mute: str
    ) -> None:
        """Set the mute state for the given channel

        Parameters
        ----------
        name : str
            name of channel.
        mute : str
            mute state (``'On'`` or ``'Off'``)

        Notes
        -----
        The defined channel names are:

        * ``'Master'`` - the master volume
        * ``'Speaker'`` - the built-in speakers
        * ``'Line'`` - the line out
        * ``'Click'`` - button click volume
        * ``'Sound'`` - sound track playback volume
        * ``'HDMI'`` - HDMI input volume
        * ``'XTP'`` - XTP input volume

        Examples
        --------
        ::

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumTLP.GetMute('HDMI') == 'On':
                    PodiumTLP.SetMute('HDMI', 'Off')
                else:
                    PodiumTLP.SetMute('HDMI', 'On')
        """
        pass

    def SetSleepTimer(
        self,
        state: bool | str,
        duration: Optional[int]=None
    ) -> None:
        """Enable/disable sleep timer. Either ``'On'`` or ``True`` enables sleep
        timer. ``'Off'`` or ``False`` disables sleep timer.

        Parameters
        ----------
        state : bool, str
            whether to enable the sleep timer
        duration : int
            time in seconds to sleep (Default value = None)

        Examples
        --------
        ::

            @event(ButtonObject, 'Pressed')
            def Initialize(button, state):
                PodiumTLP.SetSleepTimer('On', 60)
        """
        pass

    def SetVolume(
        self,
        name: str,
        level: int
    ) -> None:
        """Adjust volume level for the given channel

        Parameters
        ----------
        name : str
            name of channel.
        level : int
            volume level 0 to 100

        Notes
        -----
        The defined channel names are:

        * ``'Master'`` - the master volume
        * ``'Click'`` - button click volume
        * ``'Sound'`` - sound track playback volume
        * ``'HDMI'`` - HDMI input volume
        * ``'XTP'`` - XTP input volume
        """
        pass

    def SetWakeOnMotion(
        self,
        state: bool | str
    ) -> None:
        """Enable/disable wake on motion.

        Parameters
        ----------
        state : bool, str
            ``True`` (``'On'``) or ``False`` ('Off') to enable and disable wake
            on motion, respectively.
        """
        pass

    def ShowPage(
        self,
        page: int | str
    ) -> None:
        """Show page on the screen

        Parameters
        ----------
        page : int, str
            absolute page number or name
        """
        pass

    def ShowPopup(
        self,
        popup: int | str,
        duration: float=0
    ) -> None:
        """Display pop-up page for a period of time.

        Parameters
        ----------
        popup : int, str
            pop-up page number or name
        duration : float
            duration (in seconds) the pop-up remains on the
            screen. 0 means forever. (Default value = 0)

        Notes
        -----
        If a pop-up is already showing for a finite period of time, calling
        this method again with the same pop-up will replace the remaining
        period with the new period.
        """
        pass

    def Sleep(self) -> None:
        """Force the device to sleep immediately"""
        pass

    def StopSound(self) -> None:
        """Stop playing sound file"""
        pass

    def Wake(self) -> None:
        """Force the device to wake up immediately"""
        pass

    @property
    def AmbientLightValue(self) -> int:
        """Get the present ambient light value.

        Returns
        -------
        int
        """
        return int()

    @property
    def AutoBrightness(self) -> bool:
        """Get the present auto brightness state.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def Brightness(self) -> int:
        """Get the present brightness level.

        Returns
        -------
        int
        """
        return int()

    @property
    def BrightnessChanged(
        self
    ) -> Optional[Callable[['UIDevice', int], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `BrightnessChanged` event that triggers when LCD brightness has
        changed.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and the
        second one is the current brightness level as an integer.

        Returns
        -------
        Callable, None
            The assigned handler for the `BrightnessChanged` event or `None`
            if no handler has been assigned.

        Examples
        --------
        ::

            @event(PodiumTLP, 'BrightnessChanged')
             def HandleBrightnessChanged(tlp, brightness):
                 print('{} Brightness Changed: {}'.format(tlp.DeviceAlias, brightness))
        """
        pass

    @BrightnessChanged.setter
    def BrightnessChanged(
        self,
        handler: Optional[Callable[['UIDevice', int], Any]]
    ) -> None:
        pass

    @property
    def DisplayState(self) -> str:
        """Get the present display state of the device (``'On'``, ``'Off'``).

        Returns
        -------
        str

        Notes
        -----
        This property is applicable to TLI only.
        """
        return str()

    @property
    def DisplayTimer(self) -> int:
        """Get the present display timer timeout seconds.

        Returns
        -------
        int
        """
        return int()

    @property
    def DisplayTimerEnabled(self) -> bool:
        """Get the present display timer state.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def FirmwareVersion(self) -> str:
        """Get the firmware version of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def HDCPStatusChanged(
        self
    ) -> Optional[Callable[['UIDevice', Tuple[str, bool]], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `HDCPStatusChanged` event that triggers when HDCP Status changes.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and state
        with a tuple (str, bool): (Input, Status).

        Returns
        -------
        Callable, None
            The assigned handler for the `HDCPStatusChanged` event or `None`
            if no handler has been assigned.

        Examples
        --------
        ::

            @event(PodiumTLP, 'HDCPStatusChanged')
            def HandleHDCPStatusChangedChange(tlp, state):
                if state[0] == 'HDMI' and not state[1]:
                    PodiumTLP.ShowPopup('No HDCP')
        """
        pass

    @HDCPStatusChanged.setter
    def HDCPStatusChanged(
        self,
        handler: Optional[Callable[['UIDevice', Tuple[str, bool]], Any]]
    ) -> None:
        pass

    @property
    def Hostname(self) -> str:
        """Get the hostname of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def InactivityChanged(
        self
    ) -> Optional[Callable[['UIDevice', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `InactivityChanged` event that triggers at times specified by
        `SetInactivityTime` after state transition of inactivity timer.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and time
        with a float value of inactivity time in seconds.

        Returns
        -------
        Callable, None
            The assigned handler for the `InactivityChanged` event or `None`
            if no handler has been assigned.

        Examples
        --------
        ::

            PodiumTLP = UIDevice('Podium TLP')
            PodiumTLP.SetInactivityTime([3000, 3600])    # 50 min and 1 hr

            @event(PodiumTLP, 'InactivityChanged')
            def UnoccupyRoom(tlp, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()
        """
        pass

    @InactivityChanged.setter
    def InactivityChanged(
        self,
        handler: Optional[Callable[['UIDevice', float], Any]]
    ) -> None:
        pass

    @property
    def InactivityTime(self) -> int:
        """Get the seconds since last activity.

        Returns
        -------
        int

        Notes
        -----
        0 = Active, Nonzero = Time of inactivity.
        """
        return int()

    @property
    def InputPresenceChanged(
        self
    ) -> Optional[Callable[['UIDevice', Tuple[str, bool]], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `InputPresenceChanged` event that triggers when Input Presence
        changes.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and state
        with a tuple (str, bool): (Input, Status).

        Returns
        -------
        Callable, None
            The assigned handler for the `InputPresenceChanged` event or
            `None` if no handler has been assigned.

        Examples
        --------
        ::

            @event(PodiumTLP, 'InputPresenceChanged')
            def HandleInputPresenceChanged(tlp, state):
                if state[0] == 'HDMI' and not state[1]:
                    if PodiumTLP.GetInputPresence('XTP'):
                        PodiumTLP.SetInput('XTP')
                    else:
                        PodiumTLP.ShowPopup('No Input Available')
        """
        pass
    @InputPresenceChanged.setter
    def InputPresenceChanged(
        self,
        handler: Optional[Callable[['UIDevice', Tuple[str, bool]], Any]]
    ) -> None:
        pass

    @property
    def IPAddress(self) -> str:
        """Get the IP address of this device.

        Returns
        -------
        str
        """
        return str()

    @property
    def LidChanged(self) -> Optional[Callable[['UIDevice', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `LidChanged`
        event that triggers when the Lid state changes.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and the
        second is the current lid state (``'Opened'`` or ``'Closed'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `LidChanged` event or `None` if no
            handler has been assigned.
        """
        pass

    @LidChanged.setter
    def LidChanged(
        self,
        handler: Optional[Callable[['UIDevice', str], Any]]
    ) -> None:
        pass

    @property
    def LidState(self) -> str:
        """Get the present lid state (``'Opened'`` or ``'Closed'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def LightChanged(self) -> Optional[Callable[['UIDevice', int], Any]]:
        """``Event``: Assign or retrieve the handler for the `LightChanged`
        event that triggers when ambient light changes

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and the
        second is the ambient light level in the range of 0 to 255.

        Returns
        -------
        Callable, None
            The assigned handler for the `LightChanged` event or `None` if no
            handler has been assigned.
        """
        pass

    @LightChanged.setter
    def LightChanged(
        self,
        handler: Optional[Callable[['UIDevice', int], Any]]
    ) -> None:
        pass

    @property
    def LightDetectedState(self) -> str:
        """Get the present light detected state (``'Detected'``,
        ``'Not Detected'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def LinkLicenses(self) -> List[str]:
        """Get the presently applied LinkLicense® part numbers.

        Returns
        -------
        list of str
        """
        return [str()]

    @property
    def MACAddress(self) -> str:
        """Get the MAC address of this device

        Returns
        -------
        str
        """
        return str()

    @property
    def MotionDecayTime(self) -> int:
        """Get the period of time to trigger `MotionDetected` event after last
        motion was detected. The default (and minimum) value is 10 seconds.

        Returns
        -------
        int
        """
        return int()

    @property
    def MotionDetected(self) -> Optional[Callable[['UIDevice', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `MotionDetected`
        event that triggers when Motion is detected.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and the
        second one is a string (``'Motion'`` or ``'No Motion'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `MotionDetected` event or `None` if
            no handler has been assigned.
        """
        pass

    @MotionDetected.setter
    def MotionDetected(
        self,
        handler: Optional[Callable[['UIDevice', str], Any]]
    ) -> None:
        pass

    @property
    def MotionState(self) -> str:
        """Get the present motion state (``Motion``, ``No Motion``).

        Returns
        -------
        str
        """
        return str()

    @property
    def OverTemperature(self) -> int:
        """Get the current operating temperature value, in degrees Centigrade,
        as a differential from the product maximum operating temperature.

        .. versionadded:: 1.1

        Returns
        -------
        int

        Notes
        -----
        This feature is only supported by the TLI Pro 201 TouchLink Interface.

        Examples
        --------
        ::

            # If the product is 5 degrees C over maximum operating temperature, this
            # prints 5.
            print(PoduiumTLP.OverTemperature)

            # If the product is 15 degrees C below maximum operating temperature, this
            # prints -15.
            print(PoduiumTLP.OverTemperature)
        """
        return int()

    @property
    def OverTemperatureChanged(
        self
    ) -> Optional[Callable[['UIDevice', int], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `OverTemperatureChanged` event that triggers when Over Temperature
        changes.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and the
        second is the new temperature differential as an integer.

        .. versionadded:: 1.1

        Returns
        -------
        Callable, None
            The assigned handler for the `OverTemperatureChanged` event or
            `None` if no handler has been assigned.

        Notes
        -----
        * This event triggers for each 1 degree change but no more than once
          every 10 seconds if the temperature is oscillating.
        * This feature only supported by the TLI Pro 201 TouchLink Interface.

        Examples
        --------
        ::

            @event(PodiumTLP, 'OverTemperatureChanged')
            def HandleOverTemperatureChanged(tlp, temp):
                print('Podium TLP OverTemperature is ' + str(temp))
        """
        pass

    @OverTemperatureChanged.setter
    def OverTemperatureChanged(
        self,
        handler: Optional[Callable[['UIDevice', int], Any]]
    ) -> None:
        pass

    @property
    def OverTemperatureWarning(
        self
    ) -> Optional[Callable[['UIDevice', int], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `OverTemperatureWarning` event that triggers when the product's
        operating temperature exceeds the maximum by 5 percent.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and the
        second is current operating temperature in degrees Centigrade over the
        maximum as an integer.

        .. versionadded:: 1.1

        Returns
        -------
        Callable, None
            The assigned handler for the `OverTemperatureWarning` event or
            `None` if no handler has been assigned.

        Notes
        -----
        * This event retriggers once every minute until the operating
          temperature falls below the maximum operating temperature.
        * This feature only supported by the TLI Pro 201 TouchLink Interface.


        Examples
        --------
        ::

            @event(PodiumTLP, 'OverTemperatureWarning')
            def HandleOverTemperatureWarning(device, temp):
                print('The podium TLP is {} degrees over maximum operating '
                      'temperature.'.format(temp))
        """
        pass

    @OverTemperatureWarning.setter
    def OverTemperatureWarning(
        self,
        handler: Optional[Callable[['UIDevice', int], Any]]
    ) -> None:
        pass

    @property
    def OverTemperatureWarningState(self) -> bool:
        """Get the present Over Temperature Warning state.

        .. versionadded:: 1.1

        Returns
        -------
        bool

        Notes
        -----
        This feature only supported by the TLI Pro 201 TouchLink Interface.

        Examples
        --------
        ::

            if PodiumTLP.OverTemperatureWarningState:
                print('Podium TLP is over maximum temperature.')
        """
        return bool()

    @property
    def OverTemperatureWarningStateChanged(
        self
    ) -> Optional[Callable[['UIDevice', bool], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `OverTemperatureWarningStateChanged` event that triggers when the
        product's operating temperature warning changes state.

        The callback takes two arguments. The first one is the `UIDevice`
        instance triggering the event and the second is current state of the
        over temperature warning as a bool.

        .. versionadded:: 1.1

        Returns
        -------
        Callable, None
            The assigned handler for the `OverTemperatureWarningStateChanged`
            event or `None` if no handler has been assigned.

        Notes
        -----
        This feature only supported by the TLI Pro 201 TouchLink Interface.

        Examples
        --------
        ::

            @event(PodiumTLP, 'OverTemperatureWarningStateChanged')
            def HandleOverTemperatureWarningStateChanged(device, state):
                if state:
                    print('The podium TLP is over maximum operating temperature.')
                else:
                    print('The podium TLP operating temperature is normal.')
        """
        pass

    @OverTemperatureWarningStateChanged.setter
    def OverTemperatureWarningStateChanged(
        self,
        handler: Optional[Callable[['UIDevice', bool], Any]]
    ) -> None:
        pass

    @property
    def SerialNumber(self) -> str:
        """Get the serial number of this device

        Returns
        -------
        str
        """
        return str()

    @property
    def SleepChanged(self) -> Optional[Callable[['UIDevice', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `SleepChanged`
        event that triggers when sleep state changes.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `UIDevice` instance triggering the event and the
        second one is a string (``'Asleep'`` or ``'Awake'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `SleepChanged` event or
            `None` if no handler has been assigned.

        Examples
        --------
        ::

            @event(PodiumTLP, 'SleepChanged')
            def HandleSleepChanged(tlp, state):
                print('{} Sleep State Changed: {}'.format(tlp.DeviceAlias, state))
        """
        pass

    @SleepChanged.setter
    def SleepChanged(
        self,
        handler: Optional[Callable[['UIDevice', str], Any]]
    ) -> None:
        pass

    @property
    def SleepState(self) -> str:
        """Get the present sleep state (``'Asleep'``, ``'Awake'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def SleepTimer(self) -> int:
        """Get the present sleep timer value.

        Returns
        -------
        int
        """
        return int()

    @property
    def SleepTimerEnabled(self) -> bool:
        """Get the present sleep timer state. ``True`` if sleep timer is
        enabled, else ``False``.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def SystemSettings(self) -> dict:
        """Get a dictionary of data describing the settings (defined in
        Toolbelt) of this device

        Returns
        -------
        dict

        Examples
        --------
        ::

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
        """
        return dict()

    @property
    def UserUsage(self) -> Tuple[int, int]:
        """Get the user data usage of this device in KB ``(used, total)``.

        Returns
        -------
        tuple of int
        """
        return (int(), int())

    @property
    def WakeOnMotion(self) -> bool:
        """Get the present wake on motion state.

        Returns
        -------
        bool
        """
        return bool()
