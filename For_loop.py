#Used for iterating over a sequence...ie list, tuple, dictionary
for letters in 'Hello':
    print(letters) #Prints everything separately

my_list = ['Jamaica', 'Canada', 'Nigeria']
for x in my_list:
    print(x) #Prints everything 

my_dict = {
    'name' : 'John',
    'age' : 19
}
for values in my_dict:
    print(values) #Prints the keys 

my_list = ['Jamaica', 'Canada', 'Nigeria']
for x in my_list:
    print(x) 
    if x == 'Jamaica':
        break #stops after reaching the if condition

for x in range(14):
    print(x) #Prints numbers from 0 -13

for x in range(1, 9):
    print(x) #Prints numbers between them

for x in range(17):
    print(x)
else:
    print('Finished looping')