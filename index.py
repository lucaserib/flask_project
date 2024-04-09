from flask import Flask, render_template, request, session, make_response, redirect
import pymysql
app = Flask(__name__)

app.secret_key = "smakonakl0ioe8390732890dshui"
db = pymysql.connect(host="localhost",user="root",password="",database="flask_project")







@app.route("/deletar", methods=['GET','POST'])
def deletar():
        cursor = db.cursor()
        sql = "DELETE FROM clientes WHERE id = %s"
        cursor.execute(sql,(request.args.get('id')))
        db.commit()
        return redirect("/")


@app.route("/", methods=['GET','POST'])
def index():
        if request.method == 'POST':
                id = request.form.get('id')
                nome = request.form.get('nome')
                email = request.form.get('email')
                cursor = db.cursor()
                sql = "UPDATE clientes SET nome = %s,email = %s WHERE id = %s"

                cursor.execute(sql,(nome,email,id))
                db.commit()


                cursor = db.cursor()
                sql = "SELECT * FROM clientes"

                cursor.execute(sql)
                db.commit()
                results = cursor.fetchall()
                print(results)
                return render_template("index.html",content=results)
        else:
                cursor = db.cursor()
                sql = "SELECT * FROM clientes"

                cursor.execute(sql)
                db.commit()
                results = cursor.fetchall()
                print(results)
                return render_template("index.html",content=results)
            
        
        
    


@app.route("/sobre")
def sobre():
    return "<h2>Sobre</h2>"

@app.route("/noticia/<noticia_slug>")
def noticia(noticia_slug):
    return "Noticia: "+noticia_slug

