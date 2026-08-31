from . import UIObject


class Level(UIObject):
    """This module defines interfaces of Level UI.

    Examples
    --------
    ::

        ConfRoomLevel = Level(ConfRoomWall, 1000)
    """

    def Dec(self) -> None:
        """Nudge the level down a step."""
        pass

    def Inc(self) -> None:
        """Nudge the level up a step."""
        pass

    def SetLevel(self, Level:int) -> None:
        """Set the current level.

        Parameters
        ----------
        Level : int
            Discrete value of the level object

        Examples
        --------
        ::

            currentLevel = 0
            Inc = Button(ConfRoomWall, 'Volume Up', repeatTime=.2)
            Dec = Button(ConfRoomWall, 'Volume Down', repeatTime=.2)
            VolumeConfRoom = VolumeInterface(ConfRoom, 'VOL1')

            @event(Inc, ['Pressed', 'Repeated'])
            def IncVolume(button, state):
                global currentLevel
                if currentLevel >= 100:
                    return
                currentLevel += 1
                VolumeConfRoom.SetLevel(currentLevel)
                ConfRoomLevel.SetLevel(currentLevel)

            @event(Dec, ['Pressed', 'Repeated'])
            def DecVolume(button, state):
                global currentLevel
                if currentLevel <= 0:
                    return
                currentLevel -= 1
                VolumeConfRoom.SetLevel(currentLevel)
                ConfRoomLevel.SetLevel(currentLevel)
        """
        pass

    def SetRange(
        self,
        Min: int,
        Max: int,
        Step: int=1
    ) -> None:
        """Set level object's allowed range and the step size.

        Parameters
        ----------
        Min : int
            Minimum level
        Max : int
            Maximum level
        Step : int
            Optional step size for `Inc` and `Dec`. (Default value = 1)

        Notes
        -----
        * The default range is 0 - 100 with a step size of 1.
        * For multi-state levels, you must set the level range to match the
          number of states in the level.

        Examples
        --------
        ::

            ConfRoomLevel.SetRange(-60, 10, 5)
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
    def Level(self) -> int:
        """The current level.

        Returns
        -------
        int
        """
        return int()

    @property
    def Max(self) -> int:
        """The upper bound of the level object

        Returns
        -------
        int
        """
        return int()

    @property
    def Min(self) -> int:
        """The lower bound of the level object

        Returns
        -------
        int
        """
        return int()

    @property
    def Name(self) -> str:
        """The object Name

        Returns
        -------
        str
        """
        return str()

    @property
    def Visible(self) -> bool:
        """The current visibility state. ``True`` if the control object is
        visible else ``False``.

        Returns
        -------
        bool
        """
        return bool()
