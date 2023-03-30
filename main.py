import sys

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
            self.push(a / b)
    
    def evaluate(self, expression):
        tokens = expression.strip().split()
        for token in tokens:
            if token in "+-*/":
                self.calculate(token)
            else:
                self.push(float(token))
        return self.pop()

rpn_stack = RPNStack()

nome_arquivo = input('Digite o nome do arquivo de entrada: ')

# Abrir o arquivo e ler as linhas
with open(nome_arquivo, 'r') as arquivo:
    linhas = arquivo.readlines()

# Avaliar cada linha da expressão RPN
for linha in linhas:
    # Remover quebra de linha e espaços extras
    token = linha.strip()
    if token in "+-*/":
        rpn_stack.calculate(token)
    else:
        rpn_stack.push(float(token))

# Obter o resultado final
resultado = rpn_stack.pop()

# Imprimir o resultado
print("Resultado:", resultado)
