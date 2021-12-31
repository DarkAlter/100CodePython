

import random

words = ["asu","kuda", "kucing"]
choosenWord= random.choice(words)
guess = input("guess a letter").lower()
tampungData = []

for letter in choosenWord:
    if(letter == guess):
        tampungData.append(letter)
    else:
        tampungData.append("_")

print(tampungData)
             