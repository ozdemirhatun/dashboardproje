from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'netflix123'
app.config['MYSQL_DB'] = 'dashboardproje'

mysql = MySQL(app)

#@app.route('/gitmekistediğimizsayfa') komutu ile sayfalarımızı ekliyoruz.
@app.route('/', methods=['GET', 'POST'])
def login():

   if request.method == 'POST':
        if 'username' in request.form and 'password' in request.form:
            username = request.form['username']
            password = request.form['password']
            cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            cursor.execute('SELECT * FROM satis_ekibi WHERE mail = %s AND sifre = %s', (username, password))
            account = cursor.fetchone()
            if account is not None:
                if account['mail']== username and account['sifre']==password:
                    return "Başarıyla Giriş Yaptınız"
            # Redirect to home page
            #return redirect(url_for('home'))
            
            else:
                return 'Hatalı kullanıcı adı/şifre!'
   
   return render_template('login.html')


#giriş sayfasından sonra home page yönlendirmek için render_template yerine redirect koyuoyoruz.
if __name__ =='__main__':
	app.run()