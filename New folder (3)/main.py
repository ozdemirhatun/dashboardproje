from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb


app = Flask(__name__)

app.secret_key = 'kh2000'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'netflix123'
app.config['MYSQL_DB'] = 'dashboardproje'

mysql = MySQL(app)

#@app.route('/gitmekistediğimizsayfa') komutu ile sayfalarımızı ekliyoruz.
@app.route('/', methods=['GET', 'POST'])
def login():

    msg = ''

    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(username)
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM satis_ekibi WHERE mail = %s AND sifre = %s', (username, password))
        account = cursor.fetchone()
        if account:
            print(account)
            session['loggedin'] = True
           # session['password'] = account['password']
            session['username'] = account['mail']
            return redirect (url_for('home'))
            # Redirect to home page
            #return redirect(url_for('home'))
        else:
            msg = 'Hatalı kullanıcı adı/şifre!' 
   
    return render_template('login.html', msg=msg)


@app.route('/home')
def home():
    # Check if user is loggedin
    print(session)
    if 'username' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login')) 
 
@app.route('/insert', methods=['POST'])
def insert():
    saticiAdi=request.form['saticiAdi']
    print(saticiAdi)
    
 


#giriş sayfasından sonra home page yönlendirmek için render_template yerine redirect koyuoyoruz.
if __name__ =='__main__':
	app.run(port=5000, debug=True)

