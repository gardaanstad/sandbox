def calculator(number_1, operator, number_2):
    if operator == "+":
        return number_1 + number_2
    elif operator == "-":
        return number_1 - number_2
    elif operator == "*":
        return number_1 * number_2
    elif operator == "/":
        return number_1 / number_2
    else:
        return "invalid operator"
    
number_1 = int(input("number 1: "))
operator = input("operator: ")
number_2 = int(input("number 2: "))

print(calculator(number_1, operator, number_2))