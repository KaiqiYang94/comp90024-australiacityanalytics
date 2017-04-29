# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, render, HttpResponseRedirect
from couchdb import Server
from couchdb.http import ResourceNotFound

import datetime

#SERVER = Server('kaiqi:password@http://127.0.0.1:5984')
SERVER = Server('http://127.0.0.1:5984')
if (len(SERVER) == 0):
    SERVER.create('docs')

def index(request):
    docs = SERVER['docs']
    # cnt = len(docs)
    # now = datetime.datetime.now()
    # # # html = "<html><body>It is now %s. there are %s dbs in the data base </body></html>" % now % cnt
    # html = "<html><body>there are %s dbs in the data base </body></html>" % cnt
    # return HttpResponse(html)


    if request.method == "POST":
        title = request.POST['title'].replace(' ','')
        docs[title] = {'title':title,'text':""}
        # html = "<html><body>there are %s dbs in the data base </body></html>" % title
        # return HttpResponse(html)
        return HttpResponseRedirect(u"/doc/%s/" % title)
    # html = "<html><body>there are %s dbs in the data base </body></html>" % docs
    # return HttpResponse(html)
    return render(request, 'Example/index.html',{'rows':docs})


def detail(request,id):
    docs = SERVER['docs']
    try:
        doc = docs[id]
    except ResourceNotFound:
        raise Http404        
    if request.method =="POST":
        doc['title'] = request.POST['title'].replace(' ','')
        doc['text'] = request.POST['text']
        docs[id] = doc
    return render_to_response('Example/detail.html',{'row':doc})