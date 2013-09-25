# Create your views here.
from blog.models import blog_post
from django.http import HttpResponse
from django.shortcuts import render_to_response
#coding=utf-8
def archive(request):
	posts=blog_post.objects.all()
	return render_to_response('archive.html',{'posts':posts})

def blog_show(request,id):
	post=blog_post.objects.get(id=id)
	return render_to_response('artical.html',{'post':post})
def blog_change(request,id):
	post=blog_post.objects.get(id=id)
	return render_to_response('change.html',{'post':post})

