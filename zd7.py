class Calculator:
    def __init__(self):
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3
        }
    
    def _isOperator(self, char):
        return char in self.operators
    
    def _precedence(self, op):
        return self.operators.get(op, 0)
    
    def _applyOperator(self, a, b, op):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                raise ZeroDivisionError("Деление на ноль")
            return a / b
        elif op == '^':
            return a ** b
        else:
            raise ValueError(f"Неизвестный оператор: {op}")
    
    def infixToRPN(self, expression):
        output = []
        stack = ArrayStack()
        
        i = 0
        while i < len(expression):
            char = expression[i]
            
            if char == ' ':
                i += 1
                continue
            
            if char.isdigit() or (char == '-' and (i == 0 or expression[i-1] in '+-*/^(')):
                num = ''
                if char == '-':
                    num = '-'
                    i += 1
                
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num += expression[i]
                    i += 1
                output.append(num)
                continue
            
            if char == '(':
                stack.push(char)
            
            elif char == ')':
                while not stack.isEmpty() and stack.peek() != '(':
                    output.append(stack.pop())
                if not stack.isEmpty():
                    stack.pop()
                else:
                    raise ValueError("Несбалансированные скобки")
            
            elif self._isOperator(char):
                while (not stack.isEmpty() and 
                       stack.peek() != '(' and 
                       self._precedence(stack.peek()) >= self._precedence(char)):
                    output.append(stack.pop())
                stack.push(char)
            
            i += 1
        
        while not stack.isEmpty():
            if stack.peek() == '(':
                raise ValueError("Несбалансированные скобки")
            output.append(stack.pop())
        
        return output
    
    def evaluateRPN(self, rpn):
        stack = ArrayStack()
        
        for token in rpn:
            if token.replace('.', '').replace('-', '').isdigit():
                stack.push(float(token))
            elif self._isOperator(token):
                if stack.top < 1:
                    raise ValueError("Недостаточно операндов")
                b = stack.pop()
                a = stack.pop()
                result = self._applyOperator(a, b, token)
                stack.push(result)
            else:
                raise ValueError(f"Неизвестный токен: {token}")
        
        if stack.top != 0:
            raise ValueError("Некорректное выражение")
        
        return stack.pop()
    
    def calculate(self, expression):
        rpn = self.infixToRPN(expression)
        return self.evaluateRPN(rpn)
