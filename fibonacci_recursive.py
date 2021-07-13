n = int(input("Enter a number to find fibonacci number of that position :"))


def fibo(num):
    if num==0:
        return 0
    elif num<=2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

print(fibo(n))
