from typing import Any, Callable, List, Optional

from ..device import UIDevice, eBUSDevice
from . import UIObject


class Button(UIObject):
    """Representation of Hard/Soft buttons

    A button may trigger several events depending on the configuration;
    however, Touch Panels only issue `Pressed` and `Released` messages to the
    control processor. Other events (e.g., `Held`, `Repeated`) are timer
    driven within the Button instance.
    """

    def __init__(
        self,
        UIHost: eBUSDevice | UIDevice,
        ID: int | str,
        holdTime: Optional[float]=None,
        repeatTime: Optional[float]=None
    ):
        """
        Parameters
        ----------
        UIHost : eBUSDevice, UIDevice
            Device object hosting this UIObject
        ID : int, string
            ID or Name of the UIObject
        holdTime : float
            Time for `Held` event. Held event is triggered only once if the
            button is pressed and held beyond this time. If holdTime is given,
            it must be a floating point number specifying period of time in
            seconds of button being pressed and held to trigger Held event.
        repeatTime : float
            Time for `Repeated` event. After *holdTime* expires, the Repeated
            event is triggered for every additional *repeatTime* of button
            being held.  If repeatTime is given, it must be a floating point
            number specifying time in seconds of button being held.

        Notes
        -----
        If button is released before *holdTime* expires, a `Tapped` event is
        triggered instead of a `Released` event. If the button is released
        after *holdTime* expires, there will be no `Tapped` event.

        Examples
        --------
        ::

            powerOn = Button(PodiumTLP, 'Power On')
            showSetupPage = Button(PodiumTLP, 'Show Setup Page', holdTime=5)
            volumeUp = Button(PodiumTLP, 10, repeatTime=0.1)
            volumeDown = Button(PodiumTLP, 11, repeatTime=0.1)
        """
        pass

    def CustomBlink(
        self,
        rate: float | int,
        stateList: List[int]
    ) -> None:
        """Make the button cycle through each of the states provided.

        Parameters
        ----------
        rate : float
            duration of time in seconds for one visual state to stay
            until replaced by the next visual state.
        stateList : list of ints
            list of visual states that this button blinks among.

        Examples
        --------
        ::

            showSetupPage.CustomBlink(1, [0, 1])
        """
        pass

    def SetBlinking(self, rate: str, stateList: List[int]) -> None:
        """Make the button cycle, at ADA compliant rates, through each of the
        states provided.

        ========  =============
        **Rate**  **Frequency**
        ========  =============
        Slow      0.5 Hz
        Medium    1 Hz
        Fast      2 Hz
        ========  =============

        Parameters
        ----------
        rate : string
            ADA compliant blink rate. (``'Slow'``, ``'Medium'``,
            ``'Fast'``)
        stateList : list of ints
            list of visual states that this button blinks among.

        Notes
        -----
        * Using this function, the button will blink in unison with other
          buttons.
        * Maximum of six states in the *stateList* for eBUSDevice buttons.

        Examples
        --------
        ::

            powerOn.SetBlinking('Medium', [2, 4])   # Warming up
        """
        pass

    def SetEnable(self, enable:bool) -> None:
        """Enable or disable a UI control object.

        Parameters
        ----------
        enable : bool
            ``True`` to enable the object or ``False`` to disable it.
        """
        pass

    def SetState(self, State:int) -> None:
        """Set the current visual state

        Parameters
        ----------
        State : int
            visual state number

        Notes
        -----
        Setting the current state stops button from blinking, if it is
        running. (`SetBlinking`)

        Examples
        --------
        ::

            powerOn.SetState(1) # Powered On
        """
        pass

    def SetText(self, text:str) -> None:
        """Specify text to display on the UIObject

        Parameters
        ----------
        text : str
            text to display
        """
        pass

    def SetVisible(self, visible:bool) -> None:
        """Change the visibility of a UI control object.

        Parameters
        ----------
        visible : bool
            ``True`` to make the object visible or ``False`` to hide it.
        """
        pass

    @property
    def BlinkState(self) -> str:
        """The current blink state (``'Not blinking'`` or ``'Blinking'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def Enabled(self) -> bool:
        """The current enabled state. ``True`` if the control object is
        enabled else ``False``.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def Held(self) -> Optional[Callable[['Button', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Held` event that
        triggers when the `holdTime` expires.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `Button` instance triggering the event and the second
        one is the state as a string (e.g. 'Held').

        Returns
        -------
        Callable, None
            The assigned handler for the `Held` event or `None` if no handler
            has been assigned.

        Examples
        --------
        ::

            @event(showSetupPage, 'Held')
            def ShowSetupPage(button, state):
                PodiumTLP.ShowPage('Setup Page')
                currentVolume = PodiumTLP.GetVolume('HDMI')
        """
        pass

    @Held.setter
    def Held(
        self,
        handler: Optional[Callable[['Button', str], Any]]
    ) -> None:
        pass

    @property
    def Name(self) -> str:
        """The object Name

        Returns
        -------
        str
        """
        return str()

    @property
    def Pressed(self) -> Optional[Callable[['Button', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Pressed` event
        that trigger when the button is pressed.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `Button` instance triggering the event and the second
        is the state as a string (e.g. 'Pressed').

        Returns
        -------
        Callable, None
            The assigned handler for the `Pressed` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(powerOn, 'Pressed')
            def PowerOn(button, state):
                powerOn.SetBlinking('Medium', [2, 4])
                mainProjector.Send('POWER ON')
        """
        pass

    @Pressed.setter
    def Pressed(
        self,
        handler: Optional[Callable[['Button', str], Any]]
    ) -> None:
        pass

    @property
    def PressedState(self) -> bool:
        """The current pressed state. ``True`` if the button is pressed, else
        ``False``.

        Returns
        -------
        bool
        """
        return bool()

    @property
    def Released(self) -> Optional[Callable[['Button', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Released` event
        that trigger when the button is released.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `Button` instance triggering the event and the second
        is the state as a string (e.g. 'Released').

        Returns
        -------
        Callable, None
            The assigned handler for the `Released` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(closeSetupPage, 'Released')
            def ClosePage(button, state):
                PodiumTLP.ShowPage('Main')
        """
        pass

    @Released.setter
    def Released(
        self,
        handler: Optional[Callable[['Button', str], Any]]
    ) -> None:
        pass

    @property
    def Repeated(self) -> Optional[Callable[['Button', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Repeated` event
        that trigger when the button is repeated.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `Button` instance triggering the event and the second
        is the state as a string (e.g. 'Repeated').

        Returns
        -------
        Callable, None
            The assigned handler for the `Repeated` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(volumeUp, 'Repeated')
            def VolUp(button, state):
                global VolLevel

                if VolLevel >= 20:
                    return

                VolLevel += 1
                mainProjector.Send('VOLUME {}'.format(VolLevel))
        """
        pass

    @Repeated.setter
    def Repeated(
        self,
        handler: Optional[Callable[['Button', str], Any]]
    ) -> None:
        pass

    @property
    def Tapped(self) -> Optional[Callable[['Button', str], Any]]:
        """``Event``: Assign or retrieve the handler for the `Tapped` event
        that trigger when the button is tapped.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `Button` instance triggering the event and the second
        is the state as a string (e.g. 'Tapped').

        Returns
        -------
        Callable, None
            The assigned handler for the `Tapped` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(zoomIn, 'Tapped')
            def ZoomInTapped(button, state):
                PTZ.Send('zoom +1')   # Nudge the zoom
        """
        pass

    @Tapped.setter
    def Tapped(
        self,
        handler: Optional[Callable[['Button', str], Any]]
    ) -> None:
        pass

    @property
    def State(self) -> int:
        """The current visual state number

        Returns
        -------
        int

        Notes
        -----
        It does not return the current state if the button is blinking.
        """
        return int()

    @property
    def Visible(self) -> bool:
        """The current visibility state. ``True`` if the control object is
        visible else ``False``.

        Returns
        -------
        bool
        """
        return bool()
