f = open("notes.txt", "r") 
print(f.read()) 
f.close() 

#Practice Questions – Opening Files 
#Easy: 
#1. Write code to open a file named mydata.txt in read mode. 

f = open("mydata.txt", "r")
print(f.read())
f.closed()

#2. Write a program to read a text from a given file certificate.txt and find whether it contains the word live.  
#3. What happens if you open a non-existing file in "r" mode? 
#4. Open a file called report.txt in write mode.

# #Medium: 
#4. Create a file named saumya_info.txt using "x" mode. 
#5. Write a program to safely check whether a file exists before opening it. 