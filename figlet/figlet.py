from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    # when user doesn't use CL arguments
    if len(sys.argv[:]) == 1:
        usr_input = input("Input: ")
        figlet.setFont(font = random.choice(figlet.getFonts())) # get random font
        print("Output: " + figlet.renderText(usr_input))

    # if user inputs 2 CL arguments
    elif len(sys.argv[:]) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):

        if sys.argv[2] in figlet.getFonts():
            usr_input = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print("Output: " + figlet.renderText(usr_input))
        else:
            sys.exit("Invalid usage")

    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()

