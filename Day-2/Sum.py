

def sum(n):
    if n <=1:
        return 1
    else :
        return n + sum(n-1)

a=int(input("Enter a number : "))
sum = sum(a)
print("sum of all natural number from 1 to {} is {}".format(a,sum))