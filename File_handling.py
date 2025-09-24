# Write
f=open("Sample.txt","w") # write mode is overwrite the file means first remove then write
f.write("This is a Sample file")

# Append
f=open("Sample.txt","a") #append mode is used for write a text without overwrite means add some text 
f.write("\n Iam doing File Handling in Python")

# Read (by deafault) and text (deafault)
f=open("Sample.txt","rt") # read mode is used for read data and read by default(read entire file)
data=f.read()
print(data)
print(type(data))
f.close()

f=open("Sample.txt","r") 
data=f.read(9) # lenth of character you read
print(data)

# ReadLine
f=open("Sample.txt","r") 
data=f.read() # read
print(data)

line1=f.readline() # Readline By Line
print(line1)

line2=f.readline() # Readline By Line
print(line2)

line3=f.readline() # if no line in the text it print space
print(line3)
f.close()

# 'r+' 
# (Read and write. Raises I/O error if the file does not exist.
# Open for reading and writing. The stream is positioned at the beginning of the file.)

f=open('demo.txt','r+')
f.write("You Are") # the pointer is start of text and then overwrite
print(f.read()) # read after the pointer

#'w+'
# (Read and write. Overwrites file or creates new one.
#Open for reading and writing. The file is created if it does not exist, otherwise it is truncated.
# The stream is positioned at the beginning of the file. )

f=open('demo.txt','w+')

print(f.read()) # no text see beacause it overwrite 

f.write("XYZ") # write on demo.txt

# '+a' 
#(Read and append. Pointer at end. Creates file if it doesn't exist.
# Open for reading and writing. The file is created if it does not exist.
#  The stream is positioned at the end of the file.
# Subse- quent writes to the file will always end up at the then current end of file,
#  irrespective of any intervening fseek(3) or similar.)

f=open("demo.txt",'+a')

f.write("xyz") # write after text

print(f.read())

"""
     "r+"  read and overwrite  pointer start   no trancate
     "w+"  read and overwrite   -              trancate (remove all previous data)
     "+a"  read and append      pointer end     no trancate (no remove data )
"""
#"x" create a file
#f=open("file.txt","x") 


#2nd syntax of start "with" its does not close file beacase it close by deafault
#syntax

# with ("filename.txt","mode") as file:
#  file.write()

# Mode of txt file:
# w, r ,a

with open("sample.txt","r") as f:
    data=f.read()
    print(data)


with open("sample.txt","w") as f:
    f.write("This is a Sample file")

# deleting the file
import os 
#os.remove("file.txt") # delete the file 

# do some code 
text="""Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language.
Python 3.0, released in 2008, was a major revision not completely backward-compatible with earlier versions. Recent versions, 
such as Python 3.12, have added capabilites and keywords for typing (and more; e.g. increasing speed); helping with (optional)
static typing.[35] Currently only versions in the 3.x series are supported. """
with open("student.txt","a") as file:
    file.write(text)


# # CSV Files
#with open ('filename.csv','mode',newline='') as file:
    # handler_obj= csv.write(file,delimiter=",")
    # handler.writerow([])

import csv
with open("student_data.csv","w",newline="") as file:
    data_handler=csv.writer(file,delimiter=",")
    data_handler.writerow(['Name','Age','Class','Campus'])

with open("student_data.csv","a",newline="") as file:
    data_handler=csv.writer(file,delimiter=",")
    data_handler.writerow(['Ali','20','6','Orangi'])

with open("student_data.csv","a",newline="") as file:
    data_handler=csv.writer(file,delimiter=",")
    data_handler.writerows([['sami','20','1','Aliabad'],
                            ["Hamid","25","9","bahadurabad"],
                            ["Haris","29","10","ZamZama"]])

with open("student_data.csv","a",newline="") as file:
    read=csv.reader(file)
    print(read)

with open("student_data.csv","r",newline="") as file:
    reader=csv.reader(file)
    #print(read)
    data_list=[]
    for data in reader:
        data_list+=data
        print(data_list) 

with open("student_data.csv","r",newline="") as file:
    reader=csv.reader(file)
    #print(read)
    data_list=[]
    for data in reader:
        data_list+=data
    data_list=data_list[4:]
    print(data_list) 
# write some practice Question
# Q: Create a new file “practice.txt” using python. Add the following data in it:

# WAF that replace all occurrences of “java” with “python” in above file.

# Search if the word “learning” exists in the file or not.

# Hi everyone
# we are learning File I/O

# using Java.

# I like a propgranmming in Java.

with open("Practice.txt","w") as f:
    f.write("Hi everyone\n we are learning File I/O")
    f.write("\n using Java.\n I like a propgranmming in Java.") 

# Q: WAF that replace all occurrences of “java” with “python” in above file.
with open("Practice.txt","r") as f:
    data=f.read()
    new_data =data.replace("Java","Python")
    print(new_data)

with open("practice.txt","w") as f:
    f.write(new_data)

#Q: Search if the word “learning” exists in the file or not.
def Check_for_word():
    word="learning"
    with open("Practice.txt","r") as f:
        data=f.read()
        if(word in data):
            print("Found")
        else:
            print("Not Found")
        
Check_for_word()        
# Q: WAF to find in which line of the file does the word “learning”occur first. Print -1 if word not found.
def check_for_line():
    word="Hello"
    data=True
    line_no=1
    with open("Practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1

print(check_for_line())
# Q:From a file containing numbers separated by comma, print the count of even numbers.
count=0
with open("check_even_odd.txt","r") as f:
    data=f.read()
    num=data.split(",")
    print(num)
    for val in num:
        if (int(val)%2==0):
            count+=1
print(count)
# Writelines
f=open("write.txt","w")
line=["line: 1 \n","line: 2 \n","line: 3\n"]
f.writelines(line)
f.close()

#seek()  tell()  truncate()

f=open("dell.txt","r")

f.seek(10) # read next 10 bytes

print(f.tell()) # it tell the how many letter are seek

data=f.read(5) # read after 5 bytes after apply seek()
print(data)

#truncate()
f=open("Hp.txt","w")
f.write("Hello World3")

f.truncate(5)  # trancate is used for  how many bytes are print  
f=open("Hp.txt","r")
read=f.read()
print(read)
