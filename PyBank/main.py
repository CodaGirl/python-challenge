
import os

import csv


csvpath = os.path.join('..', 'Pybank', 'budget_data.csv')


months=[]
Profit = []
revenue = []
average = []
TotalRevenue = 0





# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)
    next(csvreader,None)

    print(csvreader)

  
    # Read each row of data after the header
    for row in csvreader:
     
        months.append(row[0])
        Profit.append(int(row[1]))
        monthsT = len(months)
        TotalRevenue += int(row[1])
    for i in range(0,monthsT):
        if i==0:
            average.append(0)
        else:    
            average.append(Profit[i]-Profit[i-1])
            
    average_change= round(sum(average)/(len(average)-1),2)
    
    Greatest_Inc=max(average)
    Max=average.index(Greatest_Inc)
    MaxMonth=months[Max]
    
    Greatest_Dec=min(average)
    Min=average.index(Greatest_Inc)
    MinMonth=months[Min]
      
    #for i in range(monthsT):
   
   
  
        
 
       
    output_path = os.path.join('..', 'PyBank', 'OutputBank.csv')
    


#output_path = "C:\\Users\\C00979\\DataViz-Lesson-Plans\\01-Lesson-Plans\\03-Python\\2\\Activities\\09-Ins_WriteCSV\\output\\jisan.csv"

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    #csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvfile.writelines('finanacial analysis\n')
    csvfile.writelines('--------------'+'\n')

    # Write the second row
    csvfile.writelines('total months:'+str(monthsT)+'\n')
    csvfile.writelines('total revenue: $'+str(TotalRevenue)+'\n')
    csvfile.writelines('average rchange:$'+str(average_change)+'\n')
    csvfile.writelines('greatest increase in profit:'+MaxMonth+" ($"+str(Greatest_Inc)+")"+'\n')
    csvfile.writelines('greatest decrease in profit:'+MinMonth+" ($"+str(Greatest_Dec)+")"+'\n')
    
with open(output_path,'r') as readfile:
        print(readfile.read())


