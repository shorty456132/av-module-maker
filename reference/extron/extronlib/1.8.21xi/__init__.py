from typing import Any, Callable, List

from .version import __version__


def event(Object: Any | List[Any], EventName: str | List[str]) -> Callable:
    """Decorate a function to be the handler of *Object* when *EventName*
    happens.

    The decorated function must have the exact signature as specified by the
    definition of *EventName*, which must appear in the *Object* class or
    one of its parent classes. Lists of objects and/or events can be passed in
    to apply the same handler to multiple events.

    Parameters
    ----------
    Object : object or list of objects
        An object or list of objects whose class or one of its/their
        parent classes defines *EventName*
    EventName : str or list of strs
        name of an event or list of events

    Returns
    -------
    callable
        decorated function

    Examples
    --------
    ::

        # Define an event handler
        @event(SomeObject, 'EventName')
        def HandlerFunction(actor, eventname):
            if actor is SomeObject and eventname == 'EventName':
                DoSomething()

        # Assign a handler to multiple events
        @event([ObjectA, ObjectB], ['EventOne', 'EventTwo'])
        @event(ObjectC, ['EventThree', 'EventFour'])
        @event([ObjectD, ObjectE], 'EventOne')
        def HandlerFunction(actor, eventname):
            if actor is ObjectA and eventname == 'EventOne':
                DoSomething()
            else:
                DoSomethingElse()


    Notes
    -----
    * Only one handler can be assigned to a given event of a given object.
    * Last handler assigned will be called when event triggers.
    """
    def _():
        pass

    return _


def Platform() -> str:
    """Get the name of the running hardware platform. One of ``'Pro'`` or
    ``'Pro xi'``.

    Returns
    -------
    str
    """
    return 'Pro xi'


def Version() -> str:
    """Get the ControlScript Pro xi version string in the form of
    ``'<major>.<minor>.<revision>'``.

    Returns
    -------
    str
    """
    return __version__
