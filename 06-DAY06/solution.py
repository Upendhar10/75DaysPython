# Calculator 

print("Basic Calculator using Simple Python")

# Solution-1

x = int (input("Enter number1 : "))

y = int (input("Enter number2 : "))

print("The value of", x, "+", y, "is: ", x + y)
print("The value of", x, "-", y, "is: ", x - y)
print("The value of", x, "*", y, "is: ", x * y)
print("The value of", x, "/", y, "is: ", x / y)

# Solution - 2

a = int (input("Enter number1 : "))

b = int (input("Enter number2 : "))

c = input("Select the Operator : + , - , * , / , % , //  : ")

if c == "+" :
    print(a+b)
elif c == "-" :
    print(a-b)
elif c == "*" :
    print(a*b)
elif c == "/" :
    print(a/b)
elif c == "%" :
    print(a%b)
elif c == "**" :
    print(a ** b)
else :
    print("Invalid Input")
  
