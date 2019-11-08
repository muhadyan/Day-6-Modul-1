
# FUNCTION
# f(x) = 2x + 2
# f(3) = 2(3) + 2 = 8

# Cara Bikin Function
def hello():
    print('Hello World')

hello()


# f(x) = x ^ 2
def kuadrat(x):
    print(x ** 2)

kuadrat(2)
kuadrat(3)


def pangkat(angka1, angka2):
    print(angka1 ** angka2)

pangkat(2,3)
pangkat(2,10)
pangkat(
    float(input('Ketik angka 1: ')),
    float(input('Ketik angka 2: '))
)


students = ['Andi', 'Budi', 'Caca']
def tes():
    print(students[0])
    print('Caca' in students)

tes()



# RETURN FUNCTION
def hello():
    print('Hello World')
def returnHello():
    return 'Hello Return World'

hello()                 # langsung keluar tanpa perintah 'print'
print(hello())          # malah ga keluar kalo pake perintah 'print'
returnHello()           # ga keluar apa-apa kalo ga diperintah 'print'
print(returnHello())    # baru keluar kalo pake perintah 'print'


def LuasPersegi(sisi):
    print('Luas =', sisi * sisi)
def LuasPersegiReturn(sisi):
    return sisi * sisi

LuasPersegi(4)
print(LuasPersegiReturn(4))


def gangen(angka):
    if angka % 2 == 0:
        return 'GENAP'
    else:
        return 'GANJIL'

print(gangen(49))



# WHILE LOOP
while True:
    print('True')       # bakal jalan terus
while False:
    print('True')       # ga ngeprint apa-apa


i = 1
while i < 10:
    print(i)    # ngeprint dari 1 sampe 29
    i += 1

i = 20
while i >= 1:
    print(i)    # ngeprint dari 20 sampe 1
    i -= 1

i = 20
while i >= 1:
    print(i)    # ngeprint dari 20 sampe 2 hanya yg angka genap
    i -= 2


students = ['Andi', 'Budi', 'Caca']
index = 0
while index <= len(students) - 1:
    print(students[index])
    index += 1


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []

index = 0
while index <= len(x) - 1:
    y.append(x[index] ** 2)
    index += 1

print(y)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = []

index = 0
while index <= len(x) - 1:
    if index == 4:
        break
    y.append(x[index] ** 2)
    index += 1

print(y)


i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    print(i)


password = '12345'
inputuser = ''

while inputuser != password:
    inputuser = input('Ketik password: ')
    if inputuser != password:
        print('Password Salah!')
    else:
        print('Password Benar!')


password = '12345'
inputuser = ''
jumlahInput = 0
batasInput = 5
lebih = False

while inputuser != password and not lebih:
    if jumlahInput < batasInput:
        inputuser = input(f'Input ke-{jumlahInput+1} Ketik password: ')
        jumlahInput += 1
    else:
        lebih = True

if lebih:
    print('Kesempatan habis, tunggu 24 Jam')
else:
    print('Password benar!')