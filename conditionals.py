# balance = 1000

# choice = input("1-Balance  2-Deposit  3-Withdraw: ")

# if choice == "1":
#     print("Balance:", balance)

# elif choice == "2":
#     amount = int(input("Amount to deposit: "))
#     balance += amount
#     print("New balance:", balance)

# elif choice == "3":
#     amount = int(input("Amount to withdraw: "))
#     if amount <= balance:
#         balance -= amount
#         print("New balance:", balance)
#     else:
#         print("Not enough money")

# else:
#     print("Invalid option")

balance = 1000

choice = input("1-Balance  2-Deposit  3-Withdraw: ")

match choice:
    case "1":
        print("Balance:", balance)

    case "2":
        amount = int(input("Amount to deposit: "))
        balance += amount
        print("New balance:", balance)

    case "3":
        amount = int(input("Amount to withdraw: "))
        if amount <= balance:
            balance -= amount
            print("New balance:", balance)
        else:
            print("Not enough money")

    case _:
        print("Invalid option")    