# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    response.flash = T("Welcome to Snap Detection!")
    return dict()


def record():

   a=0
   form = SQLFORM(db.details).process()

   if form.accepted:

        redirect(URL('thanks',vars={'your_name':form.vars.your_name},args=a))
   return dict(message=a,form=form)


def thanks():
    message = 'Thanks %s' % request.vars.your_name
    return dict(message=message)
