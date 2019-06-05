import pandas as pd

path= "budget_data.csv"
pybank= pd.read_csv(path)
pybank.head()

pybank.count()

numofmonths= pybank.shape[0]

total_net = pybank['Profit/Losses'].sum()

profit_losses_list = pybank['Profit/Losses'].tolist()

average_change_list = []
average_change_list_org=[]

for i in range(1, len(profit_losses_list)):
    ave_change = profit_losses_list[i] - profit_losses_list[i - 1]
    average_change_list.append(ave_change)
    average_change_list_org.append(ave_change)
    
average_change = sum(average_change_list)/len(average_change_list)

average_change_list.sort()

greatest_decrease = average_change_list[0]

greatest_increase = average_change_list[len(average_change_list)-1]

min_index = average_change_list_org.index(greatest_decrease) + 1
max_index = average_change_list_org.index(greatest_increase) + 1

gr_dec_month = pybank['Date'][min_index]
gr_inc_month = pybank['Date'][max_index]

# Print to console:

print('Financial Analysis')
print('----------------------------------')
print('Total Months:', numofmonths + 1)
print('Total net Profit/Losses: $', total_net)
print('Average Change: $', average_change)
print('Greatest Increase in Profits:', gr_inc_month, greatest_increase)
print('Greatest Decrease in Profits:', gr_dec_month, greatest_decrease)
# Output to file:

file = open('pybank.txt','a')

file.write('Financial Analysis\n')
file.write('----------------------------------\n')
file.write(f'Total Months: {numofmonths + 1}\n')
file.write(f'Total: {total_net}\n')
file.write(f'Average  Change: {average_change}\n')
file.write(f'Greatest Increase in Profits: {gr_inc_month} ({greatest_increase})\n')
file.write(f'Greatest Decrease in Profits: {gr_dec_month} ({greatest_decrease})\n')
file.close()

