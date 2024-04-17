# Task 1:
def task_1() -> None:
    # Create variables with different data types and arbitrary values
    var_int:   int   = 5
    var_float: float = 3.14
    var_str:   str   = 'Hello, world!'
    var_list:  list  = [1, 2, 3, 4, 5]
    var_bool:  bool  = True

    # Print the data type of each variable to the console
    print('Data type of var_int:',   type(var_int))
    print('Data type of var_float:', type(var_float))
    print('Data type of var_str:',   type(var_str))
    print('Data type of var_list:',  type(var_list))
    print('Data type of var_bool:',  type(var_bool))

# Call the function
task_1()


# Task 2:
def task_2() -> None:
    # Define a list of numbers
    a = [1, 2, 3, 5, 8, 13, 21]

    # Print the first 3 values of the list
    print('First 3 values of the list:', a[:3])

    # The sequence of numbers is called the Fibonacci sequence

# Call the function
task_2()


# Task 3:
def task_3(number: int) -> int:
    # Square the number and return the result
    return number ** 2

# Call the function and print the result to the console
print('Square of the number 5 is:', task_3(5))

