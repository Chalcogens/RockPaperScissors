import random

def play():
    user = ""
    while user not in ['r', 'p','q']:
        if user != "":
            print("Invalid input. Please input either 'r', 'p', or 's'.")
        user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n").lower()
    computer = random.choice(['r','p','s'])
    computer_guess = f"The computer played {computer}."
    if user == computer:
        return f"It's a tie! {computer_guess}"
    if iswin(user,computer):
        return f"You won! {computer_guess}"
    else:
        return f"You lost! {computer_guess}"

def iswin(play,opp):
    if (play == 'r' and opp == 's') or (play == 's' and opp == 'p') or (play == 'p' and opp == 'r'):
        return True

print(play())
print()