class VolumeInterface():
    '''
    This class will provide a common interface for controlling and collecting
    data from Volume Ports on Extron devices (:py:mod:`extronlib.device`). The
    user can instantiate the class directly or create a subclass to add,
    remove, or alter behavior for different types of devices.
    '''

    def __init__(self, Host, Port):
        '''
        :param Host: handle to Extron device class that instantiated
            this interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g. ``'VOL1'``)
        :type Port: string

        .. code-block:: python

            ConfRoom = ProcessorDevice('ConfRoom 250')
            VolumeConfRoom = VolumeInterface(ConfRoom, 'VOL1')
        '''
        pass

    def SetLevel(self, Level):
        '''
        Sets Level of volume control port

        :param Level: Level (0 % <= Value <= 100 %).
        :type Level: int

        .. code-block:: python
            :linenos:

            currentLevel = 0

            @event(Inc, ['Pressed', 'Repeated'])
            def IncVolume(button, state):
                global currentLevel
                if currentLevel < 100:
                    currentLevel += 1
                    VolumeConfRoom.SetLevel(currentLevel)

            @event(Dec, ['Pressed', 'Repeated'])
            def DecVolume(button, state):
                global currentLevel
                if currentLevel > 0:
                    currentLevel -= 1
                    VolumeConfRoom.SetLevel(currentLevel)
        '''
        pass

    def SetMute(self, Mute):
        '''
        Sets the mute state.

        :param Mute: mute state (``'On'``, ``'Off'``).
        :type Mute: string
        '''
        pass

    def SetRange(self, Min, Max):
        '''
        Set volume control object’s voltage range.

        :param Min: minimum voltage
        :type Min: float
        :param Max: maximum voltage
        :type Max: float

        .. code-block:: python

            VolumeConfRoom.SetRange(1, 7.5)   # Voltage
        '''
        pass

    def SetSoftStart(self, SoftStart):
        '''
        Enable or Disable Soft Start.

        :param SoftStart: Soft Start state (``'Enabled'``, ``'Disabled'``).
        :type SoftStart: string

        .. code-block:: python

            VolumeConfRoom.SetSoftStart('Enabled')
        '''
        pass

    @property
    def Host(self):
        '''
        :return: the host device
        :rtype: :py:mod:`extronlib.device`
        '''
        pass

    @property
    def Level(self):
        '''
        :return: Current volume level (percentage).
        :rtype: int
        '''
        pass

    @property
    def Max(self):
        '''
        :return: Maximum level (0.0 V < Max <= 10.0 V).
        :rtype: float
        '''
        pass

    @property
    def Min(self):
        '''
        :return: Minimum level (0.0 V <= Min < 10.0 V).
        :rtype: float
        '''
        pass

    @property
    def Mute(self):
        '''
        :return: Current state of volume port mute.  (``'On'``, ``'Off'``)
        :rtype: string
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

        .. versionadded:: 3.2
        '''
        pass

    @property
    def Online(self):
        '''
        ``Event:`` Triggers when port goes online

        The callback takes two arguments. The first one is the
        :py:mod:`extronlib.interface` instance triggering the event and the
        second one is a string (``'Online'``).

        .. versionadded:: 3.2
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
    def SoftStart(self):
        '''
        :return: Current state of Soft Start. (``'Enabled'``, ``'Disabled'``)
        :rtype: string
        '''
        pass
