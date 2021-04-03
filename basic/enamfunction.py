l = [100,200,300,400]
l2 =[]
# for value in l: #1 luping dengan for biasah
#     l2.append(value)
# print(l2)           #tap atau jarak pada pyton juga berpengaruh, kalau digaris lurus denganl2, maka tampil seperti dibawh ini
                                       #[100]
                                       #[100, 200, 300]
                                       #[100, 200]
                                       #[100, 200, 300, 400]

# l3 = [val * val for val in l] #2 luping for dengan disimpan di parameter
# print(l3)
# ll = [10,20,25,30,35,60,65,70,85,17]
# ll2 = [val for val in ll if val%2 == 0] #meretrun hasil yang val habis dibagi 2
# print(ll2)

# ls = ['abc','abcd', 'abcde', 'zzzzzkkk']
# ls4 = [len(val) for val in ls] #mengetahuin jumlah caracter tiap list
# print(ls4)

n = [(value,val2) for value in range(1,5) for val2 in range(100,103)] #range maxnya, -1
#print(n)
#output [(1, 100), (1, 101), (1, 102), (2, 100), (2, 101), (2, 102), (3, 100), (3, 101), (3, 102), (4, 100), (4, 101), (4, 102)]

arinar = [[1,2,3],[4,5,6],[7,8,9]] #output array multi dimesi
arEmpty = []
for value in arinar:
    for val2 in value:
        arEmpty.append(val2) #merubah array multi dimensi menjadi array indexed
#print(arEmpty)

j = [100,105,110,115,120]
po = ["habisDibagi2" if val%2 ==0 else "TIDAK" for val in j] #Looping menggatnikan item habis tiap bagi 2 akan tampil, jika tidak TIDAK
#print(po)
dic = {x:x**2 for x in range(1,10)} #mencetak 1: 1, 2: 4, 3: 9, sampai 9
#print(dic)
dicCar = {chr(x):x for x in range(1,9)}
#print(dicCar)
#---------------------------function programming map filter, lambda
def sqr(input):
    return input**2 #pangkat 2
lmp = [10,20,30,40,50]
reslt = list(map(sqr,lmp)) #map(sqr,lmp)
#print(reslt)
# for value in reslt:
#    print(value)
#--------------------------------------------- fungsi tabah map
def funcAdd(inpt1,input2):
    return inpt1+input2
w = [100,210,300,400,500]
i = [10,20,30,40,50]
hasilMap = list(map(funcAdd,w,i))
#print(hasilMap)
#--------------------------------------Filter
def functCek(inpt):
    if inpt %2 == 0:
        return True
    else:
        return False

fil = [100,320,120,125,130,135,140]
res = list(filter(functCek,fil))
#print('pake fungsi filter',res)
#---------------------------------------Lambda funct
#Lambda bisa memiliki lebih dari satu argumen atau parameter,
#tapi hanya bisa memiliki satu ekspresi atau isi.
sapa = lambda name: print(f'hallo, {name}') # 1 lambda, 2paremter,.. 3 expresion/isi
#sapa('boker')
resLambd = list(filter(lambda nu:nu%2==0,fil)) #filter bilangdn dengan lambda
#print('pake lambda',resLambd)
dicLamp ={8:50,2:40,3:30,4:20,5:11}
urut = sorted(dicLamp.items()) #sorted berdasarkna key
urut2 = dict(sorted(dicLamp.items(),key=lambda j:j[1])) #urut berdasarkan value, dan dirubah datanya ke dictornar
#print(urut2)
#---------------------------function iterations

def Val(inp):
    for value in inp:
        print(value)
z = [10,20,30,40,50]
#Val(z)
def tesfungsitambah():
    firt_num = 0
    secont_num = 1
    while(True): #proses luping
        next_val = firt_num + secont_num
        firt_num,secont_num = secont_num,next_val
        yield next_val #untuk mengembalikan objek generator, kalau return mengembalikan suatu nilai
ll = tesfungsitambah()
#print(ll)
#print(next(ll))
#print(next(ll))

#----------------------------iteratoors and iteratols
toors = [100,200,300,400,500]
i = iter(toors) #itertoors, iteratoors didukang nengan function next()
#print(next(i))
# for value in i:
#     print(value)

import itertools
l1 = [10,20,30,40]
l2 = [100,200,300,400]
l3 = [1001,2001,3001,4001]

k = itertools.chain(l1,l2,l3) #mneggabungkan list menjadi chain objek
# for value in k:
#     print(value)
count = 0
# for value in itertools.cycle(l1):
#     if count < 20:
#         print(value)
#     else:
#         break
#     count+=1

# for value in itertools.repeat(l1): #mengulangi dengan membentuk list, bukan item lagi
#     if count < 20:
#         print(value)
#     else:
#         break
#     count+=1
w = [10,20,30,40]
q = iter(w)
t = itertools.tee(q) #dapat ditambhakn multiple objek
#print(t)

for value in t[1]:
    print(value)
