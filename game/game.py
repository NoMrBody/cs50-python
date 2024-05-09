import random
import sys

def main():
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError
            break
        except ValueError:
            pass

    number = random.randint(1, level)

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > number:
                print("Too large!")
                pass
            elif guess < number:
                print("Too small!")
                pass
            else: sys.exit("Just right!")
        except ValueError:
            pass

if __name__ == "__main__":
    main()
