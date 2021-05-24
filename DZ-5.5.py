def my_sum():
    try:
        with open('numbers.txt', 'w+') as my_file:
            line = input('Введите целые числа через пробел: ')
            my_file.writelines(line)
            num = line.split()
            print(sum(map(int, num)))
    except ValueError:
        print('Программа считает сумму только целых чисел!')

my_sum()



