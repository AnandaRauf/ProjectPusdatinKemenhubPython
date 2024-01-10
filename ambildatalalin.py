import requests
import urllib
import urllib.parse
import urllib.request
import json
import schedule
import time
from datetime import date
import itertools

def getDataGerbang():
    print("Data Gerbang:\n")
    urldatagerbang = "https://jid.jasamarga.com/client-api/data/gerbang"
    headersdatagerbang = {
      'Authorization': '2454282048'
}
  
    
    respon = requests.get(urldatagerbang,headers=headersdatagerbang)
    datarespon = respon.json()
    for i in range(40):
        kodegerbang= datarespon[i]['kode_gerbang']
        kodecabang= datarespon[i]['kode_cabang']
        print("Kode Gerbang:",kodegerbang,"Kode Cabang:",kodecabang)
      
        with open('jasamargasemuagerbang_Jan.json', 'w') as file:
            json.dump(kodegerbang, file)
            json.dump(kodecabang, file)
            print("Berhasil buat file json jasamargasemuagerbang_Jan.json")
    #return json_respon[0]['kode_gerbang']
    #print(data)
    #datakode = data['kode_gerbang','kode_cabang']
    #pilihdatakode =  int(input('Pilih index data (list index 0 -1) :'))
    #print(datakode[pilihdatakode])

getDataGerbang()

def getDataLalinPerGerbang():
    print("Data Lalin:\n")
    urldatagerbang = "https://jid.jasamarga.com/client-api/data/gerbang"
    headersdatagerbang = {
      'Authorization': '2454282048'
}
  
    
    respon = requests.get(urldatagerbang,headers=headersdatagerbang)
    datarespon = respon.json()
    for i in range(40):
        kodegerbang=datarespon[i]['kode_gerbang']
        kodecabang=datarespon[i]['kode_cabang']
        print("Kode Gerbang:",kodegerbang)
        print("Kode Cabang:",kodecabang)
       
        headersdatagerbanglalin = {'Authorization': '2628228679'}
        tanggal_sekarang = date.today()
        jan10 = tanggal_sekarang.strftime('%Y/%m/%d')
        tanggaljan= jan10
        kode_cabangurl= "&kode_cabang={kodecabang}".format(kodecabang)
        kode_gerbangurl= "&kode_gerbang={kodegerbang}".format(kodegerbang)
        tanggalurl =  "&tanggal={}".format(tanggaljan)
        #args = {"&kode_cabang=": kodecabang, "&kode_gerbang=":kodegerbang ,"&tanggal=":tanggaljan}
        datagerbanglalinurl= 'https://jid.jasamarga.com/client-api/data/lalinperjam?{}'.format(kode_cabangurl, kode_gerbangurl,tanggalurl)
        #loaddatalalin = json.load(urllib.request.urlopen(datagerbanglalinurl))
        #kontendata = loaddatalalin.read().decode('utf-8')
        respon= requests.get(datagerbanglalinurl,headers=headersdatagerbanglalin)
        respon_json = respon.json()
        print(json.dumps(respon_json,indent=4, sort_keys=True))
        try:
            with open('jasamargasemuagerbangLalin_Jan10.json', 'w') as file:
                json.dump(respon_json, file)
            #print("Berhasil buat file json jasamargasemuagerbangLalin_Jan10.json")
        except TypeError:
            print("Unable to serialize the object")

getDataLalinPerGerbang()
    




#Tarik data berjadwal eksekusi
#schedule.every().seconds.do(getDataGerbang)


