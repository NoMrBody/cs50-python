import random

def main():
    lvl = get_level()
    correct = 0
    incorrect = 0

    for i in range (10):
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        sum = x + y
        while True:
            try:
                usr_input = input(f"{x} + {y} = ")
                casted = int(usr_input)
                if (casted == sum):
                    correct +=1
                    break
                else:
                    incorrect += 1
                    if (incorrect == 3):
                        print(f"EEE\n{x} + {y} = {sum}")
                        break
                    else:
                        print("EEE")
            except ValueError:
                incorrect += 1
                if (incorrect == 3):
                    print(f"EEE\n{x} + {y} = {sum}")
                    break
                else:
                    print("EEE")
    print(f"Score: {correct}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if not (1 <= level <= 3):
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    match level:
        case 1:
            return random.randint(0, 9)
        case 2:
            return random.randint(10, 99)
        case 3:
            return random.randint(100, 999)



if __name__ == "__main__":
    main()
