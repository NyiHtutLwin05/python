import cowsay

user_score, total = 0, 0

cowsay.cow("Welcome to the quiz game! ")
x = input("Wanna play! ")

if x.lower() != 'yes':
    quit()
else:
    cowsay.cow("Alright! Let's gooo")

answer_input = str(input("What's Pycharm "))

if answer_input.lower() == "python":
    cowsay.cow("Correct! ")
else:
    cowsay.cow("Incorrect!")

cowsay.cow("Bye! ")