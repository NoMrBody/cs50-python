def main():
    greeting = input("Greeting: ").strip().lower()
    if greeting.__contains__("hello"):
        print("$0")
    elif greeting.startswith("h" or "H") and not (greeting.__contains__("hello")):
        print("$20")
    else: print("$100")

main()
