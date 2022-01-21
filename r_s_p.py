import random

def play(): 
    user = input("Choose your weapon... \n 'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'It\'s a tie'

    # r > s , s > p, p > r

    if is_win(user,computer):
        return '!!!Win!!!' 
    
    return '!!!Lost!!!'

def is_win(player, oppenent):
    if (player == 'r' and oppenent == 's') or (player == 's' and oppenent == 'p') \
        or (player == 'p' and oppenent == 'r'):
        return True
print(play())



