# Token types
INTEGER, PLUS, MINUS, EOF = 'INTEGER', 'PLUS', 'MINUS', 'EOF'

class Token:
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, or EOF
        self.type = type
        # token value: integer (0, 1, 2, ..., 9), '+', or None
        self.value = value

    def __str__(self):
        return f'Token({self.type}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()

class Interpreter:
    def __init__(self, text):
        # The input expression, e.g., "3+5"
        self.text = text
        # self.pos is an index into self.text
        self.pos = 0
        # current token instance
        self.current_token = None
        self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current.isspace():
            self.advance()

    def integer(self):
        ###return a (multidigit) integer consumed from the input###
        result = ' '
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance
        return int(result)

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """Lexical analyzer (tokenizer)"""
        while self.curremt_char is not None:
            if self.currnet_char.isspace():
                self.skip_whitespace()
                continue
            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())
            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')
            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')
            
          self.error()
           
        return Token(EOF, None)
        
        current_char = self.text[self.pos]
        
        # Handle multi-digit integers
        if current_char.isdigit():
            num_str = ''
            while self.pos < len(self.text) and self.text[self.pos].isdigit():
                num_str += self.text[self.pos]
                self.pos += 1
            return Token(INTEGER, int(num_str))
        
        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token
        
        self.error()

    def eat(self, token_type):
        """Compare the current token type with the passed token type and if they match, eat the current token"""
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """parsing / interpreter
            expr -> integer plus integer
            expr -> integer minu integer
            """
        self.current_token = self.get_next_token()
        
        # We expect the current token to be an integer
        left = self.current_token
        self.eat(INTEGER)
        
        # We expect the current token to be a PLUS
        op = self.current_token
        self.eat(PLUS)
        if op.type == PLUS:
            self.eat(PLUS)
        else:
            self.eat(MINUS)
        
        # We expect the current token to be an integer
        right = self.current_token
        self.eat(INTEGER)
        if op.type == PLUS:
            result = left.value + right.value
        else:
            result = left.value - right.value
        
        # The result of adding the two integers
        
        return result

def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()
