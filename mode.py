import csv
from collections import Counter

with open('data.csv' , 'r', newline='') as f:
    reader = csv.reader(f)
    data_file = list(reader)

data_file.pop(0)
 
new_list = []
for i in range(len(data_file)):
    num = data_file[i][1]
    new_list.append(float(num))
    
data = Counter(new_list)
mode_data_for_range = {
    "50-60": 0,
    "60-70": 0,
    "70-80": 0
}

for height, occurrence in data.items():
    if 50 < height < 60:
        mode_data_for_range["50-60"] += occurrence
    elif 60 < height < 70:
        mode_data_for_range["60-70"] += occurrence
    elif 70 < height < 80:
        mode_data_for_range["70-80"] += occurrence

mode_range, mode_occurrence = 0,0

for range, occurrence in mode_data_for_range.items():
    if occurrence > mode_occurrence:
        mode_range = [int(range.split('-')[0]), int(range.split('-')[1])]
        mode_occurrence = occurrence

mode = (mode_range[0] + mode_range[1])/2
print("Mode is", mode)