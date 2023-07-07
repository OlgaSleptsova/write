new_list =[]
with open('1.txt', encoding='utf8') as file:
    new_list1 =[]
    for y in file.readlines():
        new_list1.append(y)
new_list.append(len(new_list1))

with open('2.txt', encoding='utf8') as file:
    new_list2 = []
    for y in file.readlines():
        new_list2.append(y)
new_list.append(len(new_list2))

with open('3.txt', encoding='utf8') as file:
    new_list3 = []
    for y in file.readlines():
        new_list3.append(y)
new_list.append(len(new_list3))

new_list.sort()

with open('new.txt','w',encoding='utf8') as file:
    if len(new_list3) == new_list[0]:
        file.write('3.txt' + '\n')
        file.writelines(str(len(new_list3)) + '\n')
        for d, w in enumerate(new_list3):
            file.writelines(f'Строка номер {d + 1} файл номер 3' + '\n')
    elif len(new_list1) == new_list[0]:
        file.write('1.txt' + '\n')
        file.writelines(str(len(new_list1)) + '\n')
        for d, w in enumerate(new_list1):
            file.writelines(f'Строка номер {d + 1} файл номер 1' + '\n')

    elif len(new_list2) == new_list[0]:
        file.write('2.txt'+'\n')
        file.writelines(str(len(new_list2))+'\n')
        for d, w in enumerate(new_list2):
            file.writelines(f'Строка номер {d+1} файл номер 2' + '\n')
with open('new.txt', 'a', encoding='utf8') as file:
    if len(new_list3) == new_list[1]:
        file.write('3.txt' + '\n')
        file.writelines(str(len(new_list3)) + '\n')
        for d, w in enumerate(new_list3):
            file.writelines(f'Строка номер {d + 1} файл номер 3' + '\n')
    elif len(new_list1) == new_list[1]:
        file.write('1.txt' + '\n')
        file.writelines(str(len(new_list1)) + '\n')
        for d, w in enumerate(new_list1):
            file.writelines(f'Строка номер {d + 1} файл номер 1' + '\n')

    elif len(new_list2) == new_list[1]:
        file.write('2.txt' + '\n')
        file.writelines(str(len(new_list2)) + '\n')
        for d, w in enumerate(new_list2):
            file.writelines(f'Строка номер {d + 1} файл номер 2' + '\n')

with open('new.txt', 'a', encoding='utf8') as file:
    if len(new_list3) == new_list[2]:
        file.write('3.txt' + '\n')
        file.writelines(str(len(new_list3)) + '\n')
        for d, w in enumerate(new_list3):
            file.writelines(f'Строка номер {d + 1} файл номер 3' + '\n')
    elif len(new_list1) == new_list[2]:
        file.write('1.txt' + '\n')
        file.writelines(str(len(new_list1)) + '\n')
        for d, w in enumerate(new_list1):
            file.writelines(f'Строка номер {d + 1} файл номер 1' + '\n')

    elif len(new_list2) == new_list[2]:
        file.write('2.txt' + '\n')
        file.writelines(str(len(new_list2)) + '\n')
        for d, w in enumerate(new_list2):
            file.writelines(f'Строка номер {d + 1} файл номер 2' + '\n')
