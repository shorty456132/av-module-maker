# Reading and Writing Data to a File

Reading and writing data to a file that is moved from one kind of a system to another has special programming considerations because it will likely be written on one kind of system, e.g. a PC and read on another, e.g. a Crestron control system, or vice versa. Most programmers are used to writing programs that are both written by a PC and read by a PC.

The best way to write to a file that must be transferred between systems is to write pure ASCII text and use the [FileRead](<FileRead.htm>)/[FileWrite](<FileWrite.htm>) routines. If you must write binary data as binary, e.g. structures, integers, strings, arrays, please read and consider the following.

Different kinds of systems store their internal data structures with various padding bytes and lengths, that are not always apparent. For example, a structure declared like this:

STRUCTURE

{

STRING s[5];

INTEGER I;

}

may contain a padding byte between the string and the integer, so the integer can begin on a word boundary. But this padding is system and compiler dependent, as another system or compiler may handle this data perfectly well without a padding byte. Also, some systems store integers with their most significant byte first ( the industry term is “big-endian”) or with their least significant bytes first (“little-endian”).

Because compact flash is meant to be transferred among different systems, Crestron has given the programmer two different ways to store data. It can be stored with padding bytes by writing the integers, strings, structures, etc directly (see [WriteInteger](<WriteInteger.htm>), [WriteString](<WriteString.htm>), [WriteStructure](<WriteStructure.htm>), [WriteIntegerArray](<WriteIntegerArray.htm>), etc) or it can be stored directly as a string of bytes where the programmer controls exactly what is written (see [FileWrite](<FileWrite.htm>)). There are corresponding functions to read each of these. Data written by one method should be read with the corresponding function. If you must write binary files, Crestron recommends the first way, for system independence. Details are listed in each function.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/File_Functions/Reading_and_Writing_Data_to_a_File.htm*
