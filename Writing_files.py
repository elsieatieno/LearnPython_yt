file = open('countries.txt', 'w') 
file.write('This is a new text') #Deleted everything - overwrote

file = open('country.txt', 'w') #Created a new file
file.write('New file')

file = open('countries.txt', 'a') 
file.write('\n This file has been appended') #Adds the text after existing

new_py = open('new.py','w')
new_py.write('print("\Testing\")')