# -------------------------- Data Structures ------------------------------------
''' ----> Data structures :are objects or containers that allow you to store and organize data in a specific format.

    ----> Data sturucture includes :
            > List 
                # A list is an ordered collection of items.
                # It can store elements of different data types.
                # Lists are mutable, meaning you can modify them by adding, removing, or changing elements.
            > Tuple
                # A tuple is an ordered collection of items, similar to a list.
                # Tuples are immutable, meaning they cannot be modified once created.
                # They are commonly used to store related pieces of data together.
            > Dictionary
                # A dictionary is an unordered collection of key-value pairs.
                # Each element in a dictionary is accessed by its key rather than by its position.
                # Dictionaries are mutable and can be modified by adding, updating, or deleting key-value pairs.
            > Set
                # A set is an unordered collection of unique elements.
                # Sets are useful when you want to store a collection of items without any duplicates.
                # They support operations like union, intersection, and difference.
    
    ----> Some functions performing : 
            > Indexing
            > Sorting 
            > Updating
            > Removing/deleating
            > Adding value in middle 
            > Adding Value in end
            > Use of pop
            > Counting

    ----> File handling :
            Modes of file
                > Read (reads only an existinf file)
                > Write (if you open a file which does not exist it will create that file)
                > Append  (adds content in existing file)
                > Text   (opens file in text form actually not much needed as it is present in as default)
                > Binary (opens in binary (bits) form )         

    ----> Exception Handling : process of responding unwanted and unexpectedevents when a computer program runs.
                syntax:
                    try:
                      # Statement which could generate
                      # exception
                    except:
                      # Solution of generated exception
    ----> Importing libraries : Process of loading code from python module into current script.
                                Allows us to use functions.
                

'''
#<------------------------------------------------------------------------------------------------------------------------------------->
 
#---------------- List ------------------- 
'''----> [] , square brackets are used to create list. '''

# Example:
g = [2, 4, 6, 8, 10]
print("List = ",g)

r =[2,6,3,"45",83,True,0,2,5,]
print("List = ",r)
print(type(r))              # Output list

#<------------------------------------------------------------------------------------------------------------------------------------>

#--------------- Tuple -------------
''' ----> () , parenthesis is used to create tuple.'''

# Example:
tup_1 = (5 ,1 ,6 ,8, 4, 6, 2, 8 )               
print(" Tuple = ",tup_1)
print(type(tup_1))          # output tuple

#<--------------------------------------------------------------------------------------------------------------------------------------->

#-------------- Dictionary -----------
''' ----> {} , curly brackets are used to create a dictionary.
    ----> key(on left) + values(on right) = item 
    ----> tuple and list can also be written in a dictionary.'''

dict = {                                      
    "apple" : " a fruit",                      
    "seed type " : " seeding plant ",
    "marks" : " (12,33,56 77)",
    "subjects " : " [12,34,55] "
 }
print(dict["apple"])
print(dict.items())
print(dict.keys())
print(dict.values())
print(dict.get("marks"))
print(dict)

#<---------------------------------------------------------------------------------------------------------------------------------->

# ----------------- Sets -----------------------------
''' ----> {} , curly brackets are used to create a set.'''

# Example:
set_1 = {1,3,5,7,9}                 
print("Set = ",set_1)
print(type(set_1))
set_1.add(11)
print(set_1)

#<---------------------------------------------------------------------------------------------------------------------------------->

# ----------------Performing functions ------------------------------

# -----> Indexing 
l = ['red', 'orange', 'yellow', 'green', 'blue']
# index =  [1] ,   [2]   ,     [3]   , [4]    ,[5]
print(l[1])
print(l[3: ])
print(l[ :4])
print(l[ : ]) 

# -----> Sorting
k = [6,2,4,5,63,7,43, 9,40 ]           
print("List = ",k)
k.sort()
print("sorted list is here : " ,k)

# -----> Updating
b =[ 5,73,6,34,55,98,23,12,0 ]             
print(b)
b[3] = 78
print("List = ",b)
b.sort()
print("sorted list = " , b)

# -----> Adding value at end
m =[ 6,2,4,5,63,7,43, 9,4 ]             
print("List = ",m)
m.append(40)                       #append to add value at end
print("new list = ",m)

# -----> Adding value in middle 
t =[ 78,33,12,45,7,94,56,11 ]             
print("List = ",t)
t.insert(5,7)         # (5,7) 1st parameter is position (index) ,2nd is value to insert
print("new list = ",t)

# -----> Removing/deleting
q =[1,2,3,4,5,43,6,7,8,9 ]             
print("List = ",q)
q.remove(43)           
print("new list = ", q)

# -----> Use of pop
f =[ 1,3,4,5,7,9]             
print("List = ",f)
f.pop(4)               
print("new list = ", f)

# -----> Use of Count
list_1 =[ 2,3,4,5,3,6,9,3,2,3,4,3]             
print(list_1)
print(list_1.count(3))

#<------------------------------------------------------------------------------------------------------------------->
# ------------- File handling ----------------------- 

# Reading file
j = open('myfile.txt' , 'r')
text = j.read()
print(text)
j.close()

# Writting file
j = open('myfile.txt', 'w')
j.write("Hello,World!")
j.close

# Appendind file 
j = open('myfile.txt', 'a')
j.write("Hello,World!")
j.close

# Another way 
with open('myfile.txt' , 'a'):
    j.write('hiii buddy')

#<----------------------------------------------------------------------------------------------------------------------------------->    

#----------- Exception Handling -------------
#Example 1:
try:
    num = int(input("Enter an integer : "))
except ValueError:
    print("Number entered is not integer.")

 
#Example 2:
a = input("Enter the number : ")                # here if user enter string instead of any integer it will show error
print("Multiplication table of {a} is: ")

try:                                         
    for i in range(1,11): 
         print(int(a),"x",i,"=",int(a)*i)
except:
    print("Invalis input!")

print("End of program")

#<----------------------------------------------------------------------------------------------------------------------------->

# ------------ importing libraries ----------

import math
result = math.sqrt(9 )
print(result)

# From key word
from math import sqrt,pi
result = sqrt(9 ) * pi
print(result)

# as key word 
import math 
print(dir(math))
