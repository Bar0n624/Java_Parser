import ply.lex as lex


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
    "SEMI",
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
)

t_LBRACKET = r"\["
t_RBRACKET = r"\]"
t_NUMBER = r"\d+(\.\d+)?"
t_CHAR = r"'[a-zA-Z0-9]'"
t_IDENTIFIER = r"[a-zA-Z_][a-zA-Z0-9_\.]*"
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


def t_SEMI(t):
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


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

input_text = """public class Example {
    private int count = 0;

    public void printNumbers() {
        System.out.println("Printing numbers:");
        for (int i = 1; i <= 5; i++) {
            System.out.print(i + " ");
        }
        System.out.println();
    }

    public String concatenateStrings(String s1, String s2) {
        return s1 + s2;
    }

    public static void main(String[] args) {
        Example example = new Example();
        example.printNumbers();

        int result = 10 + 20 * 2;
        System.out.println("Result: " + result);

        switch (result) {
            case 30:
                System.out.println("Case 30");
                break;
            default:
                System.out.println("Default Case");
        }

        char myChar = 'A';
        String myString = "Hello, World!";
        System.out.println(myString);

        while (result > 0) {
            System.out.println(result);
            result--;
        }

        return;
    }
}
"""
lexer.input(input_text)

if __name__ == "__main__":
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
