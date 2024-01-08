import requests
import json

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
    datagerbanglalinJan4 = ['https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=1&kode_gerbang=4&tanggal=2023-01-04','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang=1&kode_gerbang=9&tanggal=2023-01-04']
    #datagerbanglalinJan5= ['https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-05','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-06','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-07','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-08','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-09','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-10','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-11','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-12','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-13','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-14','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-15','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-16','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-17','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-18','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-19','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-20','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-21','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-22','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-23','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-24','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-25','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-26','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-27','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-28','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-29','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-30','https://jid.jasamarga.com/client-api/data/gerbang/lalinperjam?kode_cabang&kode_gerbang&tanggal=2023-01-31']
    #datagerbang =['https://jid.jasamarga.com/client-api/data/gerbang]
    with open('jasamargasemyagerbang_LalinJan4to31.json', 'w') as file:
        json.dump([requests.get(url,headers=headersdatagerbanglalin).json() for url in datagerbanglalinJan4], file, indent=2)
        
        print("Berhasil Membuat File Json")    
        
        #Lalin
    #respon= requests.get('https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=2&kode_gerbang=31&tanggal=2023-12-29',headers=headers)
    
    #respon_json = respon.json()
    #print(json.dumps(respon_json,indent=4, sort_keys=True))
    
    #with open('jasamargagerbang31_2023-12-29.json', 'w') as file:
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
        
    
    
