def evaluate_postfix(expression):
    stack = []
    
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        elif char in '+-*/':
            if len(stack) < 2:
                return "Error: Not enough operands"
            b = stack.pop()
            a = stack.pop()
            
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                if b == 0:
                    return "Error: Division by zero"
                stack.append(int(a / b))
        else:
            return "Error: Invalid character"
    
    if len(stack) != 1:
        return "Error: Invalid expression"
    
    return stack.pop()

while True:
    expr = input("Input postfix expression : ")
    if expr == "":
        break
    result = evaluate_postfix(expr)
    print("Result =", result)
