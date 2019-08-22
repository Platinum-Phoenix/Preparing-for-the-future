  

def interestRate_calculator():
    money = input ('How much money do you have in your bank account')
    years = input ('How many years are you intending to keep your money in your bank account')
    rate = input ('What is the interest rate')
    rate = float(rate) / 100
    answer = 0
    add_on = 0
    add_on = float (money) * float (rate)
    answer = float(money) + float (add_on) * float (years)
    print (''.join(str(answer)))

interestRate_calculator()    

