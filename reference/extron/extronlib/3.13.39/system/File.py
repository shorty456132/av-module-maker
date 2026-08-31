
class FileInterface():

    def close(self):
        '''Close an already opened file'''
        pass

    def read(self, size=-1):
        '''
        Read data from opened file

        :param size: max number of char/bytes to read
        :type size: int
        :return: data
        :rtype: bytes
        '''
        pass

    def readline(self):
        '''
        Read from opened file until newline or EOF occurs

        :returns: data
        :rtype: bytes
        '''
        pass

    def seek(self, offset, whence=0):
        '''
        Change the stream position

        :param offset: offset from the start of the file
        :type offset: int
        :param whence:
            * 0 = absolute file positioning
            * 1 = seek relative to the current position
            * 2 = seek relative to the file's end.
        :type whence: int

        .. note:: Files opened in text mode (i.e. not using ``'b'``), only
            seeks relative to the beginning of the file are allowed -- the
            exception being a seek to the very file end with seek(0,2).
        '''
        pass

    def tell(self):
        '''
        :return: the current cursor position
        :rtype: int
        '''
        pass

    def write(self, data):
        '''
        Write string or bytes to file

        :param data: data to be written to file
        :type data: string, bytes
        '''
        pass

    def writelines(self, seq):
        '''
        Write iterable object such as a list of strings

        :param seq: iterable sequence
        :type seq: e.g. list of strings
        '''
        pass

    @property
    def Filename(self):
        '''
        :return: name of file
        :rtype: string
        '''
        pass


class File(FileInterface):
    '''
    Access to files located in user area.  These files are stored in a
    location that can be accessed using 3rd party SFTP clients.

    .. note:: File class accesses user area with 'admin' privileges.
    '''

    def __init__(self, Filename, mode='r', encoding=None, newline=None):
        '''
        :param Filename: Name of file to open
        :type Filename: string
        :param mode: the mode in which the files is opened.
        :type mode: string
        :param encoding: the name of the encoding used to decode/encode the
            file.
        :type encoding: string
        :param newline: controls how universal newlines mode works
        :type newline: string

        .. note::
            * *mode*, *encoding*, and *newline* have the same meanings as
              those passed to the built-in function `open
              <https://docs.python.org/3.5/library/functions.html#open>`_
              (docs.python.org).
            * The default encoding is ``'ascii'``.  See the `Standard
              Encodings
              <https://docs.python.org/3.5/library/codecs.html#standard-encodings>`_
              (docs.python.org) for possible values.

        .. code-block:: python

            logFile = File('confRoom.log', 'a')
            ...
            logFile.write(message)
            ...
            logFile.close()

            with File('confRoom.log', 'r') as logFile:
                for line in logFile:
                    print(line)
                    ...

        .. versionadded:: 2.3
            Context manager (with) compatibility
        '''
        pass

    @classmethod
    def ChangeDir(cls, path):
        '''
        Change the current working directory to *path*

        :param path: path to directory
        :type path: string

        .. code-block:: python

            File.ChangeDir('/some/path')
        '''
        pass

    @classmethod
    def DeleteDir(cls, path):
        '''
        Remove a directory

        :param path: path to directory
        :type path: string

        .. code-block:: python

            File.DeleteDir('/some/path')
        '''
        pass

    @classmethod
    def DeleteFile(cls, filename):
        '''
        Delete a file

        :param filename: the name of the file to be deleted
        :type filename: string

        .. code-block:: python

            File.DeleteFile('/some/path/to/file')
        '''
        pass

    @classmethod
    def Exists(cls, path):
        '''
        Return True if path exists

        :param path: path to file or directory
        :type path: string
        :return: true if exists else false
        :rtype: bool

        .. code-block:: python

            if File.Exists('/some/path/to/file'):
                print('File exists')
            else:
                print('File does not exist')
        '''
        pass

    @classmethod
    def GetCurrentDir(cls):
        '''
        Get the current path.

        :return: the current working directory
        :rtype: string

        .. code-block:: python

            print(File.GetCurrentDir())
        '''
        pass

    @classmethod
    def ListDir(cls, path=None):
        '''
        List directory contents

        :param path: if provided, path to directory to list, else list current
            directory
        :type path: string
        :return: directory listing
        :rtype: list of strings

        .. code-block:: python

            print(File.ListDir('/some/path/'))
        '''
        pass

    @classmethod
    def MakeDir(cls, path):
        '''
        Make a new directory

        :param path: path to directory
        :type path: string

        .. code-block:: python

            File.MakeDir('/some/path/')
        '''
        pass

    @classmethod
    def RenameFile(cls, oldname, newname):
        '''
        Rename a file from *oldname* to *newname*

        :param oldname: the original filename
        :type oldname: string
        :param newname: the filename to rename to
        :type newname: string

        .. note:: If *newname* exists it will be replaced silently.

        .. code-block:: python

            File.RenameFile('usage.log', 'usage.log.bak')
        '''
        pass


