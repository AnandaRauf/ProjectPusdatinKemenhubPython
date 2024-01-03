import mysql.connector

print("==========================================================================================\n")
namaaplikasi = "Bot database Jasa Marga Gerbang\n"
versi = "Version 1.0\n"
project= "Pustadin Kemenhub"
devby = "Ananda Rauf Maududi\n"
devdate = "Project dimulai pada 03 Januari 2024\n"
print(namaaplikasi)
print(versi)
print("Developed by:",devby)
print(devdate)
print("==========================================================================================\n")

def MenuBotDatabase():
    print("Pilih nomor yang ada didalam menu:")
    print
    print("1.Konek Database")
    print("2.Buat Database")
    print("3.Buat Table Database")
    print("4.Masukin data ke table column")
    print("5.Tampilkan semua data database")
    print("6.Tampilkan data dari table")
    
    
    
    +
def KonekDatabase():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="jasamarga_gerbang")
    if dbcon.is_connected():
        print("Database berhasil dihubungkan\n")
        
def BuatDatabase():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="")
    buatdb = dbcon.cursor()
    buatdb.execute("CREATE DATABASE jasamarga_gerbang")
    print("Database berhasil dibuat\n")
    
def BuatTableDatabase():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="jasamarga_gerbang")
    buattable = dbcon.cursor()
    sql = "CREATE TABLE tb_cabangdua(kode_cabang INT(100),kode_gerbang INT(100),tanggal_gerbang DATE )"
    buattable.execute(sql)
    print("Tabel berhasil dibuat\n")
    
def MasukinDataKeTable():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="jasamarga_gerbang")
    masukindata_table = dbcon.cursor()
    sql = "INSERT INTO tb_cabangdua VALUES('2','31','2023-11-1')"
    print("Data berhasil dimasukan ke tabel\n")
    
    
    

    
MenuBotDatabase()
pilih = int(input("Masukan nomor pilihan dalam menu bot :"))
if pilih == 1:
        KonekDatabase()
elif pilih==2:
        BuatDatabse()
elif pilih==3:
        BuatTableDatabase()
else:
    print("Nomor menu tidak tersedia!")
        exit