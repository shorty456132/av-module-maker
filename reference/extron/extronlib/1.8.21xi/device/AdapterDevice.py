from . import Device, UIDevice


class AdapterDevice(Device):
    """This class provides a common interface to a TouchLink Control Adapter.
    The user can instantiate the class directly or create a subclass to add,
    remove, or alter behavior for different types of devices.
    """

    def __init__(
        self,
        Host: UIDevice,
        DeviceAlias: str
    ):
        """
        Parameters
        ----------
        Host : UIDevice
            handle to Extron `UIDevice` to which the `AdapterDevice` is
            connected
        DeviceAlias : str
            The device alias of the Extron device.

        Examples
        --------
        ::

            # Create UI Device
            ConfRoom = UIDevice('Main')

            # Create AdapterDevice
            ConfRoomAdapter = AdapterDevice(ConfRoom, 'ConfAdapter')


        Ports on the TouchLink Control Adapter are instantiated and used in
        the same way as ports built into controllers but using the TouchLink
        Control Adapter as the ``Host`` parameter.

        Examples
        --------
        ::

            MainProjector = SerialInterface(ConfRoomAdapter, 'COM1')
            MainProjectorBuffer = ''

            ProjectorStates = {
                'POWER': ['OFF', 'WARMING', 'ON', 'COOLING'],
                'INPUT': ['VGA', 'HDMI1', 'HDMI2', 'WIRELESS'],
                }

            # rcvString == 'g:POWER=ON\\rg:INPUT=HDMI1\\rg:KEYLOCK=OFF\\rg:PMM=EX'
            @event(mainProjector, 'ReceiveData')
            def MainFeedbackHandler(interface, rcvString):
                global MainProjectorBuffer
                MainProjectorBuffer += rcvString.decode()

                while True:
                    # partition() finds the first occurance of '\\r' and returns everything
                    # before it, the '\\r' itself, and everything after it.
                    status, delimiter, remainder = MainProjectorBuffer.partition('\\r')
                    if not delimiter:
                        # No '\\r' found in MainProjectorBuffer, no more complete responses
                        # to parse.
                        break

                    # Save any left over data for the next time around the loop.
                    mainBuffer = remainder

                    Command, State = status.split(':')[1].split('=')
                    try:
                        if Command == 'POWER':
                            PowerOn.SetState(ProjectorStates[Command].index(State))
                        elif Command == 'INPUT':
                            InputGroup.SetCurrent(ProjectorStates[Command].index(State))
                        else:
                            print('Unreferenced command:', Command)
                    except ValueError:
                        print('Command', Command, 'State', State, 'undefined')
        """
        pass
