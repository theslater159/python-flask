from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL  
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)
app.secret_key = 'mysecretkey'
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
       nombre = request.form['nombre']
       apellido = request.form['apellido']
       celular = request.form['celular']
       correo = request.form['correo']
       contrasenia = request.form['contrasenia'] 
       cur = mysql.connection.cursor()
       cur.execute('INSERT INTO contacts (nombre, apellido, celular, correo, contrasenia) VALUES (%s, %s, %s, %s, %s)',
       (nombre, apellido, celular, correo, contrasenia))
       mysql.connection.commit()
       flash('Persona agregada')
       return redirect(url_for('Index'))
@app.route('/edit')
def edit():
    return "editar"  
@app.route('/delete')
def delete():
    return "delete"        

app.run(debug=True,)