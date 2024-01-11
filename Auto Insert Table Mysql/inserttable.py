import mysql.connector

def konekdb():
    try:
        dbcon = mysql.connector.connect(user='uStaging', password='Qw3rty1p#', host='localhost', port=3308, database='db_staging',auth_plugin='mysql_native_password')
        if dbcon.is_connected():
            print("Database berhasil dihubungkan\n")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

  


def insert_data():
    dbcon = mysql.connector.connect(user='uStaging', password='Qw3rty1p#', host='localhost', port=3308, database='db_staging',auth_plugin='mysql_native_password')
    if dbcon.is_connected():
        print("Database connected successfully\n")
            # Your SQL query
    sql_query =  """
    INSERT INTO `jasamarga_lalinperjam` (`id`, `kode_cabang`, `kode_gerbang`, `tanggal_req`, `nama_gerbang`, `jam`, `golongan`, `shift`, `total_kendaraan`, `jumlah_gardu`, `tanggal`) VALUES
    (1, 15, 36, '2024-01-10', 'Keluar Jakarta (Cikatama 1 + Kalitama 1 + Kalihurip 1)', 6, 1, 1, 1821, 97, '2024-01-10'),
    (2, 15, 32, '2024-01-10', 'Keluar Jakarta (Cikatama 1 + Kalitama 1 + Kalihurip 1)', 7, 1, 1, 1821, 97, '2024-01-10'),
    (3, 14, 81, '2024-01-10', 'Keluar Jakarta (Cikatama 1 + Kalitama 1 + Kalihurip 1)', 14, 1, 1, 1821, 97, '2024-01-10'),
    (4, 15, 37, '2024-01-10', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-09'),
    (5, 15, 36, '2024-01-10', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-09'),
    (6, 15, 32, '2024-01-10', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-09'),
    (7, 15, 37, '2024-01-10', 'GT Pd Ranji Sayap JKT', 0, 0, 0, 0, 0, '2024-01-08'),
    (8, 14, 81, '2024-01-10', 'GT Pd Ranji Sayap JKT', 0, 0, 0, 0, 0, '2024-01-08'),
    (9, 15, 37, '2024-01-10', 'GT Pd Ranji Sayap JKT', 0, 0, 0, 0, 0, '2024-01-08'),
    (10, 15, 32, '2024-01-10', 'GT Pd Ranji Sayap JKT', 0, 0, 0, 0, 0, '2024-01-07'),
    (11, 14, 81, '2024-01-10', 'GT Pd Ranji Sayap JKT', 0, 0, 0, 0, 0, '2024-01-07'),
    (12, 15, 37, '2024-01-10', 'GT Pd Ranji Sayap JKT', 0, 0, 0, 0, 0, '2024-01-07'),
    (13, 15, 37, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-06'),
    (14, 15, 36, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-06'),
    (15, 15, 32, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-06'),
    (16, 15, 37, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-05'),
    (17, 15, 36, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-05'),
    (18, 15, 32, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-05');
        """
    sqlquery2 = """
    INSERT INTO `jasamarga_lalinperjam` (`id`, `kode_cabang`, `kode_gerbang`, `tanggal_req`, `nama_gerbang`, `jam`, `golongan`, `shift`, `total_kendaraan`, `jumlah_gardu`, `tanggal`) VALUES
    (19, 15, 37, '2024-01-11', 'GT Pd Ranji Utama BSD', 24, 0, 0, 0, 0, '2024-01-11'),
    (20, 15, 36, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-11'),
    (21, 15, 32, '2024-01-11', 'GT Pd Ranji Utama BSD', 0, 0, 0, 0, 0, '2024-01-11');
        """
    otomatisinsertjasamargagerbang = "INSERT INTO jasamargagerbang (kode_gerbang, kode_cabang) VALUES (%s, %s)"
    otomatishapusjasamargagerbang = """DELETE FROM jasamargagerbang WHERE kode_gerbang='34' AND kode_cabang='32';"""
    val = ("15", "32")
        
        
    try:
        # Create a cursor
        cursor = dbcon.cursor()
            
        # Execute the SQL query
        #cursor.execute(sqlquery2)
        #cursor.execute(otomatisinsertjasamargagerbang, val)
        #cursor.execute(otomatishapusjasamargagerbang)
        # Commit the changes
        dbcon.commit()
        #print(cursor.rowcount, "Berhasil menghapus data column kode_gerbang kode_cabang")
        #print(cursor.rowcount, "Berhasil masukin data")
        tampildatajasamargagerbang = "SELECT * FROM jasamargagerbang"
        tampildatajasamargagerbanglalin = "SELECT * FROM jasamarga_lalinperjam"
        #cursor.execute(tampildatajasamargagerbang)
        cursor.execute(tampildatajasamargagerbanglalin)
        result = cursor.fetchall()
        for row in result: 
            print(row,"Berhasil menampilkan data!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # Close the cursor and database connection
        cursor.close()
        dbcon.close()
        # print("Connection closed")

# Call the function to insert data


insert_data()

konekdb()

