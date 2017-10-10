# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
import json
from datetime import datetime
from django.views import View

def index(request):
    return render(request, 'index.html', context= {})

class BillingView(View):

    def get(self, request):
        try:
            bill_id = request.GET['bill_id']
            customer_number = request.GET['patient_number']

            if bill_id not in "":
                pass
            if customer_number not in "":
                pass
        except:
            pass

        return HttpResponse("<h1>This is the get method</h1>")

    def post(self, request):
        pass
