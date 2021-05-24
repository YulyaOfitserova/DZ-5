
rus_data = {'Один': 1, 'Два': 2, 'Три': 3, 'Четыре': 4}
with open('5.4.txt', encoding='utf-8') as my_file:
    line = my_file.read().split('\n')

data = {}
for element in line:
    key = element.split(' ')[0]
    value = element.split(' ')[1:]
    data[key] = value

new_data = dict(zip(rus_data.keys(), data.values()))
new_data_list = []
for key, value in new_data.items():
    i = [key, value]
    new_data_list.append(i)
print(new_data_list)

with open('5.4_new.txt', 'w') as f:
    for item in new_data_list:
        f.write("%s\n" % item)

