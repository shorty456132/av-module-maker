from typing import Any, List


class MESet():
    """The Mutually Exclusive set allows for the grouping of objects to allow easy
    selection of related items.  For instance, a group of buttons could be
    grouped so that selecting one button deselects the others in the group.
    """

    def __init__(self, Objects: List[Any]):
        """Compatible extronlib classes:

            * IOInterface (and any children):
                * `DigitalIOInterface` (Output only)
                * `FlexIOInterface` (Output only)
                * `PoEInterface`
                * `RelayInterface`
                * `SWACReceptacleInterface`
                * `SWPowerInterface`
                * `TallyInterface`
            * Button

        Parameters
        ----------
        Objects : list
            list of compatible objects

        Notes
        -----
        * Each object must have a method *SetState*.
        * *SetState* must take an integer argument.
        * Any object with a *SetState* function that takes an integer object
          is compatible with this class.
        * A programmer can create their own class and use it with *MESet*.

        Examples
        --------
        ::

            InputButtons = MESet([Input1, Input2, Input3, Input4])
        """
        pass

    def Append(self, obj) -> None:
        """Add an object to the list

        Parameters
        ----------
        obj : Any
            any compatible object to add

        Examples
        --------
        ::

            InputButtons.Append(Input5)
        """
        pass

    def GetCurrent(self) -> Any:
        """Get the currently selected object in the group or ``None`` if
        none selected.

        Returns
        -------
        Any
            selected object or ``None``

        Examples
        --------
        ::

            # Toggle inputs
            current = InputButtons.GetCurrent()
            if current is Input1:
                SetInput(2)
            elif current is Input2:
                SetInput(3)
            elif current is Input3:
                SetInput(4)
            elif current is Input4:
                SetInput(1)
            elif current is None:
                ClearInputStatus()
        """
        pass

    def Remove(self, obj) -> None:
        """Remove an object from the list

        Parameters
        ----------
        obj : int or Any
            the object or the index of the object

        Examples
        --------
        ::

            def SeparateRooms():
                ...
                InputButtons.Remove(Input4)
                ...
        """
        pass

    def SetCurrent(self, obj: int | Any) -> None:
        """Selects the current object in the group

        Parameters
        ----------
        obj : int or Any
            the object or the index of the object

        Notes
        -----
        When ``None`` is passed in, all objects will be deselected.

        Examples
        --------
        ::

            @event(InputButtons.Objects, 'Pressed')
            def SelectInput(button, state):
                if button is Input1:
                    SetInput(1)
                elif button is Input2:
                    SetInput(2)
                elif button is Input3:
                    SetInput(3)
                elif button is Input4:
                    SetInput(4)

                InputButtons.SetCurrent(button)
        """
        pass

    def SetStates(
        self,
        obj: int | Any,
        offState: int,
        onState: int
    ) -> None:
        """Selects the off and on states for the object (i.e. use states other
        than the default 0 and 1, respectively).

        Parameters
        ----------
        obj : int or Any
            the object or the index of the object
        offState : int
            the ID of the deselected state
        onState : int
            the ID of the selected state

        Examples
        --------
        ::

            for button in InputButtons.Objects:
                InputButtons.SetStates(button, 2, 3)
        """
        pass

    @property
    def Objects(self) -> List[Any]:
        """The list of objects to track

        Returns
        -------
        list

        Examples
        --------
        ::

            if Input6 in InputButtons.Objects:
                print('Already added')
            else:
                InputButtons.Append(Input6)
        """
        return []
