from random import randint

def rock_paper_scissor():
    # rock = 0
    # paper = 1
    # scissor = 2
    computer = randint(0, 2)

    user_input = str(input('Choose any one: Rock, Paper or Scissor: ').lower())

    if user_input == 'rock' and computer==0:
        print("Computer chose rock as well: \n it's a draw")
    elif user_input =='rock' and computer==1:
        print('Computer chose paper: \n Computer wins')
    elif user_input =='rock' and computer==2:
        print('Computer chose scissor: \nYou win')

    elif user_input == 'paper' and computer==0:
        print("Computer chose rock: \n You win")
    elif user_input=='paper' and computer==1:
        print("Computer chose paper as well: \n It's a draw")
    elif user_input=='paper' and computer==2:
        print('Computer chose scissor: \nComputer wins')

    elif user_input == 'scissor' and computer==0:
        print("Computer chose rock: \n Computer wins")
    elif user_input=='scissor' and computer==1:
        print('Computer chose paper: \n You win')
    elif user_input=='scissor' and computer==2:
        print("Computer chose scissor as well: \nIt's a draw")

    else:
        print('invalid input')

i=0
print('''
=========================================================
|   Rock, Paper, Scissor                                 |
|   (Best of 3)                                          |
=========================================================
''')
while i<3:
    rock_paper_scissor()
    i+=1


        
