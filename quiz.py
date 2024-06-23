print('Welcome to the quiz game!')

x = input('Wanna Play! ')

if x.lower() != 'yes':
    quit()
else:
    print("Let's go! ")

answer = input("What's CS stand for? ")

if answer.lower() == "computer science":
    print("Correct!")
else:
    print("Sorry, incorrect!")

answer = input("What's IDE stand for? ")

if answer.lower() == "intelligence":
    print("Correct! ")
else:
    print("Sorry, incorrect!")

print("See you!")