
# ---------------------------- indexing
s = "Pyton Sample string"
#print(s[-2]) #kalau - berarti ambil dari kata terakhir
#print(s[0:10]) #index dar9  sampai ke berapa atau disebut slicing
#print(s[7:]) #dari ke 7 sampai habis
#print(s[:5])
# ------------------------------------- stride
#print(s[::2]) #print menghapus tiap kelipatan 2
#print(s[::-1])
#print(s[::-2]) #membalik kata dan kalimat kalau -1, klau -2membalik mneghindari atau hapus di kelipatan 2

#--------------------------------------- STRING Modifaction
# num1 = 1500
# num2 = 2000
# print('value number one {val1} number two {val2}' . format(val1=num1,val2=num2)) #memformat angka array dimulai dari 0
# s = s.capitalize() #membuat huruf pertama besar , upper() = besar semua,lower,title = besar kecial tiap kata, isUpeer = true/false
# split = string jadi list/array,
ll = 'asdasfsadfsad'
kalimat = '******halo ini adalah*********'
car = 'mobil'
kata = 'html, pyton, JAVA, css, javascript'
pecah = kata.split(',')
cobaJoin = (" ").join(pecah) #merubah array menjadi string kalimat
cariIndex = kata.index('pyton')#dibaca percharacter, kalau tidak ada error
cariBolean = 'pyton' in kata
cari = kata.find('pytdaon') #sama seperti index, tapi kalau tidak ada hasil -1
rm = kalimat.strip(' ') #merimove
rm2 = kalimat.lstrip('*') #merimove yang awal
rmfirst = kalimat.rstrip('*') #merimove akhir
modif1 = car.rjust(10,'*') #center, ljust, rjust , rata string dengan tambahn caratr *
replaces = kata.replace('html', 'boker')
#print(replaces)
#-------------------------------------list atau array
arr1 = [11,12,13,44,'afaf',[22,33]]
ind = arr1[-1][1] #kalau bernilai -, dimuai dari index paling belakang,
indUntil = arr1[0:2] # tanda : bernilai index awal sampai index akhir -1
kkk = arr1[::-1] #kalau -1 dibalik,kalau -.., berarti dilompati berapa, dimuali index ke 0
kk = arr1[::-4]
#for value in arr1: #menampilkan list, kalau arr1[::2] dilompati 1, 3 dilompati 3, dimulai index 0, tetapi index 0 tetap dibaca
#    print(value)
#arr1.append('tambah') # menmbh isi array, tidak bisa dibuat variabel
#apabila nilainya dari vaiabel sama, maka id memory locationnya sama
arr2 = [100,200,300]
arr2.extend([400,500,600,700,700]) #menambhakna banyak isi array secara setara, tidak bisa dijadikan variabel, hanyak menerima satu argumnet yaitu [..isi,isi2]
#arr2.extend('piton') #kalau ini menambhakn, tapi stringnya dipecah per huruf, jadi, p,i,t,..
#print(arr2)
#-----delet from list
#arr2[0] = 11 #update element
delPop = arr2.pop(2) #delete from first index
#arr2.remove(700) #remove with value hanya satu value
#arr2.clear() #remove all value
arr3 = [33,21,44,707,3,32]
arr3.sort() #kecil - besar
arr3.reverse() #besar -> kecil, harus urut terlebih dulu
tambh = arr2 + arr3 #mirip concat
#print(tambh)
#------------------------------------------------------tuppel data type
tu =(11,12,12,12,13,14) #tupple tidak dapat di modifikasi, ad,delete, update
arrr = [11,12,12,12,13,14]
tmbhh = tu.count(34) #mencari kalau ada, berjumlah berapa, kalau tidak = 0
# for tu in enumerate(arr2): #tupel
#     print(tu)
#------------------------------------------------------------dictionary data type, /objek
dic = {'emp_id' : 101, 'name' : 'boker', 'email':'boker@gmail.com'}
tmbObj = dic['addres'] = 'mojokerto' #menambah key value
getKey = dic.get('name') # SAMA saja denga dic['name']
setKey = dic.setdefault('BARUSET','newValue') #menambah data obj baru
# val = dic.values()
# kunci = dic.keys()
# itm = dic.items() #key value semua, dibungkus tupel, bertipe dict_item
#-------------modification dictionary
keynya = ['name','club','age','nationaly']
valNya = ['zlatan','acMilan',32,'swadden']
createKamus = dict(zip(keynya,valNya)) #Membuat data dictionary atau object
dictTwo = {'name' : 'ronaldo', 'club' : 'madrid', 'age' : 22}
l = [1,2,3,4]
d = dict.fromkeys(l) #bikin dict dengan acuan key, default valunya none, fromkeys mempunyai 2 parameter
#createKamus.update(dictTwo) #update data dictionary, data key yang diupdate (dictTwo) harus sama dengan dic1 (createKamus),
                            #kalau tidak, key valuenya akan nambah diakhir, tidak bisa dijadikan variabel
