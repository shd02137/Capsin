from flask import Flask,request,render_template, url_for
from flaskext.mysql import MySQL
from datetime import datetime

app=Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = 'capsinfirst.ckzc9c4vvmcm.eu-central-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'CapsinFirst'
app.config['MYSQL_DATABASE_PASSWORD'] = 'capsinfirst'
app.config['MYSQL_DATABASE_DB'] = 'CapsinFirst'

mysql = MySQL()
mysql.init_app(app)

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main', methods = ['POST', 'GET'])
def main_page():
    if request.method == 'POST':
        id = request.form['loginid']
        pw = request.form['password']
    return render_template('main.html', loginid=id, password=pw)

@app.route('/chartselect.html')
def chart_select():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 300 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 10')

    rv = cur.fetchall()

    timelist=[]
    templist=[]
    flaglist=[]

    i=0

    for row in rv:
       data1  = row[0]
       data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
       data3  = row[2]
       i=i+1
       flaglist.append(data3)
       templist.append(data1)
       timelist.append(data2)
       templists = templist[::-1]
       timelists = timelist[::-1]
    legend = 'Temperatures'
    return render_template('chartselect.html', values=templists, labels=timelists, legend=legend, flag=flaglist)

@app.route('/chartselect2.html')
def chart_select2():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 301 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 10')

    rv = cur.fetchall()

    timelist=[]
    templist=[]
    flaglist=[]

    i=0

    for row in rv:
       data1  = row[0]
       data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
       data3  = row[2]
       i=i+1
       flaglist.append(data3)
       templist.append(data1)
       timelist.append(data2)
       templists = templist[::-1]
       timelists = timelist[::-1]

    legend = 'Temperatures'
    return render_template('chartselect2.html', values=templists, labels=timelists, legend=legend, flag=flaglist)

@app.route('/chartselect3.html')
def chart_select3():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 500 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 10')

    rv = cur.fetchall()

    timelist=[]
    templist=[]
    flaglist=[]

    i=0

    for row in rv:
       data1  = row[0]
       data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
       data3  = row[2]
       i=i+1
       flaglist.append(data3)
       templist.append(data1)
       timelist.append(data2)
       templists = templist[::-1]
       timelists = timelist[::-1]

    legend = 'Temperatures'
    return render_template('chartselect3.html', values=templists, labels=timelists, legend=legend, flag=flaglist)

@app.route('/dataselect.html', methods=['POST','GET'])
def dataselect():
	if request.method == 'POST':
		limits = request.form['rangeid']

	cur = mysql.get_db().cursor()
        cur2 = mysql.get_db().cursor()
	cur3 = mysql.get_db().cursor()
        cur.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 300 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 30')
        cur2.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 301 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 30')
	cur3.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 500 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 30')

        rv = cur.fetchall()
        rv2 = cur2.fetchall()
	rv3 = cur3.fetchall()

        timelist=[]
        templist=[]
        flaglist=[]
        timelist2=[]
        templist2=[]
        flaglist2=[]
	timelist3=[]
	templist3=[]
	flaglist3=[]

        i=0
        j=0
	k=0

        if limits == '10':
		numdata = 10
	elif limits == '20':
		numdata = 20
	else:
		numdata = 30

	for row in rv:
              data1  = row[0]
              data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
              data3  = row[2]
              flaglist.append(data3)
              templist.append(data1)
              timelist.append(data2)
              templists = templist[::-1]
              timelists = timelist[::-1]
              i=i+1
              if i==numdata:
                 break

	for row in rv2:
              data1 = row[0]
              data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
              data3 = row[2]
              flaglist2.append(data3)
              templist2.append(data1)
              timelist2.append(data2)
              templists2 = templist2[::-1]
              timelists2 = timelist2[::-1]
              j=j+1
              if j==numdata:
                 break

	for row in rv3:
              data1 = row[0]
              data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
              data3 = row[2]
              flaglist3.append(data3)
              templist3.append(data1)
              timelist3.append(data2)
              templists3 = templist3[::-1]
              timelists3 = timelist3[::-1]
              k=k+1
              if k==numdata:
                 break

	legend = 'Temperatures'
        return render_template('dataselect.html', values=templists, labels=timelists, legend=legend, flag=flaglist, values2=templists2, labels2=timelists2, flag2=flaglist2, values3=templists3, labels3=timelists3, flag3=flaglist3)

