print('Hi. \nHow are you?')
print('Hi. i\'m lonely.')

# Function 1 -> The letter in the index specified.
name = 'Royalty'
print(name[0])

# Function 2 -> Prints to uppercase / lowercase / boolean
name = 'tomato'
print(name.upper())
print(name.lower())
print(name.islower())

# Function 3 -> To check length
name = 'restful'
print(len(name))

# Function 4 -> To position the index / replace the letter
name = 'Jayy'
print(name.index('y')) #first occurrence
name = 'Tims'
print(name.replace('m', 't'))

# Function 5 -> Count number of times it appears
name = 'mangooo'
print(name.count('o'))

# Function 6 -> Display characters from a certain index
text = 'I like drawing and coding'
print(text[1:7]) #From space and the whole of like

#Function 7 -> Reverse string
word = 'Oval'
print(word[::-1])

#Function 8 -> Splits into different strings
sentence = 'I am  Moringa school student'
print(sentence.split())

#Function 9 -> Using .slice() method
myText = "I love feeding from food"
print(myText[0:5:4])