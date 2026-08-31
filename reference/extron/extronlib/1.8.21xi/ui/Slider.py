from typing import Any, Callable, Optional

from ..device import UIDevice
from . import UIObject


class Slider(UIObject):
    """This module defines interfaces of Slider UI."""

    def __init__(
        self,
        UIHost: UIDevice,
        ID: int | str
    ):
        """
        Parameters
        ----------
        UIHost : UIDevice
            Device object hosting this UIObject
        ID : int, str
            ID or Name of the UIObject

        Examples
        --------
        ::

            ProgramAudio = Slider(PodiumTLP, 'Program Audio')
        """
        self.__host = UIHost

    def SetEnable(self, enable: bool) -> None:
        """Enable or disable a UI control object.

        Parameters
        ----------
        enable : bool
            ``True`` to enable the object or ``False`` to disable it.
        """
        pass

    def SetFill(self, Fill: int | float) -> None:
        """Set the current fill level.

        Parameters
        ----------
        Fill : int, float
            Discrete value of the slider fill object

        Notes
        -----
        The default range is 0 - 100 with a step size of 1.

        Examples
        --------
        ::

            ProgramAudio = Slider(ConfRoom, 10000)
            ProgramAudio.SetFill(50)
        """
        pass

    def SetRange(
        self,
        Min: int | float,
        Max: int | float,
        Step: int | float=1
    ) -> None:
        """Set slider object's allowed range and the step size.

        Parameters
        ----------
        Min : int, float
            Minimum level
        Max : int, float
            Maximum level
        Step : int, float
            Optional step size. (Default value = 1)

        Notes
        -----
        The default range is 0 - 100 with a step size of 1.

        Examples
        --------
        ::

            ConfRoomLevel.SetRange(-60, 10, 5)
        """
        pass

    def SetVisible(self, visible: bool) -> None:
        """Change the visibility of a UI control object.

        Parameters
        ----------
        visible : bool
            ``True`` to make the object visible or ``False`` to hide it.
        """
        pass

    @property
    def Changed(
        self
    ) -> Optional[Callable[['Slider', str, int | float], Any]]:
        """``Event``: Assign or retrieve the handler for the `Changed` event
        that triggers when the slider value is changed by user interaction
        (i.e. after `Pressed` but before `Released`).

        The assigned handler must accept exactly three arguments. The first
        one is the `Slider` instance triggering the event, the second is the
        state, and the third is the new slider value.

        Returns
        -------
        Callable, None
            The assigned handler for the `Held` event or `None` if no handler
            has been assigned.

        Examples
        --------
        ::

            @event(ProgramAudio, 'Changed')
            def handleProgramAudio(slider, state, value):
                if state == 'Changed':
                    # Send new program audio level
        """
        pass

    @Changed.setter
    def Changed(
        self,
        handler: Optional[Callable[['Slider', str, int | float], Any]]
    ) -> None:
        pass

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
    def Fill(self) -> int | float:
        """The current fill level

        Returns
        -------
        int, float
        """
        return int()

    @property
    def Host(self) -> UIDevice:
        """Handle to the `UIDevice` that hosts this UI object.

        Returns
        -------
        UIDevice
        """
        return self.__host

    @property
    def Max(self) -> int | float:
        """The upper bound of the slider object.

        Returns
        -------
        int, float
        """
        return int()

    @property
    def Min(self) -> int | float:
        """The lower bound of the slider object.

        Returns
        -------
        int, float
        """
        return int()

    @property
    def Name(self) -> str:
        """The object Name

        Returns
        -------
        string
        """
        return str()

    @property
    def Pressed(
        self
    ) -> Optional[Callable[['Slider', str, int | float], Any]]:
        """``Event``: Assign or retrieve the handler for the `Pressed` event
        that triggers when the slider is pressed.

        The assigned handler must accept exactly three arguments. The first
        one is the `Slider` instance triggering the event, the second is the
        state, and the third is the new slider value.

        Returns
        -------
        Callable, None
            The assigned handler for the `Pressed` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(ProgramAudio, 'Pressed')
            def handleProgramAudio(slider, state, value):
                if state == 'Pressed':
                    # Send new program audio level
        """
        pass

    @Pressed.setter
    def Pressed(
        self,
        handler: Optional[Callable[['Slider', str, int | float], Any]]
    ) -> None:
        pass

    @property
    def Released(
        self
    ) -> Optional[Callable[['Slider', str, int | float], Any]]:
        """``Event``: Assign or retrieve the handler for the `Released` event
        that triggers when the slider is pressed.

        The assigned handler must accept exactly three arguments. The first
        one is the `Slider` instance triggering the event, the second is the
        state, and the third is the new slider value.

        Returns
        -------
        Callable, None
            The assigned handler for the `Released` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(ProgramAudio, 'Released')
            def handleProgramAudio(slider, state, value):
                if state == 'Released':
                    # Send new program audio level
        """
        pass

    @Released.setter
    def Released(
        self,
        handler: Optional[Callable[['Slider', str, int | float], Any]]
    ) -> None:
        pass

    @property
    def Step(self) -> int | float:
        """The step size of the slider object

        Returns
        -------
        int, float
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
