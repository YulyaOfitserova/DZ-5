
with open('staff.txt', 'r') as my_file:
    print('Заработная плата меньше 20000 у следующих сотрудников: ')
    data = {}
    for line in my_file:
        key, value = line.split()
        data = {key: value}
        data[key] = int(data[key])
        if data[key] < 20000:
            key_data = [k for k, v in data.items()]
            print(f'{key_data}')


