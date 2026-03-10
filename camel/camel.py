camel = input("Please enter name: ")
snake = ""

for letter in camel:
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter

print(snake)