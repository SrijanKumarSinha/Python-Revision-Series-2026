class Student: 
    name = "Srijan Kumar Sinha"   # attribute 
# creating object 
s1 = Student() 
print(s1.name)

#Practice Questions – Class & Object 
#1. Create a class Car with attribute brand = "Scorpio".  #model changed = Mercedes G - Wagon

class car:
    name = 'Mercedes G - Wagon'

c1 = car()
print(c1.name)

#2. Create a class Laptop with attributes: brand, RAM, price. Create 2 objects with different values.

class Laptop:
    brand = "Lenovo"
    RAM = "16 GB"
    price = "66,000 Rupees Only"
l1 = Laptop()
print(l1.brand)
print(l1.RAM)
print(l1.price)

#
class Bag:
    Brand = "SreeLeathers"
    Colour = "Yello with grey shade"

b1=Bag()
print(b1.Brand)
print(b1.Colour)

#
class UpcomingMovies2026:
    August = "Toxic : A Fairy Tale For Growns - up  On ---> 26/08/2026"
    November = "Ramayan On ---> 06/11/2026"
    December = "Avengers : DoomsDay ---> 18/12/2026"

m1 = UpcomingMovies2026()
print(m1.August)
print(m1.November)
print(m1.December)

#Practice Questions – Attributes 
#1. Create a class FoodItem with class attribute category = "Snacks" and instance attribute name (“Samosa”, “GulabJamun”). #Changing Gulabjamun ---> Rasmalai

class FoodItem :
    Category = "Snacks"
    def __init__ ( food , name):
        food.name = name

f1 = FoodItem("Samosa")
f2 = FoodItem("Rasmalai")

print(f1.name)
print(f2.name)