import PyInstaller.__main__
import pyinstaller_versionfile

VER='1.0.3.14'

def createBat():
    f=open('exefile.bat','w')
    f.write('pyinstaller --onefile main.py --icon "logo zohan.ico" --name "OPSURT to Kaspi KZS '+VER+'" --version-file ver.txt\n')
    f.write('pause')
    f.close()

def createEXEfile():
    PyInstaller.__main__.run([
        'main.py',
        '--onefile',
        '--windowed',
        '--icon=logo zohan.ico',
        '--name=OPSURT to Kaspi KZS '+VER+'',
        '--version-file=ver.txt'
    ])

def createVer():


    pyinstaller_versionfile.create_versionfile(
        output_file="ver.txt",
        version=VER,
        company_name="KZS Studio",
        file_description="Это приложение для конверта данных опсурт в каспи магазин",
        internal_name="OPSURT KASPI ZZZ",
        legal_copyright="© KZS Studio Company. All rights reserved.",
        original_filename="OPSURT to Kaspi KZS "+VER+".exe",
        product_name="OPSURTKASPI"
    )




if __name__=='__main__':
    #createBat()
    createVer()
    createEXEfile()
