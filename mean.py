import csv

with open('data.csv', 'r' , newline = '') as f:
    reader = csv.reader(f)
    file_data = list(reader)

file_data.pop(0)

new_list = []
for i in range(len(file_data)):
    number = file_data[i][1]
    new_list.append(float(number))

sum = 0
length = len(new_list)
for i in new_list:
    sum += i

mean = sum/length

print("Mean of the data is", mean)
