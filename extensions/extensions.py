def main():
    inp = input("File name: ").strip().lower()

    if inp.endswith(".gif"):
        print("image/gif")
    elif inp.endswith(".jpg") or inp.endswith(".jpeg"):
        print("image/jpeg")
    elif inp.endswith(".png"):
        print("image/png")
    elif inp.endswith(".pdf"):
        print("application/pdf")
    elif inp.endswith(".txt"):
        print("text/plain")
    elif inp.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
