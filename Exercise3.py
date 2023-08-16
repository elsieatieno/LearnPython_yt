#Building a calculator
num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
op = input('Enter operator: ')

if op == '+':
    print('Addition is', num1 + num2)
elif op == '-':
    print('Subtraction is', num1 - num2)
elif op == '*':
    print('Multiplication is', num1 * num2)
elif op == '/':
    print('Division is', abs(num1 / num2))
else:
    print('Invalid syntax')