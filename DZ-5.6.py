
import re

with open('subject.txt', encoding='utf-8') as my_subject:
    line = my_subject.read().split("\n")[:-1]

data = {}
for element in line:
    key = element.split(':')[0]
    value = element.split(' ')[1:]
    data[key] = value
    data_list = ' - '.join(data[key])
    num = re.findall(r'\d+', data_list)
    sum_num = sum(map(int, num))
    data[key] = sum_num

print(data)
