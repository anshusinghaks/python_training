# age =int(input("enter a age :"))

# if age >= 18:
#     print("Elligible to vote")
# else:
#     print("Not eligible to vote")    

# marks = float(input("Enter the marks :"))
# if marks >= 40:
#     print("passed")
# else:
#     print("Failed")

# year = int(input("Enter year:"))
# if (year % 400 == 0) or (year%4 == 0 and year%100 != 0):
#     print("Leap year")
# else:
#     print("Not leap year")

# year = int(input("Enter year: "))

# if ((year % 400 == 0)) or ((year % 4 == 0) and (year % 100 != 0)):

#     print("Leap year")

# else:
#     print("Not leap year")

# ch = input("Enter a character:")
# if ch == ("a" or "e" or "i" or "o" or "u"):
#     print("vowels")
# else:
#     print("consonant")

# for i in range (1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# num = int(input("enter a number:"))
# for i in  range(1,11):
#     print(num*i)

# num = int(input("Enter a number:"))
# if num%2==0:
#     print("even nuber")
# else:
#     print("odd number")

# for num1 in range(1,6):
#     for num2 in range(1,6):
#         print(num1,num2)
#     print()

# for i in range(1,6):
#     for j in range(i):
#         print("*",end="")
#     print()

# num= int(input("enter a number"))
# print(f"table for {num}:-")
# for i in range (1,11):
#     print(f"{num}x{i}={num*i}")

# n= int(input("enter a number :"))
# sum = 0
# for i in range (1,n+1):
#     if i%2==0:
#         sum+=i
# print("sum of even number from 1 to n is",sum)

# num = int(input("Enter a number :"))
# for i in range(1,11):
#     print(num*i)
# count = 0
# for i in range(1,101):
#     if i%3==0:
#           count=count+1
# print(count)

correct_password = "12345"

for i in range(5):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login successful")
        break
    else:
        print("Wrong password")

else:
    print("Account locked")
  
