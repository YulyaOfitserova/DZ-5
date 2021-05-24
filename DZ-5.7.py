import re
import  json

with open('firm.txt', encoding='utf-8') as my_file:
    line = my_file.read().split('\n')

data = {}
no_profit = {}
new_data = {}
for element in line:
    key = element.split(' ')[0]
    value = element.split(' ')[1:]
    data[key] = value
    data_list = ' - '.join(data[key])
    num = re.findall(r'\d+', data_list)
    profit = int(num[0]) - int(num[1])
    data[key] = profit

for key, value in data.items():
    if value < 0:
        no_profit[key] = value
    else:
        new_data[key] = value

av_profit = {'average profit': round(sum(new_data.values()) / len(new_data), 3)}
profit_data = [new_data, av_profit]
for_json = {
    'with_profit':
        f'{profit_data}',
    'no_profit':
        f'{no_profit}'
     }

print(for_json)
print(profit_data)
print(no_profit)

with open("firm.json", "w") as write_f:
    json.dump(for_json, write_f)





