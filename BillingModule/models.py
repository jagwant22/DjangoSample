# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import django
from django.db import models
import datetime
import json



# patient details :
#patient name
#patient number
#patient dob/ age
#patient id ( if applicable)
#gender




class BillingDetails(models.Model):
    hospital_name = models.CharField(max_length=20, null=False, blank=False)
    doctor_name = models.CharField(max_length=20, null=False, blank=False)
    department = models.CharField(max_length=20, null=False, blank=False)
    service_charges = models.CharField(max_length=20, null=False, blank=False)
    item_details = models.TextField(null=False, blank=False)
    patient_details = models.TextField(null=False, blank=False)
    for_date = models.CharField(max_length=20, null=False, blank=False)
    entry_created_on = models.DateTimeField(default =django.utils.timezone.now)

    def serializeModel(self):
        datadict = dict()
        datadict['hospital_name'] = self.hospital_name
        datadict['doctor_name'] = self.doctor_name
        datadict['department'] = self.department
        datadict['service_charges'] = self.service_charges
        datadict['item_details'] = self.item_details
        datadict['patient_details'] = self.patient_details
        datadict['for_date'] = self.for_date
        datadict['entry_created_on'] = self.entry_created_on

        return datadict

    def __str__(self):
        return "Bill : %s %s" % (self.doctor_name, self.pk)

    class Meta :
        verbose_name = 'Billing Detail'
        verbose_name_plural = 'Billing Details'