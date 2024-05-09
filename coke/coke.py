def main():
    cost = 50
    income = 0
    print(f"Amount Due: {cost - income}")
    while income < cost:
        plus = int(input(f"Insert Coin: "))
        if plus == 5 or plus == 10 or plus == 25:
            income += plus
        print(f"Amount Due: {cost - income}")
    if income > cost:
        print(f"Change Owed: {income - cost}")
    else:
        print(f"Change Owed: {income - cost}")


main()
