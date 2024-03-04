#1
import os

for i in os.listdir(r'C:\Users\asus\Desktop\lab_pp2\lab6'):
    if os.path.isdir(r'C:\Users\asus\Desktop\lab_pp2\lab6'):
         print(i, end = ' ')

for i in os.listdir(r'C:\Users\asus\Desktop\lab_pp2\lab6'):
     if os.path.isfile(r'C:\Users\asus\Desktop\lab_pp2\lab6'):
      print(i, end = ' ')
for i in os.listdir(r'C:\Users\asus\Desktop\lab_pp2\lab6'):
     print(i)

#2
import os

path = r'C:\Users\asus\Desktop\lab_pp2\lab6'
if os.path.exists(path):
    print("this file exists")
if os.access(path, os.R_OK):
    print("file is readable")
if os.access(path, os.W_OK):
    print("file is writeable")
if os.access(path, os.X_OK):
    print("file is executable")

#3
import os

path = r'C:\Users\asus\Desktop\lab_pp2\lab6\file.py'
if os.path.exists(path):
   print("Yes")
   filename = os.path.split(path)
   print(filename)
   print(filename[0])
   print(filename[1])
else:
   print("path is not exist")

#4
file = (open(r'C:\Users\asus\Desktop\lab_pp2\lab6\1.txt', 'r'))
num = 0
for i in file:
    if i != '\n':
        num +=1
print(num)

#5
file = open('1.txt', 'w')
mylist =['sagidulla', 'zhuldyz','my bd','7.03']
for i in mylist:
    file.write(str(i) + '\n')
file.close()
f = open('1.txt', 'r')
print(f.read())

file = open('1.txt')
print(file.read())

#6
import os
def generate():
    if not os.path.exists("Letters"):
        os.makedirs("Letters")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in letters:
        with open(i+".txt", "w") as lettertxt:
            lettertxt.writelines(i)

#7
file1 = open('1.txt','r')
file2 = open('2.txt', 'w')
for i in file1:
    file2.write(str(i))
file1.close()
file2.close()

file2 = open('2.txt', 'r')
print(file2.read())

#8
import os

path = r'C:\Users\asus\Desktop\lab_pp2\lab6\2.txt'
if os.path.exists(path):
   os.remove(path)
   print('removed')
else:
   print('your file does not exists')