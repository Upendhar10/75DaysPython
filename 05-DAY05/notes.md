                                                        75 DAYS OF PYTHON

# DAY - 5 :  

## Taking User Input in Python

- In Python, we can take user input directly by using the input() function.
- This input function gives a return value as a string/character hence we have to pass/store that value into a variable

    Syntax:
  
        variable = input()

- But the input() function by default returns the value as a string. 
- Hence we have to typecast them whenever required to another datatype.

Example :

  ```python

  variable=int(input())
  variable=float(input())

  ```

- We can also display a text using an input function. 
- This will make the input() function take user input and display a message as well

  Example :

  ```python

  a=input("Enter the name: ")
  print(a)

  ```

  Output:
  
  ``` markup
  Enter the name: Harry
  Harry
  ```

## Operators In Python

- Python has different types of operators for different operations.
  
### Arithmetic operators

|   Operator        |      Operator Name            |   Example      |    Result     |
|-------------------|-------------------------------|----------------|---------------|
|       +           |       `Addition`              |      15+7      |      22       |
|       -           |       `Subtraction`           |      15-7      |      8        |
|       *           |       `Multiplication`        |      5*7       |      35       |
|       **          |       `Exponential`           |      5**3      |      125      |
|       /           |       `Division`              |      5/3       |      1.66     |
|       %           |       `Modulus`               |      15%7      |      1        |
|       //          |       `Floor Division`        |      15//7     |      1        |

