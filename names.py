name = []

for _ in range(3):
    name.append(input("What's your name? "))

for x in sorted(name):
    print(f"hello, {x}")