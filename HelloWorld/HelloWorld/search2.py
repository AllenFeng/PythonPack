# -*- coding: utf-8 -*-

from django.shortcuts import render
#from django.core.context_processors import csrf
from django.middleware import csrf

# 接收POST请求数据
def search_post(request):
	ctx ={}
	ctx.update(csrf(request))
	if request.POST:
		ctx['rlt'] = request.POST['q']
	return render(request, "post.html", ctx)