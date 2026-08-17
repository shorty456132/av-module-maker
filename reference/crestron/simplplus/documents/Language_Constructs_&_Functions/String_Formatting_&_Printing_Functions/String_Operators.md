# String Operators

String Operators

OPERATOR |  NAME |  EXAMPLE |  EXPLANATION  
---|---|---|---  
= |  Assignment |  A$ = B$ |  Assigns the contents in B$ to A$.  
= |  Comparison |  A$ = B$ |  A$ equal B$  
<> |  Not Equal To |  A$ <> B$ |  A$ is not equal to B$  
< |  Less Than |  A$ < B$ |  A$ is less than B$  
> |  Greater Than |  A$ > B$ |  A$ is greater than B$  
  
For less than and greater than operations, the string is evaluated in ASCII order. For example, the comparison "ABC" > "ABD" would be false. The system looks character by character; the first two characters are identical in both strings, and when it evaluated the characters C (ASCII 67) vs. D (ASCII 68), the result is false. The comparison "ABC" < "ABCD" is true, because a shorter string alphabetically precedes one that is identical but longer.

---
*Source: https://help.crestron.com/simpl_plus/Content/Language_Constructs_%26_Functions/String_Formatting_%26_Printing_Functions/String_Operators.htm*
