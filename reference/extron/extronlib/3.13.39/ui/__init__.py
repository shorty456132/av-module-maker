'''
This package defines classes for user interactive controls.

.. note:: UI control object's states are retained and will be recovered in
    case the endpoints lose connection to the primary control processor.
'''


class UIObject():

    def __init__(self, UIHost, ID):
        '''
        :param UIHost: Device object hosting this UIObject
        :type UIHost: :py:mod:`extronlib.device`
        :param ID: ID or Name of the UIObject
        :type ID: int, string
        '''
        pass

    @property
    def Host(self):
        '''
        :return: UIDevice object that hosts this control object
        :rtype: :py:mod:`extronlib.device`
        '''
        pass

    @property
    def ID(self):
        '''
        :return: the object ID
        :rtype: int
        '''
        pass

from .Button import Button
from .Knob import Knob
from .Label import Label
from .Level import Level
from .Slider import Slider
