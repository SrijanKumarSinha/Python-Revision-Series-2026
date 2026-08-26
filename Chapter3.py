print("hello world!")
print("'hello world'")
print("I am"  +  "Iron man") #I am Iron man
print(len("Rasmalai")) #8

str = "Srijan kumar sinha"
print(str[0]) #S
print(str[0:6]) #Srijan
print(str[7:12]) #kumar

#Write a Python program that takes a user’s name as input and prints: 
#1. The first character 
#2. The last character 
#3. The total length of the name 

name = input("Enter your name : ")
print("#1. The first character :", name[0])
print("#2. The last character :", name[-1])
print("#3. The total length of the name :", len(name))

#Write a program that takes your favorite food name as input and prints: 
#● The middle 3 characters 
#● The last 2 characters

food = input("Enter your favourite food name : ")
print("The middle 3 characters :" , food[len(food)//2-1:len(food)//2+2])
print("The last 2 characters :" , food[-2:])

print("srijan kumar sinha" .upper())
print("Srijan Kumar Sinha" .lower())
print("srijan kumar sinha" .title())
print("Java is a programming language" .replace("Java" , "Python"))
print("Mango" .find("an"))
print("Missisipi" .count("s"))
print("Hello World" .startswith("Hello"))
print("Hello World" .endswith("World"))

#Write a program that: 
#● Takes a sentence as input 
#● Converts it to lowercase 
#● Replaces all spaces " " with underscores "_" 
#● Prints the new string 

sentence=input("Enter a sentence:")
x = print(sentence .lower())
y = print(sentence .replace (" " , "_"))
print("The new string is :" , sentence.lower().replace(" ","_"))

#1. Write a program that takes a sentence and prints: 
#● Total characters (len()) 
#● Uppercase version 
#● Lowercase version 

sentence = input("Enter a sentence : ")
print("Total characters :", len(sentence))
print("Uppercase version :", sentence.upper())
print("Lowercase version :", sentence.lower())

#2. Write a Python program that takes any word or sentence as input and prints: 
#● The first character 
#● The last character 
#● The total number of characters 

word = input("Enter a word or sentence :")
print("The first character :" , word[0])
print("The last character :"  , word[-1])
print("The total no. of characters :" , len(word))