from . import Interface


class SPInterface(Interface):
    '''
    This class will provide a common interface for controlling and collecting
    data from AV components on Extron devices (:py:mod:`extronlib.device`) and
    Extron Secure Platform devices (:py:mod:`~extronlib.device.SPDevice`).
    The user can instantiate the class directly or create a subclass to add,
    remove, or alter behavior for different types of devices.

    .. code-block:: python
        :linenos:

        from extronlib import event, Version
        from extronlib.device import SPDevice
        from extronlib.interface import SPInterface

        print(Version())

        SystemSwitcher = SPDevice('SysSwitcher')

        SystemSwitcher_spi = SPInterface(SystemSwitcher)

        @event(SystemSwitcher_spi, ['Online', 'Offline'])
        def handleConnection(interface, state):
            print(interface.Host.DeviceAlias, state)

        @event(SystemSwitcher_spi, 'ReceiveData')
        def handleRecvData(interface, data):
            print(interface.Host.DeviceAlias, data)
    '''

    def __init__(self, Host):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`

        .. code-block:: python
            :linenos:

            # Create a System Switcher with Secure Platform Device
            SystemSwitcher = SPDevice('SysSwitcher')

            # Create a Secure Platform Interface to the System Switcher with Secure
            # Platform Device to allow for SIS control of the device.
            SystemSwitcher_spi = SPInterface(SystemSwitcher)

        .. versionadded:: 3.8
        '''
        pass

    def Send(self, data):
        '''
        Send string over secure, Extron channel

        :param data: string to send out
        :type data: bytes, string

        .. code-block:: python

            SystemSwitcher_spi.Send('n\\r')
        '''
        pass

    @property
    def Offline(self):
        '''
        ``Event:`` Triggers when port goes offline

        The callback takes two arguments. The first one is the
        :py:class:`extronlib.interface.SPInterface` instance triggering the
        event and the second one is a string (``'Offline'``).

        .. code-block:: python

            @event(SomeInterface, ['Online', 'Offline'])
            def HandleConnection(interface, state):
                print('{} is now {}'.format(interface.Host.DeviceAlias, state))
        '''
        pass

    @property
    def Online(self):
        '''
        ``Event:`` Triggers when port goes online

        The callback takes two arguments. The first one is the
        :py:class:`extronlib.interface.SPInterface` instance triggering the
        event and the second one is a string (``'Online'``).
        '''
        pass

    @property
    def ReceiveData(self):
        '''
        ``Event:`` Receive Data event handler used for asynchronous
        transactions.

        The callback takes two arguments. The first one is the
        :py:class:`SPInterface` instance triggering the event and the second
        one is a bytes string.

        .. note::
            * The maximum amount of data per ``ReceiveData`` event that will
              be passed into the handler is 1024 bytes.  For payloads greater
              than 1024 bytes, multiple events will be triggered.

        .. code-block:: python
            :linenos:

            mainBuffer = ''

            # rcvString == 'Inf00*XYZ 1000\\r\\n12-3456-78\\r\\n192.168.1'
            @event(SystemSwitcher_spi, 'ReceiveData')
            def handleRecvData(interface, rcvString):
                global mainBuffer
                mainBuffer += rcvString.decode()

                while True:
                    msg, delim, remainder = mainBuffer.partition('\\r\\n')
                    if not delim:
                        break   # '\\r\\n' wasn't in the buffer

                    mainBuffer = remainder  # save the leftovers

                    if msg in '12-3456-78':
                        # Required polling received
                        doConnectionLogic('Connected')
                    elif msg in AnotherCommand:
                        handleAnotherCommand()
        '''
        pass
