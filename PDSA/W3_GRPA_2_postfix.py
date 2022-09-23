from collections import deque 

def EvaluateExpression(expr_str):
    expr = [x for x in expr_str.split()]
    stack = deque()
    for i in expr:
        if i not in "+ - * / **":
            stack.append(int(i))
        else:
            a, b = stack.pop(), stack.pop()
            stack.append(eval(str(str(b) + i + str(a))))

    result = stack.pop()
    return result

print(float(EvaluateExpression(input())))