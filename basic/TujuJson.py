
# json objk dict{"key" : "value"}
# number 10 10.55 int float
# array [10,"string"] list
# " "  ' ' ""         tuple()

import json
handle = open("example.json","r")
content = handle.read() #class str
handle.close()
#print(contentB)
d = json.loads(content) #merubah menjadi class dict {}
#print(d['database']) #akses d['database'] untuk manggil databse didalamnya
d['database']['user']= 2222 #merbah user yang didalam database
#print(d['files']['log'])
d['files']['log'] = ("log/app.log","/log/mysql/app.log")
#print(d)
#---------------------------------------------------------------------------------kalau ditambah indent, sort_keys merapikan file json agar bisa dibaca
do = json.dumps(d,indent=3,sort_keys=True) #memiliki banyak parametr, tpi harus disi minimal 1, contoh yaitu d
#function converts a Python object into a json string. bisa juga untk mengkonvet dictionary ke dalam bentuk json
#print(d)
lll = open("example.json","w") #merubah isi file json
lll.write(do)
lll.close()
#------------------------------------ xml to dict
#untuk install librari pada pyton
#1 pip install nama librar1
#2 pip freeze, cek apakh berhsil install
#3 pyton, - import namalibrar
#done

import xmltodict
hanxml = open("input.xml","r")
conxml = hanxml.read()
parXm = xmltodict.parse(conxml) #bertipe colenction dict, MERUBAH isi file xml menjadi dict
#cat = parXm['catalog']['food']['name'] #untuk memanggil seperti json
#parXm['catalog']['food']['name'] = "rendang" #untuk merubah sama sja seprti json

unpar = xmltodict.unparse(parXm) #membaca sperti bibasa file xmlnya
print(unpar)
