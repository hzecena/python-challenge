# modules
import os
import csv

# csv file path
csvpath = os.path.join('Resources', 'budget_data.csv')

# open csv file
with open(csvpath) as csvfile:

	budget_data = csv.reader(csvfile, delimiter= ',')
	header = next(budget_data)
	total_PL = 0
	total_months = 0
	change_list = []
	change = 0
	max_increase = 0
	max_decrease = 0

	for i, row in enumerate(budget_data):
		current_PL = int(row[1])
		total_months = total_months + 1
		total_PL = total_PL + current_PL
		if i > 0:
			change = current_PL - last_months_PL
			change_list.append(change)
			last_months_PL = int(row[1])
		else:
			last_months_PL = int(row[1])
		if change > max_increase:
			max_increase_month = row[0]
		if change < max_decrease:
			max_decrease = change
			max_decrease_month = row[0]
	average_change = sum(change_list)/len(change_list)
	print(f'Total Months: {total_months}')
	print(f'Total: {total_PL}')
	print(f'Average Change: {average_change}')
	print(f'Greatest increase in profits: {max_increase_month}, {max_increase}')
	print(f'Greatest decrease in profits: {max_decrease_month}, {max_decrease}')
	
