def task2():
    print("Soda Vending Machine")

    amount = 0.00

    while amount <= 1.00:
        print(f"Current amount ${amount:.2} out of $1.00")
        print("Insert Coin")
        print("1. Toonie  ($2.00)")
        print("2. Loonie  ($1.00)")
        print("3. Quarter ($0.25)")
        print("4. Dime    ($0.10)")
        print("5. Nickel  ($0.05)")
        x = int(input("Selection [1-5]? "))
        if x < 1 or x > 5:
            print("Invalid Selection!")
        elif x == 1:
            amount = amount + float(2.00)
        elif x == 2:
            amount = amount + float(1.00)
        elif x == 3:
            amount = amount + float(0.25)
        elif x == 4:
            amount = amount + float(0.10)
        elif x == 5:
            amount = amount + float(0.05)
        if amount < 1.00:
            pass

    rem = amount - 1
    print(f"Total amount provided: ${amount:.2}")

    if rem > 0:
        print("Thank you for your purchase")
        print(f"Please take your change {rem:.2}")
    else:
        print("Thank you for your purchase")
task2()