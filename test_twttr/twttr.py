def main():
    # მომხმარებლისგან ვიღებთ ტექსტს
    word = input("Input: ")
    # ვიძახებთ shorten ფუნქციას და ვბეჭდავთ შედეგს
    print(f"Output: {shorten(word)}")


def shorten(word):
    vowels = "aeiouAEIOU"
    result = ""
    for char in word:
        # თუ სიმბოლო არ არის ხმოვანი, ვამატებთ შედეგში
        if char not in vowels:
            result += char
    return result


if __name__ == "__main__":
    main()