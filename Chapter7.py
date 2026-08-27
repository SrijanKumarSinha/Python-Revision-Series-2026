#Practice Questions  
#1. Write a function named welcome_message() that prints “Welcome to Python Programming!” three times. 

def greet() :
    print("Welcome to Python Programming!")

greet()
greet()
greet()

#2. Define a function inspire() that prints a motivational quote with your name. 

def inspire():
    print("karm karo fal ki chinta mat karo -------[Bhagvat Gita Shlok] by Srijan Kumar Sinha        ")

inspire()

#3. Create a function good_morning() that prints "Good Morning, Saumya!". Call it twice.   #rename as - Srijan Kumar Sinha

def good_morning():
    print("""Good Morning  , Srijan Kumar Sinha!""")

good_morning()
good_morning()

#Practice Questions  
#1. Write a function display_python() that prints "Python is Fun!". 

def display_python():
    print("Python is fun!")

display_python()

#2. Create a function learn() that prints three Python topics.

def learn():
    print('1.Strings'\
    '2.Tuples' \
    '3.Variables')

learn()


def greet(name) :
    print("Hello" , name)

greet("Srijan kumar sinha")

def add(a,b):
    print(" Sum : " , a+b)

add(5,4)

#Practice Questions  
#1. Write a function show_age(name, age) that prints: "Saumya Singh is 21 years old."  #Changing Name and data

def show_age(name , age):
    print(f"{name} is {age} years old")

show_age("Srijan Kumar Sinha" , 18)

#2. Create a function add_numbers(a, b) that prints both the sum and difference.

def add_numbers(a,b):
    print("Sum :" , a+b)
    print("Difference :" , a-b)

add_numbers(5,4)

#3. Write a function fav_food(food) that prints "Saumya loves <food>". #Changing name

def fav_food(food):
    print("Srijan loves" , food)
fav_food("Rasmalai")

def add(a, b): 
    return a + b 
result = add(10, 20) 
print("Result =", result) 

#Practice Questions  
#1. Write a function square(num) that returns the square of a number. 

def square(num):
    return num**2
result = square(8)
print("Result = ", result)

#2. Write a function that takes a string and returns the count of vowels and consonants separately.

def count_vowels_consonants(text):
    vowels = set("aeiouAEIOU")
    vowel_count = 0
    consonants_counts = 0
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonants_counts+=1
    return vowel_count , consonants_counts

sample_text = "Srijan Kumar Sinha"
v_count , c_count = count_vowels_consonants(sample_text)

print(f"Text:{sample_text}")
print(f"Vowels:{v_count}")
print(f"Consonants:{c_count}")

#3. Define a function convert_to_upper(word) that returns the uppercase version of the string.

def convert_to_upper(word):
    return word.upper()
result = convert_to_upper("Srijan Kumar Sinha")
print("Name : " , result)

#4. Create a function full_name(fname, lname) that returns the full name joined with a space. 

def full_name(fname , lname):
    return fname + " " + lname  
result = full_name("Srijan",  "kumar Sinha")
print("Full Name : ", result)



def greet(name="Srijan"): 
    print("Hello", name) 
greet() 
greet("Tony")

def student_info(name, age): 
    print(name, "is", age, "years old.") 
student_info(age=18, name="Srijan Sinha") 

#Practice Questions  
#1. Define a function message(text="Keep Learning!") and call it with and without an argument.

def message(text):
    print("Text :",text)
message("Keep Learning!")

#2. Create a function login(username, password="1234") that prints the credentials. 

def login(username , password):
    print("Username :" , username)
    print("Password :" , password)
login("srijan@007" , 1234)

x = 10   # global variable 
def show(): 
    x = 5   # local variable 
    print("Inside function:", x) 
show() 
print("Outside function:", x) 

#Practice Questions  
#1. Write a program with a local variable score inside a function and a global one outside.

x=8
def show():
    x=7
    print("Inside Function : ",x)
show()
print("Outside Function : ", x)

#2. Create a program using global keyword to modify a variable from inside a function. 

counter = 10
def modify_variable():
    global counter
    counter = 50
    print("Inside function (modified value ):",counter)
print("Before function call :" , counter)
modify_variable()
print("Outside function (after call):" , counter)


def greet(): 
    print("Hello Srijan!")
result = greet() 
print(result)


def factorial(n): 
    if n == 1: 
        return 1 
    return n * factorial(n - 1) 
print(factorial(5)) 

def fibonacci(n): 
    if n <= 1: 
        return n 
    return fibonacci(n-1) + fibonacci(n-2) 
 
for i in range(6): 
    print(fibonacci(i), end=" ")
