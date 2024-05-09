import inflect
import sys

def main():
    p = inflect.engine()
    name_list = []
    while True:
        try:
            usr_input = input("Name: ").title()
            name_list.append(usr_input)
        except EOFError:
            print()
            joined_list = p.join(name_list)
            sys.exit(print(f"Adieu, adieu, to {joined_list}"))

if __name__ == "__main__":
    main()
