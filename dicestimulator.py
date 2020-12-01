import random

print("please type roll to roll the dice: ")
inp_str = input()
dice = ["YES", "yes", "roll", "Yes", "ROLL", "Roll"]
d = ["NO", "no", "No"]
for i in dice:
    number = random.randint(1, 6)

    if number == 1:
        print("----------")
        print("|        |")
        print("|   O    |")
        print("|        |")
        print("----------")
    if number == 2:
        print("----------")
        print("|        |")
        print("| O    O |")
        print("|        |")
        print("----------")
    if number == 3:
        print("----------")
        print("|    O   |")
        print("|    O   |")
        print("|    O   |")
        print("----------")
    if number == 4:
        print("----------")
        print("| O    O |")
        print("|        |")
        print("| O    O |")
        print("----------")
    if number == 5:
        print("----------")
        print("| O     O |")
        print("|    O    |")
        print("| O     O |")
        print("----------")
    if number == 6:
        print("----------")
        print("| O    O |")
        print("| O    O |")
        print("| O    O |")
        print("----------")
    print("Do you want to Continue? Type yes or No")
    dice = input()
    if dice in d:
        break
    else:
        print("type yes or no")
        break



