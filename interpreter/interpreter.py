def main():
    data = input("Expression: ").strip()

    x,y,z = data.split(" ")

    if(y == "+"):
        print(float(x) + float(z))
    elif y == "-":
        print(float(x) - float(z))
    elif y == "*":
        print(float(x) * float(z))
    elif y == "/" and float(z) != 0.0:
        print(float(x) / float(z))

main()
