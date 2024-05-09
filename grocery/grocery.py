def main():
    grocery = {}
    default_value = 1
    while True:
        try:
            item = input()
            if item in grocery:
                new_value = increment(grocery[item])
                grocery[item] = new_value
            else:
                grocery[item] = default_value
        except EOFError:
            for itm in sorted(grocery.keys()):
                print(grocery[itm], itm.upper())
            break

def increment(val):
    return val + 1

main()
