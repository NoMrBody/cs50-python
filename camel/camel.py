def main():
    camel = input("camelCase: ").strip()
    for char in camel:
        if char.isupper():
            camel = camel[:camel.index(char)] + "_" + camel[camel.index(char):]

    print(camel.lower())


main()
