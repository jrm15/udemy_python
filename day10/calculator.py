def operation(n1: int, n2: int, oper: str):
    result = float(0)
    if oper == '+':
        result = n1*n2
    elif oper == '-':
        result = n1-n2
    elif oper == '*':
        result = n1*n2
    else:
        result = n1/n2
    return result

cont = 'n'
y = 1
while y:
    if cont == 'n':
        number1 = int(input('What is the first number?: '))
    operator = str(input('+\n-\n*\n/\nChoose an operation: '))
    number2 = int(input('What is the second number?: '))
    final_result = operation(number1, number2, operator)
    print(f'{number1} {operator} {number2} = {final_result}')
    cont = str(input(f'Type "y" to continue calculating with {final_result}, or type "n" to start a new calculation: '))