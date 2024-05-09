def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            if not s[len(s)-1:].isalpha():
                if not contains_punctuation(s):
                    return True
    else:
        return False

def contains_punctuation(p):
    punct = [".", "?", "!", ";"," "]
    for char in p:
        if char in punct:
            return True
    return False


main()
