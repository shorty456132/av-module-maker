# Operator Precedence & Grouping  
  
In an expression where many operators are present, some operators have "priority" over others. Operators with the same precedence level are evaluated strictly left to right. Grouping is used to change the way an expression is evaluated.

Operator Precedence & Grouping

PRECEDENCE LEVEL |  OPERATORS  
---|---  
1 |  \- (Negate)  
2 |  ! NOT  
3 |  * / S/ MOD %  
4 |  \+ -  
5 |  {{ }}  
6 |  << >>  
7 |  > < >= <= S> S> S>= S<=  
8 |  = <>  
9 |  &  
10 |  ^  
11 |  |  
12 |  &&  
13 |  ||  
  
As an example, the expression:

3+5*6

Evaluates to 33 since the multiplication is performed first. It may be beneficial to use grouping to show which operations are performed first. Grouping is simply starting an expression with '(' and ending with ')'. Therefore, the expression 3+5*6 is equivalent to 3+(5*6). Grouping is very important if you want to override the default behavior and have one piece of the expression evaluated first. Therefore, to make sure the + is evaluated first, the expression is written as (3+5)*6, for a result of 48.

---
*Source: https://help.crestron.com/simpl_plus/Content/Operators/Operator_Precedence_%26_Grouping.htm*
