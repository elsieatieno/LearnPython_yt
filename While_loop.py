#Allows looping through a block of code while a certain condition is true
i = 1
while i < 7:
    print(i)
    i += 1

while i < 9 or i == 17: #Runs because one is true
    print(i)
    i += 1

while i < 9 and i == 17: #Will not run because both are not true
    print(i)
    i += 1