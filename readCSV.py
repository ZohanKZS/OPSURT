import csv
from ftplib import FTP
# from config import HOST,PASS,USER

def readCSVz(fn):

    a=[]

    with open(fn,'r') as r_file:
        file_reader = csv.reader(r_file, delimiter = ";")

        count = 0
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                # print(f'Файл содержит столбцы: {", ".join(row)}')
                dfgg=5
            else:
                # Вывод строк
                # print(f'    {row[0]} - {row[1]} - {row[2]}  - {row[3]}  - {row[4]} ')
                # print(row)
                a.append(row)
            count += 1

    return a

def readMethod1():
    # with open("export.csv", encoding='utf-8') as r_file:
    with open("export.csv") as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.reader(r_file, delimiter = ";")
        # Счетчик для подсчета количества строк и вывода заголовков столбцов
        count = 0
        # Считывание данных из CSV файла
        for row in file_reader:
            if count == 0:
                # Вывод строки, содержащей заголовки для столбцов
                print(f'Файл содержит столбцы: {", ".join(row)}')
            else:
                # Вывод строк
                # print(f'    {row[0]} - {row[1]} - {row[2]}  - {row[3]}  - {row[4]} ')
                print(row)
            count += 1
        print(f'Всего в файле {count} строк.')

def readMethod2():
    with open("export.csv") as r_file:
        file_reader = csv.DictReader(r_file, delimiter = ";")
        count = 0
        for row in file_reader:
            if count == 0:
                print(f'Файл содержит столбцы: {" | ".join(row)}')

            print(f'{row["goodsid"]}       {row["naim"]}       {row["izm"]}       {row["ostatok"]}       {row["priceroz"]}       {row["sku"]}       {row["barcode"]}', end='\n')

            count += 1
        print(f'Всего в файле {count + 1} строк.')

    # ss=['goodsid','naim','izm','ostatok','priceroz','sku','barcode']
    # print('|'+' | '.join(ss)+'|')

def loadFileFromFTP(h,u,p):

    PORT = 21
    ftp = FTP(h)
    ftp.login(u, p)


    file_name = 'fromZOO.csv'
    my_file = open(file_name, 'wb')
    ftp.retrbinary('RETR ' + 'export.csv', my_file.write, 1024)

    my_file.close()
    ftp.close()

    return file_name

def UPloadFileToFTP(fn,hos,usr,pas,txtf):

    PORT = 21
    ftp = FTP(hos)
    ftp.login(usr, pas)

    # ll=ftp.nlst()

    file_name = fn
    my_file = open(file_name, 'rb')
    #ftp.storbinary('STOR ' + 'exportZOO.xml', my_file)
    ftp.storbinary('STOR ' + txtf, my_file)

    my_file.close()
    ftp.close()

    return file_name
