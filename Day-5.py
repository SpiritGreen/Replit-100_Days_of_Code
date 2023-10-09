place = input('\033[36mWhere are you from? \033[0m')
if place == 'Gallifrey':
    print('\033[33mThen you might be a Doctor!\033[0m')
elif place == 'Betelgeuse':
    print('\033[33mAre you Ford Prefect?\033[0m')
else:
    print("\033[33mLooks like you're Arthur Dent!\033[0m")