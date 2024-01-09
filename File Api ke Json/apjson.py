import requests
import json
import schedule
import time
print("==========================================================================================\n")
namaaplikasi = "Tools API Json\n"
versi = "Version 1.0\n"
project= "Pustadin Kemenhub"
devby = "Ananda Rauf Maududi\n"
devdate = "Project dimulai pada 04 Januari 2024\n"
print(namaaplikasi)
print(versi)
print("Developed by:",devby)
print(devdate)
print("==========================================================================================\n")

def MenuToolsAPIJson():
    print("Pilih nomor yang ada didalam menu:")
    print
    print("1.Api Gerbang")
    print("2.Api Kode Cabang 2 Gerbang 31")
    print("3.Api Semua Gerbang")
  
    
def api_jasamarga_gerbang():
    headers = {'Authorization': '2454282048'}
    respon= requests.get('https://jid.jasamarga.com/client-api/data/gerbang',headers=headers)
    
    respon_json = respon.json()
    print(json.dumps(respon_json,indent=4, sort_keys=True))
    
    with open('jasamargagerbang.json', 'w') as file:
        json.dump(respon_json, file)
        
    print("File json api Gerbang sudah berhasil dibuat")
    


def api_jasamarga_gerbangtigasatu():
    headers = {'Authorization': '2628228679'}
    respon= requests.get('https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=2&kode_gerbang=31&tanggal=2023-11-17',headers=headers)
    
    respon_json = respon.json()
    print(json.dumps(respon_json,indent=4, sort_keys=True))
    
    with open('jasamargakodegerbang2gerbang31_2023-11-17.json', 'w') as file:
        json.dump(respon_json, file)
        
    print("File json api Gerbang 31 sudah berhasil dibuat")
def api_jasamarga_semuagerbang():
    #headersdatagerbang = {'Authorization': '2454282048'}
    
    headersdatagerbanglalin = {'Authorization': '2628228679'}
    datagerbanglalinJan = [
        'https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=15&kode_gerbang=36',
        'https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=15&kode_gerbang=32',
        'https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=14&kode_gerbang=81',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=81',
        'https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=15&kode_gerbang=37',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=15&kode_gerbang=37',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=11&kode_gerbang=28',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=11&kode_gerbang=9',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=80',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=2',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=36',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=21',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=37',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=20',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=38',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=13',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=39',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=40',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=41',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=73',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=11&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=11&kode_gerbang=2',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=2&kode_gerbang=30',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=2&kode_gerbang=31',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=74',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=4&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=26&kode_gerbang=33',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=31',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=9&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=30',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=9&kode_gerbang=2',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=9&kode_gerbang=3',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=27&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=9&kode_gerbang=4',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=27&kode_gerbang=22',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=19&kode_gerbang=26',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=3&kode_gerbang=7',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=3&kode_gerbang=8',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=33&kode_gerbang=3',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=33&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=33&kode_gerbang=2',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=37&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=37&kode_gerbang=2'
        ]
    
    respon = requests.get(url,headers=headersdatagerbanglalin) for url in datagerbanglalinJan
    respon_json = respon.json()
    
    with open('jasamargasemuagerbangLalin_Jan9To31.json', 'w') as file:
        schedule.every().day.at("13:40", "Asia/Jakarta").do(json.dump(respon_json, file))
        print("Berhasil Membuat File Json")
        
            
    #datagerbang =['https://jid.jasamarga.com/client-api/data/gerbang]
   
        
        #Lalin
    #respon= requests.get('https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=2&kode_gerbang=31&tanggal=2023-12-29',headers=headers)
    
    #respon_json = respon.json()
    #print(json.dumps(respon_json,indent=4, sort_keys=True))
    
   # with open('jasamargagerbang31_2023-12-29.json', 'w') as file:
        #json.dump(respon_json, file)
        



MenuToolsAPIJson()
pilih = int(input("Masukan nomor pilihan dalam menu:"))
if pilih == 1:
        api_jasamarga_gerbang()
elif pilih==2:
        api_jasamarga_gerbangtigasatu()
elif pilih==3:
        api_jasamarga_semuagerbang()
else:
    print("Nomor menu tidak tersedia!")
    exit
        
    
    
