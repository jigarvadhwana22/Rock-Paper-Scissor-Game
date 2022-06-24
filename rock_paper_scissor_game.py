#Rock,Paper & Scissor Game
import random
def haveAnyOneWon(usr_score,comp_score):
    if(usr_score == 3):
        print(f"---------- {usr_score}:{comp_score} ----------")
        print("****** Congratulations,You Won!! ******")
        return True
    elif(comp_score == 3):
        print(f"---------- {comp_score}:{usr_score} ----------")
        print("****** Better Luck Next time,Computer Won ******")
        return True
    else:
        return False

def conditionCheck(user_inp,comp_inp):
    if((user_inp =='r'and comp_inp =='scissor') or (user_inp=='p' and comp_inp=='rock') or (user_inp =='s' and comp_inp=='paper')): 
        return'u'
    elif((comp_inp == 'rock' and user_inp == 's') or (comp_inp == 'paper' and user_inp == 'r') or (comp_inp == 'scissor' and user_inp == 'p')):
        return 'c'
    
def letsPlay():
    user_score = 0 #initial scores 0
    comp_score = 0

    while(True):
        comp_choices=["rock","paper","scissor"]
        print("---------------------------------------------------------")
        print("Type \n's' for scissors \n'r' for rock \n'p' for paper")
        user_input=input("Your Turn : ").lower() #if user enters capital case then it wud be converted to lower
        if(user_input == 's' or user_input == 'r' or user_input == 'p'):
            #if yes then now computers turn
            comp_input=random.choice(comp_choices)
            print("Computer : ",comp_input)
            #after both have given input now its time to check the condnt
            count=conditionCheck(user_input,comp_input) 
            if(count=='u'):
                user_score +=1
               # print('Usrscore updated it is',user_score)
            elif(count=='c'):
                comp_score+=1
               # print('Comp score updated it is',comp_score)
            print("\n\t\tYour Score: ",user_score,"\n\t\tComputer Score: ",comp_score)

        else:
            print("----'Invalid selection please select s,r or p '----")
            print("\n\t\tYour Score: ",user_score,"\n\t\tComputer Score: ",comp_score)
            letsPlay() #calling back so will execute from line 1
        
        if(haveAnyOneWon(user_score,comp_score)):
            break #means someone has won
    



print("====== Rock-Paper-Scissor Game ======")
letsPlay()
