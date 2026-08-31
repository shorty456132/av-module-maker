from . import Interface


class SerialInterface(Interface):
    '''
    This class provides an interface to a serial port. This class allows the
    user to send data over the serial port in a synchronous or asynchronous
    manner. This class is used for all ports capable of serial communication
    (e.g., Serial Ports, IR Serial Ports).

    .. note::
        * :py:meth:`SendAndWait` can be used to synchronously capture
          responses.
        * For asynchronous communication, a handler function is assigned to
          the :py:data:`ReceiveData` event. Then responses and unsolicited
          messages will be sent to the user's ``ReceiveData`` handler.
        * ``SendAndWait`` cannot be called within the context of a
          ``ReceiveData`` event.
        * Using ``SendAndWait`` while unsolicited data transmission is
          possible, may cause data loss.
        * If an IR/Serial port is passed in and it has already been
          instantiated as an |IRInterface|, an exception will be raised.
    '''

    def __init__(self, Host, Port, Baud=9600, Data=8, Parity='None',
                 Stop=1, FlowControl='Off', CharDelay=0, Mode='RS232'):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g., ``'COM1'``, ``'IRS1'``)
        :type Port: string
        :param Baud: baudrate
        :type Baud: int
        :param Data: number of data bits
        :type Data: int
        :param Parity: ``'None'``, ``'Odd'`` or ``'Even'``
        :type Parity: string
        :param Stop: number of stop bits
        :type Stop: int
        :param FlowControl: ``'HW'``, ``'SW'``, or ``'Off'``
        :type FlowControl: string
        :param CharDelay: time between each character sent to the connected
            device
        :type CharDelay: float
        :param Mode: mode of the port, ``'RS232'``, ``'RS422'`` or ``'RS485'``
        :type Mode: string
        '''
        pass

    def Initialize(self, Baud=None, Data=None, Parity=None, Stop=None,
                   FlowControl=None, CharDelay=None, Mode=None):
        '''
        Initializes Serial port to given values. User may provide any or all of
        the parameters.  ``None`` leaves property unmodified.

        :param Baud: baudrate
        :type Baud: int
        :param Data: number of data bits
        :type Data: int
        :param Parity: ``'None'``, ``'Odd'`` or ``'Even'``
        :type Parity: string
        :param Stop: number of stop bits
        :type Stop: int
        :param FlowControl: ``'HW'``, ``'SW'``, or ``'Off'``
        :type FlowControl: string
        :param CharDelay: time between each character sent to the connected
            device
        :type CharDelay: float
        :param Mode: mode of the port, ``'RS232'``, ``'RS422'`` or ``'RS485'``
        :type Mode: string
        '''
        pass

    def Send(self, data):
        '''Send string over serial port if it's open

        :param data: data to send
        :type data: bytes, string
        :raise: TypeError, IOError
        '''
        pass

    def SendAndWait(self, data, timeout, **delimiter):
        '''
        Send data to the controlled device and wait (blocking) for response

        .. note:: In addition to *data* and *timeout*, the method accepts an
            optional delimiter, which is used to compare against the received
            response.  It supports any one of the following conditions:

                * *deliLen* (int) - length of the response
                * *deliTag* (bytes) - suffix of the response
                * *deliRex* (regular expression object) - regular expression

        It returns after *timeout* seconds expires, or returns immediately if
        the optional condition is satisfied.

        .. note:: The function will return an empty bytes object if *timeout*
            expires and nothing is received, or the condition (if provided) is
            not met.

        :param data: data to send.
        :type data: bytes, string
        :param timeout: amount of time to wait for response.
        :type timeout: float
        :param delimiter: optional conditions to look for in response.
        :type delimiter: see above
        :return: Response received data (may be empty)
        :rtype: bytes
        '''
        pass

    def StartKeepAlive(self, interval, data):
        '''
        Repeatedly sends *data* at the given *interval*

        :param interval: Time in seconds between transmissions
        :type interval: float
        :param data: data to send
        :type data: bytes, string
        '''
        pass

    def StopKeepAlive(self):
        '''Stop the currently running keep alive routine'''
        pass

    @property
    def Baud(self):
        '''
        :return: the baud rate
        :rtype: int
        '''
        pass

    @property
    def CharDelay(self):
        '''
        :return: inter-character delay
        :rtype: float
        '''
        pass

    @property
    def Data(self):
        '''
        :return: the number of data bits
        :rtype: int
        '''
        pass

    @property
    def FlowControl(self):
        '''
        :return: flow control
        :rtype: string'''
        pass

    @property
    def Host(self):
        '''
        :return: the host device
        :rtype: :py:mod:`extronlib.device`
        '''
        pass

    @property
    def Mode(self):
        '''
        :return: the current Mode
        :rtype: string
        '''
        pass

    @property
    def Parity(self):
        '''
        :return: parity
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
    def ReceiveData(self):
        '''
        ``Event:`` Receive Data event handler used for asynchronous
        transactions

        The callback takes two arguments. The first one is the
        |SerialInterface| instance triggering the event and the
        second one is a bytes object.

        .. code-block:: python
            :linenos:

            mainProjector = SerialInterface(ConfRoom, 'COM1')

            ProjectorStates = {
                'POWER': ['OFF', 'OFF2ON', 'ON', 'ON2PMM', 'PMM', 'PMM2ON', 'ON2OFF'],
                'INPUT': [
                    'D-RGB', 'A-RGB1', 'A-RGB2', 'COMP', 'VIDEO', 'S-VIDEO', 'HDMI', 'USB'
                    ],
                'PMM': ['OFF', 'STANDBY']
                }
            ProjectorStatus = {}
            mainBuffer = ''

            # rcvString == 'g:POWER=ON\\rg:INPUT=HDMI\\rg:KEYLOCK=OFF\\rg:PMM=EX'
            @event(mainProjector, 'ReceiveData')
            def MainFeedbackHandler(interface, rcvString):
                global mainBuffer
                tempBuffer = mainBuffer + rcvString.decode()
                if tempBuffer[-1] != '\\r':              # Partial message
                    last = tempBuffer.rfind('\\r')       # Find last <CR>
                    mainBuffer = tempBuffer[last+1:]    # Save the leftovers
                    tempBuffer = tempBuffer[:last]      # Deal with the complete strings
                else:
                    mainBuffer = ''                     # All data handled

                # Turn rcvString into:
                #   [['POWER', 'ON'], ['INPUT', 'HDMI'], ['KEYLOCK', 'OFF]]
                responses = [
                    msg.split(':')[1].split('=') \\
                    for msg in tempBuffer.split('\\r') \\
                    if not msg == ''
                    ]
                # Handle responses
                for response in responses:
                    Command, State = response[0], response[1]
                    ProjectorStatus[Command] = State    # Store data for use elsewhere
                    if Command in ProjectorStates:      # Set feedback for each
                        try:
                            if Command == 'POWER':
                                PowerOn.SetState(ProjectorStates[Command].index(State))
                            elif Command == 'INPUT':
                                InputGroup.SetCurrent(
                                    ProjectorStates[Command].index(State)
                                    )
                            elif Command == 'PMM':
                                PowerM.SetState(ProjectorStates[Command].index(State))
                        except:
                            print('State', response, 'undefined.')
                    else:
                        print('Unreferenced command:', response)
        '''
        pass

    @property
    def Stop(self):
        '''
        :return: number of stop bits
        :rtype: int
        '''
        pass
