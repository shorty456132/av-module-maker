"""This package contains Extron created tools for AV systems."""

from datetime import datetime
from ssl import SSLContext
from typing import List, NamedTuple, Optional

from .Clock import Clock
from .File import File, RFile
from .MESet import MESet
from .NetServices import Email, Ping, WakeOnLan
from .Timer import Timer
from .Wait import Wait


class CurrentTimezone(NamedTuple):
    id: str
    description: str
    MSid: str

def GetSystemUpTime() -> float:
    """
    Returns
    -------
    float
        system up time in seconds
    """
    return float()

def GetCurrentTimezone() -> CurrentTimezone:
    """The returned namedtuple contains three pieces of string data: the time zone
    ``id``, the time zone ``description``, and ``MSid`` which contains a
    Microsoft-compatible time zone identifier.

    .. versionadded:: 1.1

    Returns
    -------
    namedtuple
        the current time zone of the primary controller
    """
    return CurrentTimezone(str(), str(), str())

def GetTimezoneList() -> List[CurrentTimezone]:
    """Each item in the returned list is a namedtuple that contains three pieces
    of string data: the time zone ``id``, the time zone ``description``, and
    ``MSid`` which contains a Microsoft-compatible time zone identifier.

    .. versionadded:: 1.1

    Returns
    -------
    list of namedtuples
        all time zones supported by the system

    Examples
    --------
    ::

        for zone in GetTimezoneList():
            print(zone.id + ', ' + zone.description)
    """
    return [CurrentTimezone(str(), str(), str())]

def GetUnverifiedContext() -> SSLContext:
    """`Python 3.4.3
    <https://docs.python.org/3/whatsnew/3.4.html#pep-476-enabling-certificate-verification-by-default-for-stdlib-http-clients>`_
    changed the default behavior of the stdlib http clients.  They will now
    verify that "the server presents a certificate which is signed by  a CA in
    the platform trust store and whose hostname matches the hostname being
    requested by default".  This method returns an unverified context for use
    when a valid certificate is impossible.

    Returns
    -------
    ssl.SSLContext
        unverified context object compatible with stdlib http clients
        (`ssl.SSLContext <https://docs.python.org/3.11/library/ssl.html#ssl.SSLContext>`_).

    Examples
    --------
    ::

        import urllib.request
        from extronlib.system import GetUnverifiedContext

        # This disables all verification
        context = GetUnverifiedContext()

        urllib.request.urlopen("https://invalid-cert", context=context)

    Warnings
    --------
    This is a potential security risk.  It should only be used when a secure
    solution is impossible.  `GetSSLContext` should be used whenever possible.
    """
    return SSLContext()


def GetSSLContext(alias: str) -> SSLContext:
    """Retrieve a Certificate Authority certificate from the Security Store and
    use it to create an SSL context usable with standard Python http clients.

    Parameters
    ----------
    alias : str
        name of the CA certificate as it appears in the Security
        Store.

    Returns
    -------
    ssl.SSLContext
        an SSL context object compatible with stdlib http clients
        (`ssl.SSLContext <https://docs.python.org/3.11/library/ssl.html#ssl.SSLContext>`_).

    Examples
    --------
    ::

        import urllib.request
        from extronlib.system import GetSSLContext

        context = GetSSLContext('yourcert')

        urllib.request.urlopen("https://www.example.com", context=context)
    """
    return SSLContext()


def ProgramLog(Entry: str, Severity: str='error') -> None:
    """Write an entry to program log file.

    Parameters
    ----------
    Entry : str
        the message to enter into the log
    Severity : str
        indicates the severity to the log viewer.  (``'info'``, ``'warning'``,
        or ``'error'``) (Default value = 'error')

    Notes
    ----
    *ProgramLog* also generates a trace message.

    Examples
    --------
    ::

        ProgramLog('Projector lamp hours > 3000.', 'warning')
    """
    pass

def RestartSystem() -> None:
    """Stops the main script running on the primary control processor only then
    starts it again.

    Examples
    --------
    ::

        from extronlib.system import File, RestartSystem, SaveProgramLog
        from datetime import datetime

        def ReloadSystem():
            \"\"\"Reload the system.  Call this method when needed.\"\"\"

            # Get/apply system settings as needed.
            ...

            # Save the ProgramLog for later inspection.
            dt = datetime.now()
            filename = 'ProgramLog {}.txt'.format(dt.strftime('%Y-%m-%d %H%M%S'))

            with File(filename, 'w') as f:
                SaveProgramLog(f)

        RestartSystem()
    """
    pass

def SaveProgramLog(path: Optional[File | str]=None) -> None:
    """Save the ProgramLog to the specified User file system location.

    If no path is supplied, the Program Log will be saved in the root of the
    User file space with the name ``'ProgramLog YYYY-MM-DD HHMMSS.txt'`` where
    ``'YYYY-MM-DD'`` will be replaced with the current date and ``'HHMMSS'``
    will be replaced with the current 24-hour time including seconds.

    If path points to a directory, the log will be saved in that directory
    using the file name pattern above.

    The file will be overwritten if it already exists.

    Parameters
    ----------
    path : File or str
        The file path to save the log to. (Default value = None)
    """
    pass

def SetAutomaticTime(Server: str | List[str]) -> None:
    """Turn on NTP time synchronization using **Server** as the time source.

    .. versionadded:: 1.1

    .. versionchanged:: 1.7
        Accepts multiple server names in a list.

    Parameters
    ----------
    Server : str, list of str
        the NTP server, or list of servers, to synchronize with

    Notes
    -----
    Any number of server names maybe passed in, but only the first three will
    be used.

    Examples
    --------
    ::

        SetAutomaticTime('time.example.com')

        SetAutomaticTime(['time0.example.org', 'time1.example.org'])
    """
    pass

def SetManualTime(DateAndTime: datetime) -> None:
    """Change the system time. This will turn off NTP synchronization if it is
    on.

    .. versionadded:: 1.1

    Parameters
    ----------
    DateAndTime : datetime
        the new system date and time

    Examples
    --------
    ::

        from datetime import datetime

        # Turn off NTP sync but keep the current system time.
        SetManualTime(datetime.now())

        # Set system time to noon on January 1, 2020
        dt = datetime(2020, 1, 1, 12, 0, 0)
        SetManualTime(dt)
    """
    pass

def SetTimeZone(id: str) -> None:
    """Change the system time zone. Time zone affects Daylight Saving Time
    behavior and is used to calculate time of day when NTP time synchronization
    is turned on.

    .. versionadded:: 1.1

    Parameters
    ----------
    id : str
        The new system time zone identifier. Use an item returned by
        `GetTimezoneList` to get the time zone id for this parameter.

    Examples
    --------
    ::

        # Set the system time zone to 'Pacific'.
        for zone in GetTimezoneList():
            if 'Pacific' in zone.description:
                SetTimeZone(zone.id)
                break
    """
    pass
