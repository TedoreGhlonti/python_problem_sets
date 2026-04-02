grocery_list = {}

while True:

    try:
     user_item = user_item = input().upper().strip()
     if user_item in grocery_list:
        grocery_list[user_item] += 1
     else:
        grocery_list[user_item] = 1

    except EOFError:
       break

for item in sorted(grocery_list.keys()):
    print(f"{grocery_list[item]} {item}")