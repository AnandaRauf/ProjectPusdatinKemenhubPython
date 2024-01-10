import requests
from datetime import date
import json
from datetime import timedelta
import urllib
def getDataGerbang():
    print("Data Gerbang:\n")
    urldatagerbang = "https://jid.jasamarga.com/client-api/data/gerbang"
    headersdatagerbang = {
        'Authorization': '2454282048'
    }
  
    respon = requests.get(urldatagerbang, headers=headersdatagerbang)
    datarespon = respon.json()
    gerbang_data = []

    for i in range(40):
        kodegerbang = datarespon[i]['kode_gerbang']
        kodecabang = datarespon[i]['kode_cabang']
        print("Kode Gerbang:", kodegerbang, "Kode Cabang:", kodecabang)
        gerbang_data.append({'kodegerbang': kodegerbang, 'kodecabang': kodecabang})

    with open('jasamargasemuagerbang_Jan.json', 'w') as file:
        json.dump(gerbang_data, file)
        print("Berhasil buat file json jasamargasemuagerbang_Jan.json")

def getDataLalinPerGerbang():
    print("Data Lalin:\n")
    urldatagerbang = "https://jid.jasamarga.com/client-api/data/gerbang"
    headersdatagerbang = {
        'Authorization': '2454282048'
    }
  
    respon = requests.get(urldatagerbang, headers=headersdatagerbang)
    datarespon = respon.json()

    for i in range(3):
        kodegerbang = datarespon[i]['kode_gerbang']
        kodecabang = datarespon[i]['kode_cabang']
        print("Kode Gerbang:", kodegerbang)
        print("Kode Cabang:", kodecabang)
       
        headersdatagerbanglalin = {'Authorization': '2628228679'}
        tanggal_sekarang = date.today()
        kemarin = tanggal_sekarang - timedelta(days = 1)
        jan10 = tanggal_sekarang.strftime('%Y/%m/%d')
        kemarinJan= kemarin.strftime('%Y/%m/%d')
        tanggaljan = kemarinJan
        kode_cabangurl = urllib.parse.urlencode({'kode_cabang': kodecabang})
        kode_gerbangurl = urllib.parse.urlencode({'kode_gerbang': kodegerbang})
        tanggalurl = urllib.parse.urlencode({'tanggal': tanggaljan})
        
        datagerbanglalinurl = f"https://jid.jasamarga.com/client-api/data/lalinperjam?{kode_cabangurl}&{kode_gerbangurl}&{tanggalurl}"
        
        respon = requests.get(datagerbanglalinurl, headers=headersdatagerbanglalin)
        respon_json = respon.json()
        
        try:
            with open(f'jasamargasemuagerbangLalinJan8.json', 'w') as file:
                json.dump(respon_json, file)
                print(f"Berhasil buat file json jasamargasemuagerbangLalin_{kodegerbang}_{tanggaljan}.json")
        except TypeError:
            print("Unable to serialize the object")

#getDataGerbang()
getDataLalinPerGerbang()
