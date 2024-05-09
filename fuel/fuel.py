def main():
    fraction = get_input()
#    fin = f"{str(round(fraction*100))}%"
    fin = round(fraction*100)
    if fin <= 1:
        print("E")
    elif fin >= 99:
        print("F")
    else:
        print(f"{fin}%")


def get_input():
    while True:
        try:
            usr_input = input("Fraction: ")
            x, y = usr_input.split("/")
            fraction = int(x) / int(y)
            if fraction > 1:
                get_input()
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    return fraction

main()
