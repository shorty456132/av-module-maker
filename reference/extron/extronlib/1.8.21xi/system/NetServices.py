from typing import List, Optional, Tuple


class Email():

    """Class to send email using the configured mail settings. The configured
    settings can be over ridden during instantiation.

    Notes
    -----
    Default sender will be login username@unit-name or hostname@unit-name if
    there is no authentication. To override, call `Sender`.
    """

    def __init__(
        self,
        smtpServer: Optional[str]=None,
        port: Optional[int]=None,
        username: Optional[str]=None,
        password: Optional[str]=None,
        sslEnabled: Optional[bool]=None
    ):
        """
        Parameters
        ----------
        smtpServer : str
            IP Address or hostname of SMTP server
        port : int
            port number
        username : str
            login username for SMTP authentication
        password : str
            login password for SMTP authentication
        sslEnabled : bool
            Enable (True) or Disable (False) SSL for the connection

        Examples
        --------
        ::

            mail = Email(
                smtpServer='smtp.acme.com',
                port=25,
                username='avcontrol',
                password='some secret',
                sslEnabled=True
            )

            mail.Sender('avcontrol@acme.com')

            mail.Receiver(['system-support@acme.com'])
            mail.Receiver(['avcontrol@acme.com'], cc=True)

            mail.Subject('Test message')

            mail.SendMessage('''\\
            This is a test of the AV Alert system.  This is only a test.

            -AV Control
            ''')
        """
        pass

    def Receiver(
        self,
        receiver: Optional[List[str]]=None,
        cc: bool=False
    ) -> None:
        """Set receiver's email address(es) by passing in a list of strings.  It
        will appear in the **<To: receiver>** field of the email.  If cc is
        set to True, it will appear in the **<CC: receiver>** field of the email.

        Parameters
        ----------
        receiver : list of strs
            receiver's email address(es) (Default value = None)
        cc : bool
            Set ``True`` to put the receiver address(es) in the cc list
            (Default value = False)

        Notes
        -----
        ``Receiver()`` must be called each time the list changes.

        Examples
        --------
        ::

            recipients = ['abc@acme.com']
            mail.Receiver(recipients)
            ...
            recipients.append('xyz@acme.com')
            mail.Receiver(recipients)
        """
        pass

    def SendMessage(self, msg: str) -> None:
        """Create main body of the email and send out. Message string will be sent
        out as plain text.

        Parameters
        ----------
        msg : str
            message to send
        """
        pass

    def Sender(self, sender: str) -> None:
        """Set sender's email address. It will appear in the **<From: sender>**
        field of the email.

        Parameters
        ----------
        sender : str
            sender email address

        Notes
        -----
        Overrides default sender.
        """
        pass

    def Subject(self, subject: str) -> None:
        """Set email's subject. It will appear in the **<Subject: >** field of the
        email.

        Parameters
        ----------
        subject : str
            subject of the email
        """
        pass


def Ping(hostname: str='localhost', count: int=5) -> Tuple[int, int, float]:
    """Ping is a network administration utility that's used to test
    reachablilty of a remote network host. It achieves this by measuring the
    round-trip time of messages sent to and echoed back by the remote host.

    This function sends *count* pings from the control processor and and
    returns the result in a tuple: (# of successful pings, # of failed pings,
    avgerage round-trip time)

    Parameters
    ----------
    hostname : str
        IP address or hostname to ping. (Default value = 'localhost')
    count : int
        how many times to ping. (Default value = 5)

    Returns
    -------
    (int, int, float)
        tuple (# of successes, # of failures, average time)
    """
    return (int(), int(), float())


def WakeOnLan(macAddress: str, port: int=9) -> None:
    """Wake-on-LAN is a computer networking standard that allows a computer
    to be awakened by a network message.  The network message, 'Magic
    Packet', is sent out through UDP broadcast, port 9.

    Parameters
    ----------
    macAddress : str
        Target device's MAC address. The format is six
        groups of two hex digits, separated by hyphens
        (e.g. ``'01-23-45-67-ab-cd'``).
    port : int
        Port on which target device is listening. (Default value = 9)

    Notes
    -----
    Typical ports for WakeOnLan are 0, 7 and 9.
    """
    pass
