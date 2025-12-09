import random

cups = int(input("how many cups: "))
chances = int(input("how many chances: "))

ai_goal = random.randint(1,cups)

print("-" * 10)

for i in range(chances):
    word = "s"
    if chances - i == 1:
        word = " "
    print(f"{chances - i} chance{word} left.")
    user_guess = int(input(f"Guess [1_{cups}]: "))

    if user_guess == ai_goal:
        print("you guessed right")
        break
    else:
        print("wrong guess")

    print("-" * 15)    

if user_guess == ai_goal:
    print("-" * 15)
    print("you won !")
else:
    print(f"the right anwser is {ai_goal}")
    print("you lose!") 
