# sebuah function dengan 1 parameter
# function ==> menentukan value parameter: ganjil / genap

def gangen(x):
    if x % 2 == 0:
        print(x, 'tergolong GENAP')
    else:
        print(x, 'tergolong GANJIL')

gangen(10)



# bikin sebuah function
# 1. masukkan angka pertama: 
# 2. masukkan operator aritmatika:
# 3. masukkan angka kedua:

def calc():
    x = float(input('Masukkan angka pertama: '))
    op = input('Masukkan operator (+-*/): ')
    y = float(input('Masukkan angka kedua: '))
    if op == '+':
        print(x + y)
    elif op == '-':
        print(x - y)
    elif op == '*':
        print(x * y)
    elif op == '/':
        print(x / y)
    else:
        print('Maaf operator tidak dikenali')

calc()



# buat function yg mengubah huruf vokal menjadi o
def vocal(kalimat):
    kalimat = kalimat.lower()
    kalimat = kalimat.replace('a', 'o')
    kalimat = kalimat.replace('i', 'o')
    kalimat = kalimat.replace('u', 'o')
    kalimat = kalimat.replace('e', 'o')
    print(kalimat)

vocal('Selamat datang')