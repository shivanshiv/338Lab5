# 338 Lab 5 Exercise 1
# Note for video: to run, put test value '(+ 1 5)' - output should be 6

import sys

def evaluate(symbols):
    stack = []
    operators = {'+', '-', '*', '/'}
    
    for symbol in reversed(symbols):
        if symbol in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            
            if symbol == '+':
                stack.append(op1 + op2)
            elif symbol == '-':
                stack.append(op1 - op2)
            elif symbol == '*':
                stack.append(op1 * op2)
            elif symbol == '/':
                stack.append(op1 // op2)
        else:
            stack.append(int(symbol))
    
    return stack.pop()

def parse_expression(expr):
    expr = expr.replace('(', ' ( ').replace(')', ' ) ')
    symbols = expr.split()
    return process_symbols(symbols)

def process_symbols(symbols):
    stack = []
    
    for symbol in symbols:
        if symbol == ')':
            sub_expr = []
            while stack and stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()
            stack.append(evaluate(sub_expr[::-1]))
        else:
            stack.append(symbol)
    
    return stack.pop()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex1.py '<expression>'")
        sys.exit(1)
    
    expression = sys.argv[1]
    result = parse_expression(expression)
    print(result)


