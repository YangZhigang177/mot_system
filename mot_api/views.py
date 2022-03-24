from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json





@require_http_methods(["GET"])
def get_video(request, id):
    response = {
        'id': id,
        'content': 'ssss',
    }
    return JsonResponse(response)
