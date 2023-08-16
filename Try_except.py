#Prevents an error
try:
    x = int(input("Input an integer: "))
    print(x)
except:
    print('Value not an integer.')

#Add the type of error
try:
    x = str(input("Input an string: "))
    print(x)
except ValueError: #Gets for the type of error specified
    print('Value not a string.')

try:
    x = int(input("Input an integer: "))
    print(x)
except:
    print('Value not an integer.')
else: #For successful code
    print('Nothing went wrong')

#Prints if there is an error or not
try:
    x = int(input("Input an integer: "))
    print(x)
except:
    print('Value not an integer.')
finally:
    print('Try except finished')