def main():
    oclock = input("What time is it? ")
    conv = convert(oclock)

    if (7 <= conv <= 8):
        print("breakfast time")
    elif (12 <= conv <= 13):
        print("lunch time")
    elif (18 <= conv <= 19):
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    converted = 0.0
    if (0 <= float(hours) <= 23 and 0 <= float(minutes) <= 59):
        converted = float(hours) + float(minutes)/60
    return converted
if __name__ == "__main__":
    main()
