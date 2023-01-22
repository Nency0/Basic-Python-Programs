print("For any given integer array A ( read as input by the user ). How will you find the second largest element/value in the array? Write code for the same.")

array=[]
number=int(input("Enter total number of elements: "))
for i in range(0,number):
    a=int(input("Enter a number: "))
    array.append(a)

array.sort()

print("Second Largest value of Array is ",array[-2])