#createKamus.pop('name') #merimove key berserta valunya
#r = createKamus.popitem() #memisahkan key terakhir menjadi tuple
createKamus.clear() #delete selurh isi

#------------------------------------set data type
va ={10,20,30,40,100,11} #type set
#tipe data set, tidak dapat menampilkan data yang bernilai sama atau duplicate
#va.add(500)
va2 = {10,20,30,50,70,90}
va3 = va.union(va2) #menambah 2 buat set, setara
va4 = va.intersection(va2) #menghapus semua
#beda = va2.difference(va) #bandingkan set 1 dengan set2 acuan (va) ,mencari yang tidak ada pada set yang pertama
#sim = va.symmetric_difference(va2) #membanding kedua data set, menampilkan yang tidak ada pada keduanya dijatikan satu,depan belakng sama saja
#va.update(va2) #menampilkan semu adat va dan va2
#va.intersection_update(va2) #update data pertama, mencari data yang sama dengan data kedua ,hanya menampilkan data yang sama (va dengan va2), {10,20,30}
#va.difference_update(va2) #updata data pertama, menampilkan data yang tidak ada pada data kedua (va dan va2) 0utput{100,40,11}
#va.symmetric_difference_update(va2) #update, menampilkan semua yang beda (va dengan va2) Output = {100, 70, 40, 11, 50, 90}
#s1 = {100,200,300,400,500}
#s2 = {100,200,300}
#saj = s2.issubset(s1) #dibaca: semua data set2, ada di data set1 ?, boolean
#sup = s1.issuperset(s2) #dibaca: true, jika semua item set s2 ada pada item s1
exLis1 = [11,12,13,14]
exList2 = [20,30,40,50]
#rubahListKeset = set(exLis1) #rubah tipe dari list keset
st1 = set(exLis1)
st2 = set(exList2)
gabung = st1.union(st2) #menggabungkan dua buah set menjadi satu
urut = sorted(gabung) #mengurutkan
setnew ={10,20,30,40,11}
sorted(setnew)
#setnew.pop() #remove last set
#setnew.remove(10) #remove sepesfic value
#setnew.discard(40) #remove sama seperti remove, tapi kalau data tidak ada, tidak terjadi error
#setnew.clear()
#print(setnew)
#------------------------------------------------math function
lismat = [100,200,300,400,500]
tambhSemuaElm = sum(lismat)
maxval = max(lismat) #max, min
an = 27.111
bulat = round(an) #pembulatan , dapat disi 2 arument, argument kedua, berapa angka dibelakang koma
import math
# numlagi = 45.7777
# desiml, intgr = math.modf(numlagi)
#rad = math.radians(200)#penggunaan fungsi math
# help(math)
import random
acak = random.random()
randomForList = random.choice(lismat) #random angka dari list yang sudah ada
randomBetween = random.randint(1, 100) #mencetak angka random dari, sampai,hampir sama dengan randrange()
print(randomBetween)
