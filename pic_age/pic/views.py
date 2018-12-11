# Create your views here.
# -*- coding: UTF-8 -*-
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import os
from django.conf import settings
#sys.path.append('/home/lee/git/rude-carnie/')
#from guess import main


def upload(request):
    t = get_template('upload_pic.html')
    html = t.render(Context({}))
    return HttpResponse(html)
def back(request):
    t = get_template('upload_pic2.html')
    html = t.render(Context({}))
    return HttpResponse(html)
def uploadImg(request):
    if request.method == 'POST':
        f = request.FILES['file']
        filepath = os.path.join(settings.MEDIA_ROOT,f.name)
        with open(filepath,'wb') as fp:
            for info in f.chunks():
                fp.write(info)
        str=('python /home/lee/git/rude-carnie/guess.py --model_type inception --model_dir /home/lee/Downloads/22801 --filename ' + filepath)
        p=os.system(str)
        file_object = open('/home/lee/git/rude-carnie/log.txt')
        file_context = file_object.read()
        return HttpResponse(file_context)