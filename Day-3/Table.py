def Table(n):
    print("Table of {}".format(n))
    print("\n")
    for i in range(1,11):
        print("{} * {} = {} ".format(n,i,i*n))

for i in range(5,11):
    Table(i)
    print("\n")