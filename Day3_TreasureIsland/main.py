choices = [
    'You\'re at a cross road. Where do you want to go? Type "left" or "right" \n',
    'You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n',
    "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n",
]

extra_text =[
    "You fell into a hole. Game Over.",
    "You get attacked by an angry trout. Game Over.",
    "It's a room full of fire. Game Over.",
    "You found the treasure! You Win!",
    "You enter a room of beasts. Game Over."
]

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")


if input(choices[0].lower()) == "left":
    if input(choices[1].lower()) == "wait":
        choice = input(choices[2].lower())
        if choice == "red":
            print(extra_text[2])
        elif choice == "yellow":
            print(extra_text[3])
        elif choice == "blue":
            print(extra_text[4])
    else:
        print(extra_text[1])
else:
    print(extra_text[0])



