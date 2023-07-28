loose = ("The computer wins")
win = ("You Win")
lives = 5
score = 0
drew = 0
computer_lives = 7

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''  
print('LETS PLAY ROCK, PAPER AND SCISSORS')
# print(rock, '\n', paper ,'\n' , scissors)
while True:

    rps = input("Rock, Paper, Scissors?... ")
    rps = rps.title()
    import random
    computer = ("rock", "paper", "scissors")
    computer = random.choice(computer)
    #rock if statments
    if rps == "Rock" and computer == "paper":
        print('You Choice:', rock)
        print('The computer choise',paper )
        print("")
        print(loose)
        print("")
        print("")
        lives -=1
    if rps == "Rock" and computer == "scissors":
        print('You Choice:', rock)
        print('The computer choise',scissors )
        print("")
        print(win)
        computer_lives -=1
        print("")
        print("")
        score +=1
    #paper if statments
    if rps == "Paper" and computer == "rock":
        print('You Choice:', paper)
        print('The computer choise',rock )
        print("")
        print(win)
        computer_lives -=1
        print("")
        print("")
        score +=1
    if rps == "Paper" and computer == "scissors":
        print('You Choice:', paper)
        print('The computer choise',scissors )
        print("")
        print(loose)
        print("")
        print("")
        lives -=1
    #scissors if statments
    if rps == "Scissors" and computer == "paper":
        print('You Choice:', scissors)
        print('The computer choise',paper )
        print("")
        print(win)
        computer_lives -=1
        print("")
        print("")
        score +=1
    if rps == "Scissors" and computer == "rock":
        print('You Choice:', scissors)
        print('The computer choise',rock )
        print("")
        print(loose)
        print("")
        print("")
        lives -=1
    #duplicates
    if rps == "Scissors" and computer == "scissors":
        print('You Choice:', scissors)
        print('The computer choise',scissors )
        print("")
        print("You Drew")
        print("")
        print("")
        drew +=1
    if rps == "Rock" and computer == "rock":
        print('You Choice:', rock)
        print('The computer choise',rock )
        print("")
        print("You Drew")
        print("")
        print("")
        drew +=1
    if rps == "Paper" and computer == "paper":
        print('You Choice:', paper)
        print('The computer choise',paper )
        print("")
        print("You Drew")
        print("")
        print("")
        drew +=1
    #system
    if rps == "l":
        print(lives)
    if rps == "s":
        print(score)
    if rps == "d":
        print(drew)
    #lives
    if lives == 0 or rps =="test":
        print("Thanks for playing!")
        print("You have run out of lives. You lose")
        print("You got" , score , "correct")
        print("You drew", drew, "times")
        stop = input("Press enter to exit.")
        exit()
    if computer_lives == 0:
        print("Thanks for playing!")
        print("The computer last all it´s lives. You Win!")
        print("You got" , score , "correct")
        print("You drew", drew, "times")
        stop = input("Press enter to exit.")
        import time
        time.sleep(900)
    