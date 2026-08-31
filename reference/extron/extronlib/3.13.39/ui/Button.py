from . import UIObject


class Button(UIObject):
    '''
    Representation of Hard/Soft buttons

    A button may trigger several events depending on the configuration;
    however, Touch Panels only issue :py:data:`Pressed` and :py:data:`Released`
    messages to the control processor. Other events (e.g., :py:data:`Held`,
    :py:data:`Repeated`) are timer driven within the Button instance.
    '''

    def __init__(self, UIHost, ID, holdTime=None, repeatTime=None):
        '''
        :param UIHost: Device object hosting this UIObject
        :type UIHost: :py:mod:`extronlib.device`
        :param ID: ID or Name of the UIObject
        :type ID: int,string
        :param holdTime: Time for :py:data:`Held` event. Held event is
            triggered only once if the button is pressed and held beyond this
            time. If holdTime is given, it must be a floating point number
            specifying period of time in seconds of button being pressed and
            held to trigger Held event.
        :type holdTime: float
        :param repeatTime: Time for :py:data:`Repeated` event. After *holdTime*
            expires, the Repeated event is triggered for every additional
            *repeatTime* of button being held.  If repeatTime is given, it must
            be a floating point number specifying time in seconds of button
            being held.
        :type repeatTime: float

        .. note:: If button is released before *holdTime* expires,
            a :py:data:`Tapped` event is triggered instead of a
            :py:data:`Released` event. If the button is released after
            *holdTime* expires, there will be no :py:data:`Tapped` event.

        .. code-block:: python

            powerOn = Button(PodiumTLP, 'Power On')
            showSetupPage = Button(PodiumTLP, 'Show Setup Page', holdTime=5)
            volumeUp = Button(PodiumTLP, 10, repeatTime=0.1)
            volumeDown = Button(PodiumTLP, 11, repeatTime=0.1)
        '''
        pass

    def CustomBlink(self, rate, stateList):
        '''
        Make the button cycle through each of the states provided.

        :param rate: duration of time in seconds for one visual state to stay
            until replaced by the next visual state.
        :type rate: float
        :param stateList: list of visual states that this button blinks among.
        :type stateList: list of ints

        .. code-block:: python

            showSetupPage.CustomBlink(1, [0, 1])
        '''
        pass

    def SetBlinking(self, rate, stateList):
        '''
        Make the button cycle, at ADA compliant rates, through each of the
        states provided.

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

        .. note::
            * Using this function will blink in unison with other buttons.
            * Maximum of six states in the *stateList* for |eBUSDevice|
              buttons.

        :param rate: ADA compliant blink rate. (``'Slow'``, ``'Medium'``,
            ``'Fast'``)
        :type rate: string
        :param stateList: list of visual states that this button blinks among.
        :type stateList: list of ints

        .. code-block:: python

            powerOn.SetBlinking('Medium', [2, 4])   # Warming up
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

    def SetState(self, State):
        '''
        Set the current visual state

        :param State: visual state number
        :type State: int

        .. note:: Setting the current state stops button from blinking, if it
            is running. (:py:meth:`SetBlinking`)

        .. code-block:: python

            powerOn.SetState(1) # Powered On
        '''
        pass

    def SetText(self, text):
        '''
        Specify text to display on the UIObject

        :param text: text to display
        :type text: string
        :raises: ``TypeError``

        .. code-block:: python

            roomMode.SetText('Combined')
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
    def BlinkState(self):
        '''
        :return: the current blink state (``'Not blinking'`` or
            ``'Blinking'``)
        :rtype: string
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
    def Held(self):
        '''
        ``Event:`` Get/Set the callback when hold expire event is triggered

        The callback function must accept exactly two parameters, which are
        the :py:class:`Button` that triggers the event and the state
        (e.g. 'Held').

        .. code-block:: python

            @event(showSetupPage, 'Held')
            def ShowSetupPage(button, state):
                PodiumTLP.ShowPage('Setup Page')
                currentVolume = PodiumTLP.GetVolume('HDMI')
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
        ``Event:`` Get/Set the callback when the button is pressed

        The callback function must accept exactly two parameters, which are
        the :py:class:`Button` that triggers the event and the state
        (e.g. 'Pressed').

        .. code-block:: python

            @event(powerOn, 'Pressed')
            def PowerOn(button, state):
                powerOn.SetBlinking('Medium', [2, 4])
                mainProjector.Send('POWER ON')
        '''
        pass

    @property
    def PressedState(self):
        '''
        :return: True if the button is pressed, else False
        :rtype: bool
        '''
        pass

    @property
    def Released(self):
        '''
        ``Event:`` Get/Set the callback when the button is released

        The callback function must accept exactly two parameters, which are
        the :py:class:`Button` that triggers the event and the state
        (e.g. 'Held').

        .. code-block:: python

            @event(closeSetupPage, 'Released')
            def ClosePage(button, state):
                PodiumTLP.ShowPage('Main')

        '''
        pass

    @property
    def Repeated(self):
        '''
        ``Event:`` Get/Set the callback when repeat event is triggered

        The callback function must accept exactly two parameters, which are
        the :py:class:`Button` that triggers the event and the state
        (e.g. 'Repeated').

        .. code-block:: python

            @event(volumeUp, 'Repeated')
            def VolUp(button, state):
                global VolLevel
                if VolLevel < 20:
                    VolLevel += 1
                    mainProjector.Send('VOLUME {}'.format(VolLevel))

        '''
        pass

    @property
    def Tapped(self):
        '''
        ``Event:`` Get/Set the callback when tap event is triggered

        The callback function must accept exactly two parameters, which are
        the :py:class:`Button` that triggers the event and the state
        (e.g. 'Tapped').

        .. code-block:: python

            @event(zoomIn, 'Tapped')
            def ZoomInTapped(button, state):
                PTZ.Send('zoom +1')   # Nudge the zoom
        '''
        pass

    @property
    def State(self):
        '''
        :return: the current visual state number
        :rtype: int

        .. note:: It does not return the current state if the button is
            blinking.
        '''
        pass

    @property
    def Visible(self):
        '''
        :return: ``True`` if the control object is visible else ``False``
        :rtype: bool
        '''
        pass
