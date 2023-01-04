import os

os.chdir('data')  # Переходим в папку data в которой хранятся файлы
list_of_files = os.listdir(path=".")  # Получаем список всех файлов

counter = 0
all_items = []

for element in list_of_files:
    item = []
    date, time = element[-12:-4:1], element[-4::1]   # Получаем дату, получаем время

    list_of_data = open(element).read().split() # Открываем файл, читаем данные и делаем из них список

    item.append(counter)  # Формируем строку в виде [counter, date, time, data]
    counter += 1
    item.append(f'{date[:4]}-{date[4:6]}-{date[6:8]}')
    item.append(f'{time[:2]}:{time[2:]}')
    item.append(list_of_data[-1])  # Берём, к примеру, последний элемент в файле
    all_items.append(item)  # item= [0, '2022-11-10', '12:35', '14']

os.chdir('..')  # Возвращаемся в основную директорию
with open("output.txt", "w") as file:  # Записываем данные в файл
    for i in all_items:
        file.write(f"{str(i)},\n")
