import sys
import csv


def main():
    if len(sys.argv)==1 or len(sys.argv)==2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv)>3:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1].endswith('.csv')):
        sys.exit(f"Could not read {sys.argv[1]}")
    else:
        target_file = sys.argv[1]
        dest_file = sys.argv[2]
        try:
            with open(target_file, 'r') as csvfile_in:
                csvreader = csv.DictReader(csvfile_in)
                fieldnames = ["first", "last",] + [field for field in csvreader.fieldnames if field != "name"]

                with open(dest_file, 'w') as csvfile_out:
                    csvwriter = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
                    csvwriter.writeheader()
                    for item in csvreader:
                        first, last = item['name'].split(', ')
                        del item['name']
                        item['first'] = last
                        item['last'] = first
                        csvwriter.writerow(item)
        except FileNotFoundError:
            sys.exit("File doesn't exist")


if __name__=="__main__":
    main()
