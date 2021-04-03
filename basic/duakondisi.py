num1 = 200
num2 = 120
if num2 > num1:
    print('amgka dua lebih besar betul')
elif num2 < num1:
    print('angak dua kurang dari')
else:
    print('else')
# if els

#iterasi atau looping
#hanya berupa str, list, tuple, dict, set
list = [11,20, 30, 50,22]

sum = 5
for value in list:
    sum = sum + value #yang dipering harus berupa value
    # print(sum)
#for value in range(11, 30): #range, kalau 3 parameter, var1 dimulai dari, var2 diakhir,i, var3 kelipatan
                            #kalau 1 berarti 1 sampai maxnya
#    print(value)
#---------------------------------------------
data = [11,12,13,14,40,50]
cari =12
# for index, value in enumerate(data) : #data: #enumerate(variabel), mencetak angka mengetahu indexnya list
#     #print(index,value)
#     if value == cari:
#         print('found in index',index)
#         break
#     else:
#         pass #continue = proses carinya tidak ditampilkan, pass = ditampilkan sampai break
#         print('ini pass')
# else:
#     print('not found')

# --------------------------------------
dataQuir = [1500,2000]
for value in dataQuir:
    print(value)
