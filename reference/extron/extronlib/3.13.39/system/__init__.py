'''This package contains Extron created tools for AV systems.'''

from .Clock import Clock
from .File import File, RFile
from .MESet import MESet
from .NetServices import Email, Ping, WakeOnLan
from .Timer import Timer
from .Wait import Wait


def GetSystemUpTime():
    '''
    :return: system up time in seconds
    :rtype: float
    '''
    pass

def GetCurrentTimezone():
    r'''
    :return: the current time zone of the primary controller
    :rtype: namedtuple

    The returned namedtuple contains three pieces of string data: the time zone
    ``id``, the time zone ``description``, and ``MSid`` which contains a
    Microsoft-compatible time zone identifier.

    .. versionadded:: 3.13
    '''
    pass

def GetTimezoneList():
    r'''
    :return: all time zones supported by the system
    :rtype: list of namedtuples

    Each item in the returned list is a namedtuple that contains three pieces
    of string data: the time zone ``id``, the time zone ``description``, and
    ``MSid`` which contains a Microsoft-compatible time zone identifier.

    .. versionadded:: 3.13

    .. code-block:: python

        for zone in GetTimezoneList():
            print(zone.id + ', ' + zone.description)
    '''
    pass

def GetUnverifiedContext():
    '''
    `Python 3.4.3
    <https://docs.python.org/3/whatsnew/3.4.html#pep-476-enabling-certificate-verification-by-default-for-stdlib-http-clients>`_
    changed the default behavior of the stdlib http clients.  They will now
    verify that "the server presents a certificate which is signed by  a CA in
    the platform trust store and whose hostname matches the hostname being
    requested by default".  This method returns an unverified context for use
    when a valid certificate is impossible.

    :return: unverified context object compatible with stdlib http clients.
    :rtype: `ssl.SSLContext <https://docs.python.org/3.5/library/ssl.html#ssl.SSLContext>`_

    .. code-block:: python

        import urllib.request
        from extronlib.system import GetUnverifiedContext

        # This disables all verification
        context = GetUnverifiedContext()

        urllib.request.urlopen("https://invalid-cert", context=context)

    .. warning:: This is a potential security risk.  It should only be used
        when a secure solution is impossible.  :py:attr:`GetSSLContext` should
        be used whenever possible.

    .. versionadded:: 3.4
    '''
    pass


def GetSSLContext(alias):
    '''
    Retrieve a Certificate Authority certificate from the Security Store and
    use it to create an SSL context usable with standard Python http clients.

    :param alias: name of the CA certificate as it appears in the Security
        Store.
    :type alias: string
    :return: an SSL context object compatible with stdlib http clients.
    :rtype: `ssl.SSLContext <https://docs.python.org/3.5/library/ssl.html#ssl.SSLContext>`_

    .. code-block:: python

        import urllib.request
        from extronlib.system import GetSSLContext

        context = GetSSLContext('yourcert')

        urllib.request.urlopen("https://www.example.com", context=context)

    .. versionadded:: 3.10
    '''
    pass


def ProgramLog(Entry, Severity='error'):
    '''
    Write entry to program log file.

    :param Entry: the message to enter into the log
    :type Entry: string
    :param Severity: indicates the severity to the log viewer.  (``'info'``,
        ``'warning'``, or ``'error'``)
    :type Severity: string

    .. note:: *ProgramLog* also generates a trace message.

    .. code-block:: python

        ProgramLog('Projector lamp hours > 3000.', 'warning')

    .. versionadded:: 2.4
    '''
    pass

def RestartSystem():
    '''
    Stops the main script running on the primary control processor only then
    starts it again.

    .. code-block:: python

        from extronlib.system import File, RestartSystem, SaveProgramLog
        from datetime import datetime

        # Save the ProgramLog for later inspection.
        dt = datetime.now()
        filename = 'ProgramLog {}.txt'.format(dt.strftime('%Y-%m-%d %H%M%S'))

        with File(filename, 'w') as f:
            SaveProgramLog(f)

        RestartSystem()

    .. versionadded:: 3.11
    '''
    pass

def SaveProgramLog(path=None):
    '''
    Save the ProgramLog to the specified User file system location.

    If no path is supplied, the Program Log will be saved in the root of the
    User file space with the name 'ProgramLog YYYY-MM-DD HHMMSS.txt' where
    'YYYY-MM-DD' will be replaced with the current date and 'HHMMSS' will be
    replaced with the current 24-hour time including seconds.

    If path points to a directory, the log will be saved in that directory
    using the file name pattern above.

    The file will be overwritten if it already exists.

    :param path: The file path to save the log to.
    :type path: :py:class:`~extronlib.system.File` or string

    .. versionadded:: 3.11
    '''
    pass

def SetAutomaticTime(Server):
    r'''
    Turn on NTP time synchronization using ``Server`` as the time source.

    :param Server: the NTP server to synchronize with
    :type Server: string

    .. versionadded:: 3.13

    .. code-block:: python

        SetAutomaticTime('time.example.com')
    '''
    pass

def SetManualTime(DateAndTime):
    r'''
    Change the system time. This will turn off NTP synchronization if it is on.

    :param DateAndTime: the new system date and time
    :type DateAndTime: datetime

    .. versionadded:: 3.13

    .. code-block:: python

        from datetime import datetime

        # Turn off NTP sync but keep the current system time.
        SetManualTime(datetime.now())

        # Set system time to noon on January 1, 2020
        dt = datetime(2020, 1, 1, 12, 0, 0)
        SetManualTime(dt)
    '''
    pass

def SetTimeZone(id):
    r'''
    Change the system time zone. Time zone affects Daylight Saving Time
    behavior and is used to calculate time of day when NTP time synchronization
    is turned on.

    :param id: The new system time zone identifier. Use an item returned by
        :py:attr:`GetTimezoneList` to get the time zone id for this parameter.
    :type id: string

    .. versionadded:: 3.13

    .. code-block:: python

        # Set the system time zone to 'Pacific'.
        for zone in GetTimezoneList():
            if 'Pacific' in zone.description:
                SetTimeZone(zone.id)
                break
    '''
    pass
