from typing import Iterable, List, Optional


class FileInterface():

    def __enter__(self):
        return self

    def __exit__(self, *exc) -> bool:
        return False

    def close(self) -> None:
        """Close an already opened file"""
        pass

    def read(self, size: int=-1) -> bytes:
        """Read data from opened file.

        Parameters
        ----------
        size : int
            max number of char/bytes to read (Default value = -1)

        Returns
        -------
        bytes
            data
        """
        return bytes()

    def readline(self) -> bytes:
        """Read from opened file until newline or EOF occurs.

        Returns
        -------
        bytes
            data
        """
        return bytes()

    def seek(self, offset: int, whence: int=0) -> None:
        """Change the stream position.

        Parameters
        ----------
        offset : int
            offset from the start of the file
        whence : int
            * 0 = absolute file positioning
            * 1 = seek relative to the current position
            * 2 = seek relative to the file's end.

            (Default value = 0)

        Notes
        -----
        Files opened in text mode (i.e. not using ``'b'``), only seeks relative to
        the beginning of the file are allowed -- the exception being a seek to the
        very file end with seek(0,2).
        """
        pass

    def tell(self) -> int:
        """The current cursor position.

        Returns
        -------
        int
            cursor position
        """
        return int()

    def write(self, data: str | bytes) -> None:
        """Write string or bytes to file.

        Parameters
        ----------
        data : str, bytes
            data to be written to file
        """
        pass

    def writelines(self, seq: Iterable[str | bytes]) -> None:
        """Write iterable object such as a list of strings

        Parameters
        ----------
        seq : list of strs
            iterable sequence
        """
        pass

    @property
    def Filename(self) -> str:
        """The name of the file

        Returns
        -------
        str
        """
        return str()


class File(FileInterface):
    """Access to files located in user area.  These files are stored in a
    location that can be accessed using 3rd party SFTP clients.

    Notes
    -----
    File class accesses user area with 'admin' privileges.
    """

    def __init__(
        self,
        Filename: str,
        mode: str='r',
        encoding: Optional[str]=None,
        newline: Optional[str]=None
    ):
        """
        Parameters
        ----------
        Filename : str
            Name of file to open
        mode : str
            the mode in which the files is opened.
        encoding : str
            the name of the encoding used to decode/encode the file.
        newline : str
            controls how universal newlines mode works

        Notes
        -----
        * *mode*, *encoding*, and *newline* have the same meanings as those
          passed to the built-in function `open
          <https://docs.python.org/3.11/library/functions.html#open>`_
          (docs.python.org).
        * The default encoding is ``'ascii'``.  See the
          `Standard Encodings <https://docs.python.org/3.11/library/codecs.html#standard-encodings>`_
          (docs.python.org) for possible values.

        Examples
        --------
        ::

            logFile = File('confRoom.log', 'a')
            ...
            logFile.write(message)
            ...
            logFile.close()

            with File('confRoom.log', 'r') as logFile:
                for line in logFile:
                    print(line)
                    ...
        """
        pass

    @classmethod
    def ChangeDir(cls, path: str) -> None:
        """Change the current working directory to *path*

        Parameters
        ----------
        path : str
            path to directory

        Examples
        --------
        ::

            File.ChangeDir('/some/path')
        """
        pass

    @classmethod
    def DeleteDir(cls, path: str) -> None:
        """Remove a directory

        Parameters
        ----------
        path : str
            path to directory

        Examples
        --------
        ::

            File.DeleteDir('/some/path')
        """
        pass

    @classmethod
    def DeleteFile(cls, filename: str) -> None:
        """Delete a file

        Parameters
        ----------
        filename : str
            the name of the file to be deleted

        Examples
        --------
        ::

            File.DeleteFile('/some/path/to/file')
        """
        pass

    @classmethod
    def Exists(cls, path: str) -> bool:
        """Return True if path exists

        Parameters
        ----------
        path : str
            path to file or directory

        Returns
        -------
        bool
            true if exists else false

        Examples
        --------
        ::

            if File.Exists('/some/path/to/file'):
                print('File exists')
            else:
                print('File does not exist')
        """
        return bool()

    @classmethod
    def GetCurrentDir(cls) -> str:
        """Get the current path.
        Returns
        -------
        str
            the current working directory

        Examples
        --------
        ::

            print(File.GetCurrentDir())
        """
        return str()

    @classmethod
    def ListDir(cls, path: Optional[str]=None) -> List[str]:
        """List directory contents

        Parameters
        ----------
        path : str
            if provided, path to directory to list, else list current
            directory (Default value = None)

        Returns
        -------
        list of str
            directory listing

        Examples
        --------
        ::

            print(File.ListDir('/some/path/'))
        """
        return [str()]

    @classmethod
    def MakeDir(cls, path: str) -> None:
        """Make a new directory

        Parameters
        ----------
        path : str
            path to directory

        Examples
        --------
        ::

            File.MakeDir('/some/path/')
        """
        pass

    @classmethod
    def RenameFile(cls, oldname: str, newname: str) -> None:
        """Rename a file from *oldname* to *newname*

        Parameters
        ----------
        oldname : str
            the original filename
        newname : str
            the filename to rename to

        Notes
        -----
        If *newname* exists it will be replaced silently.

        Examples
        --------
        ::

            File.RenameFile('usage.log', 'usage.log.bak')
        """
        pass


