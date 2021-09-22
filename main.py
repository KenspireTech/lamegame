#created by TSRK
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
responses = {}
polling_active = True
entry = "\nwelcome to lame game. lets start."
easy = "\nyou are now playing easy level"
medium = "\nyou are now playing medium level"
hard = "\nyou are now playing hard level"
creator = "\n\tcreated by tsrk"
version = "\nVersion v0.0.5"
level = ['easy', 'medium', 'hard']
health = 3
exit = "\nthanks for playing this -_-"
print(Fore.RED + Style.BRIGHT + entry.upper())
print(Fore.RED +Style.BRIGHT + Back.GREEN + creator.upper())
print(Back.YELLOW + version)
while polling_active:
    name = input(Fore.MAGENTA +"\tEnter your name: ")
    print(Back.CYAN +Fore.RED + f"\nDifficulty levels: ")
    print(level)
    level = input("\nSelect the difficulty level: ")
    if level == 'easy':
        print(f"\n{name.title()}, you have selected Easy level!")
        print(f"\nYou have total of {health} lives for total of 5 questions!!")
        print("\nOnce you go wrong, you will lose 1 life!!")
        print("\nIf you could answer all then move onto medium level!!")
        print("\nHere's your Question 1: ")
        q_1 = input(
            "\nWhat do you call a bee that was born in the United States? ")
        if q_1 == 'usb':
            print("\nWell you got it right!!")
            print("\nHere's your Question 2: ")
            q_2 = input("\nWhat do we call a crying sister? ")
            if q_2 == 'crisis':
                print("\nWow you got it right!! Well done.")
                print("\nHere is your Qustion 3: ")
                q_3 = input(
                    "\nWhere do animals go when their tails fall off? ")
                if q_3 == 'retail store':
                    print("\nWooowww!!You're right!!")
                    print("\nHere is your Qustion 4: ")
                    q_4 = input("\nWhat is blue and not heavy? ")
                    if q_4 == 'light blue':
                        print("\nVery well done you're right again!!")
                        print("\nHere is your Question 5: ")
                        q_5 = input("\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print("\nYou got all questions right!! Well played")
                            polling_active = False
                            print(exit.upper())
                        else:
                            print("\nWrong!!The answer is Rock music")
                            print("\nGGWP!!Anyways you made upto last question!!")
                            polling_active = False
                            print(exit.upper())
                    else:
                        print("\nWrong!!The answer is Light Blue")
                        health -= 1
                        print(f"\nYou have {health} lives left")
                        print("\nHere is your Question 5: ")
                        q_5 = input("\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print("\nYou got this questions right!! Well played")
                            polling_active = False
                            print(exit.upper())
                        else:
                            print("\nWrong!!The answer is Rock Music")
                            print("\nGGWP!!You made upto last level!!")
                            polling_active = False
                            print(exit.upper())

                else:
                    print("\nWrong! The answer is Retail Store")
                    health -= 1
                    print(f"\nYou have {health} lives left")
                    print("\nHere is your Qustion 4: ")
                    q_4 = input("\nWhat is blue and not heavy? ")
                    if q_4 == 'light blue':
                        print("\nVery well done you're right again!!")
                        print("\nHere is your Question 5: ")
                        q_5 = input("\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print(
                                "\nYou got this questions right!! Well played")
                            polling_active = False
                            print(exit.upper())
                        else:
                            print("\nWrong!!The answer is Rock music")
                            print("\nGGWP...You came upto last question")
                            polling_active = False
                            print(exit.upper())
                    else:
                        print("\nWrong! The answer is Light Blue.")
                        health -= 1
                        print(f"\nYou have {health} lives left")
                        print("\nHere is your Question 5: ")
                        q_5 = input("\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print("\nYou got all questions right!! Well played")
                            polling_active = False
                            print(exit.upper())
                        else:
                            print("GGWP...ITS ok you came upto last question!!")
            else:
                print("\nWrong!! The answer is crisis!!")
                health -= 1
                print(f"\nYou have {health} lives left")
                print("\nHere is your Question 3: ")
                q_3 = input(
                    "\nWhere do animals go when their tails fall off? ")
                if q_3 == 'retail store':
                    print("\nWooowww!!You're right!!")
                    q_4 = input("\nWhat is blue and not heavy? ")
                    if q_4 == 'light blue':
                        print("\nVery well done you're right again!!")
                        print("\nHere is your Question 5: ")
                        q_5 = input(
                            "\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print(
                                "\nYou got all questions right!! Well played")
                            polling_active = False
                            print(exit.upper())
                    else:
                        print("\nWrong!The answer is light blue!")
                        health -= 1
                        print(f"\nYou still have {health} lives left")
                        if health <= 0:
                            polling_active = False
                            print(exit.upper())
                else:
                    print("\nWorng!The answer is retail store")
                    health -= 1
                    print(f"\nYou still have {health} lives left")
                    print("\nHere is your Qustion 4: ")
                    q_4 = input("\nWhat is blue and not heavy? ")
                    if q_4 == 'light blue':
                        print("\nVery well done you're right!!")
                    else:
                        print("\nWrong!!The answer is light blue")
                        health -= 1
                        if health <= 0:
                            print("\nYou can't continue further!!You lost all your life!!")
                            polling_active = False
                            print(exit.upper())
        else:
            print("\nWrong!! The answer is usb!!")
            health -= 1
            print(f"\n\tYou have {health} lives left")
            print("\nHere's your Question 2: ")
            q_2 = input("\nWhat do we call a crying sister? ")
            if q_2 == 'crisis':
                print("\nWow you got it right!! Well done.")
                print("\nHere is your Qustion 3: ")
                q_3 = input(
                    "\nWhere do animals go when their tails fall off? ")
                if q_3 == 'retail store':
                    print("\nWooowww!!You're right!!")
                    print("\nHere is your Qustion 4: ")
                    q_4 = input("\nWhat is blue and not heavy? ")
                    if q_4 == 'light blue':
                        print("\nVery well done you're right !!")
                        print("\nHere is your Question 5: ")
                        q_5 = input(
                            "\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print("\nYou got this right!! Well played")
                            polling_active = False
                            print(exit.upper())
                else:
                    print("\nWrong!!The answer is retail store!!")
                    health -= 1
                    print(f"\nYou have {health} lives left")
                    print("\nHere is your Qustion 4: ")
                    q_4 = input("What is blue and not heavy? ")
                    if q_4 == 'light blue':
                        print("\nVery well done you're right!!")
                        print("\nHere is your Question 5: ")
                        q_5 = input(
                            "\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print("\nYou got this right!! Well played")
                            polling_active = False
                            print(exit.upper())
                        else:
                            print(
                                "\nWrong!But anyways you made untill last level!!"
                            )
                            print("\nGGWP!!")
                            polling_active = False
                            print(exit.upper())
                    else:
                        print("\nWrong!!The answer is light blue")
                        health -= 1
                        if health <= 0:
                            print("\nYou can't continue further!!You lost all your life!!")
                            polling_active = False
                            print(exit.upper())

            else:
                print("\nWrong the answer is crisis")
                health -= 1
                print(f"\nYou have {health} life left")
                print("\nHere is your Question 3: ")
                q_3 = input(
                    "\nWhere do animals go when their tails fall off? ")
                if q_3 == 'retail store':
                    print("\nWow well done you got it right")
                    print("\nHere is your Qustion 4: ")
                    q_4 = input("\nWhat is blue and not heavy? ")
                    if q_4 == 'light blue':
                        print("\nVery well done you're right again!!")
                        print("\nHere is your Question 5: ")
                        q_5 = input("\nWhat type of music are scissors afraid of? ")
                        if q_5 == 'rock music':
                            print("\nYou got this right!! Well played")
                            polling_active = False
                            print(exit.upper())
                        else:
                            print("\nWrong!! The answer is Rock Music")
                            print("\nGGWP!!You made upto last question!!")
                            polling_active = False
                            print(exit.upper())
                    else:
                        print("\nWrong!!The answer is Light Blue")
                        health -= 1
                        if health <= 0:
                            print(
                                "\nYou lost all your lives. You cannot continue further"
                            )
                            polling_active = False
                            print(exit.upper())

                else:
                    print("\nWrong!!The answer is retail store")
                    health -= 1
                    if health <= 0:
                        print(
                            "\nYou cant continue the game since you have 0 lives left!!"
                        )
                        polling_active = False
                        print(exit.upper())
    elif level == 'medium':
        confirmation = input("\nHave you plyed the easy level(yes/no)? ")
        if confirmation == 'yes':
            question=["\tWhat kind of music is a balloon scared of? ","\tWhat is the slipperiest country in the world? ","\tWhat do you call a sad cup of coffee? ","\tWhat do you call an alligator that reads maps? ","\tWhat do you call a shoe made from a banana? "]
            answer=["popmusic","greece","depresso","navigator","slipper"]
            print(f"\n{name.title()}, you have selected Medium level!")
            print(f"\nYou have total of {health} lives for total of 5 questions!!")
            print("\nOnce you go wrong, you will lose 1 life!!")
            print("\nIf you could answer all then move onto hard level!!")
            for i in range(0,5):
                print("\nThis is ur Question:"+str(i+1)+"")
                q=input(question[i])
                if q == answer[i]:
                    print("\nWell done,Its the right answer.")
                else :
                    print("\nOops,u got the answer wrong")
                    print(f"The right answer is {answer[i]}")
                    health-=1
                if health==0:
                    print("U ran out of lives,thanks for playing")
                    break
                polling_active=False
                print(exit.upper())
        else:
            print("\nFinish the easy level first.")        
    elif level == 'hard':
        confirmation = input("\nHave you plyed the easy and medium level(yes/no)? ")
        if confirmation == 'yes':
            question=["\tWhat is Joe Roots Favourite Fruit? ","\tWhat do you say to an arabic who majored in math? ","\tWhat kind of bird can open locks? ","\tWhat is the name of a bee which tastes sweet? ","\tWhat do you call a dinosaur which is sleeping? "]
            answer=["beetroot","algebra","turkey","jalebi","dinosnore"]
            print(f"\n{name.title()}, you have selected Hard level!")
            print(f"\nYou have total of {health} lives for total of 5 questions!!")
            print("\nOnce you go wrong, you will lose 1 life!!")
            print("\nIf you could answer all then you have completed the game fully:)")
            for i in range(0,5):
                print("\nThis is ur Question:"+str(i+1)+"")
                q=input(question[i])   
                if q == answer[i]:
                    print("\nWell done,Its the right answer.")
                else :
                    print("\nOops,u got the answer wrong")
                    print(f"The right answer is {answer[i]}")
                    health-=1
                    if health==0:
                        print("U ran out of lives,thanks for playing")
                        break
                polling_active=False
                print(exit.upper())
        else:
            print("\nPlay them first.")
            break        


                

    else:
        print("Type correctly...now rerun the code-_-")
        polling_active = False 

'''changelog__
v0.0.2 = -fixed the medium and hard level introerror
v0.0.3 = -added else for confirmation in medium level 
         -added else for confirmation in hard level
v0.0.4 = -impoted colorama module        
         -changed color of intro, creator,difficulty levels
v0.0.5 = -some allignment changes 
'''
