from . import Interface


class PoEInterface(Interface):
    '''
    This is the interface class for the Power over Ethernet ports on Extron
    devices (:py:mod:`extronlib.device`). The user can instantiate the class
    directly or create a subclass to add, remove, or alter behavior for
    different types of devices.

    .. versionadded:: 2.9
    '''

    def __init__(self, Host, Port):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'POE1'``)
        :type Port: string
        '''
        pass

    def SetState(self, State):
        '''
        :param State: output state to be set (``'On'`` or ``1``, ``'Off'`` or
            ``0``)
        :type State: int, string

        .. code-block:: python

            OutputInterface.SetState('On')
        '''
        pass

    def Toggle(self):
        '''
        Changes the state to the logical opposite of the current state.
        '''
        pass

    @property
    def CurrentLoad(self):
        '''
        :return: the current load of PoE port in watts
        :rtype: float
        '''
        pass

    @property
    def PowerStatus(self):
        '''
        :return: State of power transmission on the port (``'Active'``,
            ``'Inactive'``).  ``'Active'`` if there is a device being powered
            by the port.
        :rtype: string
        '''
        pass

    @property
    def PowerStatusChanged(self):
        '''
        ``Event:`` Triggers when the state of power transmission on the port
        changes (e.g. a PoE device is plugged into the port).

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event and the
        second one is a string (``'Active'`` or ``'Inactive'``).

        .. code-block:: python

            @event(poeInterface, 'PowerStatusChanged')
            def HandlePowerStatusChanged(interface, status):
                if status == 'Active':
                    LecternInUse()
                else:
                    LecternNotInUse()
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
