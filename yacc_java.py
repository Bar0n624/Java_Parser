import ply.yacc as yacc

from lex_java import tokens

import sys


def p_programs(p):
    """programs : program
    | program programs"""
    p[0] = " ".join(map(str, p[1:]))


def p_program(p):
    """program : class
    | statement"""
    p[0] = " ".join(map(str, p[1:]))


def p_class(p):
    """class : ACCESS CLASS IDENTIFIER LBRACE stats RBRACE
    | CLASS IDENTIFIER LBRACE stats RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_this_assign(p):
    """this_assign : THIS IDENTIFIER ASSIGN IDENTIFIER SEMICOLON"""
    p[0] = " ".join(map(str, p[1:]))


def p_stats(p):
    """stats : stat
    | stat stats"""
    p[0] = " ".join(map(str, p[1:]))


def p_stat(p):
    """stat : constructor
    | statement"""
    p[0] = " ".join(map(str, p[1:]))


def p_constructor(p):
    """constructor : ACCESS IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE
    | ACCESS IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_function(p):
    """function : RETURNTYPE IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE
    | RETURNTYPE IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE
    | ACCESS RETURNTYPE IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE
    | ACCESS RETURNTYPE IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE
    | STATIC RETURNTYPE IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE
    | STATIC RETURNTYPE IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE
    | ACCESS STATIC RETURNTYPE IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE
    | ACCESS STATIC RETURNTYPE IDENTIFIER LPAREN RPAREN LBRACE statements RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_parameters(p):
    """parameters : parameter
    | parameter COMMA parameters"""
    p[0] = " ".join(map(str, p[1:]))


def p_parameter(p):
    """parameter : RETURNTYPE IDENTIFIER
    | RETURNTYPE LBRACKET RBRACKET IDENTIFIER"""
    p[0] = " ".join(map(str, p[1:]))


def p_statements(p):
    """statements : statement
    | statement statements"""
    p[0] = " ".join(map(str, p[1:]))


def p_function_call(p):
    """function_call : IDENTIFIER LPAREN params RPAREN SEMICOLON
    | IDENTIFIER LPAREN RPAREN SEMICOLON"""
    p[0] = " ".join(map(str, p[1:]))


def p_statement(p):
    """statement : assignment_statement
    | class_statement
    | print_statement
    | this_assign
    | switch
    | return
    | while
    | for
    | try_catch
    | PASS SEMICOLON
    | ACCESS assignment_statement
    | function
    | function_call
    | ifblock
    | BREAK SEMICOLON"""
    p[0] = " ".join(map(str, p[1:]))


def p_switch(p):
    """switch : SWITCH LPAREN IDENTIFIER RPAREN LBRACE cases RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_cases(p):
    """cases : case
    | case cases"""
    p[0] = " ".join(map(str, p[1:]))


def p_case(p):
    """case : CASE NUMBER COLON statements
    | DEFAULT COLON statements"""
    p[0] = " ".join(map(str, p[1:]))


