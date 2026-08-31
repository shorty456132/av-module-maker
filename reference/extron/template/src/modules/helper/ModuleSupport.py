# The ModuleSupport module provides a set of classes and functions for efficient device control.


# Copyright 2020-2023, Extron Electronics. All rights reserved.


from functools import partial
from itertools import product

from extronlib.interface import EthernetServerInterfaceEx

from extronlib.system import ProgramLog

__history__ = """
Version     Date        Notes
-------     ----        -----
1.0.0       2/8/2023    Initial release.
"""

__version__ = '1.0.0'


__dispatchmap = {}


def __eventExDispatch__(key, *args, **kwargs):
    for handler in __dispatchmap[key]:
        handler(*args, **kwargs)


def eventEx(Object, EventName, *args, **kwargs):
    r"""Decorate a function to be the handler for `Object` when `EventName` occurs. This decorator
    offers extensions over the capabilities of extronlib's built-in event decorator:

        * The event can trigger multiple handlers.
        * In addition to property names, `EventName` can refer to method names.

    The decorated function must have the exact signature as specified by the definition of
    EventName, which must appear in the `Object` class or one of its parent classes. Lists of
    `Object` and/or `EventName` can be passed in to apply the same handler to multiple events.

    This decorator may be used as a drop-in replacement for extronlib's built-in event decorator;
    however, it introduces a minimal amount of latency both in event setup and dispatch.

    Parameters
    ----------
    Object : Python object instance or list of instances
        The Object instance(s) that define EventName.
    EventName : str or list of str
        Name of an event or list of event names. If a list, all object instances in `Object` must
        implement all event names.
    *args
        A variable number of positional arguments that will be passed to the function that sets up
        the event handling (i.e. the EventName). Not applicable to events set via properties.
    **kwargs
        Keyword arguments that will be passed to the function that sets up the event handling
        (i.e. the EventName). Not applicable to events set via properties.

    Raises
    ------
    AttributeError
        If `Object` does not have an `EventName` attribute.
    TypeError
        If `EventName` is not a string or list of strings or if the attribute name in EventName
        is something other than a property or method.
    """
    if not isinstance(Object, list):
        Object = [Object]

    if not isinstance(EventName, list):
        EventName = [EventName]

    def deco(handler):
        for obj, evtname in product(Object, EventName):

            if not isinstance(evtname, str):
                raise TypeError('EventName must be a string.')

            klass = type(obj)

            callsetter = getattr(klass, evtname)

            if isinstance(callsetter, property) and callsetter.fset is not None:
                # The event handler is set via a property.
                callsetter = partial(callsetter.fset, obj)
            elif callable(callsetter):
                # The event handler is set via a method.
                callsetter = partial(callsetter, obj)
            else:
                msg = "EventName '{}' is not a method or settable property of object named '{}'.".format(
                    evtname, obj.__name__
                )
                raise TypeError(msg)

            if not (obj, evtname) in __dispatchmap.keys():
                __dispatchmap[(obj, evtname)] = []

            __dispatchmap[(obj, evtname)].append(handler)
            callsetter(partial(__eventExDispatch__, (obj, evtname)), *args, **kwargs)

        return handler

    return deco


class _ManualEventBase:
    def __init__(self, Name):
        self._name = Name
        self._handler = None

    @property
    def Name(self):
        return self._name


class GenericEvent(_ManualEventBase):
    """Trigger an ``extronlib.event`` or :py:attr:`eventEx` event handler with a function call.

    Some notification implementations use a callback function supplied as an argument in a method
    call. This is incompatible with how the @event decorator in extronlib is used. This class
    connects those callbacks to an event handler compatible with @event.

    Examples
    --------
    ::

        MyEvent = GenericEvent('my event')

        @event(MyEvent, 'Triggered')
        def HandleTriggered(src, value):
            print('Event "{}" was triggered with value {}.'.format(src.Name, value))

        MyEvent.Trigger(123)
    """

    def __init__(self, Name='unnamed event'):
        super().__init__(Name)

    @property
    def Triggered(self):
        """
        ``Event`` - Triggers when this instance's :py:attr:`Trigger` method is called.

        The parameters passed to the handler are variable. The first parameter will be the
        :py:class:`GenericEvent` instance triggering the event followed by any positional and/or
        keyword parameters that were passed to :py:attr:`Trigger`.
        """
        return self._handler

    @Triggered.setter
    def Triggered(self, handler):
        if not callable(handler):
            raise ValueError("'handler' must be callable.")

        self._handler = handler

    def Trigger(self, *args, **kwargs):
        """
        Calls to this method will cause the :py:attr:`Triggered` event to trigger.

        It accepts a variable number of positional and keyword arguments which, along with
        this instances, are passed to the ``Triggered`` handler.
        """
        if self._handler:
            self._handler(self, *args, **kwargs)


