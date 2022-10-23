from createXML import addOfer, addTitle, ET, readXMLpretty
from readCSV import loadFileFromFTP, readCSVz, UPloadFileToFTP

fn = loadFileFromFTP()

lst = readCSVz(fn)

p, of = addTitle()

ean = []

k = 1
for i in lst:
    try:
        if int(i[3]) > 0:
            if not i[6] in ean:
                addOfer(of, i[6], i[1], 'yes', i[4])
                ean.append(i[6])
    except:

        pass

    # if k==3:
    #     break

    # print(k)
    k += 1

tree = ET.ElementTree(p)
fn = "exportZOO.xml"
tree.write(fn)

tt = str(readXMLpretty(fn))

# print('-------'+tt)
tt2 = tt.replace('<?xml version="1.0" ?>', '<?xml version="1.0" encoding="UTF-8"?>')
# tt2=tt.replace('kaspi_catalog','kaspi_catalog345')


fn1 = open(fn, 'w', encoding='UTF-8')
fn1.write(tt2)
fn1.close()

UPloadFileToFTP(fn)
