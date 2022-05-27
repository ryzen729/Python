print("Welcome to Treasure Island")
print("Your mission is to find the treasure.")
path = input("Choose Left or Right?\n")
if path == "Right":
    print("Game Over")
else:
    dest = input("You arrived at an island. Swim or wait?\n")
    if dest == "Swim":
        print("Game Over")
    else:
        color = input("Choose door. red,blue or yellow")
        if color == "red":
            print("Game Over")
        elif color =="blue":
            print("Game Over")
        else:
            print("YOU WIN!!!!!!")


