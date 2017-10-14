from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import json
import getids


def get_prediction(request):
    #get the image here. Predict and return result
    profile = predict_final_face(open("test/nitin.jpg", 'rb'))
    img_url = "localhost:8000/nozimers/nozimers"
    profile['image'] = '/images/'+profile['image']
    return HttpResponse(profile)
    
