from . import Interface


class CircuitBreakerInterface(Interface):
    '''
    This class provides a common interface to a circuit breaker on an Extron
    product (:py:mod:`extronlib.device`). The user can instantiate the class
    directly or create a subclass to add, remove, or alter behavior for different
    types of devices.

    .. versionadded:: 3.1
    '''

    def __init__(self, Host, Port):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'CBR1'``)
        :type Port: string
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
        :return: current state of the circuit breaker (``'Closed'``,
            ``'Tripped'``)
        :rtype: string
        '''
        pass

    @property
    def StateChanged(self):
        '''
        ``Event:`` Triggers when the circuit breaker state changes.

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event, and
        the second is a string (``'Closed'`` or ``'Tripped'``).

        .. code-block:: python

            @event(SomeInterface, 'StateChanged')
            def HandleStateChanged(interface, state):
                if state == 'Tripped':
                    TrippedAlert()
        '''
        pass
