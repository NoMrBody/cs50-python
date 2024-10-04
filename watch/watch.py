import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    # pattern = r"src=\"(https?)://(?:www\.)?youtube.com/embed/(.)\""
    matches = re.search(r"src=\"(https?)://(?:www\.)?youtube.com/embed/(\w+)\"", s)
    if matches:
        return f"https://youtu.be/{matches.group(2)}"
    else:
        return None


if __name__ == "__main__":
    main()
