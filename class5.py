# --------- Loops --------
'''' ---->Loops: used to avoid long repeatation of code.
     ----> Two types of basic loops are there :
            > While
            > For
    ----> Advanced loops are :
            > looping with enumrates
            > looping with zip
            > looping with iter and next
            > nested loops
            > loop control statements (break,pass,continue)       
    ----> Membership operators (in, not in)
    ----> Identity operators (is ,is not)
    ----> Logical Operators (&&,||)
            '''
#<---------------------------------------------------------------------------------------------------------------------------------->
# ------------- While loop ---------
''' Syntax : 
        while (condition):
            Body ---- code                      # keeps executing until the condition is true '''

# Example 1:
i = 0
while i<=10:
    print(i)
    i += 1

# Example 2(using list):
fruits = ['Apple', 'Banana', 'watermelon', 'Mango', 'strawberry'] 
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i+1

# <------------------------------------------------------------------------------------------------------------------------------->
    
# -------- For loop ------
''' syntax : 
        for variable in iterables :              #variables = values of each item , iterable = list,tuple objects that can be iterated
            Body-----code '''

# Example 1:
l = [2,3,5,7]
for item in l:
    print(item)


 # ----> Range in functions :
''' ----> Used to generate a sequence of function
    ----> simple (6)----> by defult starts with zero
    ----> to start with 1 ----> (1,6)
    ----> specifies range (start ,stop , step size)
    ----> step size---> indicates how many no. will be skipped '''

# Example 1 :
for i in range(8):
    print(i)        # output 0 to 7

for i in range(1,8):
    print(i)        # output 1 to 7

for i in range(1,8,2):
    print(i)        # output 1,3,5,7

# Example 2 :
cars = ['Mercedes-Benz', 'Lexus', 'Tesla', 'GMC'] 
for car in cars:
    print(car)

#<----------------------------------------------------------------------------------------------------------------------------------->
#-----------Advanced loops------------
#--------- looping with enumrate ----------
                                
''' syntax:
for index, value in enumerate(iterable):
     Loop body
     Code to be executed for each index-value pair '''

# Example:
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

#<--------------------------------------------------------------------------------------------------------------------------->
#--------- looping with zip -----------
                                
''' syntax :
for item1, item2 in zip(iterable1, iterable2):
     Loop body
     Code to be executed for each pair of items from two iterables'''

#Example:
numbers = [1, 2, 3]
letters = ["a", "b", "c"]
for number, letter in zip(numbers, letters):
    print(number, letter)

#<------------------------------------------------------------------------------------------------------------------------------>

#----------- looping with iter and next----------

'''syntax:
 iter_obj = iter(iterable)
 while True:
     try:
        item = next(iter_obj)
          Loop body
          Code to be executed for each item
    except StopIteration:
        break '''

# Example:
fruits = ["apple", "banana", "cherry"]
iter_obj = iter(fruits)
while True:
    try:
        fruit = next(iter_obj)
        print(fruit)
    except StopIteration:
        break

#<--------------------------------------------------------------------------------------------------------------------------------->

#------ loop in loop (Nested loops)------
''' syntax:
        for outer_variable in outer_iterable:
                outer loop code
    
            for inner_variable in inner_iterable:
                 inner loop code '''

# Example:
for i in range(1,4):
    for j in range(1, 4):    # Inner loop
        print(i, j)
#<------------------------------------------------------------------------------------------------------------------------------>

# ------------ loops control statement -----------

# Example (break ---> terminates the loop prematurely and moves outside the loop ):
for number in range(1, 6):
    if number == 4:
        break
    print(number)

# Example (continue ---> skips the current iteration and moves to the next one in loop)
for number in range(1, 6):
    if number == 3:
        continue
    print(number)    

# Example (pass ---> It act as a place holderv and does nothing)
for number in range(1, 6):
    if number == 3:
        pass
    else:
        print(number)

#<------------------------------------------------------------------------------------------------------------------------------------>

#--------- Membership operators (in,not in)---------
''' Syntax: 
        value in sequence                  # Returns True if value is found in the sequence
        value not in sequence              # Returns True if value is not found in the sequence'''

# Example (in):
k = [2,4,6,8]
print(6 in k)           # output True
print(3 in k)           # output False

# EWxample (not in )
vowels = ['a','e','i','o','u']
print('s' not in vowels)            # output True
print('u' not in vowels)            # output False

# Example in loops:
fruits = ["apple", "banana", "orange"]

# Iterate over the fruits list
for fruit in fruits:
    if fruit == "banana":
        print("Found banana!")
    elif fruit == "kiwi":
        print("Found kiwi!")
    else:
        print(fruit, "is not what we're looking for.")

#<------------------------------------------------------------------------------------------------------------------------------->

#--------- Identity Operators(is , is not)-----------
# ''' syntax:
#         x is y              # Returns True if x and y refer to the same object
#         x is not y          # Returns True if x and y do not refer to the same object'''

#Example (is) :
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)        # True (a and b refer to the same object)
print(a is c)        # False (a and c are different objects)

#Example (is not) :
x = 5
y = 10
z = 5

print(x is not y)    # True (x and y are different objects)
print(x is not z)    # False (x and z refer to the same object)

#Example in loops:
fruits = ["apple", "banana", "orange"]
favorite_fruit = "banana"

# Iterate over the fruits list
for fruit in fruits:
    if fruit is favorite_fruit:
        print(fruit, "is my favorite fruit!")
    else:
        print(fruit, "is not my favorite fruit.")

#<---------------------------------------------------------------------------------------------------------------------------------->

#---------- Logical Operators (and,or)-----------

#Example:
n = [1, 2, 3, 4, 5,]

# Iterate over the numbers list
for number in n:
    if number % 2 == 0 and number % 3 == 0:
        print(number, "is divisible by both 2 and 3.")
    elif number % 2 == 0 or number % 3 == 0:
        print(number, "is divisible by either 2 or 3.")
    else:
        print(number, "is not divisible by either 2 or 3.")