class RFile(FileInterface):
    '''
    Access to restricted files. These files can only be created and accessed
    within the program.  Files can be uploaded to provide initial values via
    the Global Scripter® project.
    '''

    def __init__(self, Filename, mode='r', encoding=None, newline=None):
        '''
        :param Filename: Name of file to open
        :type Filename: string
        :param mode: the mode in which the files is opened.
        :type mode: string
        :param encoding: the name of the encoding used to decode/encode the
            file.
        :type encoding: string
        :param newline: controls how universal newlines mode works
        :type newline: string

        .. note::
            * *mode*, *encoding*, and *newline* have the same meanings as
              those passed to the built-in function `open
              <https://docs.python.org/3.5/library/functions.html#open>`_
              (docs.python.org).
            * The default encoding is ``'ascii'``.  See the `Standard
              Encodings
              <https://docs.python.org/3.5/library/codecs.html#standard-encodings>`_
              (docs.python.org) for possible values.

        .. code-block:: python

            logFile = RFile('confRoom.log', 'a')
            ...
            logFile.write(message)
            ...
            logFile.close()

            with RFile('confRoom.log', 'r') as logFile:
                for line in logFile:
                    print(line)
                    ...

        .. versionadded:: 2.3
            Context manager (with) compatibility
        '''
        pass

    @classmethod
    def ChangeDir(cls, path):
        '''
        Change the current working directory to *path*

        :param path: path to directory
        :type path: string

        .. code-block:: python

            RFile.ChangeDir('/some/path')
        '''
        pass

    @classmethod
    def DeleteDir(cls, path):
        '''
        Remove a directory

        :param path: path to directory
        :type path: string

        .. code-block:: python

            RFile.DeleteDir('/some/path')
        '''
        pass

    @classmethod
    def DeleteFile(cls, filename):
        '''
        Delete a file

        :param filename: the name of the file to be deleted
        :type filename: string

        .. code-block:: python

            RFile.DeleteFile('/some/path/to/file')
        '''
        pass

    @classmethod
    def Exists(cls, path):
        '''
        Return True if path exists

        :param path: path to file or directory
        :type path: string
        :return: true if exists else false
        :rtype: bool

        .. code-block:: python

            if RFile.Exists('/some/path/to/file'):
                print('File exists')
            else:
                print('File does not exist')
        '''
        pass

    @classmethod
    def GetCurrentDir(cls):
        '''
        Get the current path.

        :return: the current working directory
        :rtype: string

        .. code-block:: python

            print(RFile.GetCurrentDir())
        '''
        pass

    @classmethod
    def ListDir(cls, path=None):
        '''
        List directory contents

        :param path: if provided, path to directory to list, else list current
            directory
        :type path: string
        :return: directory listing
        :rtype: list of strings

        .. code-block:: python

            print(RFile.ListDir('/some/path/'))
        '''
        pass

    @classmethod
    def MakeDir(cls, path):
        '''
        Make a new directory

        :param path: path to directory
        :type path: string

        .. code-block:: python

            RFile.MakeDir('/some/path/')
        '''
        pass

    @classmethod
    def RenameFile(cls, oldname, newname):
        '''
        Rename a file from *oldname* to *newname*

        :param oldname: the original filename
        :type oldname: string
        :param newname: the filename to rename to
        :type newname: string

        .. note:: If *newname* exists it will be replaced silently.

        .. code-block:: python

            RFile.RenameFile('usage.log', 'usage.log.bak')
        '''
        pass
