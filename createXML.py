import xml.etree.ElementTree as ET
import xml.dom.minidom as xmm


def addTitle(cmp,id):
    p = ET.Element('kaspi_catalog')
    p.set('date', 'string')
    p.set('xmlns', 'kaspiShopping')
    p.set('xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance')
    p.set('xsi:schemaLocation', 'kaspiShopping http://kaspi.kz/kaspishopping.xsd')

    c = ET.SubElement(p, 'company')
    c.text = cmp

    c = ET.SubElement(p, 'merchantid')
    c.text = id

    of = ET.SubElement(p, 'offers')

    return p, of


def addOfer(of, art, name, dostup, cena):
    of1 = ET.SubElement(of, 'offer')
    of1.set('sku', art)
    c = ET.SubElement(of1, 'model')
    nn = name.replace('"', '')
    nn = nn.replace('&', '')
    nn = nn.replace('>', '')
    nn = nn.replace('<', '')
    nn = nn.replace("'", "")
    c.text = nn
    c = ET.SubElement(of1, 'brand')
    # c.text='AsdfX2'
    av = ET.SubElement(of1, 'availabilities')
    c = ET.SubElement(av, 'availability')
    c.set('available', dostup)
    c.set('storeId', 'PP1')
    c = ET.SubElement(av, 'availability')
    c.set('available', dostup)
    c.set('storeId', 'PP2')
    c = ET.SubElement(of1, 'price')
    c.text = str(cena)

    # comment = ET.Comment('user comment')
    # p.append(comment)


def readXMLpretty(ff):
    f = open(ff, 'r')

    tt = f.read()

    doc = xmm.parseString(tt)
    t = doc.toprettyxml()
    # print(t)
    return t
