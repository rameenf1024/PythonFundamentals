print("Hello Guyss!")

''' In this above example, 1st part (print) is a function.
--> function is a block of code that performs specific tasks.
2nd part ("Hello Guyss!) is a string.
--> string is sequence of characers. '''

#<-------------------------------------------------------------------------------------------------------------------------------->

# ----Variables and Datatypes----

''' --> Variables : 
1. name given to a memory location in program, OR works as container that contains different values.
2. reserved words(e.g; def, class,import etc) cannot be usedc as variable. '''

a = "juice"             # string type
b = 29                  # float type          
c = 67.2                #  integer type  


''' --> Data types :
1. types of data which we have in python.
2. varaiable is conatianer which stores value and data type is name of container. 
3. 5 types 
    > 1.integer (1, 2, 34, 456 etc)
    > 2.float point numbers (23.5, 1.2, 45.78 etc)
    > 3.string (' '," ",''' ''', anything written in it)
    > 4.boolean (true/false)
    > 5.none (used to show kuch nahi ,used in functions) '''

#string e.g
a =' sunshine'
b = " spring "
c = ''' today           
is a 
rainy 
day :)'''     # '''  ''' works for new line also...
print(a)
print(b)
print(c)          

#--> \n is another operator used for new line
print('''Jack and Jill  Went up the hill, \n to fetch a pail of water 
Jack fell down and broke his crown \n And Jill come tumbling after''') 


#printing types of variable
print(type(a))
print(type(b))
print(type(c))

#<------------------------------------------------------------------------------------------------------------------------------>

#---- Operators ---- 
''' 4 types of operators :
> arithmetic (+, -, *, /, %)
> assignment (=, +=, -=, *=, /=, %=)
> comparison (==, !=, <, <=, >, >=) 
> logical (and, not, or)
 '''

 # Arithmetic operators examples (used for calculations)
print("Answer of 6+3 is : " , 6+3)
print("Answer of 6*3 is : " , 6*3)
print("Answer of 6-3 is : " , 6-3)
print("Answer of 6/3 is : " , 6/3)
print("Answer of 6%3 is : " , 6%3)

# Asignment operator examples (shortcut)
a = 24
a += 12
b = 56
b -= 9
c = 5
c *= 5
d = 81
d /= 4
e = 77
e %= 5
print(a, b, c, d, e) 

# Comparison Operator examples  (return boolean )
a = (34 >= 45)
b = (2 < 8)
c = (9 != 8)
print(a , b , c)

#Logical operators example (works on boolean)
t = True
f = False
print(" value of t and f is ;" ,t and f)    # when both values are true then only it'll show true
print(" value of t or f is ;" ,t or f)      # if any one value is true it'll show true
print(" value of t not f is ;" ,not f)      # ulta kar deta hai false ko true or true ko false

#<-------------------------------------------------------------------------------------------------------------------------->

#----Type casting ----
''' Conversions :
1. integer to string (str(31))
2. string to integer (int("23"))
3. integer to float (float(87)) '''
#1.
l = 44
l = str(44)
print(l ,type(l))

#2.
k='87'
print(k, type(k))
k = int(k)
print(k,type(k))

#3.
f= 11
print(f, type(f))
f = float(f)
print(f, type(f))




