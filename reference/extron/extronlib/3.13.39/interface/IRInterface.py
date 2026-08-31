from . import Interface


class IRInterface(Interface):
    '''
    This class provides an interface to an IR port. This class allows the user
    to transmit IR data through an IR or IR/Serial port.

    .. note:: If an IR/Serial port is passed in and it has already been
        instantiated as an |SerialInterface|, an exception will be raised.
    '''

    def __init__(self, Host, Port, File):
        '''
        :param Host: handle to Extron device class that instantiated this
            interface class
        :type Host: :py:mod:`extronlib.device`
        :param Port: port name (e.g., ``'IRS1'``, ``'IRI1'``)
        :type Port: string
        :param File: IR file name (e.g. ``'someDevice.eir'``)
        :type File: string

        .. code-block:: python

            VCR = IRInterface(ConfRoom, 'IRS1', 'sony_14_92.eir')
        '''
        pass

    def Initialize(self, File=None):
        '''
        Initializes IR port to given file.  ``None`` leaves property
        unmodified.

        :param File: IR file name (e.g. ``'someDevice.eir'``)
        :type File: string

        .. code-block:: python

            VCR.Initialize('pano_14_209.eir')
        '''
        pass

    def PlayContinuous(self, irFunction):
        '''
        Begin playback of an IR function. Function will play continuously until
        stopped. Will complete at least one header, one body, and the current
        body.

        :param irFunction: function within the driver to play
        :type irFunction: string

        .. note:: *PlayContinuous* is interruptable by subsequent Play function
            calls (:py:meth:`PlayCount`, :py:meth:`PlayTime`) and
            :py:meth:`Stop`.

        .. code-block:: python

            @event(VolUp, ['Pressed', 'Released'])
            def IncVolume(button, state):
                if state == 'Pressed':
                    VCR.PlayContinuous('VOL+')
                elif state == 'Released':
                    VCR.Stop()
        '''
        pass

    def PlayCount(self, irFunction, repeatCount=None):
        '''
        Play an IR function Count times. Function will play the header once and
        the body 1 + the specified number of repeat times.

        :param irFunction: function within the driver to play
        :type irFunction: string
        :param repeatCount: number of times to repeat the body (0-15)
        :type repeatCount: int

        .. note::
            * *PlayCount* is uninterruptible, except by :py:meth:`Stop`.
            * *repeatCount* of ``None`` means play the number defined in the
              driver.

        .. code-block:: python

            VCR.PlayCount('POWER')
        '''
        pass

    def PlayTime(self, irFunction, duration):
        '''
        Play an IR function for the specified length of time. Function will
        play the header once and the body as many times as it can. Playback
        will stop when the time runs out. Current body will be completed.

        :param irFunction: function within the driver to play
        :type irFunction: string
        :param duration: time in seconds to play the function
        :type duration: float

        .. note:: *PlayTime* is uninterruptible, except by :py:meth:`Stop`.

        .. code-block:: python

            VCR.PlayTime('POWER_OFF', 0.4)
        '''
        pass

    @property
    def Port(self):
        '''
        :return: the port name this interface is attached to
        :rtype: string
        '''
        pass

    def Stop(self):
        '''Stop the current playback. Will complete the current body.'''
        pass

    @property
    def File(self):
        '''
        :return: file name
        :rtype: string
        '''
        pass
