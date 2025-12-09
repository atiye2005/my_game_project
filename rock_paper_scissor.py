import random

choices = ["r","p","s"]

choices_dict ={
    "r":"rock",
    "p":"paper",
    "s": "sessers"
}
user_score = 0
ai_score = 0


for i in range(5):
    
    user_choices = input("enter your choice [r,p,s]:")

    ai_choice = random.choice(choices)

    if user_choices in choices:
        print(f"you choose {choices_dict[user_choices]} and ai choose {choices_dict[ai_choice]}")
        if user_choices == ai_choice:
            print("mosavi")
        elif user_choices == "r" and ai_choice == "s":
            print("user +1")
            user_score += 1

        elif user_choices == "p" and ai_choice == "r":
            print("user +1")
            user_score += 1
        elif user_choices == "s" and ai_choice == "p":
            print("user +1")
            user_score += 1
        else:
            print("ai +1")
            ai_score += 1
    else:
        print("try again")
    
    print(f"user : {user_score} / ai : {ai_score}")
    print('\n', "_" *15 ,'\n')

    if user_score == 10 or ai_score == 10:
        break

if user_score == 10:
    print("you win")
else:
    print("you lose")


