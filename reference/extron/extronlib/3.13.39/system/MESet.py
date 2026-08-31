class MESet():
    '''
    The Mutually Exclusive set allows for the grouping of objects to allow easy
    selection of related items.  For instance, a group of buttons could be
    grouped so that selecting one button deselects the others in the group.
    '''

    def __init__(self, Objects):
        '''
        Compatible extronlib classes:

            * IOInterface (and any children):
                * |DigitalIOInterface| (Output only)
                * |FlexIOInterface| (Output only)
                * |PoEInterface|
                * |RelayInterface|
                * |SWACReceptacleInterface|
                * |SWPowerInterface|
                * |TallyInterface|
            * Button

        :param Objects: list of compatible objects
        :type Objects: list

        .. note::

            * Each object must have a method *SetState*.
            * *SetState* must take an integer argument.
            * Any object with a *SetState* function that takes an integer
              object is compatible with this class.
            * A programmer can create their own class and use it with *MESet*.

        .. code-block:: python

            InputButtons = MESet([Input1, Input2, Input3, Input4])
        '''
        pass

    def Append(self, obj):
        '''
        Add an object to the list

        :param obj: any compatible object to add
        :type obj: any

        .. code-block:: python

            InputButtons.Append(Input5)
        '''
        pass

    def GetCurrent(self):
        '''
        :return: the currently selected object in the group or ``None`` if
            none selected. 

        .. code-block:: python
            :linenos:

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
        '''
        pass

    def Remove(self, obj):
        '''
        Remove an object from the list

        :param obj: the object or the index of the object
        :type obj: int or compatible object

        .. code-block:: python

            def SeparateRooms():
                ...
                InputButtons.Remove(Input4)
                ...
        '''
        pass

    def SetCurrent(self, obj):
        '''
        Selects the current object in the group

        :param obj: the object or the index of the object
        :type obj: int or compatible object

        .. note:: When ``None`` is passed in, all objects will be deselected.

        .. code-block:: python
            :linenos:

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
        '''
        pass

    def SetStates(self, obj, offState, onState):
        '''
        Selects the off and on states for the object (i.e. use states other
        than the default 0 and 1, respectively).

        :param obj: the object or the index of the object
        :type obj: int or object
        :param offState: the ID of the deselected state
        :type offState: int
        :param onState: the ID of the selected state
        :type onState: int

        .. code-block:: python

            for button in InputButtons.Objects:
                InputButtons.SetStates(button, 2, 3)

        .. versionadded:: 2.5
        '''
        pass

    @property
    def Objects(self):
        '''
        :return: the list of objects to track
        :rtype: list

        .. code-block:: python

            if Input6 in InputButtons.Objects:
                print('Already added')
            else:
                InputButtons.Append(Input6)
        '''
        pass
