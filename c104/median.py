# Python program to print
# median of elements
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
# removing the list of titles using pop
file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)

n = len(new_data)
new_data.sort()


#using floor division to get the nearest number whole number
# floor division is shown by //
if n % 2 == 0:
    #getting the first number
	median1 = float(new_data[n//2])
    #getting the second number
	median2 = float(new_data[n//2 - 1])
    #getting mean of those numbers
	median = (median1 + median2)/2
else:
	median = new_data[n//2]

print("Median is: " + str(median))
