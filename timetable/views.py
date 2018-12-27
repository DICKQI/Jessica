from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.views import APIView
from timetable.models import Table
from django.http import JsonResponse
import datetime

# Create your views here.

class TableView(APIView):

    def get(self, requests, name):
        '''
        获取课表
        :param requests:
        :param name:
        :return:
        '''
        weekday = datetime.datetime.now().weekday() + 1
        tableList = Table.objects.filter(
            who=name,
            week=weekday
        )
        tableResult = [model_to_dict(table) for table in tableList]

        return JsonResponse({
            'tableList': tableResult
        })