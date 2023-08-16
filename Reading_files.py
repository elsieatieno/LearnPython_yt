#For working with external files
#Takes two parameters: 1. Location of file. 
#2. r- read only, w- write, a- append to ending r+ reading and writing
file = open('countries.txt', 'r') 
print(file.readable()) 
print(file.readlines()) #Prints everything in a list

for files in file.readlines():
    print(files)
file.close()