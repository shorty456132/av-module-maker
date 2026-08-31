from typing import Any, Callable, Optional

from ..device import UIDevice, eBUSDevice
from . import UIObject


class Knob(UIObject):

    def __init__(
        self,
        UIHost: UIDevice | eBUSDevice,
        ID: int
    ):
        """Knob is a rotary control that has 36 steps for a full revolution.

        Parameters
        ----------
        UIHost : UIDevice, eBUSDevice
            Device object hosting this UIObject
        ID : int
            ID of the UIObject
        """
        pass

    @property
    def Turned(self) -> Optional[Callable[['Knob', int], Any]]:
        """``Event``: Assign or retrieve the handler for the `Turned` event
        that triggers when the knob is turned.

        The assigned handler must accept exactly two positional arguments. The
        first one is the `Knob` instance triggering the event and the second
        one is a signed integer indicating steps that the knob was turned.
        Positive values indicate clockwise rotation.

        Returns
        -------
        Callable, None
            The assigned handler for the `Turned` event or `None` if no
            handler has been assigned.

        Examples
        --------
        ::

            @event(mainKnob, 'Turned')
            def handleMainKnob(knob, direction):
                if direction > 0:
                    for i in range(direction):
                        mainProjector.Send('VOLUME UP')
                else:
                    for i in range(direction, 0):
                        mainProjector.Send('VOLUME DOWN')
        """
        pass

    @Turned.setter
    def Turned(
        self,
        handler: Optional[Callable[['Knob', int], Any]]
    ) -> None:
        pass
