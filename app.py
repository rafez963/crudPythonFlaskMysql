#from crypt import methods
from pydoc import render_doc
from flask import Flask
from flask_mysqldb import MySQL
from flask import Flask, request, render_template, redirect, url_for,flash


#mysql connection
app = Flask(__name__)
app.config['MySQL_HOST'] = 'localhost'
app.config['MySQL_USER'] = 'root'
app.config['MySQL_PASSWORD'] = ''
app.config['MySQL_DB'] = 'flaskcontacts'

#settings
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def add_contact():
    if(request.method == 'POST'):
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']

        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES (%s, %s, %s)',
        (fullname, phone, email))

        mysql.connection.commit()

        flash('Contact added successfully')
        return redirect(url_for('index'))

@app.route('/edit')
def edit_contac():
    return 'edit contac'

@app.route('/delete')
def delete_contact():
    return 'delete contact'

if __name__ == '__main__':
    app.run(port = 3000, debug=True)