class WatchVariable(_ManualEventBase):
    """Wrap a variable in so that changes to that variable can trigger an event handler compatible
    with the ``extronlib.event`` and :py:attr:`eventEx` decorators (eventEx preferred).

    Parameters
    ----------
    Name: str
        A friendly name used to identify this instance. Usable in logging output, for example.
        Defaults to 'unnamed variable'.


    Use this class to signal to other parts of your program that the state of a system variable
    has been changed.

    Examples
    --------
    In the variable definition (`variables.py`) portion of the ControlScript program:
    ::

        CallStatus = 'On Hook'
        CallStatusWatch = WatchVariable('Video call status')

        @eventEx(CallStatusWatch, 'Changed')
        def HandleCallStatusChanged(src, value):
            global CallStatus
            # Remember to update the state of the variable.
            CallStatus = value
            print('{} changed to {}'.format(src.Name, value))

    In the portion of the ControlScript program that handles device state changes:
    ::

        from variables import CallStatusWatch

        CallStatusWatch.Change('Ringing')

    Add another eventEx handler if you need to react to a state change elsewhere in your program.
    ::

        from variables import CallStatusWatch

        @eventEx(CallStatusWatch, 'Changed')
        def HandleCallStatusChanged(src, value):
            # Handle the new state

    If the variable state is needed outside of a :py:attr:`Changed` handler:

    ::

        import variables

        print('CallStatus is', variables.CallStatus)
    """

    def __init__(self, Name='unnamed variable'):
        super().__init__(Name)

    @property
    def Changed(self):
        """
        ``Event`` - Triggers when this instance's :py:attr:`Change` method is called.

        The parameters passed to the handler are variable. The first parameter will be the
        :py:class:`WatchVariable` instance triggering the event followed by any positional
        and/or keyword parameters that were passed to :py:attr:`Change`.

        Examples
        --------
        ::

            @eventEx(MyWatcher, 'Changed')
            def HandleMyWatcherChanged(src, value):
                print('{} changed to {}'.format(src.Name, value))
        """
        return self._handler

    @Changed.setter
    def Changed(self, handler):
        if not callable(handler):
            raise ValueError("'handler' must be callable.")

        self._handler = handler

    def Change(self, *args, **kwargs):
        """
        Calls to this method will cause the :py:attr:`Changed` event to trigger.

        It accepts a variable number of positional and keyword arguments which, along with
        this instance, are passed to the Changed handler.

        Examples
        --------
        ::

            MyWatcher.Change('newstate')    # handlers will be called at this point
        """
        if self._handler:
            self._handler(self, *args, **kwargs)


# Logging Implementations -----------------------------------------------------


class ProgramLogLogger:
    r"""Implements a logger that sends log records to the Program Log."""

    def Log(self, *recordobjs, sep=' ', severity='info'):
        """Print recordobjs to ProgramLog, separated by sep.

        Parameters
        ----------
        recordobjs: objects
            objects to print in the log. Each object is converted to a
            string prior to printing.
        sep: str
            the separator to add between each recordobj. Defaults to ' '.
        severity: str
            User defined indicator of attention suggested (e.g. 'error', 'info', 'warning').

        Example
        -------
        ::

            logger = ProgramLogLogger()
            msg = 'log record.'
            logger.Log('This is', 'a', msg)
        """
        msg = severity + ': ' + sep.join(str(obj) for obj in recordobjs)
        ProgramLog(msg, 'info')


class TcpServerLogger:
    r"""Implements a logger that sends log records to all clients connected to
    a TCP server.

    Parameters
    ----------
    IPPort: int
        IP port number of the listening service.
    Interface: str
        Defines the network interface on which to listen (``'Any'``, ``'LAN'``,
        or ``'AVLAN'``)
    end: str
        The terminator for each log record sent to clients. Defaults to '\\n'.

    Example
    -------
    ::

        logger = TcpServerLogger(5000)
        msg = 'log record.'
        logger.Log('This is', 'a', msg)
    """

    def __init__(self, IPPort, Interface='Any', end='\n'):
        self.end = end
        self.server = EthernetServerInterfaceEx(IPPort, Interface=Interface)
        self.server.StartListen()

    def Log(self, *recordobjs, sep=' ', severity='info'):
        """Sends recordobjs to all connected clients, separated by sep.

        Parameters
        ----------
        recordobjs: objects
            objects to send to clients. Each object is converted to a string
            prior to sending.
        sep: str
            the separator to add between each recordobj. Defaults to ' '.
        severity: str
            User defined indicator of attention suggested (e.g. 'error', 'info', 'warning').
        """
        msg = severity + ': ' + sep.join(str(obj) for obj in recordobjs) + self.end
        for client in self.server.Clients:
            client.Send(msg)

    @property
    def IPPort(self):
        r"""The server's listening port."""
        return self.server.IPPort

    @property
    def Interface(self):
        r"""The interface this logger is listening on for client connections."""
        return self.server.Interface


class TraceLogger:
    r"""Implements a logger that sends log records to Trace Messages."""

    def Log(self, *recordobjs, sep=' ', severity='info'):
        """Print recordobjs to Trace, separated by sep.

        Parameters
        ----------
        recordobjs: objects
            objects to print in the trace. Each object is converted to a
            string prior to printing.
        sep: str
            the separator to add between each recordobj. Defaults to ' '.
        severity: str
            User defined indicator of attention suggested (e.g. 'error', 'info', 'warning').

        Example
        -------
        ::

            logger = TraceLogger()
            msg = 'log record.'
            logger.Log('This is', 'a', msg)
        """
        print(severity + ': ' + sep.join(str(obj) for obj in recordobjs))
