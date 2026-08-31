"""
This package defines classes for user interactive controls.

Notes
-----
UI control object's states are retained and will be recovered in case the
endpoints lose connection to the primary control processor.
"""

from ..device import UIDevice, eBUSDevice


class UIObject():

    def __init__(
        self,
        UIHost: eBUSDevice | UIDevice,
        ID: int | str
    ):
        """
        Parameters
        ----------
        UIHost : eBUSDevice, UIDevice
            Device object hosting this UIObject
        ID : int, string
            ID or Name of the UIObject
        """
        pass

    @property
    def Host(self) -> eBUSDevice | UIDevice:
        """Handle to the ``extronlib.device`` that hosts this UI object.

        Returns
        -------
        eBUSDevice, UIDevice
        """
        return UIDevice('')

    @property
    def ID(self) -> int:
        """The object ID as defined in the UI Layout file.

        Returns
        -------
        int
        """
        return int()

from .Button import Button
from .Knob import Knob
from .Label import Label
from .Level import Level
from .Slider import Slider
