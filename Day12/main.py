import random


        
    
print("Welcome The Number Guess Game !!")
print("I'm Thinking a number between 1 to 100")
level = input("please choose and type 'easy' or 'hard' level: ")
guessNumber = random.randint(1,100)
lives = 0
endGame = False
if level == "easy":
    lives +=10
else:
    lives +=5
    
    
def checkAnswer(answer, life):
    if guessNumber != answer and life > 0:
        if(guessNumber < answer):
            print("Too High")
        else:
            print("Too Low")
        return False
    else:
        return True
    
    
    
    
while lives > 0 and endGame == False: 
    print(f"your have {str(lives)} attempt")  
    answer = int(input("Please guess the answer: "))

    if checkAnswer(answer,lives) == False and lives > 0:
        lives = lives - 1
        if(lives == 0):
            endGame = True
            print("You lose")
    elif checkAnswer(answer,lives) == True and lives > 0:
        endGame = True
        print("You Win")

        
        


