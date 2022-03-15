import csv

from matplotlib.pyplot import legend

with open('data.csv', 'r' , newline = '') as f:
    reader = csv.reader(f)
    data_file = list(reader)

data_file.pop(0)

new_list = []
for i in range(len(data_file)):
    num = data_file[i][1]
    new_list.append(float(num))

new_list.sort()
length = len(new_list)

if length % 2 == 0:
    median1_index = length//2
    median2_index = median1_index - 1
    median = (new_list[median1_index] + new_list[median2_index]) / 2
else:
    median_index = length//2
    median = new_list[median_index]

print('The median is' , median)