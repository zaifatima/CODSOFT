import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")

while True:

    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")
    ch = int(input("Enter your choice :"))

    while ch > 3 or ch < 1:
        ch = int(input('Enter a valid choice please'))

    if ch == 1:
        choice_name = 'Rock'
    elif ch == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'
    print('User choice is \n', choice_name)
    print('Now its Computers Turn....')

    comp_choice = random.randint(1, 3)

    while comp_choice == ch:
        comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = 'RocK'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'
    print("Computer choice is \n", comp_choice_name)
    print(choice_name, 'Vs', comp_choice_name)
    if ch == comp_choice:
        print('Its a Draw', end="")
        result = "DRAW"
    if (ch == 1 and comp_choice == 2):
        print('paper wins =>', end="")
        result = 'Paper'
    elif (ch == 2 and comp_choice == 1):
        print('paper wins =>', end="")
        result = 'Paper'

    if (ch == 1 and comp_choice == 3):
        print('Rock wins =>\n', end="")
        result = 'Rock'
    elif (ch == 3 and comp_choice == 1):
        print('Rock wins =>\n', end="")
        result = 'RocK'

    if (ch == 2 and comp_choice == 3):
        print('Scissors wins =>', end="")
        result = 'Scissors'
    elif (ch == 3 and comp_choice == 2):
        print('Scissors wins =>', end="")
        result = 'Rock'
    if result == 'DRAW':
        print("<== Its a tie ==>")
    if result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")
    print("Do you want to play again? (Y/N)")
    ans = input().lower()
    if ans == 'n':
        break
    print("thanks for playing")
