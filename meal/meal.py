def main():
    customer = input("Please enter your time: ")
    result = convert(customer)

    if 7.0 <= result <= 8.0:
        print("breakfast time")
    elif 12.0 <= result <= 13.0:
        print("lunch time")
    elif 18.0 <= result <= 19.0:
        print("dinner time")
    else:
        return

def convert(time):
    hours, minutes = time.split(":")
    new_time = float(hours) + float(minutes) / 60
    return new_time

if __name__ == "__main__":
    main()




















