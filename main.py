# Classe para identificar se um token é um operador ou um número
class Regex:

  def __init__(self, token):
    self.token = token

  def isOp(self):
    # Verifica se o token é um dos operadores básicos (+, -, *, /)
    if self.token in "+-*/":
      return True
    else:
      return False

  def isNum(self):
    # Verifica se o token é um número, incluindo números negativos
    if self.token.isdigit() or (self.token.startswith("-")
                                and token[1:].isdigit()):
      return True
    else:
      return False


# Classe para definir um tipo de token, como "NUM" para números ou "SUM" para soma
class TokenType:

  def __init__(self, token_type, valid_values):
    self.token_type = token_type
    self.valid_values = valid_values

  def __str__(self) -> str:
    return "{}".format(self.token_type)


# Classe para definir um token, contendo um tipo e um valor
class Token:

  def __init__(self, token_type, value):
    self.token_type = token_type
    self.value = value

  def __str__(self) -> str:
    return "Token [type={}, lexeme={}]".format(self.token_type.__str__(),
                                               self.value)


# Classe para representar uma pilha na notação polonesa inversa (RPN)
class RPNStack:

  def __init__(self):
    self.stack = []

  def push(self, value):
    self.stack.append(value)

  def pop(self):
    return self.stack.pop()

  def calculate(self, operator):
    if len(self.stack) < 2:
      print("Erro: faltam operandos na pilha")
      return
    b = self.pop()
    a = self.pop()
    if operator == "+":
      self.push(a + b)
    elif operator == "-":
      self.push(a - b)
    elif operator == "*":
      self.push(a * b)
    elif operator == "/":
      if b == 0:
        print("Erro: divisão por zero")
        return
      self.push(a / b)

  def scan(self, expression):
    tokens = expression.strip().split()
    token_list = []
    for token in tokens:
      reg = Regex(token)

      if reg.isOp():
        if token == "+":
          token_type = TokenType("SUM", token)
        elif token == "-":
          token_type = TokenType("MINUS", token)
        elif token == "*":
          token_type = TokenType("MULTIPLY", token)
        elif token == "/":
          token_type = TokenType("DIVIDE", token)
      elif reg.isNum():
        token_type = TokenType("NUM", token)
      else:
        print("Erro: token inválido na expressão")
        return
      token_list.append(Token(token_type, token))
    return token_list


rpn_stack = RPNStack()

nome_arquivo = input('Digite o nome do arquivo de entrada: ')

# Abrir o arquivo e ler as linhas
with open(nome_arquivo, 'r') as arquivo:
  linhas = arquivo.readlines()

# Avaliar cada linha da expressão RPN
for linha in linhas:
  # Remover quebra de linha e espaços extras
  tokens = rpn_stack.scan(linha.strip())
  if tokens is not None:
    for token in tokens:
      if token.token_type.token_type in ["SUM", "MINUS", "MULTIPLY", "DIVIDE"]:
        rpn_stack.calculate(token.value)
      else:
        rpn_stack.push(float(token.value))
      print(token.__str__())

# Obter o resultado final
resultado = rpn_stack.pop()

# Imprimir o resultado
print("Resultado:", resultado)
