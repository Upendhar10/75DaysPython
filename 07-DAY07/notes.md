                                            75 DAYS OF PYTHON

# DAY-7: 

## Typecasting in python

- The conversion of one data type into the other data type is known as type casting in Python or type conversion in Python.

- Python supports a wide variety of functions or methods like: 
    int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. 
    for type casting in Python.

- Two Types of Typecasting:

1. Explicit Conversion (Explicit type casting in Python)
2. Implicit Conversion (Implicit type casting in Python).


### Explicit typecasting:

- The conversion of one data type into another data type, done via developer or programmer's intervention or manually as per the requirement, is known as explicit type conversion. 

- It can be achieved with the help of Python’s built-in type conversion functions such as int(), float(), hex(), oct(), str(), etc.

Example of explicit typecasting:

```python

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both numbers is: ", sum)

```
Output:   
``` 
The Sum of both numbers is 22
```

### Implicit type casting:

- Data types in Python do not have the same level i.e. ordering of data types is not the same in Python. 
- Some of the data types have a higher order, and some have a lower order. 
- While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type. 
- According to the level, one data type is converted into another by the Python interpreter itself (automatically). This is called, implicit typecasting in python.

Python converts a smaller data type to a higher data type to prevent data loss.

Example of implicit type casting:

```python

# Python automatically converts a to int

a = 7
print(type(a))
 
# Python automatically converts b to float

b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition

c = a + b
print(c)
print(type(c))
```

Output:

```

<class 'int'>
<class 'float'>
10.0
<class 'float'>

```
