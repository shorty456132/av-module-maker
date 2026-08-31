from . import UIObject


class Label(UIObject):
    '''Label object displays text string on the screen'''

    def SetText(self, text):
        '''
        Specify text to display on the UIObject

        :param text: text to display
        :type text: string
        :raises: ``TypeError``

        .. code-block:: python

            roomMode.SetText('Combined')
        '''
        pass

    def SetVisible(self, visible):
        '''
        Change the visibility of a UI control object.

        :param visible: ``True`` to make the object visible or ``False`` to
            hide it.
        :type visible: bool
        '''
        pass

    @property
    def Name(self):
        '''
        :return: the object Name
        :rtype: string
        '''
        pass

    @property
    def Visible(self):
        '''
        :return: ``True`` if the control object is visible else ``False``
        :rtype: bool
        '''
        pass
