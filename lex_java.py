import ply.lex as lex

import sys

tokens = (
    "LOGICAL",
    "WHILE",
    "FOR",
    "SOP",
    "RETURNTYPE",
    "IDENTIFIER",
    "NUMBER",
    "LBRACKET",
    "RBRACKET",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "COMMA",
    "ASSIGN",
    "PLUS",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "SEMICOLON",
    "BREAK",
    "SWITCH",
    "CASE",
    "DEFAULT",
    "COLON",
    "RETURN",
    "ACCESS",
    "THIS",
    "CLASS",
    "CHAR",
    "STATIC",
    "NEW",
    "STRING",
    "IF",
    "ELSE",
    "TRY",
    "CATCH",
    "FINALLY",
    "PASS",
    "TRUE",
    "FALSE",
    "COMMENT",
)

t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_NUMBER = r"\d+(\.\d+)?"
t_CHAR = r"'[a-zA-Z0-9]'"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_COMMA = r","
t_ASSIGN = r"="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_SEMICOLON = r";"


t_ignore = " \t\n"

def t_COMMENT(t):
    r"/[*][^*]*[*]+([^/*][^*]*[*]+)*/|//[^\n]*"
    pass

def t_IF(t):
    r"if"
    return t


def t_ELSE(t):
    r"else"
    return t

def t_PASS(t):
    r"pass"
    return t


def t_STRING(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]  # Remove double quotes
    return t


def t_NEW(t):
    r"new"
    return t


def t_FINALLY(t):
    r"finally"
    return t


def t_STATIC(t):
    r"static"
    return t


def t_SOP(t):
    r"System\.out\.println|System\.out\.print"
    return t


def t_WHILE(t):
    r"while"
    return t


def t_LOGICAL(t):
    r"\&\&|\|\||\!|\&|\||\<=|\>=|\<|\>|=="
    return t


def t_TRUE(t):
    r"true"
    return t


def t_FALSE(t):
    r"false"
    return t


def t_RETURNTYPE(t):
    r"float|int|char|void|String|double"
    return t


def t_CASE(t):
    r"case"
    return t


def t_TRY(t):
    r"try"
    return t


def t_CATCH(t):
    r"catch"
    return t


def t_DEFAULT(t):
    r"default"
    return t


def t_COLON(t):
    r":"
    return t


def t_BREAK(t):
    r"break"
    return t


def t_FOR(t):
    r"for"
    return t


def t_SWITCH(t):
    r"switch"
    return t


def t_RETURN(t):
    r"return"
    return t


def t_ACCESS(t):
    r"public|private|protected"
    return t


def t_THIS(t):
    r"this\."
    return t


def t_CLASS(t):
    r"class"
    return t

def t_IDENTIFIER(t):
    r'[a-zA-Z_$][a-zA-Z_$0-9]*(\.[a-zA-Z_$][a-zA-Z_$0-9]*)*'
    return t    

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)



def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        try:
            with open(sys.argv[1], "r") as f:
                data = f.read()
            lexer.input(data)
        except FileNotFoundError:
            print("File not found")
            sys.exit(1)
    else:
        print("Usage: python lex_java.py <filename>")
        sys.exit(1)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
