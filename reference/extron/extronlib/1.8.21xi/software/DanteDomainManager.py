from typing import Optional, Tuple


class DanteDomainManager():
    def __init__(
        self,
        Hostname: str,
        Credentials: Optional[Tuple[str, str]]=None
    ):
        """This class provides a re-usable Dante Domain Manager definition that
        can be supplied to a `DanteInterface`.

        .. versionadded:: 1.2

        Parameters
        ----------
        Hostname : str
            IP address or DNS Hostname of the Dante Domain
            Manager.
        Credentials : tuple
            Username and password for connection.

        Examples
        --------
        ::

            from extronlib.interface import DanteInterface
            from extronlib.software import DanteDomainManager

            # Always required once per project
            DanteInterface.StartService()

            DomainManager = DanteDomainManager(manager_hostname, ('username',
                                                                  'password'))

            axi22at = DanteInterface('AXI22-AB-CD-EF',
                                     DanteDomainManager=DomainManager,
                                     Domain='Auditorium')
            axi22at.Connect()
        """
        pass

    @property
    def Credentials(self) -> Optional[Tuple[str, str]]:
        """Username and password for the connection
        ('<username>', '<password>').

        Returns
        -------
        tuple, None

        Notes
        -----
        Will return ``None`` if credentials are not provided.
        """
        pass

    @property
    def Hostname(self) -> str:
        """Dante Domain Manager server Host name or IP address.

        Returns
        -------
        str
        """
        return str()
