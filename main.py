from createXML import addOfer, addTitle, ET, readXMLpretty
from readCSV import loadFileFromFTP, readCSVz, UPloadFileToFTP
import os
import datetime

VER = '1.0.3.12'


def readData():
    with open('config.ini') as f:
        dat = f.read()
        dat = dat.replace('\n', '')
        dat = dat.replace("'", '')
        ls = dat.split(',')

    dic = {}
    for i in ls:
        d = i.split(':')
        dic[d[0].lower().replace('"','')] = d[1].replace(';',':')

    # print(dic['host1'])

    return dic


def appStart():
    # fn = loadFileFromFTP(h,u,p)
    dat = readData()
    #fn0="C:\\Program Files (x86)\\OPSURT\\Server\\export.csv"
    s1='\\'
    s2='\\'
    fn0 = dat['path'].replace(s1,s2)
    print('Start... OPSURT to Kaspi KZS v' + VER)
    print('Read CSV...')
    lst = readCSVz(fn0)
    print('Create XML...')
    p, of = addTitle(dat['comp'], dat['id'])
    ean = []
    k = 1
    for i in lst:
        try:
            if int(i[3]) > 0:
                if not i[6] in ean:
                    addOfer(of, i[6], i[1], 'yes', i[4])
                    ean.append(i[6])
        except:
            print('error')
            print(i)

        # if k==3:
        #     break

        # print(k)
        k += 1

    tree = ET.ElementTree(p)
    fn = "exportZOO.xml"
    print('Save XML...')
    tree.write(fn)

    tt = str(readXMLpretty(fn))

    tt2 = tt.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="UTF-8"?>')

    fn1 = open(fn, 'w', encoding='UTF-8')
    fn1.write(tt2)
    fn1.close()

    print('1 Upload XML to FTP...')
    h = dat['host']
    u = dat['user']
    p = dat['pass']
    UPloadFileToFTP(fn, h, u, p,'exportZOO.xml')# send price file

    fnt = "info.txt"
    #t = os.path.getmtime(dat['path'])
    t = os.path.getmtime(fn0)
    tfn=datetime.datetime.fromtimestamp(t)

    fn1 = open(fnt, 'w', encoding='UTF-8')
    fn1.write(str(tfn))
    fn1.close()

    print('2 Upload XML to FTP...')
    UPloadFileToFTP(fnt, h, u, p,'info.txt')# send info file


    print('Upload SUCCESSFUL!')


if __name__ == '__main__':
    appStart()
    # print(readData())
