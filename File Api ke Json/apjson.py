import requests
import json
import schedule
import time
#import pandas as pd
#from io import StringIO
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
    print("Prosess tarik data........")
    #headersdatagerbang = {'Authorization': '2454282048'}
    
    headersdatagerbanglalin = {'Authorization': '2628228679'}
    datagerbanglalin1 = [
        'https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=15&kode_gerbang=36','https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=15&kode_gerbang=32']
    datagerbanglalin2 = [  'https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=14&kode_gerbang=81',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=1',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=81',
        ]
    datagerbanglalin3 = ['https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=15&kode_gerbang=37',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=15&kode_gerbang=37',
    
        ]
    datagerbanglalin4 = [ 'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=11&kode_gerbang=28',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=11&kode_gerbang=9']
    
    datagerbanglalin5 = [  'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=80',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=2'
        ]
    datagerbanglalin6 = [  'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=80',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=2',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=36'
       ]
    datagerbanglalin7 = [ 'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=21',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=14&kode_gerbang=37'
     ]
    
    datagerbanglalin8 = [   'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=20',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=38',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=13'
        ]
    datagerbanglalin9 = ['https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=39',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=1'
        ]
    datagerbanglalin10 = ['https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=13&kode_gerbang=39',
        'https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=12&kode_gerbang=1']
    #io = StringIO('datagerbanglalinJan')
    #json.load(io)
    #print("Berhasil di decode")

    #url='https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam'
    #respon = requests.get(url,headers=headersdatagerbanglalin) 
    #for url in datagerbanglalinJan:
        #respon_json = respon.json()
        #print(json.dumps(respon_json,indent=4, sort_keys=True))
        
        #List URL
        #url2,url3,url4,url5,url6,url7,url8,url9
        
    with open('jasamargasemuagerbangLalin_Jan9To31.json', 'w') as file:
        json.dump([requests.get(url1,headers=headersdatagerbanglalin).json() for url1 in datagerbanglalin1 for url2 in datagerbanglalin2 for url3 in datagerbanglalin3 for url4 in datagerbanglalin4 for url5 in datagerbanglalin5 for url6 in datagerbanglalin6 for url7 in datagerbanglalin7 for url8 in datagerbanglalin8 for url9 in datagerbanglalin9], file,indent=2,sort_keys=True)
        
        #df = pd.read_json('jasamargasemuagerbangLalin_Jan9To31.json')
        #print("Hasil Pandas:",df)

        print("Berhasil Membuat File Json")

schedule.every().day.at("2024-01-04").do(api_jasamarga_semuagerbang)
        
            
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
        
    
    
