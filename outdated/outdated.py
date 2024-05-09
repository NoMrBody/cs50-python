def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    while True:
        try:
            usr_input = input("Date: ")
            if usr_input.__contains__("/"):
                mm, dd, yy = usr_input.split("/")
                # output shoild be year-month-day
                if int(mm) > 12 or int(dd) > 31:
                    raise ValueError
                print(f"{int(yy)}-{(int(mm)):02}-{int(dd):02}")
                break
            elif usr_input.__contains__(","):
                left_part, right_part = usr_input.split(",")
                month, day = left_part.split(" ")
                if int(day) > 31:
                    raise ValueError
                if month in months:
                    print(f"{int(right_part.strip())}-{(months.index(month) + 1):02}-{(int(day)):02}")
                break

        except ValueError:
            pass

main()
