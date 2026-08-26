#Write a Python program that takes your age as input and prints: 
#● The value entered 
#● Its data type

input(print('Enter your age: '))
print('18')
print(type(18))

# Program to find sum of two numbers , EXAMPLE 
a = int(input("Enter first number: ")) 
b = int(input("Enter second number: ")) 
sum = a + b 
print("The sum is:", sum) 

#Modify this program to find the average of two numbers instead of the sum.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
average = (a + b) // 2  # here '//' to take output in pure integer not in boolean form like (3.0)
print("The average is:" , average)

#Take a number as input, convert it to a float, and print both the original and converted values with their data types.

x = int(input('Enter your no. :'))
y = float(x)
print( x , y)
print(type(x))
print(type(y))

#Practice Question: Write a program that takes two numbers and prints: ● Their sum, difference, and product , ● Whether the first number is greater than the second

x = int(input("Enter your 1st no. : "))
y = int(input("Enter your 2nd no. : "))

print( x + y )
print( x - y )
print( x * y ) 
print( x > y )

# 1⃣ Smart Temperature Converter 
#Take input in Celsius and print its equivalent in Fahrenheit and Kelvin. 
#(Use explicit type conversion and arithmetic operators.) 
#Formula: 
#● Fahrenheit = (C × 9/5) + 32 
#● Kelvin = C + 273.15 

C = float(input("Enter your temperature in celcius : "))
Farenheit = float(C * (9/5) + 32)
Kelvin = float((C + 273.15))

print("Temperature in farenheit is :" , Farenheit)
print("Temperature in kelvin is :" , Kelvin)

# 2⃣ Bill Split Calculator 
#Write a program that takes total bill amount and number of friends as input. 
#Calculate how much each person will pay. 
#Also print the data type of each variable used. 

B = float(input("Total Bill :"))
F = float(input("Total friends :"))
print( B / F )
print(type(B))
print(type(F))

#�
#�
#Section C: Application / Output-Based 
#1. Predict the output: 
x = 5 
y = 2.0 
print(x // y) 
print(x ** y) 



#2.  Identify and correct the error: 
#if = float("10") 
#print(if)



