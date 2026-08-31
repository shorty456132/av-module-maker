from .version import __version__

def event(Object, EventName):
    '''
    Decorate a function to be the handler of *Object* when *EventName*
    happens.

    The decorated function must have the exact signature as specified by the
    definition of *EventName*, which must appear in the *Object* class or
    one of its parent classes. Lists of objects and/or events can be passed in
    to apply the same handler to multiple events.

    :param Object: An object or list of objects whose class or one of its/their
        parent classes defines *EventName*
    :type Object: object or list of objects
    :param EventName: name of an event or list of events
    :type EventName: string or list of strings

    .. code-block:: python
        :linenos:

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

    .. note::
        * Only one handler can be assigned to a given event of a given object.
        * Last handler assigned will be called when event triggers.

    .. versionadded:: 2.4
        List of Objects and Events
    '''
    pass


def Platform():
    r'''Return the name of the running hardware platform. One of ``'Pro'`` or
    ``'Pro xi'``.
    '''
    pass


def Version():
    '''
    Return the ControlScript |platform| version string in the form of
    <major>.<minor>.<revision>
    '''
    return __version__
