list1 = [1, 2, 3, 4, 5]
list2 = ['oranges', 'bananas', 'mangoes', 'tomato']

#To join two lists
list1.extend(list2)
print(list1)

#To add data to a list
list2.append('apples')
print(list2)

list2.insert(2, 'cherry') #Adds it at that specifies index
print(list2)

#To remove a value
list1.remove(5)
print(list1)

list1.clear() #Removes everything
print(list1)

del list1

list1.pop()

#To determine Index
print(list1.index(3))

# To arrange items
list2.reverse() #descending order
list1.sort() #ascending order
