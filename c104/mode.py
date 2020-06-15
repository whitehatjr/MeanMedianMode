# Python program to print
# mode of elements
from collections import Counter
import csv

with open('height-weight.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_data=[]
for i in range(len(file_data)):
	n_num = file_data[i][1]
	new_data.append(n_num)


n = len(new_data)
#using counter function to get the occurences of numbers
data = Counter(new_data)
# # print(data)
get_mode = dict(data)
#
mode = []
mode1 = []
mode2 = []

#taking a,v for key and value
for a,v in get_mode.items():
    #changing type of a from string to float
    a= float(a)
    if 50< a <60:
        #checking if v is equal to the maximum of values in data
        if v == max(list(data.values())):
            mode.append(a)
    elif 60< a <70:
        if v == max(list(data.values())):
            mode1.append(a)
    elif 70< a <75:
        if v == max(list(data.values())):
            mode2.append(a)



if len(mode)>len(mode1) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode)))
elif len(mode1)>len(mode) and len(mode2):
    print("Mode is /are "+ ', '.join(map(str, mode1)))
elif len(mode2)>len(mode) and len(mode1):
    print("Mode is /are "+ ', '.join(map(str, mode2)))

# print(get_mode,"this is  mdoe")
