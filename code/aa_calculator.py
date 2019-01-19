def print_amounts(names, amounts):
    for i in range(0, len(names)): 
        print(names[i] + ': ' + str(amounts[i]))
    print('')

def calculate(pays, names):
    mean = round(sum(pays) / len(pays), 2)
    print('Mean Value: ' + str(mean) + '\n')
    # Calculate net amount
    net_amounts = pays.copy()
    net_amounts[:] = [round(mean - x, 2) for x in net_amounts]
    print('Earnings: ')
    print_amounts(names, net_amounts)
    for i in range(0, len(net_amounts)):
        while net_amounts[i] < 0:
            for j in range(0,len(net_amounts)):
                if j != i and net_amounts[j] > 0:
                    i_amount = net_amounts[i]
                    j_amount = net_amounts[j]
                    to_pay = 0
                    if j_amount > abs(i_amount):
                        to_pay = abs(i_amount)
                    else: 
                        to_pay = j_amount

                    print(names[j] + ' pays ' + str(to_pay) + ' to ' + names[i] )               
                    net_amounts[j] =  round(net_amounts[j] - to_pay, 2)
                    net_amounts[i] =  round(net_amounts[i] + to_pay, 2)

if __name__ == '__main__':
    amounts = [55,    31,     23,     0]
    names = ['A',   'B',    'C',     'D']
    print('Payments:')
    print_amounts(names, amounts)

    calculate(  
        [10,    30,     20,     15], 
        ['A',   'B',    'C',     'D']
    )
                     
                    






    

