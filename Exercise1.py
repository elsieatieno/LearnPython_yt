#Building a word replacement program
sentence = input('Enter Your Sentence: ')
print('Your sentence is: '+sentence)
word1 = input('Enter word to replace: ')
word2 = input('Enter the word to replace it with: ')
print(sentence.replace(word1, word2))