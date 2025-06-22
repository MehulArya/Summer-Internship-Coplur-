def palindrome(num):
    if num == num[::-1]:
        print("True")
    else:
        print("False")

x = input("Enter the Value to check Palindrome: ")
palindrome(x)