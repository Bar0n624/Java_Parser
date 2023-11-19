# Java_Parser
A simple python ply program to parse some Java programs

## Supports the following Java constructs:
- Classes
- Constructors
- Functions
- switch statements
- One dimensional Arrays
- if else blocks
- try catch finally blocks
- Simple function calls
- Simple class declerations
- Simple expressions
- Print statements
- for loop
- while loop

## Requirements:
- Python version 3.7 and above
- ply for python `pip install ply`

## Usage:
- To check syntax of a file: `python yacc_java.py your_file.extension`
- To check syntax of any input string: `python yacc_java.py`
- To tokenize: `python lex_java.py your_file.extension`
