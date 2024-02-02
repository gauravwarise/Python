num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not prime number")
            break
    else:
        print(num, "prime number")
else:
    print(num, "is not prime number")

# a= input("Enter your string: ")

# b=a[::-1]

# if a==b:
#     print("string is palindrome")
# else:
#     print("String is not palindrome")

# n = int(input())
# for i in range(n):
#     if (n%i)==0:
#         print("prime")
#         break
#     else:
#         print("not prime")
#         break
