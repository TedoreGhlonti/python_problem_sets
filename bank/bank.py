client = input("Greeting: ").strip().lower()
if client.startswith("hello"):
    print("$0")
elif client.startswith("h"):
    print("$20")
else:
    print("$100")