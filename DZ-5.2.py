
my_file = open('data.txt', 'r')
str_count = my_file.readlines()
str_num = len(str_count)
print(f'Количество строк в файле: {str_num}')

word_num = [len(line.split()) for line in str_count]
n = len(word_num)
i = 0
while i < n:
    print(f'Количество слов в {i + 1} строке - {word_num[i]}')
    i += 1
    