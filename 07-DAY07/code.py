
a = "1"
b = "2"

print(int(a) + int(b))

# Explicit Typecasting 

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum = number + string_number
print("The Sum of both the numbers is: ", sum)


# Implicit TypeCasting

c = 2.1     # float
d = 9       # int

print(c+d)  # float
