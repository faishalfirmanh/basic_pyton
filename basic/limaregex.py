import re
#regula expresion [a-aA-Z] dan semua caracter [0-9],
#regex adalah deretan, untuk mencari sebuah string(kata) pada karakter contoh, email
#+ -
#^ start dari string $ end string
# s = "ABCDE1234A"
# r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")#tanda {} berarti jumlah caraternya,[] = string dari sampe.., JUMLH caracternya harus sama, kalau tidak berniali[]
#                                  #compile mengembalikan object regex
#                                  #kalau tidak dikasih {}, defaultnya 1
# l = re.findall(r,s) #find medapatkan semua string yang cocok, mencari dengan mereturn list. ada 2 argument,1 = kata yang dicari, 2= daftarnya
#print(l)
st = "9998123456789"
ca = re.compile("^[5-9][0-9]{12}$")
procesCari = re.findall(ca,st)
#print(procesCari)
tgl = '12-04-1994'
reg = re.compile('^([0-9]{2})-([0-9]{2})-([0-9]{4})$') #penambahan group dengan(),group untuk mengelompokan
reg2 = re.compile('^(?P<date>[0-9]{2})-(?P<month>[0-9]{2})-(?P<year>[0-9]{4})$')
#jadi = re.findall(reg,tgl)
#print(jadi)
#--------------------------regular expresion module
# m = re.search(reg2,tgl) #meretrun match opbect, bial text dicari tidak ada meretru none, ada meretrun Match, object match memiliki metode group
# if m:
#     print(m.group('date')) #group dimulai dari 1, kalau tidak ada error, #untuk pemanggilan bisa setring ("mont") dll, kalu gk da error
# else:
#     print('no found')
# st2 ="+62 99812345678"
# ca2 = re.compile("(\+62\s)?([6-9][0-9]{10}$)") #tambh \s untu spasi, {10} = 10 +1
# pro = re.search(ca2,st2)
# if pro:
#     print(pro.group(2)) #group dimulai dari 1
# else:
#     print('patern no found')
