import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) == 3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].endswith('.csv')):
        sys.exit("Not a CSV file")
    else:
        header = []
        rows = []
        target_file = sys.argv[1]
        try:
            with open(target_file, 'r') as csvfile:
                csvreader = csv.reader(csvfile)
                header = next(csvreader)
                for row in csvreader:
                    rows.append(row)
        except FileNotFoundError:
            sys.exit("File doesn't exist")

    print(tabulate(rows, headers=header, tablefmt="grid"))


if __name__ == "__main__":
    main()
