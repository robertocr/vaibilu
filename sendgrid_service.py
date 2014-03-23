# -*- coding: utf-8 -*-
import sendgrid
from flask import Blueprint, request
from _config import sendgrid_conf as config


def send_email(message_text, user, subject):
    # aqui manda o email pra esse user com esse message
    message_text = message_text.encode('utf8')
    MANDA_EMAIL = True
    if not MANDA_EMAIL:
        return "<b>message_text</b>:<br>%s<hr><b>user</b>:<br>%s<hr><b>subject</b>:<br>%s" % (message_text, user, subject)
    else:
        sg = sendgrid.SendGridClient(config.SENDGRID_USER, config.SENDGRID_PASS)

        message = sendgrid.Mail()
        message.add_to(user)
        message.set_subject(subject)
        message.set_html(message_text)
        message.set_text(message_text)
        message.set_from('ET Bilu <bilu@vaibilu.com>')
        status, msg = sg.send(message)
        return ""