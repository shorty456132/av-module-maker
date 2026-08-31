'''
This package contains libraries for Extron hardware interfaces.

.. warning::
    1. An exception will be raised if an attempt is made to instantiate any
       physical interface more than once.  Use the Initialize or Set*
       functions to change modes where applicable.
    2. Instantiating a physical interface that the control processor does not
       have, will be logged.

       * Subsequent calls to that object's methods will fail silently.
       * Subsequent calls to read that object's properties will return
         ``None``.

.. topic:: Summary of interface port names:

    .. list-table::
            :widths: 20 20

            * - **Interface**
              - **Port Name**
            * - |CircuitBreakerInterface|
              - ``'CBR1'``
            * - |ContactInterface|
              - ``'CII1'``
            * - |DigitalInputInterface|
              - ``'DII1'``
            * - |DigitalIOInterface|
              - ``'DIO1'``
            * - |FlexIOInterface|
              - ``'FIO1'``
            * - |IRInterface|
              - ``'IRS1'``, ``'IRI1'``
            * - |PoEInterface|
              - ``'POE1'``
            * - |RelayInterface|
              - ``'RLY1'``
            * - |SerialInterface|
              - ``'COM1'``
            * - |SWACReceptacleInterface|
              - ``'SAC1'``
            * - |SWPowerInterface|
              - ``'SPI1'``
            * - |TallyInterface|
              - ``'TAL1'``
            * - |VolumeInterface|
              - ``'VOL1'``

    See :ref:`ref-Products` to identify which :py:mod:`~extronlib.device` and
    :py:mod:`~extronlib.interface` classes to use for each product.
'''

class Interface():

    @property
    def Host(self):
        '''
        :return: handle to Extron device class that instantiated this interface
            class
        :rtype: :py:mod:`extronlib.device`
        '''
        pass

    @property
    def Offline(self):
        '''
        ``Event:`` Triggers when port goes offline

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event and the
        second one is a string (``'Offline'``).

        .. code-block:: python

            @event(SomeInterface, ['Online', 'Offline'])
            def HandleConnection(interface, state):
                print('{} is now {}'.format(interface.Port, state))
        '''
        pass

    @property
    def Online(self):
        '''
        ``Event:`` Triggers when port goes online

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event and the
        second one is a string (``'Online'``).
        '''
        pass

from .CircuitBreakerInterface import CircuitBreakerInterface
from .ContactInterface import ContactInterface
from .DigitalInputInterface import DigitalInputInterface
from .DigitalIOInterface import DigitalIOInterface
from .EthernetClientInterface import EthernetClientInterface
from .EthernetServerInterface import EthernetServerInterface
from .EthernetServerInterfaceEx import ClientObject, EthernetServerInterfaceEx
from .FlexIOInterface import FlexIOInterface
from .IRInterface import IRInterface
from .PoEInterface import PoEInterface
from .RelayInterface import RelayInterface
from .SerialInterface import SerialInterface
from .SPInterface import SPInterface
from .SWACReceptacleInterface import SWACReceptacleInterface
from .SWPowerInterface import SWPowerInterface
from .TallyInterface import TallyInterface
from .VolumeInterface import VolumeInterface
