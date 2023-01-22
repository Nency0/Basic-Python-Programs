print("Loan EMI Calculator")

p = float(input('Please enter principal amount: '))
i = float(input('Please enter annual interest rate in %: '))
t = float(input('Please enter tenure in years: '))

n = t*12
r = (i/(12*100))
e = (p*r*((1+r)**n)) / (((1+r)**n)-1)


print(' \n EMI: {} \n Principal Amount: {} \n Interest Amount: {} \n Total Payable: {} '.format(e,p,(e*n)-p,e*n))
