from flask import Flask,request,render_template
from flaskext.mysql import MySQL

app=Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'capsinfirst.ckzc9c4vvmcm.eu-central-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'CapsinFirst'
app.config['MYSQL_DATABASE_PASSWORD'] = 'capsinfirst'
app.config['MYSQL_DATABASE_DB'] = 'temp'

mysql = MySQL()
mysql.init_app(app)




@app.route("/")
def hello_db():
    conn = mysql.connect()
    cursor =conn.cursor()
    cursor.execute('SELECT * from temp')
    data = cursor.fetchall()
    return str(data)





'''
@test.route('/select', methods=['GET'])
def select():
    db_class = dbModule.Database()
 
    sql      = "SELECT *  FROM temp"
    row      = db_class.executeAll(sql)
 
    print row

	return  'hi'

@app.route('/index')
def index():
	cur = mysql.get_db().cursor()
	cur.exeute('SELECT * FROM temp')
	rv =cur.fetchall()
	return srt(rv)


@app.route('/')
def hello():
	return 'welcome to first lab'

@app.route('/login')
def login():
	return render_template('check.html')


@app.route('/login_inspect', methods=['post','get'])
def login():
    error = None
    if request.method == 'POST':

        email = request.form['email']
        pw = request.form['pw']
        
        conn = mysql.connect(host='capsinfirst.ckzc9c4vvmcm.eu-central-1.rds.amazonaws.com', user='Capsin', passwd='capsin', db='temp', charset='utf8')
        cursor = conn.cursor()
         
        query = "SELECT * FROM temp"
        value = (email, pw)
        cursor.execute("set names utf8")
        cursor.execute(query, value)
        data = (cursor.fetchall())
        
        cursor.close()
        conn.close()
        
        for row in data:
            data = row[0]
        
        if data:
            print 'login success'
            return redirect(url_for('success', name=data))
        else:
            error = 'Invalid input data detected!'
            
        #return redirect(url_for('success', name=user))
    
    return render_template('check.html', error=error)
'''


if __name__=='__main__':
	app.run(host='0.0.0.0',port=5000,debug=True)

