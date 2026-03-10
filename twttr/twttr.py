user = input('Please enter text: ')
text_list = "aeiouAEIOU"

for l in user:
    if l not in text_list:
        print(l, end="")