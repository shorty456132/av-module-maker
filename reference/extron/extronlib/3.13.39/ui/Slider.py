from . import UIObject


class Slider(UIObject):
    '''
    This module defines interfaces of Slider UI.

    .. versionadded:: 3.3
    '''

    def __init__(self, UIHost, ID):
        '''
        :param UIHost: Device object hosting this UIObject
        :type UIHost: |UIDevice|
        :param ID: ID or Name of the UIObject
        :type ID: int, string

        .. code-block:: python

            ProgramAudio = Slider(PodiumTLP, 'Program Audio')
        '''
        pass

    def SetEnable(self, enable):
        '''
        Enable or disable a UI control object.

        :param enable: ``True`` to enable the object or ``False`` to disable
            it.
        :type enable: bool
        '''
        pass

    def SetFill(self, Fill):
        '''
        Set the current fill level.

        :param Fill: Discrete value of the slider fill object
        :type Fill: int, float

        .. note:: The default range is 0 - 100 with a step size of 1.

        .. code-block:: python

            ProgramAudio = Slider(ConfRoom, 10000)
            ProgramAudio.SetFill(50)
        '''
        pass

    def SetRange(self, Min, Max, Step=1):
        '''
        Set slider object's allowed range and the step size.

        :param Min:  Minimum level
        :type Min: int, float
        :param Max:  Maximum level
        :type Max: int, float
        :param Step: Optional step size.
        :type Step: int, float

        .. note:: The default range is 0 - 100 with a step size of 1.

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
    def Changed(self):
        '''
        ``Event:`` Triggers when the slider value is changed by user
        interaction (i.e. after :py:attr:`Pressed` but before
        :py:attr:`Released`).

        The callback takes three arguments. The first is the
        :py:class:`Slider` instance triggering the event, the second is
        the state, and the third is the new slider value.

        .. code-block:: python

            @event(ProgramAudio, 'Changed')
            def handleProgramAudio(slider, state, value):
                if state == 'Changed':
                    # Send new program audio level
        '''
        pass

    @property
    def Enabled(self):
        '''
        :return: ``True`` if the control object is enabled else ``False``
        :rtype: bool
        '''
        pass

    @property
    def Fill(self):
        '''
        :return: the current fill level
        :rtype: int, float
        '''
        pass

    @property
    def Max(self):
        '''
        :return: the upper bound of the slider object
        :rtype: int, float
        '''
        pass

    @property
    def Min(self):
        '''
        :return: the lower bound of the slider object
        :rtype: int, float
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
    def Pressed(self):
        '''
        ``Event:`` Triggers when the slider is pressed.

        The callback takes three arguments. The first is the
        :py:class:`Slider` instance triggering the event, the second is
        the state, and the third is the new slider value.

        .. code-block:: python

            @event(ProgramAudio, 'Pressed')
            def handleProgramAudio(slider, state, value):
                if state == 'Pressed':
                    # Send new program audio level
        '''
        pass

    @property
    def Released(self):
        '''
        ``Event:`` Triggers when the slider is released.

        The callback takes three arguments. The first is the
        :py:class:`Slider` instance triggering the event, the second is
        the state, and the third is the new slider value.

        .. code-block:: python

            @event(ProgramAudio, 'Released')
            def handleProgramAudio(slider, state, value):
                if state == 'Released':
                    # Send new program audio level
        '''
        pass

    @property
    def Step(self):
        '''
        :return: the step size of the slider object
        :rtype: int, float
        '''
        pass

    @property
    def Visible(self):
        '''
        :return: ``True`` if the control object is visible else ``False``
        :rtype: bool
        '''
        pass
