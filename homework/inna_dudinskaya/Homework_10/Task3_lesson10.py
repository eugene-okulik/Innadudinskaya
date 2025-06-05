def choose_operation(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@choose_operation
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return "Неизвестная операция"


num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

result = calc(num1, num2)
print(f"Результат: {result}")
