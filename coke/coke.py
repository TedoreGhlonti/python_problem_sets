amount_due = 50

while amount_due > 0:
    user = int(input("Please enter coin: "))
    if user == 25 or user == 10 or user == 5:
        amount_due -= user

    if amount_due > 0:
        print(f"Amount Due: {amount_due}")

print(f"Change Owed: {abs(amount_due)}")