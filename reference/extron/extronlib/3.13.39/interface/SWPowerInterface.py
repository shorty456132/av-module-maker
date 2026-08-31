from . import Interface


class SWPowerInterface(Interface):
    '''
    This is the interface class for the Switched Power ports on Extron devices
    (:py:mod:`extronlib.device`). The user can instantiate the class directly
    or create a subclass to add, remove, or alter behavior for different types
    of devices.
    '''

    def __init__(self, Host, Port):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'SPI1'``)
        :type Port: string
        '''
        pass

    def Pulse(self, duration):
        '''
        Turns the port on for the specified time in seconds with 10ms accuracy
        and a 100ms minimum value.

        :param duration: pulse duration
        :type duration: float

        .. code-block:: python

            OutputInterface.Pulse(0.3)
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
        Changes the state of the IO Object to the logical opposite of the
        current state.
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
