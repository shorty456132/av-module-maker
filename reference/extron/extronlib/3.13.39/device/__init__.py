'''This package contains libraries to interact with Extron Control Devices.'''


class Device():

    def __init__(self, DeviceAlias, PartNumber=None):
        '''

        :param DeviceAlias: Device Alias of the Extron device
        :type DeviceAlias: string
        :param PartNumber: device's part number
        :type PartNumber: string

        .. note::
            * *DeviceAlias* must be a valid device Device Alias of an
              Extron device in the system.
            * If the part number is provided, the device will trigger a
              warning message in the program log if it does not match the
              connected device.

        .. code-block:: python

            # Create Primary Processor
            ConfRoom = ProcessorDevice('Main')

            # Create Secondary Processor, Confirm Partnumber
            ConfRoom3 = ProcessorDevice('profRobertsRm', '60-1234-01')

            # Create Touch Panel
            PodiumTLP = UIDevice('Podium TLP')

            # Create System Switcher AV Device
            SystemSwitcher = SPDevice('SysSwitcher')
        '''
        pass

    @property
    def DeviceAlias(self):
        '''
        :return: the device alias of the object
        :rtype: string
        '''
        pass

    @property
    def ModelName(self):
        '''
        :return: Model name of this device
        :rtype: string

        .. versionadded:: 2.4
        '''
        pass

    @property
    def Online(self):
        '''
        ``Event:`` Triggers when the device comes online.

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.device` instance triggering the event and the
        second one is a string (``'Online'``).
        '''
        pass

    @property
    def Offline(self):
        '''
        ``Event:`` Triggers when the device goes offline.

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.device` instance triggering the event and the
        second one is a string (``'Offline'``).
        '''
        pass

    @property
    def PartNumber(self):
        '''
        :return: the part number of this device
        :rtype: string
        '''
        pass

from .eBUSDevice import eBUSDevice
from .ProcessorDevice import ProcessorDevice
from .SPDevice import SPDevice
from .UIDevice import UIDevice
