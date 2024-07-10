print("You are at start of forest u have to go in to get treasure.")
inventory = []

x = input("Do u wait till morning or go in now? (Now/Morning) ")
if x == "Now":
    print("You go in and find a blunt axe, a badminton racket and a dagger.")
    y = input("Do you want to pick up any? (Yes/No) ")
    if y == "Yes":
        print("Which tool would u like to pick up?")
        z = input("(Dagger/Axe/Racket)")
        inventory.append(z)
        print("You have "+str(inventory)+" in your inventory")
    
    if y == "No":
        print("Alright. Remember, you cannot change your decision.")
    

if x == "Morning":
    print("You find out the forest becomes a restricted area at night, you have no choice but to go at night.")
    print("You go in and find a blunt axe, a badminton racket and a dagger.")
    y = input("Do you want to pick up any? (Yes/No) ")
    if y == "Yes":
        print("Which tool would u like to pick up?")
        z = input("(Dagger/Axe/Racket)")
        inventory.append(z)
        print("You have "+str(inventory)+" in your inventory")
    
    if y == "No":
        print("Alright. Remember, you cannot change your decision.")

