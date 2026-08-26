#Practice Question 1 
#Write a Python program that takes a number as input and prints: 
#● “Positive” if number > 0 
#● “Zero” if number == 0 
#● “Negative” if number < 0

from doctest import Example
from operator import index, le


Number = int(input("Enter your number :"))

if Number > 0 :
    print("Postive")
elif Number == 0 :
    print("Zero")
else :
    print("Negative")



#Practice Question 2 
#Write a program that takes names of 3 favorite foods from the user and stores them in a list. Then print the list and its length. 
#1ST ATTEMPT

#FoodList = input("Enter your 3 favourite food names :")
#print(list(FoodList))
#print(len(FoodList))

#2ND ATTEMPT

food_list = []

food1 = input("Enter your 1st favourite food : ")
food2 = input("Enter your 2nd favourite food : ")
food3 = input("Enter your 3rd favourite food : ")

food_list.append(food1)
food_list.append(food2)
food_list.append(food3)

print(food_list)
print(len(food_list))

#Practice Question 3 
#Create a tuple of your favorite 5 fruits. 
#Then print: 
#1. The total number of fruits 
#2. The index of one selected fruit

tup = ( "Mango" , "Guava" , "Papaya" , "Banana" , "Apple" )
print(len(tup))
print(tup[0])

#Practice Assignment :

#1. Ask the user for their 3 favorite movies and store them in a list.

Movie_list = []

movie1 =("Enter your 1st favourite movie : ")
movie2 =("Enter your 2nd favourite movie : ")
movie3 =("Enter your 3rd favourite movie : ")

Movie_list.append(movie1)
Movie_list.append(movie2)
Movie_list.append(movie3)

#2. Create a tuple of marks (87, 64, 33, 95, 76) and print the highest and lowest marks using max() and min(). 

tup = (71, 82, 86, 88, 89)
print("Highest Marks : " , max(tup))
print("Lowest Marks :  " , min(tup))

#3. Write a program to check grade based on marks (A/B/C/D) using if-elif-else.

marks =int(input("Enter your marks :"))

if marks > 90:
    print("Grade A")
elif marks > 80:
    print("Grade B")
elif marks > 70:
    print("Grade C")
else:
    print("Grade D")

