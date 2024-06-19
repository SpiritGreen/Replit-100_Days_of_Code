# Fake fan question generator

show = input("What's your favourite show? ")

if show == "Hitchhiker's Guide to the Galaxy":
    print('Great choice! But are you a true fan?')
    character = input("Who's your favourite character? ")
    if character == "Arthur Dent":
        print("Ok, let's see if you know the character well.")
        planet = input("What planet does Arthur Dent come from? ")
        if planet == 'Earth':
            print("You're right!")
        else:
            print("Nope! You're not a true fan.")
    elif character == "Ford Prefect":
        print("That's my favourite character too!")
        home = input("Well. Where's Ford Prefect from? ")
        if home == 'Betelgeuse star system':
            print("You're a true fan!")
        else:
            print("Nope! You're not a true fan.")
    else:
        print("I didn't think of that character.")
else:
    print("I didn't think of that show.")