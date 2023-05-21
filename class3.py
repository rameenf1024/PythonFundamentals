#-----String------
''' ----> data type in python.
----> sequence of characters enclosed in qoutes.
----> three ways of writing a sting 
        > Single qoutes(' ')
        > Double qoutes(" ")
        > Triple qoutes('''  ''')'''

# Example
a='peanut'
b="peanut"
c='''peanut'''
print("type of a is : ",type(a))
print("type of b is : ",type(b))
print("type of c is : ",type(c))

#<---------------------------------------------------------------------------------------------------------------------------->

# ------ Input function ------
''' > A sting is taken from user as input.'''
# Example
name = input("Enter your name : ")
print("Have a nice day " + name)

#<----------------------------------------------------------------------------------------------------------------------------->

#  ----- Concatenating of two strings --------
''' ----> when two strings are added. '''

# Example(use of string as variable)
gd="Good "
mr="Morning"
print(gd+mr)
a=gd+mr
print(a)


# ----- Using type casting in concatenation -------

''' 1.Interger + string'''
a= "356"                    #here type of a is string not int
print( a, type(a))

# print(a+6)                 # it won't work as "a" is a string so here we'll use typecasting
a = int(a)
print(a ,type(a))
print(a+6)


'''2.string + string'''
a = "40"                     #when we add 2 strings it'll simply printed togather e.g; 4012
b = "12"
print(a , "+" ,b, " = ",a + b)  

a = int(a)                     #using typecasting
b = int(b)
print(a , "+" ,b, " = ",a + b) 


''' 3.input values are always string'''
s = input('Enter your good name : ')
s = int(s)                   #converting to integer type (just numbers)
print(s,type(s))

#<------------------------------------------------------------------------------------------------------------------------>
# ----- String slicing ------
''' > extracting a portion of string by specifing a range.'''

word = "Honeycomb" 
''' H o n e y c o m b
    0 1 2 3 4 5 6 7 8   '''       # indexing starts wih 0, length = 9

# Extract a substring
substring = word[3:8]             # [ start(index included) : end(index not included) ]
print(substring)    #output eycom         

# Extract characters from the beginning
beginning = word[:5]
print(beginning)   #output honey

# Extract characters until the end
ending = word[7:]
print(ending)    #output mb

# Extract every other character
every_other = word[0:7:3]                 # [start index : end index : everyskipping no.]
print(every_other)  #output heo (skips 2 no.)

# Reverse the string
reverse = word[::-1]
print(reverse)   # output bmocyenoh 

#<------------------------------------------------------------------------------------------------------------------------------->

# ----- String functions (Methods of string variables)-----
''' > A function is simply a “chunk” of code that you can 
      use over and over again, rather than 
      writing it out multiple times. '''

# ----> commonly used functions are :
car = "ferrari"

# 1. len()  ----> tells about the total characters
print(len(car))         # output 7

# 2. .upper, .lower ----> upper(capatilize all ), lower(makes all characters lowercase)
print(car.upper())     # output FERRARI

# 3. .find  ----> tells index no.
print(car.find('a'))    #output 4

# 4. .endswith ----> gives ans in True/False
print(car.endswith("i"))        #output true
print(car.endswith("d"))        #output false

# 5. .replace ----> replace words (' old word' , 'new word')
story = " Kent is a rich boy."
print(story.replace('rich' , 'poor')) # output kent is a poor boy.

#<------------------------------------------------------------------------------------------------------------------------->

#----- Escape sequence Characters ------

''' > It allow you to include special characters within a string by using a backslash.
    > commonly used are :
        \n - New line
        \t - Tab
        \" - Double quote
        \' - Single quote
        \\ - Backslash '''

# Example
qoute1 = "Art is the lie that enables us to realize the truth."
print(qoute1)
qoute2 = "Art \nis the \"lie that \tenables us to rea\\lize the \'truth."
print(qoute2)

