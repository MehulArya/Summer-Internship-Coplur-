#...........Question-2............
# studentName = input("Enter Students Name: ")
# studentsClass = input("Enter Class of the Student: ")
# Maths = int(input("Enter marks of Maths: "))
# Physics = int(input("Enter marks of Physics: "))
# Chemistry = int(input("Enter marks of Chemistry: "))
# English = int(input("Enter marks of English: "))
# Biology = int(input("Enter marks of Biology: "))
# totalMarks = Maths + Physics + Chemistry + English + Biology
# percentage = int((totalMarks/500) * 100)
#
# print(f"\n{studentName} of class {studentsClass} has scored {totalMarks} out of 500.\n\nPercentage: {percentage}%,\n"
#       f"\nMaths: {Maths}\nPhysics: {Physics}\nChemistry: {Chemistry}\nEnglish: {English}\nBiology: {Biology}\n")
#
# if  percentage >= 60:
#     print("Grade: A")
# elif percentage < 60 and percentage > 50:
#     print("Grade B")
# elif percentage < 50 and percentage > 40:
#     print("Grade C")
# elif percentage < 40 and percentage > 30:
#     print("Grade D")
# elif percentage < 30 and percentage > 20:
#     print("Grade E")
# else:
#     print("Grade: Fail")


#...........Question-3............
# fact = int(input("Enter a value to find factorial: "))
# for i in range(1, fact):
#     fact*=i
#     print(fact, end=" ")
# print(f"\nFactorial for the given number is: {fact}")

#...........Question-4............
# bill_list = []
# while True:
#     print('''
#      1. Create Bill
#      2. Display Item Price and Total Bill Amount
#      3. Display Total
#      4. Exit
#      ''')
#
#     choice = input("Enter your choice: ")
#
#     if choice == '1':
#         for j in range(100):
#             name = input("Enter item name: ")
#             price = float(input("Enter item price: "))
#
#             bill_list.append([name, price])
#
#             add_more = input("Add another item? 0 for yes and 1 for no: ")
#             if add_more != '0':
#                 break
#
#     elif choice == '2':
#         total = 0
#         print("\nBill Items:")
#         if len(bill_list) == 0:
#             print("No items in the list")
#         else:
#             for item in bill_list:
#                 print(item[0], ": Rs. ", item[1])
#                 total = total + item[1]
#             print("Total Bill Amount: Rs.", total)
#
#     elif choice == '3':
#         total = 0
#         for item in bill_list:
#             total = total + item[1]
#         print("Total Bill Amount: Rs.", total)
#
#     elif choice == '4':
#         print("EXIT_SUCCESS")
#         break
#
#     else:
#         print("Invalid choice. Please enter a number between 1 and 4.")

#...........Question-5............
# numbers = []
# while True:
#     a = int(input("enter value in the list: "))
#     numbers.append(a)
#     choice = input("If want to add more numbers press 0 else 1: ")
#     if choice == "0":
#         continue
#     else:
#         break
#
# smallest = numbers[0]
# for num in numbers:
#     if num < smallest:
#         smallest = num
#
# print("\nSmallest number:", smallest)
