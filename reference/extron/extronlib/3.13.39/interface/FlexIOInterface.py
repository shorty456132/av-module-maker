from . import Interface


class FlexIOInterface(Interface):
    '''
    This class will provide a common interface for controlling and collecting
    data from Flex IO ports on Extron devices (:py:mod:`extronlib.device`).
    The user can instantiate the class directly or create a subclass to add,
    remove, or alter behavior for different types of devices.
    '''

    def __init__(self, Host, Port, Mode='DigitalInput', Pullup=False,
                 Upper=2.8, Lower=2.0):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'FIO1'``)
        :type Port: string
        :param Mode: Possible modes are: ``'AnalogInput'``, ``'DigitalInput'``
            (default), and ``'DigitalOutput'``.
        :type Mode: string
        :param Pullup: pull-up state on the port
        :type Pullup: bool
        :param Upper: upper threshold in volts
        :type Upper: float
        :param Lower: lower threshold in volts
        :type Lower: float
        '''
        pass

    def Initialize(self, Mode=None, Pullup=None, Upper=None, Lower=None):
        '''
        Initializes Flex IO port to given values. User may provide any or all
        of the parameters.  ``None`` leaves property unmodified.

        :param Mode: Possible modes are: ``'AnalogInput'``,
            ``'DigitalInput'``, and ``'DigitalOutput'``.
        :type Mode: string
        :param Pullup: pull-up state on the port
        :type Pullup: bool
        :param Upper: upper threshold in volts
        :type Upper: float
        :param Lower: lower threshold in volts
        :type Lower: float
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
    def AnalogVoltage(self):
        '''
        :return: current voltage of analog input port
        :rtype: float
        '''
        pass

    @property
    def AnalogVoltageChanged(self):
        '''
        ``Event:`` triggers when the input voltage changes.

        The callback takes two arguments. The first one is the
        |FlexIOInterface| instance triggering the event and the second one is
        the voltage.

        .. note:: Minimum voltage change required to trigger event is 0.05V.

        .. versionadded:: 2.4
        '''
        pass

    @property
    def Lower(self):
        '''
        :return: lower threshold for digital input in volts
        :rtype: float

        .. note:: Only applicable when Flex IO is in ``'DigitalInput'`` mode.
        '''
        pass

    @property
    def Mode(self):
        '''
        :return: mode of the Flex IO port (``'AnalogInput'``,
            ``'DigitalInput'``, ``'DigitalOutput'``).
        :rtype: string
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
        :return: indicates if the input port is being pulled up or not
        :rtype: bool
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

        .. note:: Only triggers for ports in Input mode.

        .. code-block:: python

            @event(InputInterface, 'StateChanged')
            def HandleStateChanged(interface, state):
                if state == 'On':
                    StartCombinedInit()
                else:
                    StartSeparateInit()
        '''
        pass

    @property
    def Upper(self):
        '''
        :return: upper threshold for digital input in volts
        :rtype: float

        .. note:: Only applicable when Flex IO is in ``'DigitalInput'`` mode.
        '''
        pass
