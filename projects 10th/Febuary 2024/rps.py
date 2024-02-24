import random

player_score = 0
comp_score = 0


print ("ROCK PAPER SCISSOR TIME")

option =  ["rock", "paper", "scissor"]

while True:
    game = input('pick: rock, paper, scissor. type stop to stop duh ').lower().strip()
    if game == "stop":
        break
   
    if game not in option:
        print ("that aint a option bud")
        continue

    random_num = random.randint(0, 2)
    comp = option[random_num]
    print ("computer picked " + comp + ".")

    if game == "rock" and comp == "scissor":
        print ("Goodjob you won!")
        player_score += 1
    
    elif game == "scissor" and comp == "paper":
        print ("Goodjob you won!")
        player_score += 1
    
    elif game == "paper" and comp == "rock":
        print ("Goodjob you won!")
        player_score += 1
    
    elif game == comp:
        print ("its a draw")
    #elif game == "paper" and comp == "paper":
        #print ("its a draw")
    
    #elif game == "scissor" and comp == "scissor":
        #print ("its a draw")

    #elif game == "rock" and comp == "rock":
        #print ("its a draw")
    else:
        print ("you lost")
        comp_score += 1

print ("gg, computer won " + str(comp_score) + " times and you won " + str(player_score) + " times!")