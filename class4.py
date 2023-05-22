# ------------ Conditional Expressions -----------------
''' ----> Conditional sentences are statements that check whether a certain condition is true or false. 
    ----> These conditions are usually expressed using conditional or comparison operators.
    ----> Conditional/relational operators (==, !=, <, <=, >=,> )
    ----> If-Else statement.
    ----> If-elif-else statement.
    ----> nested if-else statement.
    ----> Binary operators (+,-,*,/,%.**)
    ----> Logical operators (and, or, not).
    ----> Different styles to write condition.
    '''
#<--------------------------------------------------------------------------------------------------------------------->

# --------- If-else satetment ----------
''' ----> If-else statement syntax
          if condition:
              //////////////// code runs if it's true
          else:
              //////////////// code runs if it's false '''

# Example
x = int(input("Enter any integer : "))
if (x > 0):
    print("It is a positive integer.")
else:
    print("It is a non-positive integer.")

# #<---------------------------------------------------------------------------------------------------------------------------->

# # ------------ If-elif-else statement ---------
''' -----> If-elif-else statement syntax
    if condition1:
         ///////////////// execute if condition1 is true
    elif condition2:
         //////////////// execute if condition2 is true
    else:
         /////////////// execute if all conditions are false '''

# Example 
a=78
if(a<50):
    print("a is smaller than 50")          
elif (a==50):
    print("a is equal to 50")                    
else:                                                 
   print("a is greater than 50 ")    

# #<----------------------------------------------------------------------------------------------------------------------------------->

# # -------------- Nested if-else statement -------------
   
''' ----> nested if-else statement syntax
         if condition1:
            ////// execute if condition1 is true
                    if condition2:
                        ///// execute if condition2 is true
                    else:
                        ///// execute if condition2 is false
         else:
            /////// execute if condition1 is false '''

# Example
x = int(input("Enter any integer : "))
if (x > 0):
    print("x is positive")
    if (x % 2 == 0):
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is non-positive")

#<------------------------------------------------------------------------------------------------------------------------------------>

# --------- Elif-cluase---------
'''  ----> elif-clause syntax 
if condition1:
    ////////// execute if condition1 is true
elif condition2:
    ////////// execute if condition2 is true
elif condition3:
    ////////// execute if condition3 is true
else:
    ///////// execute if none of the conditions are true'''

# Example 
x = -7

if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
elif x < 0:
    print("x is negative")
else:
    print("x is something else")

#<------------------------------------------------------------------------------------------------------------------------------------->

# ---------- Binary Operators --------
''' + for addition
    - for subtraction
    * for multiplication
    / for division
    % for modulus (reminder)
    ** for exponentiation (power)'''

# Example 1
x = 2
y = 3
result = x ** y                 #2 power 3 (2*2*2)
print(result)  # Output: 8

# Example 2
x = 10
y = 3
result = x % y
print(result)  # Output: 1

#<-------------------------------------------------------------------------------------------------------------------------------------->

# ----------- Logical operators ---------     
 
# 1. Logical AND (and):                         
age = int(input("Enter your age : "))
if(age>20 and age<60):                          # when both the conditions are true then only it will execute
    print ("You can work with us.")
else:
    print("You cannot work with us :( ")

# 2. Logical OR (or):
age = int(input("Enter your age : "))
if(age>20 or age<60):                          # if any one of the condition is true it will exucute
    print ("You can work with us.")
else:
    print("You cannot work with us :( ")

# 3. Logical NOT (not):
x = -6

if not x:                                       # not true = false & not false = true 
    print("x is falsy")
else:
    print("x is truthy")

#<-------------------------------------------------------------------------------------------------------------------->

# --------Relational Operators -------------
''' == ,!=, < ,<= ,> ,>= '''

# Example 1
x = 5
y = 10

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

#Example 2
x = 99
y = 86

if x > y:
    print("x is greater than or equal to y")
else:
    print("x is less than y")    

#Example 3 
x = 25
y = 25

if x <= y:
    print("x is less than or equal to y")
else:
    print("x is greater than y")

#<----------------------------------------------------------------------------------------------------------------------------------->

# ------------ Different Styles to write a condition ------------

# 1.Explicit Style:
''' the condition is explicitly written in a full form.'''

#Example:
x = 5
if x == 5:
    print("x is equal to 5")


# 2.Implicit Style:
''' the condition is written without explicitly comparing it to a value. It 
relies on the truthiness or falsiness of the condition.'''

#Example:
x = 5
if x:
    print("x is truthy")


# 3.Inequality Style:
'''use the inequality operator (!=) to check for a specific condition.'''

#Example:
x = 5
if x != 0:
    print("x is not zero")


# 4.Multiple Conditions Style:
'''You can combine multiple conditions using logical operators (and, or) to create complex conditions.'''

#Example:
x = 5
y = 10
if x > 0 and y > 0:
    print("Both x and y are positive")


# 5.Membership Style:
'''You can use the in operator to check if a value is present in a sequence (such as a list or string).'''

#Example:
name = "John"
if name in ["John", "Jane", "Jim"]:
    print("The name is valid")


# 6.Negation Style:
'''You can use the not operator to negate a condition.'''

#Example:
x = 5
if not x:
    print("x is falsy")


