from . import UIObject


class Level(UIObject):
    '''
    This module defines interfaces of Level UI.

    .. code-block:: python

        ConfRoomLevel = Level(ConfRoomWall, 1000)
    '''

    def Dec(self):
        '''Nudge the level down a step.'''
        pass

    def Inc(self):
        '''Nudge the level up a step.'''
        pass

    def SetLevel(self, Level):
        '''
        Set the current level.

        :param Level: Discrete value of the level object
        :type Level: int

        .. code-block:: python
            :linenos:

            currentLevel = 0
            Inc = Button(ConfRoomWall, 'Volume Up', repeatTime=.2)
            Dec = Button(ConfRoomWall, 'Volume Down', repeatTime=.2)
            VolumeConfRoom = VolumeInterface(ConfRoom, 'VOL1')

            @event(Inc, ['Pressed', 'Repeated'])
            def IncVolume(button, state):
                global currentLevel
                if currentLevel < 100:
                    currentLevel += 1
                    VolumeConfRoom.SetLevel(currentLevel)
                    ConfRoomLevel.SetLevel(currentLevel)

            @event(Dec, ['Pressed', 'Repeated'])
            def DecVolume(button, state):
                global currentLevel
                if currentLevel > 0:
                    currentLevel -= 1
                    VolumeConfRoom.SetLevel(currentLevel)
                    ConfRoomLevel.SetLevel(currentLevel)
        '''
        pass

    def SetRange(self, Min, Max, Step=1):
        '''
        Set level object's allowed range and the step size.

        :param Min: Minimum level
        :type Min: int
        :param Max: Maximum level
        :type Max: int
        :param Step: Optional step size for :py:meth:`Inc` and :py:meth:`Dec`.
        :type Step: int

        .. note::
            * The default range is 0 - 100 with a step size of 1.
            * For multi-state levels, you must set the level range to match
              the number of states in the level.

        .. code-block:: python

            ConfRoomLevel.SetRange(-60, 10, 5)
        '''
        pass

    def SetVisible(self, visible):
        '''
        Change the visibility of a UI control object.

        :param visible: ``True`` to make the object visible or ``False`` to
            hide it.
        :type visible: bool
        '''
        pass

    @property
    def Level(self):
        '''
        :return: the current level
        :rtype: int
        '''
        pass

    @property
    def Max(self):
        '''
        :return: the upper bound of the level object
        :rtype: int
        '''
        pass

    @property
    def Min(self):
        '''
        :return: the lower bound of the level object
        :rtype: int
        '''
        pass

    @property
    def Name(self):
        '''
        :return: the object Name
        :rtype: string
        '''
        pass

    @property
    def Visible(self):
        '''
        :return: ``True`` if the control object is visible else ``False``
        :rtype: bool
        '''
        pass
