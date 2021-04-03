# mode :
# r => read
# r+
# w => write
# w+
# a=>append
# a+
#arti + = hnaya menambah bisa read saja
#menyediakan 2 argument
fp = open("contoh.txt","r")
# content = fp.read() # tidak dapat menduplicate
# print(content)

# print("-----------------------------")
# conten2 = fp.read(100) #membaca hanay 10 caracter
# print(conten2)

content3 = fp.readlines()#membaca enter dengan mencetak satu barus enter digantikna \n. bertipe class list. :3 = limit sampai ke list berapa
#readline = hnaya berupa string, membaca paragraf pertama saja
#readlines = berlitpe list
# print(content3)
# for value in content3:
#     print(value)

# fr = open("input.txt","w+") #menulis data, mengantikan tidak menambah, apabila diexsekusi, ada w= open and write dan w+ open write and reading,
# #print(fr.tell())
# fr.write("tes cokbak bokk") #write
# #print(fr.tell()) #tell() menghitung jumlah caracter pada fileopen.txt
# fr.seek(3,0) #parameter 1 titik dimulainya,parametr 2 kedua kalau kosong, defaultnya 0, digunkn untuk menampikan teks jika sudah di write
# print(fr.tell())
# contw = fr.read()
# print(contw)

fp2 = open("contoh.txt","r+")#digunakan untuk membaca sekaligus menulis data ke file, r = hanya read saja
con2 = fp2.read()
#fp2.write("\n\n TEKS BARU") #menulis isi,kalau pake r+ akan menulis terus
#print(con2)

# fw = open("blablaba.txt","a+") #append , mirip fungsi pada r+,kalau a = filenya tidak ada maka akan dibuat writing, a+ = sama tapi bisa writing and read
# # print(fw.tell())
# fw.write("\n TAMBAHAN DARI TEXT APPEND TIGA")
# fw.seek(0,0)
# ccc = fw.read()
# print(ccc)
