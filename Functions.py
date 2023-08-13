def greetings_function(): 
    print('Welcome mkubwa')

greetings_function()

#Args & Parameters
def greetings(name):
    print('Welcome ' +name)

greetings('Mheshimiwa')

def greetings(name, age): #Two parameters
    print('Welcome ' +name+ ' you are ' +str(age))

greetings('Mheshimiwa', 40)

def greetings(*names): #For a list
    print('Welcome ' +names[1])

greetings('Mheshimiwa', 'Mkuu', 'Raia')

def greetings(name, age): #With prompt
    print('Welcome ' +name+ ' you are ' +str(age))

name = input('Enter your name: ')
age = input('Enter your age: ')
greetings(name, age)