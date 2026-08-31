from typing import Callable, Optional


class Wait():
    """The wait class allows the user to execute programmed actions after a
    desired delay without blocking other processor activity.

    Examples
    --------
    ::

        @event(PowerOn, 'Pressed')
        def HandlePowerButton(button, state):
            mainProjector.Send('Power=On\\r')
            @Wait(30)
            def CheckPowerState():
                mainProjector.Send('get Power\\r')
    """

    def __init__(
        self,
        Time: float | int,
        Function: Optional[Callable]=None
    ):
        """In addition to being used as a one-shot (decorator), *Wait* can be
        named and reusable.

        Parameters
        ----------
        Time : float
            Expiration time of the wait in seconds
        Function : function
            Code to execute when Time expires

        Examples
        --------
        ::

            closeWait = None    # Delay to hide Setup Page

            @event(ShowSetup, 'Released')
            def handleShowSetup(button, state):
                global closeWait
                def CloseSetupPage():
                    ConfRoomWall.ShowPage('Main')
                closeWait = Wait(60, CloseSetupPage)
                ConfRoomWall.ShowPage('Setup')
        """
        pass

    def __call__(self, Function: Callable) -> Callable:
        return Function

    def Add(self, Time: float | int) -> None:
        """Add time to current interval.

        Notes
        -----
        Add() does not modify `Time`.

        Parameters
        ----------
        Time : float
            Time in seconds

        Examples
        --------
        ::

            QueryDelay = Wait(3)

            def ErrorRecieved():    # Called by received data handler
                QueryDelay.Add(1)
        """
        pass

    def Cancel(self) -> None:
        """Stop *Function* from executing when the *Time* expires.

        Examples
        --------
        ::

            @event(CloseSetup, 'Released')
            def CloseSetup(button, state):
                global closeWait
                if closeWait:
                    closeWait.Cancel()
                    closeWait = None
                ConfRoomWall.ShowPage('Main')
        """
        pass

    def Change(self, Time: float | int) -> None:
        """Set a new *Time* value for current and subsequent runs of this
        instance.

        Notes
        -----
        Change() will modify `Time`.

        Parameters
        ----------
        Time : float
            Time in seconds

        Examples
        --------
        ::

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                closeWait.Change(60)
        """
        pass

    def Restart(self) -> None:
        """Restarts the *Wait* (i.e. executes the *Function* in *Time* seconds).
        If the *Wait* is active, Restart() cancels that *Wait* before starting
        a new one.

        Examples
        --------
        ::

            @event(buttonObject, 'Pressed')
            def buttonObjectHandler(button, state):
                DoSomething()
                closeWait.Restart()
        """
        pass

    @property
    def Function(self) -> Optional[Callable]:
        """Code to execute when *Time* expires.

        Returns
        -------
        function
        """
        pass

    @property
    def Time(self) -> float | int:
        """Expiration time of the *Wait* in seconds with 10ms precision.

        Returns
        -------
        float
        """
        return float()
