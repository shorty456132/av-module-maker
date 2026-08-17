# Lua 5.3 Reference Manual -  The Complete Syntax of Lua

> Source: https://help.qsys.com/Content/Control_Scripting/Lua_5.3_Reference_Manual/9_-_The_Complete_Syntax_of_Lua.htm

# Lua 5.3 Reference Manual

by Roberto Ierusalimschy, Luiz Henrique de Figueiredo, Waldemar Celes

Copyright Â© 2015â2018 Lua.org, PUC-Rio. Freely available under the terms of the [Lua license](http://www.lua.org/license.html).

[contents](Contents-Index.htm#contents)
Â·
[index](Contents-Index.htm#index)

# The Complete Syntax of Lua

Here is the complete syntax of Lua in extended BNF.
As usual in extended BNF,
{A} means 0 or more As,
and [A] means an optional A.
(For operator precedences, see [Precedence](3_-_The_Language.htm#4.8);
for a description of the terminals
Name, Numeral,
and LiteralString, see [Lexical Conventions](3_-_The_Language.htm#1).)

```lua

			chunk ::= block

			block ::= {stat} [retstat]

			stat ::=  ';' | 
			varlist '=' explist | 
			functioncall | 
			label | 
			break | 
			goto Name | 
			do block end | 
			while exp do block end | 
			repeat block until exp | 
			if exp then block {elseif exp then block} [else block] end | 
			for Name '=' exp ',' exp [',' exp] do block end | 
			for namelist in explist do block end | 
			function funcname funcbody | 
			local function Name funcbody | 
			local namelist ['=' explist] 

			retstat ::= return [explist] [';']

			label ::= '::' Name '::'

			funcname ::= Name {'.' Name} [':' Name]

			varlist ::= var {',' var}

			var ::=  Name | prefixexp '[' exp ']' | prefixexp '.' Name 

			namelist ::= Name {',' Name}

			explist ::= exp {',' exp}

			exp ::=  nil | false | true | Numeral | LiteralString | '...' | functiondef | 
			prefixexp | tableconstructor | exp binop exp | unop exp 

			prefixexp ::= var | functioncall | '(' exp ')'

			functioncall ::=  prefixexp args | prefixexp ':' Name args 

			args ::=  '(' [explist] ')' | tableconstructor | LiteralString 

			functiondef ::= function funcbody

			funcbody ::= '(' [parlist] ')' block end

			parlist ::= namelist [',' '...'] | '...'

			tableconstructor ::= '{' [fieldlist] '}'

			fieldlist ::= field {fieldsep field} [fieldsep]

			field ::= '[' exp ']' '=' exp | Name '=' exp | exp

			fieldsep ::= ',' | ';'

			binop ::=  '+' | '-' | '*' | '/' | '//' | '^' | '%' | 
			'&' | '~' | '|' | '>>' | '<<' | '..' | 
			'<' | '<=' | '>' | '>=' | '==' | '~=' | 
			and | or

			unop ::= '-' | not | '#' | '~'
```
