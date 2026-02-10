expenses = []
income = []

print("💰 daily money tracker started")

while True:
    print("\nchoose option:")
    print("1. add expense")
    print("2. add income")
    print("3. view summary")
    print("4. save and exit")

    choice = input("enter choice: ")

    if choice == "1":
        name = input("enter expense name: ")
        amount = float(input("enter amount: "))
        expenses.append(amount)
        print("✅ expense added")

    elif choice == "2":
        name = input("enter income name: ")
        amount = float(input("enter amount: "))
        income.append(amount)
        print("✅ income added")

    elif choice == "3":
        print("\n📊 summary")
        print("total expenses:", sum(expenses))
        print("total income:", sum(income))
        print("balance:", sum(income) - sum(expenses))

    elif choice == "4":
        f = open("money_tracker.txt", "w")
        f.write("total expenses: " + str(sum(expenses)) + "\n")
        f.write("total income: " + str(sum(income)) + "\n")
        f.write("balance: " + str(sum(income) - sum(expenses)))
        f.close()

        print("📁 data saved")
        print("👋 exiting tracker")
        break

    else:
        print("❌ invalid choice")
