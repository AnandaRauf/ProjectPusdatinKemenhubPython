from flask import Flask, request, url_for, redirect, render_template
import mysql.connector
berandaweb = Flask(__name__)

#mydatabase = mysql.connector.connect(host = 'localhost', user = 'root',passwd = '', database = 'jasamarga_gerbang')
#mycursor = mydatabase.cursor()
@berandaweb.route('/')

def beranda():
    dbcon = mysql.connector.connect(host="localhost",user="root",passwd="",database="jasamarga_gerbang")
    buattable = dbcon.cursor()
    sql = "SELECT * FROM tb_cabangdua"
    buattable.execute(sql)
    data =  buattable.fetchall()
    print(data)

render_template('index.html',output_data=data,title='Website Jasa Marga Gerbang')
    #mycursor.execute('SELECT * FROM tb_cabangdua')
    #mycursor.execute()
    #data = mycursor.fetchall()

#render_template('index.html',output_data=data,title='Website Jasa Marga Gerbang')



#@berandaweb.route('/rekrut')
#@berandaweb.route('/TampilSemuaData')
#@berandaweb.route('/TampilSatuData')
#def rekrut():
    #return render_template("rekrut.html", title='Rekrut tim Ananda Rauf Maududi')


if __name__ == '__main__' :
	berandaweb.run('localhost',5050)

