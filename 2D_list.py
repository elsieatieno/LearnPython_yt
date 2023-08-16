#Having multiple lists inside a variable
my_list = [1, 2, 3, 4, 5]
print(my_list) #Normal list

my_list_too = [
  [1, 2, 3, 4,],
  [5, 6, 7, 8],
  [9, 10, 11, 12]  
]
print(my_list_too) 
print(my_list_too[0][0]) #Prints 1

#Nested loops
for list in my_list_too:
    for row in list:
        print(row)