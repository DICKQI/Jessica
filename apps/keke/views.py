from rest_framework.views import APIView
from django.forms.models import model_to_dict
from django.http import JsonResponse
from apps.keke.models import *
from apps.xixi.models import *
import datetime

# Create your views here.
class kekeView(APIView):
    def get(self, requests):
        weekday = datetime.datetime.now().weekday() + 1
        keke = kkTable.objects.filter(week=weekday)
        xixi = xxTable.objects.filter(week=weekday)
        return JsonResponse({
            'keke':[model_to_dict(kk) for kk in keke],
            'xixi':[model_to_dict(xx) for xx in xixi],
            'weekday':weekday
        })