# Q1 Find Factorial
fact = int(input("Enter a value to find factorial: "))
for i in range(1, fact):
    fact*=i
    print(fact, end=" ")
print(f"\nFactorial for the given number is: {fact}")

# Q2 Create a Bill and add features to display item price and total amount on the bill.
bill_list = []
while True:
    print('''
     1. Create Bill
     2. Display Item Price and Total Bill Amount
     3. Display Total
     4. Exit
     ''')

    choice = input("Enter your choice: ")

    if choice == '1':
        for j in range(100):
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))

            bill_list.append([name, price])

            add_more = input("Add another item? 0 for yes and 1 for no: ")
            if add_more != '0':
                break

    elif choice == '2':
        total = 0
        print("\nBill Items:")
        if len(bill_list) == 0:
            print("No items in the list")
        else:
            for item in bill_list:
                print(item[0], ": Rs. ", item[1])
                total = total + item[1]
            print("Total Bill Amount: Rs.", total)

    elif choice == '3':
        total = 0
        for item in bill_list:
            total = total + item[1]
        print("Total Bill Amount: Rs.", total)

    elif choice == '4':
        print("EXIT_SUCCESS")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
