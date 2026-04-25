'''Float in Python is a data type used to represent numbers with a decimal point, such as 3.14, 2.0, or -0.5.'''
x = 5.7
y = 2.0
print(type(x))  
'''<class 'float'>'''
'''
==============================
FLOAT IN PYTHON 
=============================='''

''' DEFINITION'''
''' Float is a number with a decimal point'''

x = 3.14
y = -0.5
z = 2.0


''' TYPE CHECK'''
''' Use type() to check float'''

x = 5.6
print(type(x))   # <class 'float'>


''' TYPE CONVERSION'''
''' Convert int/string to float'''

a = float(5)        # 5.0
b = float("2.5")    # 2.5


''' BASIC OPERATIONS (WORK ON FLOAT)'''
a = 5.5
b = 2.0

print(a + b)   # Addition → 7.5
print(a - b)   # Subtraction → 3.5
print(a * b)   # Multiplication → 11.0
print(a / b)   # Division → 2.75
print(a // b)  # Floor Division → 2.0
print(a % b)   # Modulus → 1.5
print(a ** b)  # Power → 30.25
'''
Division → “How many times?
Modulus → “What is left?
'''


''' IMPORTANT FUNCTIONS'''

print(round(3.456, 2))   # 3.46 return the round off value the 2 means how many decimal places we want to keep 
print(abs(-3.5))         # 3.5 return the absolute value always return positive 
print(max(2.3, 5.6))     # 5.6 return the maximum value
print(min(2.3, 5.6))     # 2.3 return the minimum value
print(pow(2.5, 2))       # 6.25 multiply the number by it self n time here  2 times will be 2.5 * 2.5


''' FLOAT PRECISION ISSUE'''
''' Floats are not always exact'''

print(0.1 + 0.2)        # 0.30000000000000004
print(round(0.1+0.2,2)) # 0.3 here python removes the unnesserary 0 from 0.30


''' INFINITY VALUES'''

x = float("inf") #float("inf") = convert text → infinity number
y = float("-inf")
print ("here seee")
print(x)        # inf
print(y)        # -inf


''' HOW INFINITY WORKS'''

print(10 < float("inf"))     # True
print(999999999 < float("inf"))  # True

print(float("inf") + 100)    # inf
print(float("inf") * 2)      # inf

print(float("inf") - float("inf"))  # nan (undefined)


''' NAN (NOT A NUMBER)'''

z = float("nan") # i sused to fill empty spaces in the data set so taht machine can ignore them 
print(z)   # nan stands for not a number


''' FORMAT FLOAT'''

x = 3.14159 
print(f"{x:.2f}")   # 3.14 2f used to write tbe decimal places
#It does NOT change the number
#Only changes how it is displayed (printing/output)

''' MIXING INT AND FLOAT'''

print(5 + 2.0)   # 7.0 (result is float)

'''
==============================
OPERATIONS ON INTEGERS vs FLOAT
=============================='''

''' IMPORTANT RULE '''
''' ALL THESE OPERATIONS WORK ON BOTH INT AND FLOAT'''
'''
Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Floor Division (//)
Modulus (%)
Power (**)

 EXAMPLES WITH INTEGERS
 '''

a = 5
b = 2

print(a + b)   # 7
print(a - b)   # 3
print(a * b)   # 10
print(a / b)   # 2.5   (NOTE: always float)
print(a // b)  # 2
print(a % b)   # 1
print(a ** b)  # 25
'''

 IMPORTANT DIFFERENCE 

 Division (/) ALWAYS gives FLOAT
5 / 2 → 2.5

 Floor division (//) gives INT if both are int
5 // 2 → 2


==============================
END
==============================


'''