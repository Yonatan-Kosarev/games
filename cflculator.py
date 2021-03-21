print("hello i am calculator")
try:
    number1 = float(input("enter your first number"))
    number2 = float(input("enter your second number"))
except:
    print("please write only numbers")
operator = input("what shall we do? +-*/%")
try:
    if operator == "+":
        print(number1+number2)
    elif operator == "-":
        print(number1-number2)
    elif operator == "*":
        print(number1*number2)
    elif operator == "/":
        print(number1/number2)
    elif operator == "%":
        print(number1%number2)
except:
    print("plise write only +-*/")