import os
import csv

#opened the csv file
budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    #excludes the header row
    next(csvreader)

    #initializes all of the variables used
    total_months = 0

    total = 0
    initial_change = 0
    next_change = 0
    total_sum = 0
    
    total_sum_array = []

    max_date = ""
    max_change = 0
    min_date = ""
    min_change = 0

    #loops through each row
    for row in csvreader:

        #calculates the marginal change
        initial_change = next_change
        next_change = int(row[1])
        total_sum = next_change - initial_change

        #excludes the first change
        if(not(initial_change == 0)):
            total_sum_array.append(total_sum)

            #ensures the values of max and min change hold
            if(total_sum > max_change):
                max_change = total_sum
                max_date = str(row[0])
            if(total_sum < min_change):
                min_change = total_sum
                min_date = str(row[0])
            

        total_months += 1

        total += int(row[1])  
        
    average = float((sum(total_sum_array))/(total_months-1))
    rounded_average = round(average, 2)

    print("")
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${rounded_average}")
    print(f"Greatest Increase in Profits: {max_date} (${max_change})")
    print(f"Greatest Decrease in Profits: {min_date} (${min_change})")


#exports to txt
file = open("Analysis/Analysis_PyBank.txt","w")
file.write("Financial Analysis\n")
file.write("----------------------------\n")
file.write(f"Total Months: {total_months}\n")
file.write(f"Total: ${total}\n")
file.write(f"Average Change: ${rounded_average}\n")
file.write(f"Greatest Increase in Profits: {max_date} (${max_change})\n")
file.write(f"Greatest Decrease in Profits: {min_date} (${min_change})\n")
file.close()