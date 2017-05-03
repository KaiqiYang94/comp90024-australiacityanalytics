# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from couchdb import Server
from django.shortcuts import render


def index(request):

    # using localhost to test
    server = Server()

    db = server['dataset_ieo']
    doc = db['seifa_ieo_aust_sa2.fid-6ec8c59a_15bb93bc511_-28d6']
    print(doc['_id'])
    # must parameters, passing content to html using json
    content = {'key': doc['_id']}

    # template = loader.get_template('tweetswebsite/index.html')
    # return HttpResponse(template)

    return render(request, 'tweetswebsite/index.html', content)
