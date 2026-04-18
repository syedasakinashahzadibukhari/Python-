'''Float in Python is a data type used to represent numbers with a decimal point, such as 3.14, 2.0, or -0.5.'''
x = 5.7
y = 2.0
print(type(x))  
'''<class 'float'>'''
'''
==============================
FLOAT IN PYTHON (COMMENT NOTES)
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


''' IMPORTANT FUNCTIONS'''

print(round(3.456, 2))   # 3.46
print(abs(-3.5))         # 3.5
print(max(2.3, 5.6))     # 5.6
print(min(2.3, 5.6))     # 2.3
print(pow(2.5, 2))       # 6.25


''' FLOAT PRECISION ISSUE'''
''' Floats are not always exact'''

print(0.1 + 0.2)        # 0.30000000000000004
print(round(0.1+0.2,2)) # 0.3


''' INFINITY VALUES'''

x = float("inf")
y = float("-inf")

print(x)        # inf
print(y)        # -inf


''' HOW INFINITY WORKS'''

print(10 < float("inf"))     # True
print(999999999 < float("inf"))  # True

print(float("inf") + 100)    # inf
print(float("inf") * 2)      # inf

print(float("inf") - float("inf"))  # nan (undefined)


''' NAN (NOT A NUMBER)'''

z = float("nan")
print(z)   # nan


''' FORMAT FLOAT'''

x = 3.14159
print(f"{x:.2f}")   # 3.14


''' MIXING INT AND FLOAT'''

print(5 + 2.0)   # 7.0 (result is float)

'''
==============================
OPERATIONS ON INTEGERS vs FLOAT
=============================='''

''' IMPORTANT RULE '''
''' ALL THESE OPERATIONS WORK ON BOTH INT AND FLOAT'''

Addition (+)
Subtraction (-)
Multiplication (*)
Division (/)
Floor Division (//)
Modulus (%)
Power (**)

''' EXAMPLES WITH INTEGERS'''

a = 5
b = 2

print(a + b)   # 7
print(a - b)   # 3
print(a * b)   # 10
print(a / b)   # 2.5   (NOTE: always float)
print(a // b)  # 2
print(a % b)   # 1
print(a ** b)  # 25


''' IMPORTANT DIFFERENCE'''

''' Division (/) ALWAYS gives FLOAT'''
5 / 2 → 2.5

''' Floor division (//) gives INT if both are int'''
5 // 2 → 2
'''

==============================
END
==============================

'''