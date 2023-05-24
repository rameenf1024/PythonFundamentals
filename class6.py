#------------------------- Functions -----------------------------------------
'''  ----> Function : Group of statements perform specific tasks.
        
    ----> Simple Syntax with and without arguments

    ----> Decalaration of function , defining , calling

    ----> types of function 

    ----> with and without a returning value,pass

    ----> simple and advance return 

    ----> with and without a main file'''
#<------------------------------------------------------------------------------------------------------------------------------------>

#-------- Syntax of function -------
''' > simple function :
        def function_name():
            ////// funtion body
            
    > funtion with arguments:
            def function_name(argument 1, argument 2, ...):
            ////// funtion body        '''

#<------------------------------------------------------------------------------------------------------------------------------------>

#-------------- decalaration,defination,calling------------------
''' 
> simple 
    Function Decalaration : def function_name(): 
    Funtion Defination : def function_name():
                                    ///////// funtion body
    Function calling : function_name() 

> with Arguments    
    Function Decalaration : def function_name(argument1, argument2): 
    Funtion Defination : def function_name( argument1 , argument2):
                                    ///////// funtion body
    Function calling : function_name(value1, value2) '''

#<--------------------------------------------------------------------------------------------------------------------------------->

#---------- Example ----------
# ------ Simple -----
def greet():                                # Decalaraing    
    print("Hello, there!")                  # Defining

    #calling
    greet()

# ----- with argument ----- 
# Declaration
def add_numbers(a, b):
    # Definition (Function body)
    sum = a + b
    print("The sum is:", sum)

# Calling the function
add_numbers(3, 4)

# ----- Default parameter -----
def greet(name="Stranger"):
    print("Good day," + name)

greet("Sara")
greet()             # output Good day, Stranger (as stranger is default value)    

#<----------------------------------------------------------------------------------------------------------------------->
#-------Types of function --------
''' > Built in functions (alreafy present e.g; print(), type(), len(), sum() etc)

    > User defined functions (defined by user e.g above example greet(), add_number()'''

#<------------------------------------------------------------------------------------------------------------------------>
    
'''> Recursive Functions:
        Recursive functions are functions that call themselves within their own body. 
        They solve problems by breaking them down into smaller, similar subproblems.'''
# Example (factorial)
def factorial_iter(n):                  # using loop
    p = 1
    for i in range(n):
        p = p * (i+1)
    return p

f = factorial_iter(5)
print(f)                        # output 120

# using recursive 
def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursive(n-1)

print(factorial_recursive(5))               # output 120


#<-------------------------------------------------------------------------------------------------------------------->

'''>  Lambda Functions (Anonymous Functions):
        Lambda functions are small, anonymous functions that don't require a formal function definition using def. 
        They are defined using the lambda keyword and are typically used for simple and one-time operations. '''
# Example :
square = lambda x: x ** 2
result = square(5)
print(result)  # Output: 25


avg = lambda x,y : (x +y)/2
print(avg(3,5))

#<---------------------------------------------------------------------------------------------------------------------->
''' >  Higher-Order Functions:
        Higher-order functions are functions that can accept other functions as arguments and/or return functions as results.
        They treat functions as first-class citizens, allowing them to be manipulated and passed around as data.
        Examples include map(), filter(), and reduce(). '''
# Example :
numbers = [1, 2, 3, 4, 5]
square = lambda x: x ** 2
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

#<---------------------------------------------------------------------------------------------------------------------->

'''> Generator Functions:
        Generator functions are functions that use the yield keyword instead of return to generate a sequence of values. 
        Generator functions are defined like regular functions but contain one or more yield statements '''
# Example :
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
for _ in range(10):
    print(next(fib_gen))


#<---------------------------------------------------------------------------------------------------------------------->
#------- with and without a returning value,pass -------

#Example (without return value)

def greet(name):
    print("Hello, " + name + "!")

greet("Alice")

# Example ( with return value )( Example for "Simple return" also )

def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(3, 4)
print(result)  # Output: 7

#<-------------------------------------------------------------------------------------------------------------------------------->

# --------  Advance return --------
'''  > Returning multiple values
     > Returning with condition
     > Returning data structures '''

# --->Example (Returning multiple values )
def get_name_and_age():
    name = "Aron"
    age = 19
    return name, age

name, age = get_name_and_age()
print(name, age)  # Output: Aron 19 


# --->Example ( Returning with conditions)
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

grade = get_grade(85)
print(grade)  # Output: B


# --->Example ( Returning Data Structures )
def get_person_details():
    person = {"name": "Bob", "age": 30, "country": "USA"}
    return person

person_details = get_person_details()
print(person_details["name"])  # Output: Bob

#<---------------------------------------------------------------------------------------------------------------------------------->

#--------- with and without a main file -------

# --->Example (with main file) :
def main():
    print("Hello, world!")

if __name__ == "__main__":          #ensures that the main function is only executed when the script is run directly as the main file.
    main()


# --->Example (other files(Modules)):
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print(add(7,7))
print(subtract(10,5))

