
#print('function')
# 1 code reuse, 2 modularity
s = 'Pyton,HTML,CSS'
#print(s.index('Pyton'))
l = 'Piton'
def value_reverse(value): #1 membuat function harus didefinisikan dengan def namafungsi(): dulu
    reverse = value[::-1]#2 spasi atau tab (menjorok) setelah fungsi = identasi, pemanggilan fungsi sama seperti biasah
    #print(reverse)
    #return reverse
# value_reverse(l)
l = [10,20,30,40]
result = value_reverse(l)
#print(result) #output 40,30,20,10
#--------------------------------------passing parrameter teqniek
#1 position argumnet
def linear_search(listnya, serch):
    for value in listnya: #yang kebaca hnaya first index, lainnya tidak :(
        if serch==value : #return hanya mengembalikan firt index, apabilas berupa list, kalau print semua
            return True
        else:
            return False

ls = [100, 200, 300, 400]
key = 100
hasil = linear_search(ls,key)
# print(hasil)
#----------------------looping function yg berner
# def loopy(items):
#     kos =[]
#     for item in items:
#         kos.append(item)
#         #print(kos)
#         #return item # mengembalikan first index
# loopy(ls)

#----------------------looping function yg berner

#2 default argument
#ord('c') #fungsi yang mengembalikan integer, hanya berupa input 1 charatker dari input character string
#chr(1) #fungsi yang mengembalikan character lawan ord, dari input character integer
# import random
# def generate_pass(Length=8): #Length=8,default parameter, kalau tidak disi return jadi 8 pass,nya caratr
#     spesialchar = ['@','#','$','%','&']
#     upper = chr(random.randint(65, 90)) #generate integer random, dari 65 ->90, haya satu outputnya
#     lower = chr(random.randint(97, 122))
#     spesl = random.choice(spesialchar)
#     dgit = random.randint(10000, 99999)
#     paswd = upper + lower + spesl + str(dgit) #pasword asli ,str merubah int jadi string
#     la = random.sample(paswd,Length) #modifikasi jumlah charctr pada password
#     paswd =("").join(la) #join mengabungkan
#     return paswd #untuk mencetaknya tidk bisa pake print, harus di return
# hasilPassword = generate_pass(3) #parementr tidak boleh lebih dari 8,
# print(hasilPassword)

# validate---------------------------------
def validasiCek(username,password):
    if username == 'ABC' and password == 'abc123':
        print('succes Login')
    else:
        print('invalid')
#validasiCek(password='abc123', username='ABC') #bisa dirubah posisi
# print(100,200,sep=",",end=" ") #output (100,200 welcome), default pyton kalau , = spasi, sep untuk edit,
# print('welcome')

# def add_value(*args): #bermasalah ----------------------- #argument
#     #print(args)
#     arKosong =[]
#     for value in args :
#         arKosong.append(value)
#         print(type(arKosong))
# add_value(100,200,300)

# def get_details(**kwargs):  #---------------keyword arguments,jika argumentnya ada keywordnya
#     print(kwargs)
# get_details(name='abc',email='abc@gmail.com',contact=32323,dob='12-03-2001') #tidak masalah apablia keywordnya beda beda,
# get_details(name='boker',dob='12-03-1993')
# get_details(name='indah',email='juna@gmail.com',contact=111111,dob='32-13-1871', club="man united")

#3 recursive function ----------------------------------------------------------
# def factorial(num):
#     if num == 1:
#         return 1
#     else:
#         return num * factorial(num-1)
#
# num = 7
# hasilRes = factorial(num)
# print(hasilRes)
def binary_serach(lll, keyyy):
    if len(lll) == 0: #jumlh pada pyton menggunakan len
        return False
    else:
        mid = len(lll) // 2
        if lll[mid] == keyyy:
            return True
        elif keyyy < lll[mid]:
            return binary_serach(lll[:mid], keyyy)
        else:
            return binary_serach(lll[mid+1:], keyyy)
lll =[100,200,300,400,500,600,700,800]
keyyy = 8100
r = binary_serach(lll, keyyy)
print(r)
