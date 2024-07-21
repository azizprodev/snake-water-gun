from random import randint

computer_user = randint(1, 3)
manual_user = int(input("Press (1) for snake, (2) for water, and (3) for gun: "))

dic = {1: "Snake", 2: "Water", 3: "Gun"}

print(f"You Choose {dic[manual_user]} and Computer choose {dic[computer_user]}")

if (computer_user == manual_user):
    print("match tie!")
else:
    if ((computer_user == 1 and manual_user == 2) or (computer_user == 2 and manual_user == 3) or (computer_user == 3 and manual_user == 1)):
        print(f"Computer win!")
    else:
        print(f"You win!")