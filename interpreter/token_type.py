from enum import Enum


class TokenType(Enum):
    # Single character tokens
    LEFT_PAREN = "("
    RIGHT_PAREN = ")"
    LEFT_BRACE = "{"
    RIGHT_BRACE = "}"
    COMMA = ","
    DOT = "."
    MINUS = "-"
    PLUS = "+"
    SEMICOLON = ";"
    SLASH = "/"
    STAR = "*"
    QUESTION = "?"
    COLON = ":"

    # One or more than one character tokens
    BANG = "!"
    BANG_EQUAL = "!="
    EQUAL = "="
    EQUAL_EQUAL = "=="
    GREATER = ">"
    GREATER_EQUAL = ">="
    LESS = "<"
    LESS_EQUAL = "<="
    INCREMENT = "++"
    DECREMENT = "--"
    POWER = "**"
    PLUS_EQUAL = "+="
    MINUS_EQUAL = "-="
    STAR_EQUAL = "*="
    SLASH_EQUAL = "/="
    MODULO = "%"
    MODULO_EQUAL = "%="
    AND = "&&"
    BIT_AND = "&"
    BIT_AND_EQUAL = "&="
    BIT_NOT = "~"
    BIT_LSHIFT = "<<"
    BIT_LSHIFT_EQUAL = "<<="
    BIT_OR = "|"
    BIT_OR_EQUAL = "|="
    BIT_RSHIFT = ">>"
    BIT_RSHIFT_EQUAL = ">>="
    BIT_XOR = "^"
    BIT_XOR_EQUAL = "^="

    # Literals
    IDENTIFIER = "IDENTIFIER"
    STRING = "STRING"
    NUMBER = "NUMBER"

    # Keywords
    BREAK = "break"
    CLASS = "class"
    CONTINUE = "continue"
    ELSE = "else"
    FALSE = "false"
    FN = "fn"
    FOR = "for"
    IF = "if"
    LET = "let"
    NIL = "nil"
    OR = "||"
    RETURN = "return"
    SUPER = "super"
    THIS = "this"
    TRUE = "true"
    WHILE = "while"

    EOF = "EOF"
