print("Given a number A ( read as input ), find the sum of its digits.")

a=input("Enter a number :")
sum=0
for i in a:
    sum=sum+int(i)

print(sum)
