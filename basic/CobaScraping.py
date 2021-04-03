import requests
import csv
from bs4 import BeautifulSoup

#scripitng BeautifulSoup hanya mendukung format file yang bertpe html, tidak semua bisa dibaca tag htmlnya,
#ada cara kususnya
#--------------------------------------------------------
# response = requests.get("https://www.magicbricks.com/independent-house-for-rent-in-hyderabad-pppfr")
# soup = BeautifulSoup(response,"lxml")
# print(soup.prettify())
#-------------------------------------------------- 1 local
with open("coba.html","r") as html_file:
    cont = html_file.read()
    #print(cont)
soup2 = BeautifulSoup(cont, 'lxml') #param  1 = contetn, param2 = parser method
lihatHtml = soup2.prettify() # prettify = melihat html code
cariTag = soup2.find_all('li') #find cari 1, findAll = cari semua data /find_all
cariWithClass = soup2.find_all('span',class_="_2tW1I") #untuk memanggil dengan class yang ada class..
moreClass = soup2.find_all('span',{"class": ["_2tW1I", "_89yzn"]}) #untuk askse lebih dari 1 class
for value in moreClass:
    teknya = value.text # hanya mereturn text, tag htmlnya tidak dibaca
#    print(teknya)
#--------------------------------------------------- 2 real scarping website
#.text hanya mengambil textnya saja
urlHtmlnya = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=php&txtLocation=Singapore').text
lihatHtlm = BeautifulSoup(urlHtmlnya, 'lxml')
filtrClass = lihatHtlm.find_all('li',class_="clearfix job-bx wht-shd-bx")
for value in filtrClass:
    date = value.find('span', class_="sim-posted").span.text #didalam span, terdapat span, maka dipanggi seprti itu
    if 'few' in date:
        companyName = value.find('h3', class_="joblist-comp-name")
        repaceCompanyName = companyName.text.replace('\n','')
        skil = value.find('span', class_="srp-skills").text.replace(' ', '').replace('\n','')
        more_info = value.header.h2.a['href'] #['atribut']untuk mengambil atributnya saja
        print(f"company name : {repaceCompanyName.strip()}") #strip untuk menghapus spasi dan newline, f =templte string bisa diisi variabel, mirip jasavscirpt {}
        print(f"Skil         : {skil.strip()}") #strip harus sudah berupa string, tidak ada tag htmlnya
        print(f"more info    : {more_info}")
        print("-----")
