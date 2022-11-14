from flask import Flask,render_template,request, redirect,url_for, session
import ibm_db
import re
app=Flask(__name__)
app.secrete_key = 'a'
conn=ibm_db.connect(" DATABASE =
bludb;HOSTNAME=b70af05b-76e4-4bca-a1f5-23dbb4c6a74e.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=
32716;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=kcv39089;PWD=pthMo96lY5zuNGGs",''.'')

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def login():
    global userid
    msg= ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        sql="SELECT * FROM Users WHERE username= ? AND password =?"
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account= ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['loggedin']= True
            session ['id'] = account['username']
            userid =account['USERNAME']
            session ['username']= account['USERNAME']
            msg ='logged in successfully'
            return render_template('dashboard.html', msg=msg)
        else:
            msg = 'incorrect username/password'
            return render_template('login.html', msg=msg)  
          
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='POST':
        username=request.form ['username']
        email=request.form['email']
        password = request.form['password']
        sql="SELECT * FROM Users WHERE username= ? "
        stmt = ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt 1, username)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        