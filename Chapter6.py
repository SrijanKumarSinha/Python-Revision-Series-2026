i = 1
while i<= 7:
    print("Hi , Srijan kumar sinha")
    i+=1

#Practice Questions 
#1. Write a Python program to print numbers from 1 to 10 using a while loop. 

i = 1
while i<=10:
    print(i)
    i += 1

#2. Write a program to print numbers from 10 down to 1 using a while loop. 
#(Hint: start from 10 and decrease the counter each time.) 
#Example Output: 10  9  8  ... 1 

#i = 10
#while i <= 10:
#    print(i)
#    i -= 1     # it cause infinite loop to the negative of the infinity

i = 10
while i>=1:
    print(i)
    i-=1


#3. Write a program to print all even numbers between 1 and 50 using a while loop. 
#(Hint: Use the modulus operator % to check for even numbers.) 
#Example Output: 2 4 6 8 ... 50 

#Method 1 :
num  = 2                                             
while num <=50 :
    print(num, end=" ")
    num += 2
#Method 2 :

i=1
while i<=50:
    if i%2==0:
        print(i)
    i=i+1

#4. Write a program that prints the sum of first n natural numbers. For example, if n = 5, then output should be 1 + 2 + 3 + 4 + 5 = 15. 
#(Hint: Keep a running total inside the loop.) 

n = int(input("Enter a number :"))
sum=0
while n>=1:
    sum = sum+n
    n= n-1
print("sum" , sum)
print("n" , n)

#5. Write a program to print this pattern using a while loop:  
#(Hint: use one while loop and string multiplication like '*' * count)

n=1
while n<=4:
    print("*" * n)
    n=n+1


#6. Saumya wants to print her name 5 times, but each time with a number in front of it. Write a program using a while loop that prints:



#7. Write a program to print the multiplication table of any number using a while loop. 
#(Hint: Start i = 1 and run the loop until i <= 10.) 