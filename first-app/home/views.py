from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    response = HttpResponse()
    response.writelines("<h1>Xin chào</h1>")
    response.write("<h2>Đây là app home</h2>")
    return response