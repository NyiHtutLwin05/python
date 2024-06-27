name = input("What's your name? ")

with open("text.txt","a") as file:
    file.write(f"{name}\n")