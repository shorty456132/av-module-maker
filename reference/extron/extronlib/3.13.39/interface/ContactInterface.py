from . import Interface


class ContactInterface(Interface):
    '''
    This class will provide a common interface for controlling and collecting
    data from Contact Input ports on Extron devices
    (:py:mod:`extronlib.device`). The user can instantiate the class directly
    or create a subclass to add, remove, or alter behavior for different types
    of devices.
    '''

    def __init__(self, Host, Port):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'CII1'``)
        :type Port: string

        .. versionadded:: 3.2
            Host can be eBUSDevice.
        '''
        pass

    @property
    def Port(self):
        '''
        :return: the port name this interface is attached to
        :rtype: string
        '''
        pass

    @property
    def State(self):
        '''
        :return: current state of IO port (``'On'``, ``'Off'``)
        :rtype: string
        '''
        pass

    @property
    def StateChanged(self):
        '''
        ``Event:`` Triggers when the input state changes.

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event and the
        second one is a string (``'On'`` or ``'Off'``).

        .. code-block:: python

            @event(InputInterface, 'StateChanged')
            def HandleStateChanged(interface, state):
                if state == 'On':
                    StartCombinedInit()
                else:
                    StartSeparateInit()
        '''
        pass
