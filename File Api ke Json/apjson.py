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
    print("3.Api lainnya")
  
    
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
    
def api_jasamarga_gerbang_lainnya():
    #headers = {'Authorization': '2628228679'}
    #respon= requests.get('https://jid.jasamarga.com/client-api/data/lalinperjam?kode_cabang=2&kode_gerbang=31&tanggal=2023-12-29',headers=headers)
    
    #respon_json = respon.json()
    #print(json.dumps(respon_json,indent=4, sort_keys=True))
    
    #with open('jasamargagerbang31_2023-12-29.json', 'w') as file:
        #json.dump(respon_json, file)
        
    print("Maintenance")


MenuToolsAPIJson()
pilih = int(input("Masukan nomor pilihan dalam menu:"))
if pilih == 1:
        api_jasamarga_gerbang()
elif pilih==2:
        api_jasamarga_gerbangtigasatu()
elif pilih==3:
        api_jasamarga_gerbang_lainnya()
else:
    print("Nomor menu tidak tersedia!")
    exit
        
    
    