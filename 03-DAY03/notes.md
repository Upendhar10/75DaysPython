
                                                    75 DAYS OF PYTHON

# DAY 3 : 
    
## FIRST PROGRAM 

- Today we will write our first-ever Python program from scratch. 
- It will consist of a bunch of print statements. 
- print can be used to print something on the console in Python

### Quick Quiz 

- Write a program to print a poem in Python. Choose the poem of your choice.
    
    print("---Your poem here---")

## Python Comments

- A comment is a part of the coding file that the programmer does not want to execute, rather the programmer uses it to either explain a block of code or to avoid the execution of a specific part of code while testing.

    #### 1. Single-Line Comments: To write a comment just add a ‘#’ at the start of the line.

    Example 1 :
    ``` python
    # This is a 'Single-Line Comment'
    print("This is a print statement.")
    ```
    
    Output:
  
    ``` python
    This is a print statement.
    ```

    Example 2 :
    ``` python
    print("Hello World !!!")    #Printing Hello World
    ```
     Output:
    ``` python
    Hello World !!!
    ``` 

    #### 2. Multi-Line Comments: To write multi-line comments you can use ‘#’ at each line or you can use the multiline string.

    The use of ‘#’.
    ``` python 
    # It will execute a block of code if a specified condition is true.
    # If the condition is false then it will execute another block of code.
    ``` 

    The use of multiline string.
    ``` python 
    """
    This is an if-else statement.
    It will execute a block of code if a specified condition is true.
    If the condition is false then it will execute another block of code.
    """
    ```
    
## Escape Sequence Characters

- To insert characters that cannot be directly used in a string, we use an escape sequence character.
- An escape sequence character is a backslash ( \ ) followed by the character you want to insert.
- An example of a character that cannot be directly used in a string is a double quote inside a string that is surrounded by double quotes:

Example : 

``` python 
    print("This doesn't "execute")
    print("This will \" execute")
``` 

## More on the Print statement

- The syntax of a print statement looks something like this:

    print(object(s), sep=separator, end=end, file=file, flush=flush)

    ** Other Parameters of Print Statement

    1. object(s): Any object, and as many as you like. Will be converted to string before printed
    2. sep='separator': Specify how to separate the objects, if there is more than one. The default is ' '
    3. end='end': Specify what to print at the end. Default is '\n' (line feed)
    4. file: An object with a write method. The default is sys.stdout 

    Parameters 2 to 4 are optional
