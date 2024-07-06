print('Aviv Calculator!!')

runCalculator = True
while(runCalculator):
    num1 = float(input('Please enter first number  '))
    num2 = float(input('Please enter second number '))
    operator = input('please enter operator ')

    result = 0
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 *num2
    elif operator == '/':
        result = num1 / num2

    print('The result is: ', result)
    keepgoing =input('do you want to continue? (Yes/No):')
    if keepgoing == 'no':
        runCalculator = False
