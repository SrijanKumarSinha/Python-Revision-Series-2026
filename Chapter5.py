#Practice Question 1 
#Create a dictionary named marks to store marks of 3 subjects. 
#Add the subjects one by one and print the final dictionary.

from ast import Try
from statistics import mean
from turtle import pu


marks = {
    "English" : 86,
    "Chemsitry" : 88,
    "Physics" : 89
}

print(marks)

nums = {1, 2,3,4}
print(nums)

nums.add(7)
nums.add(8)
nums.remove(3)
nums.remove(1)

print(nums)

#Practice Question 2 
#You are given a list of programming languages: 
#["Python", "Java", "C++", "Python", "Java", "C"] 
#Convert it into a set and print how many unique languages Divya knows.

languages = { "Python" , "Java" , "C++" , "Python" , "Java" , "C++" , "C"}
print(languages)
x = len(languages)
print(f"Divya Knows {x} unique languages" )

#Mini Assignment 
#1. Create a dictionary storing meanings of 3 English words. 

meanings = { 
    "Cat" : "A small furry pet that purrs" ,
    "Dog" : "A friendly pet animal that barks" ,
    "Sun" : "The bright star in the sky that gives us light"
}

print(meanings)

#2. Create a set of numbers and show union and intersection with another set. 

set1 = {1,2,3}
set2 = {2,3,4}

print(set1.union(set2))
print(set1.intersection(set2))

#print({1,2}.union({2,3}))   #Output : {1,2,3}
#print({1,2,3}.intersection({2,3,4}))  #Output : {2,3}


#3. Try to add both integer 9 and float 9.0 to a set and observe what happens. 
#(Hint: You can convert one into a string to make both unique.)

set = {9 , str(9.0)}
print(set)