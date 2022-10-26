from createXML import addOfer, addTitle, ET, readXMLpretty
from readCSV import loadFileFromFTP, readCSVz, UPloadFileToFTP
import json

def readJSON():

    with open('settings.json') as f:
        # templates = json.load(f)
        file_content = f.read()
        dat = json.loads(file_content)

    # print(dat['host'])
    return dat

def createBat(v):
    f=open('exefile.bat','w')
    f.write('pyinstaller --onefile main.py --icon "logo zohan.ico" --name "'+v+'"\n')
    f.write('pause')
    f.close()

def appStart():
    # fn = loadFileFromFTP(h,u,p)
    dat=readJSON()
    # fn="C:\Program Files (x86)\OPSURT\Server\export.csv"
    fn=dat['path']
    print('OPSURT to Kaspi KZS v1.0')
    print('Read CSV...')
    lst = readCSVz(fn)
    print('Create XML...')
    p, of = addTitle(dat['comp'],dat['id'])
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

    print('Upload XML to FTP...')
    h=dat['host']
    u=dat['user']
    p=dat['pass']
    UPloadFileToFTP(fn,h,u,p)

if __name__=='__main__':
    appStart()
    # createBat('OPSURT to Kaspi KZS v1.0')
    # readJSON()
# конец кода
