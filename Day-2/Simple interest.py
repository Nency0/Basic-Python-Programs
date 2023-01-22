from time import time


amount = float(input("Enter Principal Amunt : "))
Time = float(input("Enter Time period :"))
Rate =float(input("Enter Interest Rate :"))

print("Simple interest of Principal amount {} with interest rate {} and time {} is {}".format(amount,Rate,Time,(amount*Rate*Time)/100))