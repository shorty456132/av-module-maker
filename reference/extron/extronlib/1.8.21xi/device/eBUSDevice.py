from typing import Any, Callable, List, Optional, Tuple

from . import Device, ProcessorDevice


class eBUSDevice(Device):
    """Defines common interface to Extron eBUS panels"""

    def __init__(
        self,
        Host: ProcessorDevice,
        DeviceAlias: str
    ):
        """
        Parameters
        ----------
        Host : ProcessorDevice
            handle to Extron `ProcessorDevice` to which the `eBUSDevice` is
            connected
        DeviceAlias : str
            The device alias of the Extron device.

        Notes
        -----
        *Host* must be the primary processor.

        Examples
        --------
        ::

            # Create Primary Processor
            ConfRoom = ProcessorDevice('Main')

            # Create eBUSDevice
            ConfRoomPanel = eBUSDevice(ConfRoom, 'ConfEBP')
        """
        pass

    def Click(
        self,
        count: int=1,
        interval: Optional[int]=None
    ) -> None:
        """Play default buzzer sound on applicable device

        Parameters
        ----------
        count : int
            number of buzzer sound to play (Default value = 1)
        interval : int
            time gap in millisecond between consecutive sounds (Default value = None)

        Notes
        -----
        If *count* is greater than 1, *interval* must be provided to indicate
        the time gap in ms between consecutive buzzer sounds.
        """
        pass

    def GetMute(
        self,
        name: str
    ) -> str:
        """Get the mute state for the given channel

        Parameters
        ----------
        name : string
            name of channel.

        Returns
        -------
        str
            mute state (``'On'`` or ``'Off'``)

        Notes
        -----
        The defined channel names are:

        * ``'Click'`` - button click volume

        Examples
        --------
        ::

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumEBP.GetMute('Click') == 'On':
                    PodiumEBP.SetMute('Click', 'Off')
                else:
                    PodiumEBP.SetMute('Click', 'On')
        """
        return str()

    def Reboot(self) -> None:
        """Performs a soft restart of this device -- this is equivalent to
        rebooting a PC.
        """
        pass

    def SendCommand(
        self,
        command: str,
        value: int | Tuple[int] | None=None
    ) -> None:
        """Send command to eBUSDevice.

        Parameters
        ----------
        command : str
            command name to issue
        value : int, tuple of ints
            command specific value to pass with commend (Default value = None)

        Notes
        -----
        * For supported eBUS devices.
        * See device documentation for supported commands.

        Examples
        --------
        ::

            VoiceLiftDevice.SendCommand('Chime', 1)     # Enable Chime
            VoiceLiftDevice.SendCommand('Usage')        # Query usage
        """
        pass

    def SetInactivityTime(
        self,
        times: List[int]
    ) -> None:
        """Set the inactivity times of the `eBUSDevice`.  When each time
        expires, the `InactivityChanged` event will be triggered.  All times
        are absolute.

        Parameters
        ----------
        times : list of ints
            list of times.  Each time in whole seconds

        Notes
        -----
        Applies to EBP models only.

        Examples
        --------
        ::

            PodiumPanel = eBUSDevice('Podium Panel')
            PodiumPanel.SetInactivityTime([3000, 3600])    # 50 min and 1 hr

            @event(PodiumPanel, 'InactivityChanged')
            def UnoccupyRoom(Panel, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()
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

        * ``'Click'`` - button click volume

        Examples
        --------
        ::

            @event(ToggleMute, 'Pressed')
            def toggleMute(button, state):
                if PodiumEBP.GetMute('Click') == 'On':
                    PodiumEBP.SetMute('Click', 'Off')
                else:
                    PodiumEBP.SetMute('Click', 'On')
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
                PodiumPanel.SetSleepTimer('On', 60)
        """
        pass

    def Sleep(self) -> None:
        """Force the device to sleep immediately"""
        pass

    def Wake(self) -> None:
        """Force the device to wake up immediately"""
        pass

    @property
    def Host(self) -> ProcessorDevice:
        """Get the device object that hosts this eBUS object.

        Returns
        -------
        ProcessorDevice
        """
        return ProcessorDevice('')

    @property
    def ID(self) -> int:
        """Get the eBUS ID (set by DIP switch).

        Returns
        -------
        int
        """
        return int()

    @property
    def InactivityChanged(
        self
    ) -> Optional[Callable[['eBUSDevice', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `InactivityChanged` event the triggers at times specified by
        `SetInactivityTime` after state transition of inactivity timer.

        The assigned handler for the `InactivityChanged` event must accept two
        positional arguments. The first one is the `eBUSDevice` instance
        triggering the event and time with a float value of inactivity time in
        seconds.

        Returns
        -------
        Callable, None
            The assigned handler for the `InactivityChanged` event or `None`
            if no handler has been assigned.

        Notes
        -----
        Applies to EBP models only.

        Examples
        --------
        ::

            PodiumPanel = eBUSDevice('Podium Panel')
            PodiumPanel.SetInactivityTime([3000, 3600])    # 50 min and 1 hr

            @event(PodiumPanel, 'InactivityChanged')
            def UnoccupyRoom(Panel, time):
                if time == 3000:
                    ShowWarning()
                else:
                    ShutdownSystem()
        """
        pass

    @InactivityChanged.setter
    def InactivityChanged(
        self,
        handler: Optional[Callable[['eBUSDevice', float], Any]]
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
        * 0 = Active, Nonzero = Time of inactivity.
        * Applies to EBP models only.
        """
        return int()

    @property
    def LidChanged(self) -> Optional[Callable[['eBUSDevice', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `LidChanged`
        event that triggers when the Lid state changes.

        The assigned handler for the `LidChanged` event must accept two
        arguments. The first one is the `eBUSDevice` instance triggering the
        event and the second is the current lid state (``'Opened'`` or
        ``'Closed'``).

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
        handler: Optional[Callable[['eBUSDevice', str], Any]]
    ) -> None:
        pass

    @property
    def LidState(self) -> str:
        """Get the lid state (``'Opened'`` or ``'Closed'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def ReceiveResponse(
        self
    ) -> Optional[Callable[['eBUSDevice', str, Tuple[int]], Any]]:
        """``Event``: Assign or retrieve the handler for the `ReceiveResponse`
        event that triggers when asynchronous responses arrive.

        The assigned handler for the `ReceiveResponse` event must accept three
        arguments. The first one is the `eBUSDevice` instance triggering the
        event, the second one is a the command (string), and the third is a
        tuple of context specific integers.

        Returns
        -------
        Callable, None
            The assigned handler for the `ReceiveResponse` event or `None` if
            no handler has been assigned.

        Notes
        -----
        * For supported eBUS devices.
        * See device documentation for supported commands.

        Examples
        --------
        ::

            # Receive Response == 'Mute', (1,)
            @event(VoiceLiftDevice, 'ReceiveResponse')
            def MainFeedbackHandler(interface, command, value):
                if command == 'Mute':
                    state = value[0]
                    ...
        """
        pass

    @ReceiveResponse.setter
    def ReceiveResponse(
        self,
        handler: Optional[Callable[['eBUSDevice', str, Tuple[int]], Any]]
    ) -> None:
        pass

    @property
    def SleepChanged(self) -> Optional[Callable[['eBUSDevice', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `SleepChanged`
        event that triggers when sleep state changes.

        The assigned handler for the `SleepChanged` event must accept two
        arguments. The first one is the `eBUSDevice` instance triggering the
        event and the second one is a string (``'Asleep'`` or ``'Awake'``).

        Returns
        -------
        Callable, None
            The assigned handler for the `SleepChanged` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(PodiumPanel, 'SleepChanged')
             def HandleSleepChanged(Panel, state):
                 print('{} Sleep State Changed: {}'.format(Panel.DeviceAlias, state))
        """
        pass

    @SleepChanged.setter
    def SleepChanged(
        self,
        handler: Optional[Callable[['eBUSDevice', str], Any]]
    ) -> None:
        pass

    @property
    def SleepState(self) -> str:
        """Get the sleep state (``'Asleep'``, ``'Awake'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def SleepTimer(self) -> int:
        """Get the sleep timer timeout.

        Returns
        -------
        int
        """
        return int()

    @property
    def SleepTimerEnabled(self) -> bool:
        """Get the sleep time state. ``True`` if sleep timer is enabled, else
        ``False``.

        Returns
        -------
        bool
        """
        return bool()
