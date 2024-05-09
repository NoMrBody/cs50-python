# def main():
#     vowels = ["a", "e", "i", "o", "u"]
#     tweet = input("Input: ")
#     for char in tweet:
#         if char.lower() in vowels:
#             tweet = tweet.replace(char, "")
#     print(f"Output: {tweet}")

# main()

def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    for char in word:
        if char.lower() in vowels:
            word = word.replace(char, "")
    return word


if __name__ == "__main__":
    main()
