import os
import csv

# csv file path
csvpath = os.path.join('Resources', 'budget_data.csv')

total_months = 0
total_PL = 0

# open csv file
with open(csvpath) as csvfile:

	budget_data = csv.reader(csvfile, delimiter= ',')

#The total number of months included in the dataset
	for i in budget_data:
		if str(i[0][0:3]) == 'Jan': 
			total_months = total_months + 1
			current_PL = int(i[1])
			total_PL = total_PL + current_PL
			last_month_PL = int((i-1)[1])
#print(total_PL)
print(total_months)
print(average_change)