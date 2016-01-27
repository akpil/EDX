balance = 999999
annualInterestRate = 0.18
monthlyInterestRate = annualInterestRate / 12.0
monthlyLowerBound = balance/12
monthlyUpperBound = (balance *((1 + monthlyInterestRate)**12))/12.0
while(True):
    checkbalance = balance
    midMonthlyPayment = (monthlyLowerBound + monthlyUpperBound)/2
    for Month in range(1, 13):
        monthlyUnpaidBalance = checkbalance - midMonthlyPayment
        checkbalance = monthlyUnpaidBalance +(monthlyInterestRate*monthlyUnpaidBalance)
    if(round(checkbalance,2) == 0.0):
        print 'Lowest Payment: ' + str(round(midMonthlyPayment,2))
        break
    elif(checkbalance > 0):
        monthlyLowerBound = midMonthlyPayment
    else:
        monthlyUpperBound = midMonthlyPayment
