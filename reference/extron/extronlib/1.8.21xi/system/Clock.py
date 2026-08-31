from datetime import datetime
from typing import Any, Callable, Dict, List, Optional


class Clock():
    """The clock is used to create timed events. It will allow the user to
    schedule programmed actions to occur based on calendar time.

    Notes
    -----
        * When DST causes the clock to spring forward one hour, events
          scheduled within the skipped hour do not fire.
        * When DST causes the clock to fall back an hour, events scheduled
          within the repeated hour fire twice.
    """

    def __init__(
        self,
        Times: List[str],
        Days: Optional[List[str]]=None,
        Function: Optional[Callable[['Clock', datetime], Any]]=None
    ):
        """
        Parameters
        ----------
        Times : list of strs
            list of times (e.g. ``'HH:MM:SS'``) of day to call `Function`
        Days : list of strs
            list of weekdays to set alarm. If Days is omitted, the alarm is
            set for every weekday
        Function : function
            function to execute when alarm time is up

        Examples
        --------
        ::

            def ShutdownSystems(clock, dt):
                print('Shutting down...')
                ...

            nightlyShutdown = Clock(['19:00:00'], None, ShutdownSystems)
            nightlyShutdown.Enable()
        """
        pass

    def Disable(self) -> None:
        """Disable alarm

        Examples
        --------
        ::

            nightlyShutdown.Disable()
        """
        pass

    def Enable(self) -> None:
        """Enable alarm

        Examples
        --------
        ::

            nightlyShutdown.Enable()
        """
        pass

    def SetDays(self, Days: List[str]) -> None:
        """Set new alarm days

        Parameters
        ----------
        Days : list of strs
            a list of Calendar days, as listed in `WEEKDAYS`

        Examples
        --------
        ::

            nightlyShutdown.SetDays(['Monday', 'Wednesday', 'Friday'])
        """
        pass

    def SetTimes(self, Times: List[str]) -> None:
        """Set new alarm times

        Parameters
        ----------
        Times : list of strs
            list of times (e.g. ``'HH:MM:SS'``) of day to call
            `Function`

        Examples
        --------
        ::

            nightlyShutdown.SetTimes(['20:00:00'])
        """
        pass

    @property
    def Days(self) -> List[str]:
        """The days the `Function` will be called.

        Returns
        -------
        list of strs

        Notes
        -----
        list will be empty if it was not provided to the constructor (i.e. the
        Clock is set for every day).
        """
        return [str()]

    @property
    def Function(self) -> Optional[Callable[['Clock', datetime], Any]]:
        """Code to execute at given Times.

        Returns
        -------
        function

        Notes
        -----
        Function must accept two parameters: the Clock object and datetime
        object.
        """
        pass

    @property
    def State(self) -> str:
        """State of the clock device (``'Enabled'``, ``'Disabled'``).

        Returns
        -------
        str
        """
        return str()

    @property
    def Times(self) -> List[str]:
        """Get the list of times to execute (``['12:29:00', ...]``).

        Returns
        -------
        list of strs
        """
        return [str()]

    @property
    def WEEKDAYS(self) -> Dict[str, int]:
        """Get the calendar weekdays dictionary.

        Returns
        -------
        dict

        Examples
        --------
        ::

            {
                'Monday': 0,
                'Tuesday': 1,
                'Wednesday': 2,
                'Thursday': 3,
                'Friday': 4,
                'Saturday': 5,
                'Sunday': 6
            }
        """
        WEEKDAYS = {
            'Monday': 0,
            'Tuesday': 1,
            'Wednesday': 2,
            'Thursday': 3,
            'Friday': 4,
            'Saturday': 5,
            'Sunday': 6
        }
        return WEEKDAYS
