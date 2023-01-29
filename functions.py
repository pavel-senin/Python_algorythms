filename = 'tel.txt'


def writeFile():
    with open(filename, 'a') as data:
        data.writelines()

def showFile():
    result = []
    with open(filename, 'r+') as data:
        for line in data:
            result.append(line)
    return result

def findPersonFile(Item):
    result = []
    with open(filename, 'r+') as data:
        for line in data:
            if Item in line:
                result.append(line)
    return result

def findNumberFile(Item):
    result = []
    with open(filename, 'r+') as data:
        for line in data:
            if Item in line:
                result.append(line)
    return result

def AddContact(addSurname, addName, addPatr, addNumber):
    text = [addSurname + ', '+addName+', '+addPatr+', '+addNumber]
    print(text)
    with open(filename, 'a') as data:
        data.writelines('\n')
        data.writelines(text)
        print('Контакт добавлен')
    return 0


def DeleteContact(Sname, Name, Patr, Number):
    result = []
    text = str(Sname+', '+Name+', '+Patr+', '+Number)
    counter = 0
    it = -1
    with open(filename, 'r+') as data:
        for line in data:
            if not(text == line) and len(line)!=0:
                result.append(line)
                it = it+1
            counter = counter+1
    data.close()
    if counter == it+1:
        print('контакт не найден')
        return 1
    with open(filename, 'w') as data:
        for i in range (0, len(result)):
            data.writelines(result[i])
    data.close()
    print('Контакт удален')
    return 0

def changeNumber(Sname, Name, Patr, Number):
    text = str(Sname+', '+Name+', '+Patr+', '+Number)
    result = []
    counter = 0
    it = -1
    with open(filename, 'r+') as data:
        for line in data:
            if len(line)!=0:
                if (Sname in line and Name in line and Patr in line):
                    result.append(text)
                    it = it+1
                else:
                    result.append(line)
            counter = counter+1
    data.close()
    if counter == it+1:
        print('контакт не найден')
        return 1
    with open(filename, 'w') as data:
        for i in range (0, len(result)):
            data.writelines(result[i])
    data.close()
    print('Номер контакта изменен')
    return 0


command = 0

while (command!=7):
    print('Введите номер действия:')
    print('1 - Показать все записи')
    print('2 - Найти запись по вхождению частей имени')
    print('3 - Найти запись по телефону')
    print('4 - Добавить новый контакт')
    print('5 - Удалить контакт')
    print('6 - Изменить номер телефона у контакта')
    print('7 - Выход')
    command = input("Ввод команды: ")
    command = int(command)
    if command == 7:
        print('Выход')
        break
    elif command == 1:
        printAllData = showFile()
        if len(printAllData)>0:
            for i in range (0,len(printAllData)):
                print(printAllData[i])
        else:
            print('Пусто')
    elif command == 2:
        find = input('Введите часть имени: ')
        find = str(find)
        matches = findPersonFile(find)
        if (len(matches) == 0):
            print('Найдено совпадений: 0')
        else:    
            print('Найдено совпадений: ', len(matches))
            print(matches)
    elif command == 3:
        find = input('Введите номер: ')
        find = str(find)
        matches = findNumberFile(find)
        if (len(matches) == 0):
            print('Найдено совпадений: 0')
        else:    
            print('Найдено совпадений: ', len(matches))
            print(matches)
    elif command == 4:
        addSurname = input('Введите фамилию: ')
        addName = input('Введите имя: ')
        addPatr = input('Введите отчество: ')
        addNumber = input('Введите номер: ')
        addSurname = str(addSurname)
        addName = str(addName)
        addPatr = str(addPatr)
        addNumber = str(addNumber)
        AddContact(addSurname, addName, addPatr, addNumber)
    elif command == 5:
        print('Удаляем контакт')
        addSurname = input('Введите фамилию: ')
        addName = input('Введите имя: ')
        addPatr = input('Введите отчество: ')
        addNumber = input('Введите номер: ')
        addSurname = str(addSurname)
        addName = str(addName)
        addPatr = str(addPatr)
        addNumber = str(addNumber)
        DeleteContact(addSurname, addName, addPatr, addNumber)
    elif command == 6:
        print('Меняем номер телефона контакта')
        addSurname = input('Введите фамилию: ')
        addName = input('Введите имя: ')
        addPatr = input('Введите отчество: ')
        addNumber = input('Введите НОВЫЙ номер: ')
        addSurname = str(addSurname)
        addName = str(addName)
        addPatr = str(addPatr)
        addNumber = str(addNumber)
        changeNumber(addSurname, addName, addPatr, addNumber)
