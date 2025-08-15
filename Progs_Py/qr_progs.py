import openpyxl
import glob
import qrcode

archivos = [f for f in glob.glob('*.py')]

for nam in archivos:
    T = list(open(nam,'r'))
    A = ''.join(T)
    img = qrcode.make(A)
    print(nam)
    img.save(nam.replace('.py','.png'))
