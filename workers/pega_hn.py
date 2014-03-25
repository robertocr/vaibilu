# coding: utf-8
from threading import Thread
from sendgrid_service import send_email

def get_hn(qtd = 1,email=None, subject = None):
    #pega as Notícias do Hacker News
    from hn import HN

    novidades = HN()
    results = []
    for s in novidades.get_stories(story_type='newest', limit = qtd):
        results.append(s.link)

    if qtd > 1:
        return results
    else:
        return results[0]

class get_hn_thread(Thread):

    def __init__(self, service,email, subject, *args, **kwargs):
        Thread.__init__(self)
        self.service = service
        self.email = email
        self.subject = subject
        self.args = args
        self.kwargs = kwargs

    def run(self):
        response  = get_hn()

        if self.service == u"sendgrid":
            response = response+"<br>"
            response += u"<br>-------<br>"+\
                        u"\"Busquem conhecimento\" - ET Bilu<br>" +\
                        u"<img src='http://vaibilu.com/static/bilu_small.jpg'>"

            return send_email(response, self.email, self.subject)

        elif self.service == "twitter":
            if response:
                response = response[:160]
            else:
                response = u'Busquem conhecimento!'

