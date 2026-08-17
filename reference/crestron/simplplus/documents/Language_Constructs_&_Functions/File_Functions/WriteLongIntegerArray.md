# WriteLongIntegerArray

Name:

WriteLongIntegerArray

Syntax:

SIGNED_INTEGER WriteLongIntegerArray ( INTEGER file_handle,

LONG_INTEGER ilArray[m][n] )

Description:

Writes the array to a file starting at the current file position. Two bytes are written, most significant first containing the row dimension of the array, then two more bytes are written, containing the column dimension of the array. Then each long integer is written as a four byte quantity, most significant byte first. The integers are stored in row-major order, e.g. all the elements of row 0 first, then the elements of row 1, etc. Note that there is one more row and one more column than the dimensions that are written, because there is a row 0 and a column 0. Refer to the section entitled “[Reading and Writing Data to a File](<Reading_and_Writing_Data_to_a_File.htm>)” for a discussion of when to use this function and when to use the related functions: [FileWrite](<FileWrite.htm>), [WriteInteger](<WriteInteger.htm>), [WriteString](<WriteString.htm>), [WriteStructure](<WriteStructure.htm>), [WriteSignedInteger](<WriteSignedInteger.htm>), [WriteLongInteger](<WriteLongInteger.htm>), [WriteSignedLongInteger](<WriteSignedLongInteger.htm>), [WriteIntegerArray](<WriteIntegerArray.htm>), [WriteSignedIntegerArray](<WriteSignedIntegerArray.htm>), [WriteSignedLongIntegerArray](<WriteSignedLongIntegerArray.htm>), [WriteStringArray](<WriteStringArray.htm>).

NOTE: Use [ReadLongIntegerArray](<ReadLongIntegerArray.htm>) to read this.

Parameters:

FILE_HANDLE specifies the file handle of the previously opened file (from [FileOpen](<FileOpen.htm>)).

ilArray is the array whose values are Write.

Return Value:

Number of bytes written to the file. If the return value is negative, it is an error code.

Example: 

(see [File Functions Overview](<File_Functions_Overview.htm>))

INTEGER nFileHandle, iErrorCode;

LONG_INTEGER ilArray[10];

StartFileOperations();

nFileHandle = FileOpen ( "\\\CF0\\\MyFile", _O_WRONLY );

IF (nFileHandle >= 0)

{

iErrorCode = WriteLongIntegerArray(nFileHandle, ilArray);

if (iErrorCode > 0)

PRINT ( “Array written to file correctly.\n");

else

PRINT ( “Error code %d\n", iErrorCode);

}

EndFileOperations();

Version:

X Generation: Not Supported

2-Series: SIMPL Version 2.03.18 and later

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/WriteLongIntegerArray.htm*
