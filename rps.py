import random

user_score, computer_score, draw_time = 0, 0, 0
options = ['rock', 'paper', 'scissors']

while True:
    user_input = input("Type 'rock', 'paper', 'scissors' & 'Q' to quit: ").lower()
    if user_input == 'q':
        break
    if user_input not in options:
        continue

    computer_picked = random.choice(options)
    print("Computer picked " + computer_picked)

    if user_input == computer_picked:
        print("Draw")
        draw_time += 1
    elif (user_input == 'rock' and computer_picked == 'scissors') or \
         (user_input == 'paper' and computer_picked == 'rock') or \
         (user_input == 'scissors' and computer_picked == 'paper'):
        print("You won!")
        user_score += 1
    else:
        print("Computer won!")
        computer_score += 1

print("Bye Bye")
print(f"You won {user_score} times")
print(f"Computer won {computer_score} times")
print(f"Draw {draw_time} times")
