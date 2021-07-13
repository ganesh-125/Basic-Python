n = int(input("Enter a number to find fibonacci series :"))
num1 = 0
num2 = 1
next = 1
# O/P : 0 1 1 2 3 4
if (n<0):
    print("Not valid Number")
else:
    for i in range(n):
        print(num1)
        num1=num2
        num2=next
        next=num1+num2