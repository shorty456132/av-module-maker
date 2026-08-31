class Email():

    '''
    Class to send email using the configured mail settings. The configured
    settings can be over ridden during instantiation.

    .. note:: default sender will be login username@unit-name or
        hostname@unit-name if there is no authentication. To override, call
        :py:meth:`Sender`
    '''

    def __init__(self, smtpServer=None, port=None, username=None, password=None, sslEnabled=None):
        '''
        :param smtpServer: ip address or hostname of SMTP server
        :type smtpServer: string
        :param port: port number
        :type port: int
        :param username: login username for SMTP authentication
        :type username: string
        :param password: login password for SMTP authentication
        :type password: string
        :param sslEnabled: Enable (True) or Disable (False) SSL for the
            connection
        :type sslEnabled: bool

        .. code-block:: python
            :linenos:

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

            mail.SendMessage("""\\
            This is a test of the AV Alert system.  This is only a test.

            -AV Control
            """)
        '''
        pass

    def Receiver(self, receiver=None, cc=False):
        '''
        Set receiver’s email address(es) by passing in a list of strings.  It
        will appear in the **<To: receiver>** field of the email.  If cc is
        set to True, it will appear in the **<CC: receiver>** field of the email.

        :param receiver: receiver’s email address(es)
        :type receiver: list of strings
        :param cc: Set ``True`` to put the receiver address(es) in the cc list
        :type cc: bool

        .. note:: ``Receiver()`` must be called each time the list changes.

        .. code-block:: python

            recipients = ['abc@acme.com']
            mail.Receiver(recipients)
            ...
            recipients.append('xyz@acme.com')
            mail.Receiver(recipients)
        '''
        pass

    def SendMessage(self, msg):
        '''
        Create main body of the email and send out. Message string will be sent
        out as plain text.

        :param msg: message to send
        :type msg: string
        '''
        pass

    def Sender(self, sender):
        '''
        Set sender’s email address. It will appear in the **<From: sender>**
        field of the email.

        :param sender: sender email address
        :type sender: string

        .. note:: Overrides default sender.
        '''
        pass

    def Subject(self, subject):
        '''
        Set email’s subject. It will appear in the **<Subject: >** field of the
        email.

        :param subject: subject of the email
        :type subject: string
        '''
        pass


def Ping(hostname='localhost', count=5):
    '''
    Ping is a network administration utility that's used to test reachablilty
    of a remote network host. It achieves this by measuring the round-trip time
    of messages sent to and echoed back by the remote host.

    This function sends *count* pings from the control processor and and
    returns the result in a tuple: (# of successful pings, # of failed pings,
    avg. round-trip time)

    :param hostname: IP address or hostname to ping.
    :type hostname: string
    :param count: how many times to ping.
    :type count: int
    :returns: tuple (# of successes, # of failures, avg. time)
    :rtype: (int, int, float)

    .. versionadded:: 2.3
    '''
    pass


def WakeOnLan(macAddress, port=9):
    '''
    Wake-on-LAN is an computer networking standard that allows a computer
    to be awakened by a network message.  The network message, 'Magic
    Packet', is sent out through UDP broadcast, port 9.

    :param macAddress: Target device's MAC address. The format is six
        groups of two hex digits, separated by hyphens
        (``'01-23-45-67-ab-cd'``, e.g.).
    :type macAddress: string
    :param port: Port on which target device is listening.
    :type port: int

    .. note:: Typical ports for WakeOnLan are 0, 7 and 9.

    .. versionadded:: 3.1
        port parameter.
    '''
    pass
