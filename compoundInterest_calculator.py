def compound_Interest():
    money = input ('How much money is in your bank account')
    months = input ('How many months are you keeping your money in your bank account')
    rate = input ('what is the monthly interest rate')
    i = 0
    partial_answer = 0
    answer = 0
    add_on = 0
    while i < int (months):
        add_on = float (money) * ((float (rate) / 100)/int(months))
        money = float (money) + float (add_on)
        print (''.join(str(money)))
        i = i+1
    answer = money
    print (''.join(str(answer)))

    
compound_Interest()
    
    
