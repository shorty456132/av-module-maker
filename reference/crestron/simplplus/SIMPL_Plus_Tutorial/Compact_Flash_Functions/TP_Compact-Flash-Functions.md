# Compact Flash Functions  
  
The 2‑series and newer control systems support reading and wiritng to and from compact flash cards and other storage mediums.

Data storage is a valuable, powerful and important part of programming. The ability to store and retrieve data from a removable data source can provide many useful and powerful solutions. Some of these solutions include the ability to backup data, transferring data from one control system to another, reading and writing data to and from formats that other database programs can recognize, and implementing database‑driven programs (the ability for a program to act dynamically based on actions defined in the database).

The SIMPL+ file functions perform file access with the control system’s compact flash card. Because of the overhead involved with maintaining current directory and file positions, there are restrictions on file I/O. Each SIMPL+ thread (main loop or event handler) that requires file operations must first identify itself with the operating system. This is done with the function, `StartFileOperations`. Before terminating the thread, the function, `EndFileOperations` must be called. Files cannot be opened across threads. In other words, you cannot open a file in one thread, such as `Function Main`, and then access the file with the returned file handle in another thread, such as an event handler. Files should be opened, accessed and closed within the same thread.

## CheckForDisk and WaitForNewDisk

Before accessing compact flash, the program must either first check to see if a compact flash card exists within the control system, or wait for a card to be inserted.

Certain programs might rely on the compact flash card being inserted within the control system. The function in the example below, `CheckForDisk`, will test for the existence of a compact flash card within the control system. The function will return an error code and the program can act accordingly.

Other programs might prompt the end‑user to insert a compact flash card. The function in the example below, `WaitForNewDisk`, will halt the program and resume when a compact flash card is detected within the control system.

The following is an example of a program that needs to read data from a compact flash card upon startup:

FUNCTION ReadMyCompactFlashCard()  
{  
// call functions to read the compact flash card  
//  
// Note that this function will exist within the same  
// thread as the calling function (Function Main).  
// Because of this, the functions, StartFileOperations  
// and EndFileOperations should not be used here.}

Function Main()  
{  
StartFileOperations();

if (CheckForDisk() = 1)  
Call ReadMyCompactFlashCard();  
else if ( WaitForNewDisk() = 0 )  
Call ReadMyCompactFlashCard();

EndFileOperations(); }

If the program is dependent upon data that read in from the compact flash card, it is imperative for the program to validate the existence of the card. Otherwise, the program will not have the necessary data needed to execute properly. The above function will first check if the compact flash card is already inserted into the control system upon system startup. If so, it will call the user‑defined function, `ReadMyCompactFlashCard`, to perform any file read operations on the compact flash card. If the compact flash card was not found in the control system, the program will wait for the card to be inserted before continuing. Once inserted, the same function, `ReadMyCompactFlashCard`, is called.

### Reading and Writing Data

Once the existence of the compact flash card is verified, the reading and writing of data can be performed. Data can be read or written either with individual elements (i.e., a single integer or string), or with entire structures of data.

Because each datatype (i.e.: `INTEGER`, `STRING`, `LONG_INTEGER`) uses a different amount of storage in memory, there are different functions to read and write each of these types. The return value of each of these functions is the actual number of bytes read or written to the file. The reason why different functions have to be called instead of having just one function is for the following reason. Data elements are written to a file by inserting one element after another. The file does not contain any information as to what that data is or how it is to be extracted out. It is up to the program that will ultimately read that file to know exactly what is contained within the file and how to extract the data back out of it.

The following example demonstrates this:

DIGITAL_INPUT readCompactFlashCard;  
DIGITAL_INPUT writeCompactFlashCard; 

INTEGER myInt;  
LONG_INTEGER myLongInt;  
STRING myStr[50]; 

PUSH writeCompactFlashCard  
{  
SIGNED_INTEGER nFileHandle;  
INTEGER nNumBytes;

StartFileOperations();

nFileHandle = FileOpen( "\\\CF0\\\MyFile", _O_WRONLY | _O_CREAT | _O_BINARY );  
if( nFileHandle >= 0 )  
{nNumBytes = WriteInteger( nFileHandle, myInt );  
nNumBytes = WriteLongInteger( nFileHandle, myLongInt );  
nNumBytes = WriteString( nFileHandle, myStr );

FileClose( nFileHandle );}

EndFileOperations();}

PUSH readCompactFlashCard  
{  
SIGNED_INTEGER nFileHandle;  
INTEGER nNumBytes;

StartFileOperations();

nFileHandle = FileOpen( "\\\CF0\\\MyFile", _O_RDONLY | _O_BINARY );  
if( nFileHandle >= 0 )  
{nNumBytes = ReadInteger( nFileHandle, myInt );  
nNumBytes = ReadLongInteger( nFileHandle, myLongInt );  
nNumBytes = ReadString( nFileHandle, myStr );

FileClose( nFileHandle );}

EndFileOperations();}

The functions, `ReadStructure` and `WriteStructure`, automate the reading and writing of the individual fields within the structure. These functions do not return the number of bytes read or written. Instead, both functions have an additional argument that will contain the number of bytes read or written after the function call executes.

The following example demonstrates this:

DIGITAL_INPUT readCompactFlashCard;  
DIGITAL_INPUT writeCompactFlashCard;

STRUCTURE myStruct  
{  
INTEGER myInt;  
LONG_INTEGER myLongInt;  
STRING myStr[50];  
}  
myStruct struct;

PUSH writeCompactFlashCard  
{SIGNED_INTEGER nFileHandle;  
INTEGER nNumBytes;

StartFileOperations();

nFileHandle = FileOpen( "\\\CF0\\\MyFile", _O_WRONLY | _O_CREAT | _O_BINARY );if( nFileHandle >= 0 )  
{"WriteStructure( nFileHandle, struct, nNumBytes );

Print( “The number of bytes written = %d”, nNumBytes );

FileClose( nFileHandle );}

EndFileOperations();}

PUSH readCompactFlashCard  
{SIGNED_INTEGER nFileHandle;  
INTEGER nNumBytes;

StartFileOperations();

nFileHandle = FileOpen( "\\\CF0\\\MyFile", _O_RDONLY | _O_BINARY );  
if( nFileHandle >= 0 )  
{ReadStructure( nFileHandle, myInt, nNumBytes );

Print( “The number of bytes read = %d”, nNumBytes );

FileClose( nFileHandle );}

EndFileOperations();}

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Compact_Flash_Functions/TP_Compact-Flash-Functions.htm*
