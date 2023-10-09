print('Welcome to your adventure simulator. I am going to ask you a bunch of questions and then create an epic story with you as the star!')
print()

name = input('What is your name? ')
enemy = input("What is your worst enemy’s name? ")
superpower = input('What is your superpower? ')
place = input('Where do you live? ')
food = input('What is your favorite food? ')
print()

print(f'Hello, \033[36m{name}\033[0m! Your ability to \033[33m{superpower}\033[0m will make sure you never have to look at \033[31m{enemy}\033[0m again. Go eat \033[32m{food}\033[0m as you walk down the streets of \033[35m{place}\033[0m and use \033[33m{superpower}\033[0m for good and not evil!')