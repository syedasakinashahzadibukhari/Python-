# Integers (int) are numbers without any decimal point.

a = 10
b = -5
c = 0
'''1. Whole Numbers Only'''

# ❌ 3.14 (this is a float)

'''2. Unlimited Size'''

#Python integers can be very large (no fixed limit like in other languages).

x = 999999999999999999999999999999

'''3. Supports Arithmetic Operations'''

#You can perform all basic math operations:

a = 10
b = 3    #  Here we changed the variable value so the old value is replaced.

print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.333... (float result) singlle devide always give float
print(a // b)  # Floor division → 3 double devide gives integer
print(a % b)   # Modulus → 1
print(a ** b)  # Power → 1000

'''4. Type Checking'''

#You can check if a variable is an integer using type():

x = 5
print(type(x))   # <class 'int'>

'''5. Conversion to Integer'''

#You can convert other data types into integers:

x = int(3.7)    # 3
y = int("10")   # 10

'''
You cannot convert invalid strings:
int("abc")  # ❌ Error
'''
