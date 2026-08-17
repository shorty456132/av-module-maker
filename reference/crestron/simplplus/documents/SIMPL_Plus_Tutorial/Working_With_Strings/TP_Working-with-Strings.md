# Working with Strings

In [Working with Data (Variables)](<../Working_With_Data/TP_Working-with-Data-\(Variables\).htm>) and [Operators, Expressions, and Statements](<../Operators,_Expressions_and_Statements/TP_Operators, Expressions, and Statements.htm#Inputs,>) the concept of the **`BUFFER_INPUT`** was discussed. This section provides a more in-depth treatment of working with incoming serial data.

## `BUFFER_INPUT`

To review what was discussed earlier, serial data entering a SIMPL+ program may be treated as either a **`STRING_INPUT`** or as a **`BUFFER_INPUT`**. What is the difference, and which one should be used?

The difference between a **`STRING_INPUT`** and **`BUFFER_INPUT`** is quite simple. The value of a **`STRING_INPUT`** is always the last value of the serial signal that feeds it from the SIMPL program. This means that every time new data is generated on the serial signal in the SIMPL program, the **`STRING_INPUT`** variable in the SIMPL+ program changes to contain that data; any data that was previously contained in that variable is lost.

**`BUFFER_INPUT`** s on the other hand do not lose any data that was stored there previously. Instead, any new data that is generated onto the serial signal in the SIMPL program is appended to the data currently in the **`BUFFER_INPUT`** variable.

To make this concept even clearer, consider the following simple example. The SIMPL program shown below contains two Serial Send symbols, each one triggered by a button press. The outputs of these symbols are tied together so that both symbols can generate a string onto the same serial signal. Next this signal is connected in two places to the SIMPL+ module. The first input is mapped to a **`STRING_INPUT`** and the second is mapped to a **`BUFFER_INPUT`**. The declaration section for this module should appear as follows.

STRING_INPUT theString[100];  
BUFFER_INPUT theBuffer[100]; 

NOTE: The Serial Send symbol simply generates the static text defined in its parameter field onto the output serial signal whenever the trigger input sees a rising signal. 

The table below shows the state of these two input variables in response to button presses.

**States of Two Input Variables** Action | theString | theBuffer  
---|---|---  
system initializes | empty | empty  
button 1 pressed | “Now is” | “Now is”  
button 2 pressed | “the time” | “Now is the time”  
button 1 pressed | “Now is” | “Now is the time Now is”  
  
From this table, notice that each time the serial signal changes, **theString** assumes this value and the old data stored there is lost. On the other hand, **theBuffer** retains any old data and simply appends the new data onto the end.

Each application should dictate whether it is appropriate to use a **`STRING_INPUT`** or a **`BUFFER_INPUT`**. In general, use **`STRING_INPUT`** s when the serial signal that is feeding it is being driven from a logic symbol like a Serial Send, Analog to Serial, or Serial Gather. In these cases, the serial data is issued on a single logic wave. Therefore, it is certain that the entire string is copied into the **`STRING_INPUT`**.

NOTE: A logic wave is the time needed for a signal to propagate from the input to the output of a single logic symbol. This concept is discussed fully in [Understanding Processing Order](<../Understanding_Processing_Order/TP_Understanding-Processing-Order.htm>).

If, on the other hand, the signal feeding into the SIMPL+ program comes from a streaming source such as a serial port, use a **`BUFFER_INPUT`** , which can gather up the data as it dribbles in.

To solidify this concept, consider another example. Say the program is written for a CD jukebox, which is capable of sending text strings containing the current song information. Typical data received from this device might appear as the following.

Artist=Frank Sinatra, Track=My Way, Album=Very Good Years<CR>

Where the **< CR>** at the end of the string represents a carriage return character. This is a relatively long string of data and it is quite possible, even probable, that the operating system would not remove the entire string from the serial port in one piece. This is due to the fact that the control system checks the state of the serial ports very often and removes any data that is found there. Since this data takes some time to reach the port (depending on the baud rate), it is likely that the port’s input buffer is collected before the whole string is there. If there was a serial signal called **jukebox_in** connected to the rx terminal on the COM port definition, the program might be written as follows.

first pass:

jukebox_in = "Artist=Frank Sinatra, Trac"

second pass:

jukebox_in = "k=My Way, Album=Very Good Yea"

third pass:

jukebox_in = "rs<CR>"

If this signal, **jukebox_in** , were then connected to a **`STRING_INPUT`** of a SIMPL+ program, it is likely that the string might not be seen as one complete piece. Thus the artist’s name, the track name, and the album name might not be parsed out for display on a touchpanel. On the other hand, if a **`BUFFER_INPUT`** were used instead, this buffer would collect the data as it arrived. Therefore, after the processor read the port the third time, this **`BUFFER_INPUT`** would contain the complete string.

## Removing Data From Buffers

Once data has been routed into a **`BUFFER_INPUT`** , techniques are required to extract data from it. Typically the first thing to be done with data on a **`BUFFER_INPUT`** is to pull off a completed command and store it into a separate variable. For example, most data that comes from other devices are delimited with a certain character (or characters) to denote the end of the command. In many instances a carriage return (or carriage return followed by a line feed) is used.

The **getc** function is the most basic way to remove data from a buffer. Each call of **getc** pulls one character out of the buffer and returns that character’s ASCII value as the function’s return value. Characters are removed from the buffer in the order they arrived. Thus the first character in becomes the first character out. This function now provides the ability to extract data until the desired delimiter is seen. For example, the following code is read data from the buffer until a carriage return is seen.

BUFFER_INPUT data_in[100];  
INTEGER nextChar;  
STRING temp[50], line[50]; 

CHANGE data_in // trigger whenever a character comes in  
{  
do  
{nextChar = getc(data_in); // get the next character  
temp = temp + chr(nextChar);  
if (nextChar = 0x0D) // is it a carriage return?  
{line = temp;  
temp = "";}} until (len(data_in) = 0) // empty the buffer}

Function Main()  
{  
temp = "";}

Notice that a **do‑until** loop was used in the example above. Every time a change event is triggered for the **data_in** buffer, it is uncertain that only one character has been inserted. In fact, many characters may have been added since the last change event. Due to this possibility, continue to pull characters out of the buffer with **getc** until the buffer is empty, which is what the expression **(len(data_in) = 0)** reveals.

Also notice from the example that the extracted character is stored into an integer. This is because **getc** returns the ASCII value of the character, which is an integer. On the next line, the **chr** function is used to convert that value into a one‑byte string, which can be added to temp.

Although this example should work for real‑world applications, there is a potential problem should multiple lines of data come in on the same logic wave. Should this happen, only the last complete line is stored into **line** and the rest is lost. To account for this, make **line** into a string array and store each subsequent line into a different array element. Another possibility is that any code that is needed to further act upon the data could be built directly into this loop. Thus removing the need to store more than one line of data.

Once the data has been removed from the buffer and stored in a known format (in this case, one complete command from the device), the desired data can be extracted. Using the example above where the data was coming from a CD jukebox, the following example could be used to extract the artist, track, and album title.

BUFFER_INPUT jukebox[100];  
STRING_OUTPUT artist, track, album;  
INTEGER startPos;  
STRING searchStr[20], tempStr[100];

CHANGE jukebox  
{  
do  
{tempStr = tempStr + chr(getc(jukebox));  
if ( right(tempStr,1) = "\r" )  
{searchStr = "Artist=";  
startPos = Find(searchStr,tempStr);  
if (startPos) { // was the string found?  
startPos = startPos + len(searchStr);  
artist = mid(tempStr, startpos,  
Find(",",tempStr,startpos) ‑ startpos);  
searchStr = "Track=";  
startpos = Find(searchStr,tempStr) + len(searchStr);  
track = mid(tempStr, startpos,  
Find("\r",tempStr,startpos) ‑ startpos);  
searchStr = "Album=";  
startpos = Find(searchStr,tempStr) + len(searchStr);  
album = mid(tempStr, startpos,  
Find("\r",tempStr,startpos) ‑ startpos);  
tempStr = ""; }}

} until (len(jukebox) = 0);} 

Function Main()  
{  
tempStr = "";}

This example introduces two new system functions, which are extremely useful for string manipulation, the **Find** and **Mid** functions. To search for the existence of a substring inside of another string, use **Find**. If it is located, the return value of the function is the character position where this string was found. If the substring was not found, then **Find** returns zero. Notice that towards the top of the example the program checked to see if the substring **Artist=** is found in the string. If it is not, then assume that the incoming data was of another format and there is no need to bother looking for the other search strings (**Track=** and **Album=**).

---
*Source: https://help.crestron.com/simpl_plus/Content/SIMPL_Plus_Tutorial/Working_With_Strings/TP_Working-with-Strings.htm*
