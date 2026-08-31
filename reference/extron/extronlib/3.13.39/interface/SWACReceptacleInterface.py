from . import Interface


class SWACReceptacleInterface(Interface):
    '''
    This class provides a common interface to a switched AC power receptacle on
    an Extron product (:py:mod:`extronlib.device`). The user can instantiate the
    class directly or create a subclass to add, remove, or alter behavior for
    different types of devices.

    .. versionadded:: 3.1
    '''

    def __init__(self, Host, Port):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'SAC1'``)
        :type Port: string
        '''
        pass

    def SetState(self, State):
        '''
        :param State: output state to be set (``'On'`` or ``1``, ``'Off'`` or
            ``0``)
        :type State: int, string

        .. code-block:: python

            SomeInterface.SetState('On')
        '''
        pass

    def Toggle(self):
        '''
        Changes the state of the receptacle to the logical opposite of the
        current state.
        '''
        pass

    @property
    def Current(self):
        '''
        :return: instantaneous current draw in Amperes
        :rtype: float
        '''
        pass

    @property
    def CurrentChanged(self):
        '''
        ``Event:`` triggers when the current draw changes.

        The callback takes two arguments. The first one is the
        |SWACReceptacleInterface| instance triggering the event, and the
        second is the current.
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
        :return: current state of the receptacle (``'On'``, ``'Off'``)
        :rtype: string
        '''
        pass

    @property
    def StateChanged(self):
        '''
        ``Event:`` Triggers when the receptacle state changes.

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event, and
        the second is a string (``'On'`` or ``'Off'``).

        .. code-block:: python

            @event(SomeInterface, 'StateChanged')
            def HandleStateChanged(interface, state):
                print('{} is now {}.'.format(interface.Port, state))
        '''
        pass
