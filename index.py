# -*- coding: utf-8 -*-
import sys
sys.path.append('/home/freitas/webapps/flask_bilu/htdocs/')
sys.path.append('/home/freitas/webapps/flask_bilu/htdocs/workers/')
sys.path.append('/home/freitas/webapps/flask_bilu/htdocs/duckduckgosdk/')
from flask import Flask, request
from router import router
from sendgrid_service import send_email

app = Flask(__name__)

@app.route("/")
def hello():
    if request.method == 'GET':
        return """
        <html>
        <head><title>Vai, Bilu!</title>
        <style>html {   background: url(static/bilu.jpg) no-repeat center center fixed;   -webkit-background-size: cover;  -moz-background-size: cover;  -o-background-size: cover;  background-size: cover;}</style>
        <body style="background: url(static/bilu.jpg) no-repeat center center;">
        <div style="margin:auto; padding-top:5%; height:300px;color: red;font-family: Comic Sans MS;padding-left: 10%; font-weight: bold; font-size:x-large;">
            Bilu veio ajudar a humanidade.<br>
            Para buscar conhecimento de diversas bases,<br>
            basta me mandar um email<br>
            para: bilu@vaibilu.com<br>
            assunto: alguma serie #torrent<br>
            ---<br>
            ET Bilu também usa Twitter.<br>
            @vaibilu #weather varginha<br>
            ---<br>
            Sou muito jovem, tenho só 4010 anos,<br>
            mas sei de muitas coisas (#placar #mm #porn #fonte)<br>
            Compartilhe conhecimento!!!
        </div>
        </body>
        </html>"""
    else:
        return "Hello World!"

@app.route("/apihackdayemail", methods=['GET', 'POST'])
def get_email():
    if request.method == 'GET':
        return False
        # return "<img src='/static/bilu.jpg' width='100%' height='100%'>"
    email_from = request.form["from"].encode('utf8')
    subject = request.form["subject"].encode('utf8')

    response = router(subject, "sendgrid", email=email_from, subject = subject)

    if response != 'SAIR':
        return send_email(response, email_from, subject)
    else:
        return "OK"


# receive and send

# app.register_blueprint(twitter)

# the different services
# app.register_blueprint(torrent)

if __name__ == "__main__":
    app.run(debug=False)
    #aqui abre o twitter_streaming.py

application = app
#from twitter_streaming import tstream
#tstream()