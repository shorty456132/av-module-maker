from . import UIObject


class Knob(UIObject):
    '''Knob is a rotary control that has 36 steps for a full revolution'''

    def __init__(self, UIHost, ID):
        '''
        :param UIHost: Device object hosting this UIObject
        :type UIHost: :py:mod:`extronlib.device`
        :param ID: ID of the UIObject
        :type ID: int
        '''
        pass

    @property
    def Turned(self):
        '''
        ``Event:`` Get/Set callback when knob is turned

        The callback takes two parameters. The first one is the
        :py:class:`Knob` itself and the second one is a signed integer
        indicating steps that was turned. Positive values indicate clockwise
        rotation.

        .. code-block:: python

            @event(mainKnob, 'Turned')
            def handleMainKnob(knob, direction):
                if direction > 0:
                    for i in range(direction):
                        mainProjector.Send('VOLUME UP')
                else:
                    for i in range(direction, 0):
                        mainProjector.Send('VOLUME DOWN')
        '''
        pass
