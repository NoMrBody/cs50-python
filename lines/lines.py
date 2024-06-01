import sys
import os
directory = 'path/to/file'
def main():
    number_of_lines = 0
    if len(sys.argv[:]) == 1:
        sys.exit('Too few command-line arguments')
    target_file = search_file(sys.argv[1])
    try:
        with open(target_file) as file:
            for line in file:
                if (is_blank(line) or line.startswith('#')):
                    continue
                else: number_of_lines +=1
    except FileNotFoundError:
        sys.exit('File does not exist')
    print(number_of_lines)

def is_blank(st):
    return st.lstrip()==""

def search_file(clarg):
    fname, extension = clarg.split(".")
    if (extension != "py"):
        sys.exit('Not a Python file')
    for _ in os.listdir(directory):
        full_path = os.path.join(directory, fname, clarg)
        if os.path.isfile(full_path):
            return full_path
        else: sys.exit("File does not exist")

if __name__ == "__main__":
    main()