class RFile(FileInterface):
    """Access to restricted files. These files can only be created and accessed
    within the program.  Files can be uploaded to provide initial values via
    the Global Scripter® project.
    """

    def __init__(
        self,
        Filename: str,
        mode: str='r',
        encoding: Optional[str]=None,
        newline: Optional[str]=None
    ):
        """
        Parameters
        ----------
        Filename : str
            Name of file to open
        mode : str
            the mode in which the files is opened.
        encoding : str
            the name of the encoding used to decode/encode the file.
        newline : str
            controls how universal newlines mode works

        Notes
        -----
        * *mode*, *encoding*, and *newline* have the same meanings as those
          passed to the built-in function `open
          <https://docs.python.org/3.11/library/functions.html#open>`_
          (docs.python.org).
        * The default encoding is ``'ascii'``.  See the
          `Standard Encodings <https://docs.python.org/3.11/library/codecs.html#standard-encodings>`_
          (docs.python.org) for possible values.

        Examples
        --------
        ::

            logFile = RFile('confRoom.log', 'a')
            ...
            logFile.write(message)
            ...
            logFile.close()

            with RFile('confRoom.log', 'r') as logFile:
                for line in logFile:
                    print(line)
                    ...
        """
        pass

    @classmethod
    def ChangeDir(cls, path: str) -> None:
        """Change the current working directory to *path*

        Parameters
        ----------
        path : str
            path to directory

        Examples
        --------
        ::

            RFile.ChangeDir('/some/path')
        """
        pass

    @classmethod
    def DeleteDir(cls, path: str) -> None:
        """Remove a directory

        Parameters
        ----------
        path : str
            path to directory

        Examples
        --------
        ::

            RFile.DeleteDir('/some/path')
        """
        pass

    @classmethod
    def DeleteFile(cls, filename: str) -> None:
        """Delete a file

        Parameters
        ----------
        filename : str
            the name of the file to be deleted

        Examples
        --------
        ::

            RFile.DeleteFile('/some/path/to/file')
        """
        pass

    @classmethod
    def Exists(cls, path: str) -> bool:
        """Return True if path exists

        Parameters
        ----------
        path : str
            path to file or directory

        Returns
        -------
        bool
            true if exists else false

        Examples
        --------
        ::

            if RFile.Exists('/some/path/to/file'):
                print('File exists')
            else:
                print('File does not exist')
        """
        return bool()

    @classmethod
    def GetCurrentDir(cls) -> str:
        """Get the current path.
        Returns
        -------
        str
            the current working directory

        Examples
        --------
        ::

            print(RFile.GetCurrentDir())
        """
        return str()

    @classmethod
    def ListDir(cls, path: Optional[str]=None) -> List[str]:
        """List directory contents

        Parameters
        ----------
        path : str
            if provided, path to directory to list, else list current
            directory (Default value = None)

        Returns
        -------
        list of str
            directory listing

        Examples
        --------
        ::

            print(RFile.ListDir('/some/path/'))
        """
        return [str()]

    @classmethod
    def MakeDir(cls, path: str) -> None:
        """Make a new directory

        Parameters
        ----------
        path : str
            path to directory

        Examples
        --------
        ::

            RFile.MakeDir('/some/path/')
        """
        pass

    @classmethod
    def RenameFile(cls, oldname: str, newname: str) -> None:
        """Rename a file from *oldname* to *newname*

        Parameters
        ----------
        oldname : str
            the original filename
        newname : str
            the filename to rename to

        Notes
        -----
        If *newname* exists it will be replaced silently.

        Examples
        --------
        ::

            RFile.RenameFile('usage.log', 'usage.log.bak')
        """
        pass
