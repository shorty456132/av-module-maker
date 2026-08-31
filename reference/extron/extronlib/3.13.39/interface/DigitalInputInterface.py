from . import Interface


class DigitalInputInterface(Interface):
    '''
    This class will provide a common interface for collecting data from
    Digital Input ports on Extron devices (:py:mod:`extronlib.device`).
    The user can instantiate the class directly or create a subclass to add,
    remove, or alter behavior for different types of devices.

    .. versionadded:: 3.1
    '''

    def __init__(self, Host, Port, Pullup=False):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'DII1'``)
        :type Port: string
        :param Pullup: pull-up state on the port
        :type Pullup: bool
        '''
        pass

    def Initialize(self, Pullup=None):
        '''
        Initializes Digital Input port to given values. User may provide
        any or all of the parameters.  ``None`` leaves property unmodified.

        :param Pullup: pull-up state on the port
        :type Pullup: bool
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
    def Pullup(self):
        '''
        :return: indicates if the Input port is being pulled up or not
        :rtype: bool
        '''
        pass

    @property
    def State(self):
        '''
        :return: current state of Input port (``'On'``, ``'Off'``)
        :rtype: string
        '''
        pass

    @property
    def StateChanged(self):
        '''
        ``Event:`` Triggers when the input state changes.

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event and
        the second is a string (``'On'`` or ``'Off'``).

        .. code-block:: python

            @event(InputInterface, 'StateChanged')
            def HandleStateChanged(interface, state):
                if state == 'On':
                    StartCombinedInit()
                else:
                    StartSeparateInit()
        '''
        pass
