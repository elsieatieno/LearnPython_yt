# write number, if divisible by two, number is even else odd number
a = 17
b = 9

if a>b:
    print(str(a) + 'is greater than ' +str(b))

if a == b:
    print(str(a) + 'is equal to ' +str(b))    #Will not run
else: 
    print('Not equal')

if a>b:
    print(str(a) + 'is greater than ' +str(b))
elif b<a:
    print('Im less')  #Many conditions


# Exercise
value = input('Enter a value: ')

if type(value) == str:
    print(value + ' is a string')
elif type(value) == int:
    print(value + ' is an integer')
elif type(value) == list:
    print(value + ' is a list')
else:
    print('Dont know type of value')