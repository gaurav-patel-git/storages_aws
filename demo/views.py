from django.shortcuts import render
from storages_aws.settings import use_s3
# Create your views here.

def index(request):
    return render(request, 'demo/index.html', {'use_s3': use_s3})