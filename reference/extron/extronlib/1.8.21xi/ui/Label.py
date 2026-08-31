from ..device import UIDevice
from . import UIObject


class Label(UIObject):
    """Label object displays text string on the screen"""

    def SetText(self, text:str) -> None:
        """Specify text to display on the UIObject

        Parameters
        ----------
        text : str
            text to display
        """
        pass

    def SetVisible(self, visible:bool) -> None:
        """Change the visibility of a UI control object.

        Parameters
        ----------
        visible : bool
            ``True`` to make the object visible or ``False`` to hide it.
        """
        pass

    @property
    def Host(self) -> UIDevice:
        """Handle to the `UIDevice` that hosts this UI object.

        Returns
        -------
        UIDevice
        """
        return UIDevice('')

    @property
    def Name(self) -> str:
        """The object Name

        Returns
        -------
        str
        """
        return str()

    @property
    def Visible(self) -> bool:
        """The current visibility state. ``True`` if the control object is
        visible else ``False``.

        Returns
        -------
        bool
        """
        return bool()
