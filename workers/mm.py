# coding: utf-8

def get_mms(self):
    import requests
    r = requests.get("http://likemachine.herokuapp.com/glass")

    print r.text
