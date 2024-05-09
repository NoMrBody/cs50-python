def main():
    greeting = input("Greeting: ").strip().lower()
    print(value(greeting))


def value(greeting):
    if greeting.lower().__contains__("hello"):
        return "$0"
    elif greeting.lower().startswith("h") and not (greeting.__contains__("hello")):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()
