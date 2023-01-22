
print('Given an array nums ( read as input by the user), separate the odd and even numbers from the array and print them on separate lines.')
array=[]
number=int(input("Enter total number of elements: "))
for i in range(0,number):
    a=int(input("Enter a number: "))
    array.append(a)
even=[]
odd=[]
for i in array:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)


print(odd)
print(even)