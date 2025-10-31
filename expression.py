class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

def evaluate_expression(expression):
    tokens = expression.split()
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = Stack()
    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            operators.push(token)
        elif token == ')':
            while not operators.is_empty() and operators.peek() != '(':
                output.append(operators.pop())
            if not operators.is_empty():
                operators.pop()
        elif token in precedence:
            while not operators.is_empty() and operators.peek() != '(' and precedence[operators.peek()] >= precedence[token]:
                output.append(operators.pop())
            operators.push(token)
    while not operators.is_empty():
        output.append(operators.pop())

    # Evaluate postfix
    operands = Stack()
    for token in output:
        if token.isdigit():
            operands.push(int(token))
        else:
            b = operands.pop()
            a = operands.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '*':
                result = a * b
            elif token == '/':
                result = a // b
            operands.push(result)
    return operands.pop()

def main():
    results = []
    with open('input.txt', 'r') as f:
        for line in f:
            stripped = line.strip()
            if stripped == '----':
                results.append('----')
            else:
                result = evaluate_expression(stripped)
                results.append(str(result))
    with open('output.txt', 'w') as f:
        for res in results:
            f.write(res + '\n')

if __name__ == '__main__':
    main()