def p_while(p):
    """while : WHILE LPAREN params RPAREN LBRACE statements RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_params(p):
    """params : param
    | param LOGICAL params"""
    p[0] = " ".join(map(str, p[1:]))


def p_param(p):
    """param : increment
    | expression"""
    p[0] = " ".join(map(str, p[1:]))

def p_values(p):
    """values : expression
    | expression COMMA values
    """

def p_class_statement(p):
    """class_statement : IDENTIFIER IDENTIFIER SEMICOLON
    | IDENTIFIER IDENTIFIER ASSIGN NEW IDENTIFIER LPAREN RPAREN SEMICOLON
    | IDENTIFIER IDENTIFIER ASSIGN NEW IDENTIFIER LBRACKET RBRACKET SEMICOLON
    | IDENTIFIER IDENTIFIER ASSIGN NEW IDENTIFIER LPAREN values RPAREN SEMICOLON
    | IDENTIFIER IDENTIFIER ASSIGN NEW IDENTIFIER LBRACKET NUMBER RBRACKET SEMICOLON"""
    p[0] = " ".join(map(str, p[1:]))


def p_arrays(p):
    """arrays : LBRACKET RBRACKET
    | LBRACKET RBRACKET arrays
    | LBRACKET expression RBRACKET arrays
    | LBRACKET expression RBRACKET"""
    p[0] = " ".join(map(str, p[1:]))


def p_bool(p):
    """bool : TRUE
    | FALSE"""
    p[0] = " ".join(map(str, p[1:]))


def p_assignment_statement(p):
    """assignment_statement : RETURNTYPE IDENTIFIER ASSIGN expression SEMICOLON
    | RETURNTYPE IDENTIFIER SEMICOLON
    | RETURNTYPE IDENTIFIER PLUS ASSIGN expression SEMICOLON
    | RETURNTYPE IDENTIFIER MINUS ASSIGN expression SEMICOLON
    | RETURNTYPE IDENTIFIER TIMES ASSIGN expression SEMICOLON
    | RETURNTYPE IDENTIFIER DIVIDE ASSIGN expression SEMICOLON
    | RETURNTYPE IDENTIFIER PLUS PLUS SEMICOLON
    | IDENTIFIER ASSIGN expression SEMICOLON
    | IDENTIFIER PLUS ASSIGN expression SEMICOLON
    | IDENTIFIER MINUS ASSIGN expression SEMICOLON
    | IDENTIFIER TIMES ASSIGN expression SEMICOLON
    | IDENTIFIER DIVIDE ASSIGN expression SEMICOLON
    | IDENTIFIER arrays PLUS PLUS SEMICOLON
    | increment SEMICOLON
    | IDENTIFIER arrays MINUS MINUS SEMICOLON
    | PLUS PLUS IDENTIFIER arrays SEMICOLON
    | MINUS MINUS IDENTIFIER arrays SEMICOLON
    | RETURNTYPE IDENTIFIER arrays ASSIGN LBRACE items RBRACE SEMICOLON
    | RETURNTYPE arrays IDENTIFIER ASSIGN LBRACE items RBRACE SEMICOLON
    | IDENTIFIER arrays ASSIGN expression SEMICOLON
    | IDENTIFIER arrays ASSIGN LBRACE items RBRACE SEMICOLON
    | RETURNTYPE IDENTIFIER arrays ASSIGN NEW RETURNTYPE arrays SEMICOLON
    | RETURNTYPE arrays IDENTIFIER ASSIGN NEW RETURNTYPE arrays SEMICOLON"""

    p[0] = " ".join(map(str, p[1:]))


def p_print_statement(p):
    """print_statement : SOP LPAREN expression RPAREN SEMICOLON
    | SOP LPAREN RPAREN SEMICOLON"""
    p[0] = " ".join(map(str, p[1:]))


def p_array_access(p):
    """array_access : IDENTIFIER arrays"""
    p[0] = " ".join(map(str, p[1:]))


def p_expression(p):
    """expression : IDENTIFIER
    | IDENTIFIER LPAREN RPAREN
    | LPAREN expression RPAREN
    | IDENTIFIER LPAREN values RPAREN
    | NUMBER
    | array_access
    | expression PLUS
    | expression MINUS
    | expression PLUS expression
    | expression MINUS expression
    | expression TIMES expression
    | expression DIVIDE expression
    | STRING
    | CHAR
    | bool"""
    p[0] = " ".join(map(str, p[1:]))


def p_return(p):
    """return : RETURN IDENTIFIER SEMICOLON
    | RETURN SEMICOLON
    | RETURN expression SEMICOLON"""
    p[0] = " ".join(map(str, p[1:]))


def p_items(p):
    """items : item
    | item COMMA items"""
    p[0] = " ".join(map(str, p[1:]))


def p_item(p):
    """item : NUMBER
    | CHAR"""
    p[0] = " ".join(map(str, p[1:]))


def p_ifblock(p):
    """ifblock : if
    | if else
    | if else_if"""
    p[0] = " ".join(map(str, p[1:]))


def p_if(p):
    """if : IF LPAREN params RPAREN LBRACE statements RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_else(p):
    """else : ELSE LBRACE statements RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_else_if(p):
    """else_if : ELSE if
    | ELSE if else_if
    | ELSE if else"""
    p[0] = " ".join(map(str, p[1:]))


def p_for(p):
    """for : FOR LPAREN assignment_statement params SEMICOLON increment RPAREN LBRACE statements RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_increment(p):
    """increment : PLUS PLUS IDENTIFIER
    | MINUS MINUS IDENTIFIER
    | IDENTIFIER PLUS PLUS
    | IDENTIFIER MINUS MINUS"""
    p[0] = " ".join(map(str, p[1:]))


def p_try_catch(p):
    """try_catch : TRY LBRACE statements RBRACE CATCH LPAREN IDENTIFIER IDENTIFIER RPAREN LBRACE statements RBRACE
    | TRY LBRACE statements RBRACE CATCH LPAREN IDENTIFIER IDENTIFIER RPAREN LBRACE statements RBRACE FINALLY LBRACE statements RBRACE"""
    p[0] = " ".join(map(str, p[1:]))


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")


parser = yacc.yacc()


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        try:
            with open(filename, "r") as file:
                program_input = file.read()
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
            return
    else:
        program_input = input("Enter the Java program: ")

    result = parser.parse(program_input)
    if result is None:
        print("Error")
    else:
        print("Valid Java Program")
        print(result)


if __name__ == "__main__":
    main()
