from flask import Flask, render_template, request, session, make_response


app = Flask(__name__)

app.secret_key = 'alsdhbaousdv'

@app.route("/", methods = ['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        if request.cookies.get('usuario'):
            resp = make_response('Meu website com cookie setado.')
        else:
            resp = make_response('meu website sem cookie')
            resp.set_cookie('usuario','Lucas')
            
        return resp
            
    else:
        return "o que retorna do form: " + request.form['conteudo']


@app.route("/sobre")
def sobre():
    return '<h2>Tela sobre</h2>'

@app.route("/noticia/<noticia_slug>")
def noticia(noticia_slug):
    return 'Noticia: '+noticia_slug