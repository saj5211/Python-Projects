balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02
month = 0
totalpaid = 0

def minimumPayment(monthlyPaymentRate, balance):
    monthlyPayment = balance * monthlyPaymentRate
    return monthlyPayment

def UnpaidBalance(balance, monthlyPayment):
        unpaidbalance = balance - monthlyPayment
        return unpaidbalance 
def Interest(annualInterestRate, unpaidbalance):
    interest = annualInterestRate/12 * unpaidbalance
    return interest
def newBalance (interest, unpaidbalance):
        newbalance = interest + unpaidbalance
        return newbalance
while month < 12:
    month += 1
    print ('Month: ' + str(month))
       
                                                             
    monthlyPayment= minimumPayment(monthlyPaymentRate, balance)
    roundedmonthlypayment = round (monthlyPayment, 2)
    print ('Minimum monthly payment: ' + str(roundedmonthlypayment))    
    
    unpaidbalance =UnpaidBalance(balance, monthlyPayment)
    interest = Interest(annualInterestRate, unpaidbalance)
    newbalance = newBalance (interest, unpaidbalance)
    balance = newbalance
    newroundedbalance = round (newbalance, 2)
    print ('Remaining Balance: ' + str(newroundedbalance))
    totalpaid += monthlyPayment
    newtotalpaid = totalpaid
    roundedtotalpaid = round (totalpaid, 2)

print ('Total Paid: ' + str(roundedtotalpaid))
newroundedtotal = round (newbalance, 2)
print ('Remaining Balance: ' + str(newroundedtotal))