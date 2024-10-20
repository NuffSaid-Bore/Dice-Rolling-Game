import random

roll_count = 0
while True:
    choice = input('Do you want to roll the dice (y/n): ')
    if choice == 'y':
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        roll_count += 1
        print(f'You have rolled {dice1} and {dice2}')
    elif choice == 'n':
        print(f'Thanks for playing. You rolled the dice {roll_count} times.')
        break
    else:
        print('Invalid choice, Please try again')