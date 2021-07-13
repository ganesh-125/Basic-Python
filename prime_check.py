n = int(input("Enter a number to check prime :"))
# print(n//2)
count = 0
for i in range(2,((n//2)+1)):
    # print(i)
    if n%i==0:
        count = count +1
    if count ==1:
        print("Not Prime number")
        break
if count==0:
    print('Prime Number')


# Time complicity : O(n)