@app.route('/chart.html', methods = ['POST', 'GET'])
def index():
	cur = mysql.get_db().cursor()
        cur2 = mysql.get_db().cursor()
        cur.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 300 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 10')
        cur2.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 301 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 10')

        rv = cur.fetchall()
        rv2 = cur2.fetchall()

        timelist=[]
        templist=[]
        flaglist=[]
        timelist2=[]
        templist2=[]
        flaglist2=[]

	for row in rv:
              data1  = row[0]
              data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
              data3  = row[2]
              flaglist.append(data3)
              templist.append(data1)
              timelist.append(data2)
              templists = templist[::-1]
              timelists = timelist[::-1]

        for row in rv2:
              data1 = row[0]
              data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
              data3 = row[2]
              flaglist2.append(data3)
              templist2.append(data1)
              timelist2.append(data2)
              templists2 = templist2[::-1]
              timelists2 = timelist2[::-1]

	legend = 'Temperatures'
        return render_template('chart.html', values=templists, labels=timelists, legend=legend, flag=flaglist, values2=templists2, labels2=timelists2, flag2=flaglist2)

@app.route('/chart2.html')
def chart2():
    cur = mysql.get_db().cursor()
    cur.execute('SELECT Temp, M, Flag, H, S FROM CapsinFirst where code = 500 ORDER BY Mon desc, D desc, H desc, M desc LIMIT 10')

    rv = cur.fetchall()

    timelist=[]
    templist=[]
    flaglist=[]

    i=0

    for row in rv:
       data1  = row[0]
       data2  = str(row[3])+"h"+str(row[1])+"m"+str(row[4])+"s"
       data3  = row[2]
       i=i+1
       flaglist.append(data3)
       templist.append(data1)
       timelist.append(data2)
       templists = templist[::-1]
       timelists = timelist[::-1]

    legend = 'Temperatures'
    return render_template('chart2.html', values=templists, labels=timelists, legend=legend, flag=flaglist)

@app.route('/chart3.html')
def chart3():
    return render_template('chart3.html')

@app.route('/chart4.html')
def chart4():
    legend = 'Monthly Data'
    labels = ["January", "February", "March", "April", "May", "June", "July", "August"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template('chart4.html', values=values, labels=labels, legend=legend)

@app.route('/checksen.html')
def checksen():

	cur = mysql.get_db().cursor()
	cur.execute('SELECT DISTINCT Code, Mon, D, H, M FROM CapsinFirst ORDER BY Mon desc, D desc, H desc, M desc LIMIT 300')
	rv =cur.fetchall()
	now=datetime.now()
	nowtime = int(now.month)*1000000+int(now.day)*10000+int(now.hour)*100+int(now.minute)

	Codelist=[]
	Monlist=[]
	Dlist=[]
	Hlist=[]
	Mlist=[]
	Notcomelist=[]
	i=0
	uniquecode=[]
	uniquetime=[]
	uniqueNotcome=[]
	uniquetime.append("LastMessage")
	uniqueNotcome.append("Is it OK?")
        for row in rv:
           data1  = row[0]
	   data2  = row[1]
	   data3  = row[2]
	   data4  = row[3]
	   data5  = row[4] 
	   i=i+1
	   if nowtime>=int(data2*1000000+data3*10000+data4*100+data5+130):
		Notcomelist.append("Something Wrong")
	   else:
		Notcomelist.append("Not Error")
           Codelist.append(data1)
	   Monlist.append(data2*1000000+data3*10000+data4*100+data5)
	   Dlist.append(data3)
           Hlist.append(data4)
	   Mlist.append(data5)
	setCode=set(Codelist)
	uniquecode=list(setCode)
	uniquecode.sort()

	for i in uniquecode:
		index= Codelist.index(i)
		uniquetime.append(Monlist[index])
		uniqueNotcome.append(Notcomelist[index])


	num=len(uniquecode)

	uniquecode.insert(0,"SensorCode")
	return render_template('checksen.html', Code=uniquecode, Month=Monlist, Time=uniquetime,Num=num,Errornode=uniqueNotcome)


@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)

'''
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
	app.run(host = '0.0.0.0', port = 5000, debug=True)
