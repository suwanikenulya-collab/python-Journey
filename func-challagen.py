import random

#from algo import Position

print("Hello user!")
word =["apple","banana","pinnaple"]


#create an empty list

#force each letter in the secret_word add a "_" that will be

# printed to the console
#example if the word is hacker "_"

secret_word = random.choice(word)
display_word=[]
for letter in secret_word:
    display_word += "_"
    print(display_word)
guess  = input("Guess the letter: ").lower()

#loop through each of the letters in the choses word
#if the letter is in the word replace the "_" with the letter
#it should look like this "_","c", "a","_"


print(guess)

for Position in range(len(secret_word)):
    letter = secret_word[Position]

    if letter == guess:
        display_word[Position] = letter

print(display_word)



