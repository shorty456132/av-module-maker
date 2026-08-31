from typing import Any, Callable, Optional

from ..device import SPDevice
from . import Interface


class TemperatureInterface(Interface):
    """
    This class will provide a common interface for collecting data from
    Temperature ports on Extron devices (`extronlib.device`). The user can
    instantiate the class directly or create a subclass to add, remove, or
    alter behavior for different types of devices.

    .. versionadded:: 1.6
    """

    def __init__(
        self,
        Host: SPDevice,
        Port: str,
        LimitThreshold: float=24.0,
        OverThreshold: float=30.0
    ):
        """
        Parameters
        ----------
        Host : SPDevice
            handle to Extron device class that instantiated this interface
            class
        Port : str
            port name (e.g. ``'TCI1'``)
        LimitThreshold : float
            Temperature, in degrees Celsius, that defines the boundary between
            Normal and Limit Temperature States. Valid values are in the range
            of -50.0 to 105.0 but must be lower than the OverThreshold.
            Defaults to 24.0.
        OverThreshold : float
            Temperature, in degrees Celsius, that defines the boundary between
            Limit and Over Temperature States. Valid values are in the range
            of -50.0 to 105.0 but must be higher than the LimitThreshold.
            Defaults to 30.0.

        Raises
        ------
        ValueError
            When LimitThreshold is higher than the OverThreshold, either
            threshold is outside the bounds of -50.0 to 105.0 degrees Celsius,
            or there is less than 0.1 degree of separation between the
            thresholds.
        """
        pass

    def Initialize(
        self,
        LimitThreshold: Optional[float]=None,
        OverThreshold: Optional[float]=None
    ) -> None:
        """Initializes Temperature port to given values. User may provide any
        or all of the parameters.  ``None`` leaves property unmodified. See
        the constructor for valid parameter values.

        Parameters
        ----------
        LimitThreshold : float
            Temperature, in degrees Celsius, that defines the boundary between
            Normal and Limit Temperature States. (Default value = None)
        OverThreshold : float
            Temperature, in degrees Celsius, that defines the boundary between
            Limit and Over Temperature States. (Default value = None)

        Raises
        ------
        ValueError
            When LimitThreshold is higher than the OverThreshold, either
            threshold is outside the bounds of -50.0 to 105.0 degrees Celsius,
            or there is less than 0.1 degree of separation between the
            thresholds.
        """
        pass

    @property
    def Host(self) -> SPDevice:
        """Get the host device

        Returns
        -------
        SPDevice
        """
        return SPDevice('')

    @property
    def LimitThreshold(self) -> float:
        """Get the current temperature boundary between Normal and Limit.

        Returns
        -------
        float
        """
        return float()

    @property
    def OverThreshold(self) -> float:
        """Get the current temperature boundary between Limit and Over.

        Returns
        -------
        float
        """
        return float()

    @property
    def Port(self) -> str:
        """Get the port name this interface is attached to.

        Returns
        -------
        str
        """
        return str()

    @property
    def Temperature(self) -> float:
        """Get the current temperature value in degrees Celsius.

        Returns
        -------
        float

        Examples
        --------
        ::

            print(RackTempSensor.Temperature)
        """
        return float()

    @property
    def TemperatureChanged(
        self
    ) -> Optional[Callable[['TemperatureInterface', float], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `TemperatureChanged` event that triggers when the temperature reading
        changes.

        The assigned handler must accept two positional arguments. The first
        is the `TemperatureInterface` instance triggering the event and the
        second is the new temperature reading as a float.

        Returns
        -------
        Callable, None
            The assigned handler for the `TemperatureChanged` event or `None`
            if no handler has been assigned.

        Notes
        -----
        * This event triggers for each 1 degree change but no more than once
          every 10 seconds.
        * Use this event to display temperature on a user interface.

        Examples
        --------
        ::

            @event(RackTempSensor, 'TemperatureChanged')
            def HandleTemperatureChanged(sensor, temp):
                degreesF = temp * 9/5 + 32
                print('Rack temperature is %s degrees Fahrenheit.' % degreesF)
        """
        pass

    @TemperatureChanged.setter
    def TemperatureChanged(
        self,
        handler: Optional[Callable[['TemperatureInterface', float], Any]]
    ) -> None:
        pass

    @property
    def TemperatureState(self) -> str:
        """Get the current state of the temperature.

        Returns
        -------
        str
            One of ``'Normal'``, ``'Limit'``, ``'Over'``, or
            ``'Probe Error'``.
        """
        return str()

    @property
    def TemperatureStateChanged(
        self
    ) -> Optional[Callable[['TemperatureInterface', str], Any]]:
        """``Event``: Assign or retrieve the handler for the
        `TemperatureStateChanged` event that triggers when Temperature State
        changes.

        The assigned handler must accept two positional arguments. The first
        is the `TemperatureInterface` instance triggering the event and the
        second is the new Temperature State.

        Returns
        -------
        Callable, None
            The assigned handler for the `TemperatureStateChanged` event or
            `None` if no handler has been assigned.

        Notes
        -----
        Use this event to react quickly to abnormal temperatures.

        Examples
        --------
        ::

            @event(RackTempSensor, 'TemperatureStateChanged')
            def HandleTemperatureStateChanged(sensor, state):
                if state == 'Normal':
                    ... Normal state actions
                elif state == 'Limit':
                    ... Limit state actions
                elif state == 'Over':
                    ... Over state actions
                elif 'Error' in state:
                    ... Error state actions
        """
        pass

    @TemperatureStateChanged.setter
    def TemperatureStateChanged(
        self,
        handler: Optional[Callable[['TemperatureInterface', str], Any]]
    ) -> None:
        pass
