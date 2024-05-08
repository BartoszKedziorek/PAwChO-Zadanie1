from django.views import View
from datetime import date
import datetime
from django.shortcuts import render
import pytz
from django.utils.timezone import localtime


class IndexView(View):
    def get(self, request, format=None):
       
        client_ip = request.META['REMOTE_ADDR']
        client_timezone = pytz.timezone(request.META.get('HTTP_TIMEZONE', 'UTC'))
      #  client_datetime = localtime(datetime.datetime.now(), client_timezone)

        return render(request, 'mserwer/index.html', context={
            'ip': client_ip,
            #'timezone':client_timezone,
            #'time': datetime.datetime.now(client_timezone) #client_datetime.strftime('%Y-%m-%d %H:%M:%S')
        })




