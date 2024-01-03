from flask import Flask
from flask import render_template
import jinja2
homeweb = Flask(__name__)
@homeweb.route('/')

def home():
	return render_template('index.html',title='Website Jasa Marga Gerbang')

@homeweb.route('/rekrut')
def rekrut():
    return render_template("rekrut.html", title='Rekrut tim Ananda Rauf Maududi')
if __name__ == '__main__' :
	homeweb.run('localhost',5050)

