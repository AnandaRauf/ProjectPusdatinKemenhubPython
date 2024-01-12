import requests
from datetime import date, timedelta
import urllib.parse
import json
import csv
import mysql.connector
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 12),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'jasamarga_workflow',
    default_args=default_args,
    description='Jasa Marga Workflow',
    schedule_interval='@monthly',  # Adjust the schedule as needed
)

def getDataLalinPerGerbang():
    print("Data Lalin:\n")
    urldatagerbang = "https://jid.jasamarga.com/client-api/data/gerbang"
    headersdatagerbang = {"Authorization": "2454282048"}

    respon = requests.get(urldatagerbang, headers=headersdatagerbang)
    datarespon = respon.json()

    all_data = []

    for i in range(3):
        kodegerbang = datarespon[i]["kode_gerbang"]
        kodecabang = datarespon[i]["kode_cabang"]
        print("Kode Gerbang:", kodegerbang)
        print("Kode Cabang:", kodecabang)

        headersdatagerbanglalin = {"Authorization": "2628228679"}
        tanggal_sekarang = date.today()
        kemarin = tanggal_sekarang - timedelta(days=3)
        kemarinTgl = kemarin.strftime("%Y/%m/%d")
        sekarang = tanggal_sekarang
        bulansek_tglsek = sekarang
        kode_cabangurl = urllib.parse.urlencode({"kode_cabang": kodecabang})
        kode_gerbangurl = urllib.parse.urlencode({"kode_gerbang": kodegerbang})
        tanggalurl = urllib.parse.urlencode({"tanggal": bulansek_tglsek})

        datagerbanglalinurl = f"https://jid.jasamarga.com/client-api/data/lalinperjam?{kode_cabangurl}&{kode_gerbangurl}&{tanggalurl}"

        respon = requests.get(datagerbanglalinurl, headers=headersdatagerbanglalin)
        respon_json = respon.json()

        data_lalin_sorted = sorted(respon_json, key=lambda x: (x['kode_cabang'], x['kode_gerbang'], x['jam']))

        data_entry = {
            "kode_cabang": kodecabang,
            "kode_gerbang": kodegerbang,
            "data_lalin": data_lalin_sorted,
        }

        all_data.append(data_entry)

    try:
        with open(f"jasamargasemuagerbangLalin_Sekarang.json", "w") as file:
            json.dump(all_data, file, indent=2)
            print(f"Berhasil buat file json jasamargasemuagerbangLalin_Sekarang.json")
    except TypeError:
        print("Unable to serialize the object")



def FileJsonToCSV():
    with open('jasamargasemuagerbangLalin_Sekarang.json') as json_file:
        data = json.load(json_file)

        datas = []
        for entry in data:
            datas.extend(entry['data_lalin'])

        sorted_data = sorted(datas, key=lambda x: (x['kode_cabang'], x['kode_gerbang'], x['jam']))

        with open('jasamargasemuagerbangLalin_BulanSekarang.csv', 'w', newline='') as data_file:
            csv_writer = csv.writer(data_file)

            count = 0
            for entry in sorted_data:
                if count == 0:
                    header = entry.keys()
                    csv_writer.writerow(header)
                    count += 1
                csv_writer.writerow(entry.values())

    print("Berhasil membuat file CSV")

def DataCSVToMysql():
    dbcon = mysql.connector.connect(
        user="uStaging",
        password="Qw3rty1p#",
        host="localhost",
        port=3308,
        database="db_staging",
        auth_plugin="mysql_native_password",
    )
    if dbcon.is_connected():
        print("Database connected successfully\n")

    sqlquery = """
    INSERT INTO `jasamarga_lalinperjam` (`kode_cabang`, `kode_gerbang`, `tanggal_req`, `nama_gerbang`, `jam`, `golongan`, `shift`, `total_kendaraan`, `jumlah_gardu`, `tanggal`)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """

    try:
        cursor = dbcon.cursor()

        with open('jasamargasemuagerbangLalin_BulanSekarang.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                cursor.execute(sqlquery, (row['kode_cabang'], row['kode_gerbang'], row['tanggal'], row['nama_gerbang'], row['jam'], row['golongan'], row['shift'], row['total_kendaraan'], row['jumlah_gardu'], row['tanggal']))

        dbcon.commit()
        print(cursor.rowcount, "Berhasil masukkan data")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        dbcon.close()
        print("Connection closed")

dag >> PythonOperator(
    task_id='get_data_lalin',
    python_callable=getDataLalinPerGerbang,
    dag=dag,
)

dag >> PythonOperator(
    task_id='json_to_csv',
    python_callable=FileJsonToCSV,
    dag=dag,
)

dag >> PythonOperator(
    task_id='csv_to_mysql',
    python_callable=DataCSVToMysql,
    dag=dag,
)
